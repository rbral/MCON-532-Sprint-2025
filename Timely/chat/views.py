from datetime import datetime, timedelta

import pytz
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.conf import settings

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from openai import OpenAI

from chat.models import ChatMessage

# Initialize OpenAI client
client = OpenAI(api_key=settings.OPEN_AI_API_KEY, organization=settings.OPENAI_ORG_ID)

def index(request):
    return render(request, 'index.html')


def response(request):
    if request.method == 'POST':
        message = request.POST.get("message", "")
        if not message:
            return JsonResponse({'response': 'No message provided.'}, status=400)

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        answer = completion.choices[0].message.content
        ChatMessage.objects.create(message=message, response=answer)
        return JsonResponse({'response': answer}, status=200)

    return JsonResponse({'response': 'Invalid Request'}, status=400)

# Define Google OAuth scopes
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid',
]
def google_login(request):
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    auth_url, _ = flow.authorization_url(prompt='consent',
                                         access_type='offline',
                                         include_granted_scopes=False )

    return redirect(auth_url)


def oauth2callback(request):
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials

    # Get user info
    user_service = build('oauth2', 'v2', credentials=credentials)
    user_info = user_service.userinfo().get().execute()
    email = user_info.get('email')
    first_name = user_info.get('given_name')
    last_name = user_info.get('family_name')

    if not email:
        return HttpResponse("Unable to retrieve user email.", status=400)

    user, _ = User.objects.get_or_create(username=email, first_name=first_name, last_name=last_name, defaults={'email': email})
    login(request, user)

    # Save credentials in session (for prototype; use DB for production)
    request.session['google_token'] = credentials_to_dict(credentials)
    return redirect('/')


def list_events(request):
    token_info = request.session.get('google_token')
    if not token_info:
        return redirect('/calendar/google_login/')

    creds = Credentials(**token_info)
    if creds.expired:
        if creds.refresh_token:
            creds.refresh(Request())
            request.session['google_token'] = credentials_to_dict(creds)
        else:
            return redirect('/calendar/google_login/')

    service = build('calendar', 'v3', credentials=creds)
    # Set time window: now to 2 weeks from now
    now = datetime.now(pytz.utc).isoformat()
    two_weeks = (datetime.now(pytz.utc) + timedelta(weeks=2)).isoformat()

    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        timeMax=two_weeks,
        maxResults=50,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    return render(request, 'events.html', {'events': events})


def logout_view(request):
    logout(request)
    return redirect('/')


def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': list(credentials.scopes),
    }

