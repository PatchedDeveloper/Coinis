from flask import Flask, request
import json, os 

app = Flask(__name__)
db_file = 'users_main.json'

def read_db():
    if not os.path.exists(db_file):
        return []

    with open(db_file, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
        
def write_db(data):
    with open(db_file, "w") as file:
        json.dump(data, file, indent=4)

@app.route("/user", methods=["POST"])

def create_user():
    users = read_db()
    request_data = request.get_json()
    new_user = {'name': request_data['name'], 'email': request_data['email']}
    users.append(new_user)
    write_db(users)
    return json.dumps(new_user)


@app.route('/user/<string:name>', methods=['GET'])

def get_user(name):
    users = read_db()
    user = [ u for u in users if u['name'] == name ]
    if user:
        return json.dumps(user)
    else:
        return json.dumps({'error': 'User not found'})
    

@app.route('/users')

def get_all_users():
    users = read_db()
    if users:
     return json.dumps(users)
    else:
        return json.dumps({'error': 'No users found'})
    
@app.route('/user/<string:name>', methods=['DELETE'])

def delete_user(name):
    users = read_db()
    new_user = [u for u in users if u['name'] != name]
    if len(users) == len(new_user):
         return json.dumps({'error': 'No users found'})
    else:
        write_db(new_user)
        return json.dumps({'message': 'User deleted'})

@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port = 5000)