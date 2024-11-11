from flask import Flask, request, jsonify #added to top of file
from flask_cors import CORS #added to top of file
from database import *


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_users())
@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/api/users/add', methods = ['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))


@app.route('/api/users/update', methods = ['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_user(user))

@app.route('/api/users/delete/<user_id>', methods = ['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))
user1 = {
"name": "kassem yassine",
"email": "kmy05@mail.aub.edu",
"phone": "067765434567",
"address": "John Doe Street, Innsbruck",
"country": "Austria"
}
if __name__ == "__main__":
    create_db_table()
    insert_user(user)
    insert_user(user1)
    app.run(debug=True)