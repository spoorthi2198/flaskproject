from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Use a stronger key in production

# Replace with your real client ID and secret
client_id = "86.apps.googleusercontent.com"
client_secret = "GOC"

google_bp = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    scope=["profile", "email"],
    redirect_to="welcome"
)

app.register_blueprint(google_bp, url_prefix="/login")

@app.route("/")
def index():
    return '<a href="/login/google">Login with Google</a>'

@app.route("/welcome")
def welcome():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    user_info = resp.json()
    return f"<h1>Welcome {user_info['email']}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
