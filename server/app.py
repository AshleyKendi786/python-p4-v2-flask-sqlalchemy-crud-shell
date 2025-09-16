# server/app.py
from flask import Flask
from models import db, Pet

# Create the Flask app
app = Flask(__name__)

# Configure database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Welcome to the Pet App!</h1>'

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run server
    app.run(port=5555, debug=True)
