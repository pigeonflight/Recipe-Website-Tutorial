.. index::
   single: jquery
   single: ajax
   single: jsonify

.. _databases_forms_and_file_uploads_chapter:

Part 5 - Databases, Forms and File Uploads
============================================================================

In this section we look at Databases and Forms

- request
- CRUD
- initializing a database
- Flask and requests
- file uploads with multipart forms

CRUD
-------------------------------
What does CRUD stand for?
This section explores how we can implement CRUD like behaviour using the available methods in Flask.

.. note:: CRUD stands for Create Read Update and Delete, it is usually associated with storing data in some kind of persistent backend such as a relational SQL database like MySQL or PostGreSQL or a key-value storage NOSQL database such as MongoDB.

Use Flask Starter to create the application
-----------------------------------------------

Download and unzip the starter scaffold http://dl.dropbox.com/u/1004432/flask_starter.zip
copy `flask_starter` to `user_crud`

Then bootstrap flask and activate the environment.

.. note:: this effectively uses the flask_starter folder as the "blueprint" for your projects::

   wget http://dl.dropbox.com/u/1004432/flask_starter.zip
   unzip flask_starter.zip
   cp -r flask_starter user_crud
   cd user_crud
   python bootstrapflask.py
   source venv/bin/activate

We're ready to go!

Creating the Database
--------------------------
This example uses an sqlite3 database that stores user information:
Let's create a simple schema in a file called ``schema.sql``::

  drop table if exists users;
  create table users (
  id integer primary key autoincrement,
  username string not null,
  fullname string not null,
  photo string not null
  );

And then use ``schema.sql`` to create a database called ``users.db``::

  sqlite3 users.db < schema.sql

Checklist of our application
------------------------------
Our application will do the following::

1. Allow basic CRUD by using a custom form
2. Store files on the file system in a folder called `uploads`

The application
--------------------
Below we have a simple program which implements CRUD for the users.db database,
We'll call it usercrud.py::

    from flask import Flask, request, g, os
    import sqlite3

    SECRET_KEY = "the global object 'g' needs this"

    app = Flask(__name__) 
    app.config.from_object(__name__)


    # database method, which is triggered
    # before each request
    def connect_db():
    return sqlite3.connect('./users.db')

    @app.before_request
    def before_request():
        g.db = connect_db()

    @app.teardown_request
        def teardown_request(exception):
        g.db.close()


    @app.route('/create')
    def create():
        fullname = request.form['fullname']
        username = request.form['username']
        photo = request.form['photo']
        

    @app.route('/read')
    def read():
        cur = g.db.execute('select fullname,username,photo from users order by id desc') 
        entries = [dict(fullname=row[0], username=row[1],photo=row[2]) for row in cur.fetchall()] 
        return render_template('users.html', entries=entries) 


    @app.route('/update')
    def update():

    @app.route('/delete')
    def delete():

    if __name__ == "__main__":
        app.debug = True
        app.run(port=9000)

.. note:: Notice that request object uses request.form to retrieve data that it expects to get from a form.

The Form  and Template
--------------------------
Go to the ``templates`` folder and create a template called users.html.

   cd templates
   cp index.html users.html

Make it look like this::

   {% extends "layout.html" %}
   {% block body %}
   <form action="{{ url_for('create') }}" method=post class=add-entry>
      <dl>
        <dt>Username:
        <dd><input type=text size=30 name=username>
        <dt>Fullname:
        <dd><input type=text size=30 name=fullname>
        <dt>Photo:
        <dd><input type=text size=30 name=photo>
        <dd><input type=submit value=Share>
      </dl>
    </form>
    <h2>List User here:</h2>
    <ul class=entries>
  {% for user in users %}
    <li>{{ user.fullname }}
    <li>{{ user.photo }}
    <li>{{ user.username }}
  {% else %}
    <li><em> No users yet</em>
  {% endfor %}
  </ul>

    
    {% endblock %}



File Uploads
------------------------------------
File uploads need a few more considerations when integrating them with your forms

Adding a form to your template
----------------------------------
Example with multi part form and using the
request.files

