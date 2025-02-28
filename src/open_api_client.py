import os # allows us to manipulate files, find files
from openai import OpenAI
from dotenv import load_dotenv #openAI client

# Load the .env file only once
# .env is a package that contains environment variables
# that can be used during execution of a program

# path is a method in the os module. allows you to join two paths:
# gets path of current file + combines with: \.env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

# execute the current python process
load_dotenv(dotenv_path=dotenv_path)

# Initialize the client only once
_client_instance = None
# this is very global
# trying to avoid calling create client again and again

# instance of the ai api
# create an https client
def get_openai_client():
    global _client_instance
    # if this does not exist, create it
    if _client_instance is None:
        api_key = os.getenv("OPEN_API_KEY")
        org_id = os.getenv("OPEN_API_ID").strip()
        # call openAI method to fetch an instance of a client
        _client_instance = OpenAI(api_key=api_key, organization=org_id)
    return _client_instance