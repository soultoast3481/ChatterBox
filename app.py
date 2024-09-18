import os
import json
import logging
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Replace with a secure key in production

# Configure logging to output to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Directories to save uploaded files by category
UPLOAD_FOLDER = {
    'files': 'uploads/files',
    'images': 'uploads/images',
    'videos': 'uploads/videos'
}

# Create directories if they do not exist
for folder in UPLOAD_FOLDER.values():
    os.makedirs(folder, exist_ok=True)
    logging.info(f"Ensured directory exists: {folder}")

# A global list to store messages
messages = []

# File to store user data
USER_DATA_FILE = 'user_data.json'

def load_user_data():
    """Load user data from a JSON file."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_user_data(data):
    """Save user data to a JSON file."""
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(data, f)
    logging.info("User data saved.")

@app.route('/')
def home():
    """Render the home page with file listings and messages."""
    files = {category: os.listdir(path) for category, path in UPLOAD_FOLDER.items()}
    username = session.get('username')
    logging.info(f"Home page accessed by user: {username}")
    return render_template('index.html', messages=messages, files=files, username=username)

@app.route('/username_password', methods=['GET', 'POST'])
def username_password():
    """Handle user registration and login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_data = load_user_data()

        if 'register' in request.form:
            # Register new user
            if username in user_data:
                logging.info(f"Attempted registration with taken username: {username}")
                return render_template('username_taken.html', message='Username already taken.')
            user_data[username] = generate_password_hash(password)
            save_user_data(user_data)
            session['username'] = username
            logging.info(f"User registered: {username}")
            return redirect(url_for('home'))
        
        elif 'login' in request.form:
            # Log in existing user
            if username not in user_data:
                logging.info(f"Attempted login with non-existent username: {username}")
                return render_template('username_taken.html', message='Username does not exist.')
            if not check_password_hash(user_data[username], password):
                logging.info(f"Failed login attempt for username: {username}")
                return render_template('username_taken.html', message='Incorrect password.')
            session['username'] = username
            logging.info(f"User logged in: {username}")
            return redirect(url_for('home'))

    logging.info("Accessed username/password page.")
    return render_template('username_password.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    """Handle sending messages."""
    message = request.form['message']
    username = session.get('username', 'Anonymous')
    if message:
        messages.append(f"{username}: {message}")
        logging.info(f"Message sent by {username}: {message}")
    return redirect(url_for('home'))

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads."""
    if 'file' not in request.files:
        logging.error("No file part in the request.")
        return 'No file part'
    file = request.files['file']
    category = 'images' if file.mimetype.startswith('image/') else 'videos' if file.mimetype.startswith('video/') else 'files'
    if file.filename == '':
        logging.error("No selected file.")
        return 'No selected file'
    if category not in UPLOAD_FOLDER:
        logging.error(f"Invalid category: {category}")
        return 'Invalid category'
    file.save(os.path.join(UPLOAD_FOLDER[category], file.filename))
    logging.info(f"File uploaded: {file.filename} in category {category}")
    return redirect(url_for('home'))

@app.route('/uploads/<category>/<filename>')
def uploaded_file(category, filename):
    """Serve uploaded files."""
    if category not in UPLOAD_FOLDER:
        logging.error(f"Invalid category: {category}")
        return 'Invalid category'
    logging.info(f"Serving file: {filename} from category {category}")
    return send_from_directory(UPLOAD_FOLDER[category], filename)

@app.route('/clear_chat', methods=['POST'])
def clear_chat():
    """Clear chat messages for admin."""
    if session.get('username') == 'admin':
        global messages
        messages = []
        logging.info("Chat cleared by admin.")
    return redirect(url_for('home'))

@app.route('/get_messages')
def get_messages():
    """Return chat messages as JSON."""
    return jsonify(messages)

@app.route('/sign_out')
def sign_out():
    """Handle user sign out."""
    session.pop('username', None)
    logging.info("User signed out.")
    return redirect(url_for('username_password'))

if __name__ == '__main__':
    logging.info("Starting the Flask application.")
    app.run(host='0.0.0.0', port=5000, debug=True)
