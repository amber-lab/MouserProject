from flask import Flask, url_for, render_template, request, jsonify, make_response, redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def data():
    return {'name' : 'Leo', 'age' : 24, 'city' : 'Valpaços'}

@app.route('/test')
def testme():
	return "PASS"

@app.route('/static')
def getStatic():
	return url_for('static', filename='style.css')

@app.route('/hello/')
@app.route('/hello/<string:name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
	print("\n", dir(request), "\n\n")
	if request.method == 'POST':
		input_json = request.get_json()
		print(input_json)
		return_json = {'answer':'LOGGED'}
		return jsonify(return_json)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		print("--------\n",secure_filename(file.filename),"\n--------")
	return render_template('file_upload_template.html')

@app.route('/cookietest')
def cookietest():
	req = request.cookies.get('username')
	if req:
		print("Has cookie")
		return redirect('/hello/'+req)
	else:
		print("No cookie for you! :P")
		return redirect('/hello')

@app.route('/setcookie')
@app.route('/setcookie/<string:usr>')
def setcookie(usr=None):
	print("\n\n",usr,"\n\n")
	if usr and not request.cookies.get('username'):
		resp = make_response(render_template('hello.html', name=usr))
		resp.set_cookie('username', usr)
		print("Cookie defined")
		return resp
	else:
		return "No cookie to define or already defined"
