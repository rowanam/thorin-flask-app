import os
from flask import Flask


# Create and store an instance of Flask class
app = Flask(__name__)


# Add route decorator to created app
@app.route("/")
# When we navigate to route directory ("/"), flask triggers index() function
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True # Change to debug=False before production deployment or submission!
    )
