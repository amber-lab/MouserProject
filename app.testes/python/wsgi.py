from flask import Flask, url_for, render_template, request, jsonify
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
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
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
