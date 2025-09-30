# main.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, DevOps Students! Version 666.0"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
