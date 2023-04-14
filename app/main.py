from flask import Flask
import os

app = Flask(__name__)

variant = os.environ.get("VARIANT", "DEMO")

@app.route("/")
def hello():
    return f"Hello from Python!! ({variant})"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
