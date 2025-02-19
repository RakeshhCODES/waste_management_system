from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for user data
users = {}

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if username in users:
            return jsonify({"message": "User already exists"}), 400
        
        users[username] = password
        return jsonify({"message": "Signup successful", "data": data}), 201
    else:
        return render_template('signUp.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if username not in users or users[username] != password:
            return jsonify({"message": "Invalid username or password"}), 401
        
        return jsonify({"message": "Login successful", "data": data}), 200
    else:
        return render_template('login.html')

@app.route('/add_food', methods=['GET', 'POST'])
def add_food():
    if request.method == "POST":
        data = request.get_json()
        # Add logic to handle adding food
        return jsonify({"message": "Food added successfully", "data": data}), 201
    else:
        return render_template('addFood.html')

@app.route('/get_matches', methods=['GET'])
def get_matches():
    # Add logic to get matches
    matches = []  # Replace with actual match data
    return jsonify({"matches": matches}), 200

if __name__ == '__main__':
    app.run(debug=True)