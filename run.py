from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/time')
def time():
    # Return the current time in HH:MM:SS format
    return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

