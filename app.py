from flask import Flask, request, jsonify
from src.github_api import get_user_stats

app = Flask(__name__)

@app.route('/api/user/<username>', methods=['GET'])
def user_stats(username):
    """Retrieve GitHub profile statistics."""
    try:
        stats = get_user_stats(username)
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
