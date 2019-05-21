from bson import objectid
from flask import Flask, jsonify
from API.UserApi import user_route
from flask_cors import CORS
from Classes.Tools import Tools

app = Flask(__name__)

app.register_blueprint(user_route)

CORS(app)


@app.route("/")
def what():
    return jsonify({"What": "Authentication",
                    "Author": "AminJamal",
                    "NickName": "Includeamin",
                    "Email": "aminjamal10@gmail.com",
                    "WebSite": "includeamin.com"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3032, debug=True)
