from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the get_user_stats function
def get_user_stats(username):
    # Define the GitHub API URL for user data
    url = f"https://api.github.com/users/{username}"
    
    # Send a request to the GitHub API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant statistics
        stats = {
            "login": data.get("login"),
            "name": data.get("name"),
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following"),
            "bio": data.get("bio"),
        }
        
        return stats
    else:
        # Handle errors (e.g., user not found)
        return {"error": "User not found or API request failed"}

# Define a route to access the user stats
@app.route('/user_stats/<username>', methods=['GET'])
def user_stats(username):
    stats = get_user_stats(username)
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
