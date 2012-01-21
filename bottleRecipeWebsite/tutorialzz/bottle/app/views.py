from bottle import TEMPLATE_PATH, route, jinja2_template as template
from models import *

TEMPLATE_PATH.append("./app/templates")

@route('/')
@route('/hello/:name')
def hello(name='Stranger'):
	return template('home.html', name=name)