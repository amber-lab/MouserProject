# Ferramentas
	- Flask: WSGI

# Termos
	- WSGI: Web Server Gateway Interface

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
