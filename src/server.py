from flask import Flask, request, app, jsonify
from data import *

app = Flask(__name__)

def call_endpoint(request, endpoint_func, arg_list):
	args = [request.args.get(x) for x in arg_list]

	# catch invalid arguments  
	if any(x == None for x in args):
		return { "error": "invalid" }

	return endpoint_func(*args)

def call_endpointj(request, endpoint_func, arg_list):
	return jsonify(call_endpoint(request, endpoint_func, arg_list))

def send_json(obj):
    response = jsonify(obj)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/user_create')
def route_user_create():
    return call_endpointj(request, user_create, ["wallet_id"])

@app.route('/user_set_data')
def route_user_set_data():
    return call_endpointj(request, user_set_info, ["wallet_id", "user_name", "user_address"])



if __name__ == '__main__':
    app.run()