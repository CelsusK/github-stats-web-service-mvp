from flask import Blueprint, request, jsonify
from services.github_service import fetch_github_data

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/api/github/<username>', methods=['GET'])
def get_github_stats(username):
    data = fetch_github_data(username)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Failed to fetch GitHub data"}), 400
