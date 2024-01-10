import requests

def execute_rest_api(endpoint, token):

  # Using Rest API
  url = f"https://api.github.com/{endpoint}"
  headers = {
      "Authorization": f"Bearer {token}"
  }

 response = requests.get(url, headers=headers)

 if response.status_code == 200:
   return response.json()
else:
  print(f"REST API request failed with status code {response.status_code}")
  print(response.text)
  return None

rest_api_endpoint = "user"
token = "YOUR_PERSONAL_ACCESS_TOKEN"
result = execute_rest_api(rest_api_endpoint, token)

if result:
  print("User Information:")
  print(f"Login: {result.get('login')}")
