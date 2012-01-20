from bottle import route, run, template, static_file, debug

debug(True)


@route('/')
def index(name="what"):
    return template('templates/default',title="The Recipe Website", project="Recipe Website")

@route('/content')
def index(name="what"):
    return template('templates/content',title="The Recipe Website", project="Recipe Website")

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host='localhost', port=9080)
