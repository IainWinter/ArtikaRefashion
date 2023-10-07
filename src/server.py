from flask import Flask, app, jsonify

app = Flask(__name__)

def send_json(obj):
    response = jsonify(obj)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/')
def hello_world():
    return send_json({ "status": "ok"})

@app.route('/user_set_data')
def route_user_set_data():
    return send_json({ "status": "ok"})

if __name__ == '__main__':
    app.run()