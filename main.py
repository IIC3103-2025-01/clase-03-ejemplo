from flask import Flask, request, jsonify
from user import User


app = Flask(__name__)

users = []

@app.route("/")
def home():
  return "API HOME"

@app.route('/users', methods=['GET', 'POST'])
def users_method():
  global users

  if request.method == 'POST':
    if not request.is_json:
      return jsonify({"error": "Request body must be JSON"}), 400

    try:
      user_data = request.get_json()
    except Exception as e:
      return jsonify({"error": f"Invalid JSON format: {str(e)}"}), 400
    
    if not User.validate_user_data(user_data):
      return jsonify({"error": "Invalid data"}), 400

    new_user = User(user_email=user_data["email"], user_name=user_data["name"])
    users.append(new_user)

    return jsonify(new_user.to_json())

  else:
    users_json = [u.to_json() for u in users] 
    return jsonify(users_json)
