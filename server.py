print('I am Server .....')

from flask import Flask, request, jsonify, make_response, abort
from flask_httpauth import HTTPBasicAuth

from functions_server import function_home_page, function_page_1, function_page_2, function_page_3, function_page_4
from functions_server import function_person_info, function_person_detail

#Authentication of REST the service
auth = HTTPBasicAuth()

port = '5000'
host = '0.0.0.0'

server_username = 'user'
server_password = '123'

rest_api_flask = Flask(__name__)
#rest_api_flask.secret_key = "SecretKeyMyApi"
#rest_api_flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@auth.get_password
def get_password(username):
    if username == server_username:
        return server_password
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@rest_api_flask.route("/")
def home_page():
    resp = function_home_page()
    return resp

@rest_api_flask.route("/Page_1")
def page_1():
    resp = function_page_1()
    return resp

@rest_api_flask.route("/Page_2")
def page_2():
    resp = function_page_2()
    return resp

@rest_api_flask.route("/Page_3")
def page_3():
    resp = function_page_3()
    return resp

@rest_api_flask.route("/Page_4")
def page_4():
    resp = function_page_4()
    return resp

@rest_api_flask.route("/Person_Info", methods=['GET', 'POST'])
def person_info():
    resp = function_person_info()
    return resp


@rest_api_flask.route("/Person_Detail", methods=['GET', 'POST'])
def person_detail():
    if not request.json or not 'first_name' in request.json:
        abort(400)
    first_name = request.json['first_name']
    if not request.json or not 'last_name' in request.json:
        abort(400)
    last_name = request.json['last_name']
    if not request.json or not 'age' in request.json:
        abort(400)
    age = request.json['age']
    if not request.json or not 'height' in request.json:
        abort(400)
    height = request.json['height']
    resp = function_person_detail(first_name, last_name, age, height)
    return jsonify({'full_name': resp})

def serve():
    certificateFile = 'xyz.crt'
    keyFile = 'xyz.key'
    # switch on or off certificates
    authorization_certificates = False
    if authorization_certificates:                      # certificates required
        rest_api_flask.run(host=host, port=port, debug=False, ssl_context=(certificateFile, keyFile))
    else:                                               # certificates not required
        rest_api_flask.run(host=host, port=port, debug=False)

if __name__ == '__main__':
    serve()