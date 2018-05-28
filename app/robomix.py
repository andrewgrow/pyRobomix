from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1 style='color:blue'>Hello There 4!</h1>"


@app.route('/v1', methods=['POST'])
def api_request() -> str:
    return "Test response"


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
