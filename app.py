from flask import Flask
from views.guitar_view import guitar
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(guitar)

# WRAPPER FUNCTION DEFINING THE ENDPOINT
@app.route("/")
def index():
    return "HOME"

if __name__ == "__main__":
    app.run()

# flask --app app run