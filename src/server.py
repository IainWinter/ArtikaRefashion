from flask import Flask, request, app, jsonify, send_file
from data import *

app = Flask(__name__)

with app.app_context():
	init_tables()

@app.route('/')
def route_home_page():
    return send_file("static/community.html")

@app.route('/link_account')
def route_link_account_page():
    return send_file("static/link_account.html")

@app.route('/edit_account')
def route_edit_account_page():
    return send_file("static/edit_account.html")

def call_endpoint(request, endpoint_func, arg_list):
	args = [request.args.get(x) for x in arg_list]

	# catch invalid arguments  
	if any(x == None for x in args):
		return { "error": "invalid" }

	return endpoint_func(*args)

def call_endpointj(request, endpoint_func, arg_list):
    response = jsonify(call_endpoint(request, endpoint_func, arg_list))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/user_link_wallet')
def route_user_signin():
    return call_endpointj(request, user_link_wallet, ["wallet_id", "is_designer"])

@app.route('/user_set_data')
def route_user_set_data():
    return call_endpointj(request, user_set_info, ["wallet_id", "user_name", "user_address"])

@app.route('/user_get_data')
def route_user_get_data():
    return call_endpointj(request, user_get_info, ["wallet_id"])

if __name__ == '__main__':
    app.run()