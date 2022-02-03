from flask import Flask, jsonify, request, Response

from auth import is_allowed, goto_shave

app = Flask(__name__)


@app.route('/')
def index():
    response = {
        "status": 200,
        "message": "ok",
    }
    return response


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        content = request.json
        login = content.get('login')
        password = content.get('password')
        params = request.args
        if not login or not password:
            return jsonify({"error": "One of the required parameters is missing",
                            "description": "Use both login and password"}), 401
        elif is_allowed(login, password):
            return goto_shave(login, password, params)
        else:
            return jsonify({"error": "Access denied",
                            "description": "Use correct login and password"}), 403
    else:
        return jsonify({"error": "Method Not Allowed",
                        "description": "Use GET"}), 405


@app.route('/shave', methods=['GET'])
def shave():
    вернуть куки в виде сообщения


@app.route('/marketplace', methods=['GET'])
def marketplace():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
