.. index::
   single: jquery
   single: ajax
   single: jsonify

.. _databases_forms_and_file_uploads_chapter:

Part 5 - Databases, Forms and File Uploads
============================================================================
.. warning:: Do not use the code from this tutorial in production applications, it does not implement any verification or user security. For a more thorough and secure approach to file uploads read: http://flask.pocoo.org/docs/patterns/fileuploads/

In this section we look at Databases and Forms

- request
- CRUD
- initializing a database
- Flask and requests
- file uploads with multipart forms

.. note:: You will need images for this tutorial. Here are some small pictures for testing: http://dl.dropbox.com/u/1004432/bridges.zip

CRUD
-------------------------------
What does CRUD stand for?
This section explores how we can implement CRUD like behaviour using the available methods in Flask.

.. note:: CRUD stands for Create Read Update and Delete, it is usually associated with storing data in some kind of persistent backend such as a relational SQL database like MySQL or PostGreSQL or a key-value storage NOSQL database such as MongoDB.

Use Flask Starter to create the application
-----------------------------------------------

We will do the following:

1. Download and unzip the starter scaffold http://dl.dropbox.com/u/1004432/flask_starter.zip

2. copy `flask_starter` to `user_crud`

3. Then bootstrap flask and activate the environment.

::

   wget http://dl.dropbox.com/u/1004432/flask_starter.zip
   unzip flask_starter.zip
   cp -r flask_starter user_crud
   cd user_crud
   python bootstrapflask.py
   source venv/bin/activate


.. note:: What we've done is use the `flask_starter` folder as the "blueprint" for our new `user_crud` project. 

We're ready to go!

Creating the Database
--------------------------
.. note:: We are using sqlite3 NOT sqlite. You may need to install it for your operating system.

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
2. Upload files (pictures) to the file system into a folder called `uploads`
3. Retrieve and display the files for visitors 

The application
--------------------
Below we have a simple program which implements CRUD for the users.db database,
We'll call it ``usercrud.py``::

    from flask import Flask, request, g,render_template, \ 
               url_for, redirect, flash
    import sqlite3, os

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


    @app.route('/create', methods=['POST'])
    def create():
        fullname = request.form['fullname']
        username = request.form['username']
        photo = request.form['photo']
        g.db.execute('insert into users (fullname, username, photo) \
                         values (?, ?, ?)',
                                     [fullname, username, photo])
        g.db.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('read'))
        

    @app.route('/read')
    @app.route('/')
    def read():
        cur = g.db.execute('select fullname,username,photo \
                       from users order by id desc') 

        users = [dict(fullname=row[0], username=row[1],photo=row[2]) \
                               for row in cur.fetchall()] 

        return render_template('users.html',users=users) 


    @app.route('/update')
    def update():
        # we will add this code later
        pass

    @app.route('/delete')
    def delete():
        # we will add this code later
        pass

    if __name__ == "__main__":
        app.debug = True
        app.run(port=9000)

.. note:: We are about to create a form in a template called ``users.html``. Notice that we use the ``request.form`` object to retrieve data from our form. Why do we have to use the POST method for create?

The Form  and Template
--------------------------
Go to the ``templates`` folder and create a template called users.html.
::

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

Testing it out so far
----------------------------
Start the application::

    python usercrud.py

Visit http://localhost:9000/

1. Try adding a new entry (for the photo put a URL e.g. http://blah.com/myimage.jpg)
2. How would you modify the code so that photo is displayed?
3. Why does the read() function have two @app.route() decorators?
4. How would you get the images to display? Hint: <img src...
5. What improvements do we need for this application?
   Hint: Think security, validation, user experience.


File Uploads
------------------------------------
File uploads need a few more considerations when integrating them with your forms

File uploads depend on the ``request.files`` object.

Create a folder called ``uploads``::

   mkdir uploads

Update the users.html template to support multi part forms, by declaring the enctype::

    <form enctype="multipart/form-data" method="post">

Change the input type for photo::

    <input type=file name=photo>

Update the create() method to look like this::

    @app.route('/create', methods=['POST'])
    def create():
        fullname = request.form['fullname']
        username = request.form['username']
        file = request.files['photo']
        photo = file.filename
        file.save(os.path.join('uploads', photo))
        g.db.execute('insert into users (fullname, username, photo) \
                         values (?, ?, ?)',
                                     [fullname, username, photo])
        g.db.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('read'))

.. note:: ``request.files['photo']`` returns an object with additional properties and methods such as ``filename`` and ``save()``


**Questions**

1. What happens if we don't have the enctype set properly?
2. What if  a user does not upload an image?

Displaying Files
----------------------------------
We will now add a new function which can be used to retrieve files from the filesystem.
We'll use a special method called ``send_from_directory``.
::

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory('uploads',
                               filename)

Modify the template to make use of our new route::

   <img src="/uploads/{{filename}}" />

.. note:: Try visiting localhost:9000/uploads/{YOUR FILE NAME} and see what happens. If you've done everything and it still breaks, then make sure that you have imported 'send_from_directory' at the top in your imports
  
 
More about Flask and Uploading
--------------------------------
For a more thorough and secure approach to file uploads read:
http://flask.pocoo.org/docs/patterns/fileuploads/



What Next?
-------------
What more features do we need?

1. A way to standardize images
2. To make it a complete CRUD application, we need a way to update and delete.
3. A way to enforce the file type
4. A login/logout system and authentication

Expect to solve these and other problems in the next lab.
