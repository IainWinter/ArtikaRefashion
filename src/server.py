from flask import Flask, app

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/") and a function to handle it
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask app on the development server
    app.run()