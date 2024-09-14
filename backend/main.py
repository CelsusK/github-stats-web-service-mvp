from flask import Flask, jsonify, request
from pymongo import MongoClient
import requests

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['github_stats']
users_collection = db['users']

@app.route('/github-stats/<username>', methods=['GET'])
def get_github_stats(username):
    # Check if the user's data is already in MongoDB
    user_data = users_collection.find_one({"username": username})

    if user_data:
        # Return data from MongoDB
        return jsonify({
            "username": user_data['username'],
            "repos": user_data['repos'],
            "followers": user_data['followers'],
            "stars": user_data['stars'],
            "most_popular_repo": user_data['most_popular_repo']
        })
    else:
        # Fetch data from GitHub API
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url)
        data = response.json()

        # Example of fetching stats from the API
        user_stats = {
            "username": data['login'],
            "repos": data['public_repos'],
            "followers": data['followers'],
            "stars": get_total_stars(username),  # You would have to implement this function
            "most_popular_repo": get_most_popular_repo(username)  # You would have to implement this function
        }

        # Store data in MongoDB
        users_collection.insert_one(user_stats)

        # Return the fetched data
        return jsonify(user_stats)

if __name__ == "__main__":
    app.run(debug=True)
