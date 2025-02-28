from src.open_api_client import get_openai_client
from pprint import pprint

client = get_openai_client()
pprint(vars(client))

# Make a request to OpenAI API
completion = client.chat.completions.create(
    # passing 2 parameters: model and messages
    # this is in the json format
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "When was the State of Israel founded?"
        }
    ]
)

# Output the response
pprint(completion)
pprint(completion.choices[0].message.content)