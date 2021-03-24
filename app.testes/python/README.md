## Flask
HTTP Server

### Configuration
$ export FLASK_APP='wsgi.py'

### Running Server
$ flask run
$ python -m flask run

### Externally Visible Server
$ flask run --host=0.0.0.0

### Debug Mode
```sh
$ export FLASK_ENV=development
$ flask run
```
OR
```sh
$ export FLASK_DEBUG=1
```
### Routing
```python
@app.route('/')
def index():
	return 'Index Page'
```
### Variable Rules
Its possible to mark sections with variable name.\
Use <variable-name> to define the variable and use it as a parameter variable in code.\
Use <type:variable-name> to define the type of the variable name.\

```python
@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % escape(username)
```
##### Variable types
- string = any text without a slash
- int    = accepts positive integers
- float  = accepts positivefloating point values
- path   = like string but also accepts slashes
- uuid	 = accepts UUID strings

### URL Building
To build a URL to a specific function, user the url_for() function.\
app.test_request_context() is used to handle a request even while used in a Python shell.\
url_for(function_name, kwargs).
#### Example

```python
from flask import Flask, url_for
from markupsage import escape

app = Flask(__name__)

@app.route('/')
def index():
	return 'index'

@app.route('/login')
def login():
	return 'login'

@app.route('/user/<username>')
def profile(username):
	return "{}\'s profile".format(escape(username))

with app.test_request_context():
	print(url_for('index'))
	print(url_for('login'))
	print(url_for('login', next('/'))
	print(url_for('profile', username='John Doe'))
```

### HTTP Methods

Flask will only answer to GET requests by default. It is needed to pass an list of methods to route() to use all the methods.\
If GET is present, Flask will add support for the HEAD method.

```python
from flask import request

app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return do_the_login()
	else:
		return show_the_login_form()
```

### Static Files
Share CSS and JS files. Files should be at /static/filename.ext 

```python
url_for('static', filename='style.css')
```

### Rendering Templates

To keep aplication secure is needed to do HTML escaping. To render a template it is used render_template('template_name.html', kwargs) where kwargs are keyword arguments used on the template engine.

```python
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)
``` 

### Request Object
The request object has data related to the request operation such as form and json data. It's available by using the method attribute when routing. If keys from request.form is not avaiable an HTTP 400 error is returned. To access parameters submitted in the URL use request.args.get('key')

### File Uploads

Files can be handled by Flask, the HTML form must have enctype="multipart/form-data" attribute.
Uploaded files are stored in memory or at a temporary location on the filesystem. Those can be acessed with request.files, ecah uploaded file is stored in that dictionary. It behaves like a python file, but it also has a save() method that allow to store that file in the filesystem of the server. Example:

```python
from flask import request
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('~/Desktop/amber-lab/MauserProject/app.testes/python/uploaded_files/file1.txt')

```

### Cookies

To access cookies use cookies dictionary attribute from the response object. To set cookie use the set_cookie() method of the response object.

##### Reading cookies
```python
@app.route('/')
def index():
	username = request.cookies.get('username')
```
##### Storing cookies

```python
@app.route('/')
def index():
	resp = make_response(render_template('hello.html'))
	resp.set_cookie('username', 'theusername')
	return resp


```

### Redirects and Errors

Use redirect() function to redirect user to another endpoint. Use abort() function to abort a request early with an error code.

```python
@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login')
def login():
	abort(401)
```

Error 401 is by default a black and white error page, to customize it use errorhandler() decorator

```python

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
```

### About Responses

The return value from a view funciton is automatically converted into a response object following these rules

- if a response object of the correct type is returned it's directly returned from the view
- if it's a string, a response object is created with that data and the default parameters
- if it's a dict, a response object is created using jsonify
- if a tuple is returned the items in the tuple can provide extra information to the response object. Such tuples have to be in the form(response, status), (response, headers), or (response, status, headers). The status value will override the code and headers can be a list or dictionary of adicional headers values.
- if none of those, Flask will assume the return value is a valid WSGI apllication and convert that into a response.

To manipulate the results can be used make_response().

```python
@app.errorhandler(404)
def not_fount(error):
	return render_template('error.html'), 404

# Wrap the return expression with make_response and modify it

@app.errorhandler(404)
def not_found(error):
	resp = make_response(render_template('error.html'), 404)
	resp.headers['something'] = 'value'
	return resp
```

### APIs with JSON

A common response when writing an API is JSON. A returned dictionary will be converted to a JSON response.

```python
@app.route("/me")
def me_api():
	user = get_current_user()
	return {"username":user.username, "theme":user.theme, "image":url_for("user_image", filename=user.image)}
```

To create JSON responses for types other than dictionaries use jsonify()

```python
@app.route("/users")
def users_api():
	users = get_all_users()
	return jsonify([user.to_json() for user in users])
```

### Sessions
Sessions allow to store information specific to a user from one request to the next. This is implemented on top of cookies, and signs it cryptographically. This means that the user could look at the contents of cookie but not modify it, unless they know the secret key used for signing. b

```python
from flask import Flask, session, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))
```

##### Generating a good secret keys:
```sh
$ python -c 'importos; print(os.urandom(16))'
```
