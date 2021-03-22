from flask import Flask, url_for, render_template, request, jsonify
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
	if request.method == 'POST':
		input_json = request.get_json()
		print(input_json)
		return_json = {'answer':'LOGGED'}
		return jsonify(return_json)
