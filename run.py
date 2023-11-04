import os
from flask import Flask, render_template


# Create and store an instance of Flask class
app = Flask(__name__)


# Add route decorator to created app
@app.route("/")
# When we navigate to route directory ("/"), flask triggers index() function
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True # Change to debug=False before production deployment or submission!
    )
