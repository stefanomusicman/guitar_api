from flask import Flask
from views.guitar_view import guitar

app = Flask(__name__)

app.register_blueprint(guitar)

# WRAPPER FUNCTION DEFINING THE ENDPOINT
@app.route("/")
def index():
    return "HOME"

if __name__ == "__main__":
    app.run()

# flask --app app run