import flask
from flask_restful import Api, Resource, reqparse, request
from dbase import db
import json



api = Api()
app = flask.Flask(__name__)
bs = db.database()


@app.route("/api_get", methods=["GET"])
def get():
    try:
        user_id = int(request.args.get("user_id"))
        if user_id == 0:
            return bs.send_json()
        else:
            return bs.read_message(user_id=user_id)
    except Exception:
        return {"Ошибка": "Хз что делать"}
    
@app.route("/api_del", methods=["DELETE"])
def delete():
    user_id = int(request.args.get("user_id"))
    try:
        bs.delete_message(user_id=user_id)
        file = bs.send_json()
        return file
    except Exception:
        return {"Ошибка": "Неверный запрос"}

@app.route("/api_post", methods=["POST"])
def post():
    try:
        user_id = int(request.args.get("user_id"))
        name = request.args.get("name")
        bs.write_in_data_base(user_id, name)
        file = bs.send_json()
        return file
    except Exception:
        return {"Ошибка": "ошибка в запросе"}

@app.route("/api_put", methods=["PUT"])
def put():
    try:
        user_id = int(request.args.get("user_id"))
        message = request.args.get("message")
        bs.send_message(user_id, message)
        file = bs.send_json()
        return file
    except Exception:
        return {"Ошибка": "ошибка в запросе"}

if __name__ == "__main__":
    app.run(debug=True)