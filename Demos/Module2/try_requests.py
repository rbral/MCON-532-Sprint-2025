import requests

# GET example
url = 'https://jsonplaceholder.typicode.com/posts/1'  # Public API
response = requests.get(url)
print(response.status_code)  # Status code (200 means success)
print(response.json())  # JSON response from API


# POST Request Example (Sending JSON Data)
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "New Post", "body": "This is an example post", "userId": 1}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())

# POST Request Example (Sending Form Data)
url = "https://httpbin.org/post"  # Public API for testing requests
data = {"username": "test_user", "password": "secure123"}
response = requests.post(url, data=data)
print(response.text)  # Raw response output



