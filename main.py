from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    response = {
        "status": 200,
        "message": "ok",
    }
    return response


@app.route('/auth', methods=['POST'])
def auth():
    pass


@app.route('/shave', methods=['GET'])
def shave():
    pass


@app.route('/marketplace', methods=['GET'])
def marketplace():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
