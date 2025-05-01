from django.urls import path
from chat.views import index, response,  google_login, oauth2callback, list_events

urlpatterns = [
    path('',index, name="index"),
    path('response', response, name="response"),
    path('calendar/authorize/', google_login, name="google_login"),
    path('calendar/oauth2callback', oauth2callback, name="oauth2callback"),
    path('calendar/list/', list_events, name="list_events"),
]
