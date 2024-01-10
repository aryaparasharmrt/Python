import requests

def execute_graphql_query(query, token):
  endpoint = "https://api.github.com/graphql"
  headers = {
      "Authorization": f"Bearer {token}"
  }
  data = {"query": query}

  response = requests.post(endpoint, json=data, headers=headers)

  if response.status_code == 200:
    return response.json()
  else:
    print(f"GraphQL request failed with status code {response.status_code}")
    print(response.text)
    return None

graphql_query = """
{
repository(owner: "aryaparasharmrt", name: "Python") {
  name
  description
  createdAt
  stargazerCount
  }
  }
  """

token = "YOUR_PERSONAL_ACCESS_TOKEN"
result = execute_graphql_query(graphql_query, token)

if result:
  repository_info = result.get("data", {}).get("repository", {})
  print("Repository Information:")
  print(f"Name: {repository_info.get('name')}")
  print(f"Description: {repository_info.get('description')}")
