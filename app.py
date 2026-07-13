from flask import Flask
from routes.medicine import medicine_bp


app = Flask(__name__)

# Required for Flask session and flash messages
from config import FLASK_SECRET_KEY
app.secret_key = FLASK_SECRET_KEY
app.register_blueprint(medicine_bp)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
