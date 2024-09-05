import requests

def get_user_stats(username):
    """Fetch GitHub user stats from the GitHub API."""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "login": data.get("login"),
            "name": data.get("name"),
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following"),
            "bio": data.get("bio")
        }
    else:
        response.raise_for_status()
