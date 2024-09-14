import requests

GITHUB_API_URL = "https://api.github.com/users"

def fetch_github_data(username):
    try:
        response = requests.get(f"{GITHUB_API_URL}/{username}/repos")
        if response.status_code == 200:
            repos_data = response.json()
            # Further processing if needed
            return repos_data
        else:
            return None
    except Exception as e:
        print(f"Error fetching GitHub data: {e}")
        return None
