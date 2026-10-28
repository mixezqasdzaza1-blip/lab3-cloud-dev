from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Cloud Lab!</h1><p>This app is running on Codespaces 🚀</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
