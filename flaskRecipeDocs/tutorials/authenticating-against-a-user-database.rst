.. index::
   single: convention
   single: best practice
   single: authentication
   single: user database

.. _authenticating_user_database_chapter:

Part 6  - Authenticating against a user database
===============================================================

At this point we have covered the following

:ref:`planning_mockups_chapter`
    Where we looked at process of planning the user interface (UI) of your application
:ref:`setting_up_dev_chapter`
    This looked at what we needed on our computer to get started.
    We also gained some experience with configuring views (routes) and templates by working on a simple application.
:ref:`deploying_application_chapter`
    We have explored the details of publishing your application to the web
:ref:`databases_forms_and_file_uploads_chapter`
    We used sqlite to create a database and created custom create and read methods that integrated with a Jinja2 template.

By the end of this tutorial you will have reviewed the following topics:

- Extending an existing login system
- Managing Users in a database
- Working with hashed passwords

The application
-------------------------------------------------------------------

This application will be an extension of the one we did in the last tutorial.
Download http://dl.dropbox.com/u/1004432/user_crud.zip
As a starting point.
::

   wget http://dl.dropbox.com/u/1004432/user_crud.zip
   unzip user_crud.zip
   cd user_crud
   python bootstrapflask.py
   source venv/bin/activate


A schema that stores usernames and passwords
----------------------------------------------
Look at the schema.sql file. Notice that it define two tables, ``users`` and ``logins``, we will use the ``logins` table to manage user login information.
::

    drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    fullname string not null,
    photo string not null
    );

    drop table if exists logins;
    create table logins (
    uid integer,
    username string not null,
    password string not null,
    FOREIGN KEY(uid) REFERENCES users(id)
    );

.. note:: What is the purpose of having a foreign key in a database?

Create the database (we'll call it users.db)::

   sqlite3 users.db < schema.sql

Adding users to the database
---------------------------------

We will use a simple python script ``adduser.py`` for adding new users.
It will write to the ``users.db`` database.

.. note:: Eventually we will want to create a form in Flask which makes it possible to add users

Create a new file called ``adduser.py`` with the following code
::
   
    import sqlite3
    import getpass

    password = getpass.getpass('your password: ')
    fullname = raw_input('your fullname: ')
    username = raw_input('your user: ')
    photo = raw_input('photo url: ')

    conn = sqlite3.connect('users.db')

    output = conn.execute('INSERT into users (fullname, photo) \
                         values (?, ? )',
                                     [fullname, photo])
    conn.commit()

    # get last id
    id = output.lastrowid
    conn.execute('INSERT into logins (uid,username, password) \
                         values (?, ?, ? )',
                                     [id,username,password])

    cur = conn.execute('SELECT * from logins order by uid desc')
    conn.commit()
    print cur.fetchall()
    cur.close()

Try out the application by launching it on the commandline::

    python adduser.py

.. note:: getpass is a useful utility for commandline python applications, notice that the password is not
           visible when being entered.

Beware of Clear Text Passwords
-----------------------------------
The code above, by default, stores passwords as clear text.

The python crypt module can be used to make 'hashes' of the password, we can then store the hashed passwords in our database
instead of the actual passwords.
::

     import crypt
     SECRET = 'an important secret'
     hashedpassword = crypt.crypt('password',SECRET)

In the lab you will be asked to use this method to ensure that passwords are stored in hashed format.

Notes for creating the flask app
----------------------------------
In a previous `Lecture on Authentication`_ (starting at slide 18), you will see notes on creating a login system. The code that actually authenticates the user is a method called login()
shown on slide number 20::

 @app.route('/login', methods=['GET', 'POST']) 
 def login():
    error = None 
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username' 
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password' 
        else: 
            session['logged_in'] = True
            flash('You were logged in') 
            return redirect(url_for('show_entries')) 
    return render_template('login.html', error=error)

The login method compares a hardcoded USERNAME and PASSWORD with the username and password submitted via a form. We will need to change the login method so that it queries the database instead. This will be an exercise in the lab.

.. note:: Additionally, this can be made more secure by storing passwords as hashed values, as  result when quering the database , you will need to hash the password to successfully compare the stored password hash with the password entered via the form.

What Next?
---------------
You will need to solve the following issues in the next lab:

- Make use of python's crypt module to hash passwords
- Integrate adding users via flask and a form 
- hash passwords entered via the form so that they can be compared to the login table
- Update the login system to support querying the users.db login table

.. _Lecture on Authentication: https://docs.google.com/a/alteroo.com/present/edit?id=0AVmqNRWnzBQ2ZHR2dGRwZl80MzJoazJycHFnaw
