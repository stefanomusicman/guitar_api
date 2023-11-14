from flask import Flask
from views.guitar_view import guitar
from database.__init__ import database

app = Flask(__name__)

app.register_blueprint(guitar)

print("DATABASE CONNECTION -> ", database.dbConnection)

# WRAPPER FUNCTION DEFINING THE ENDPOINT
@app.route("/")
def index():
    return "HOME"

if __name__ == "__main__":
    app.run()

# flask --app app run