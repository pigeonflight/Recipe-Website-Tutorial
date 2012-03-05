.. index::
   single: jquery
   single: ajax
   single: jsonify

.. _databases_and_forms_chapter:

Part 5 - Databases and Forms
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

.. note:: CRUD stands for Create Read Update and Delete, it is usually associated with storing data in a some kind of persistent backend such as a relational SQL databases like MySQL and PostGreSQL or a key-value storage NOSQL database such as MongoDB.

Below we have a simple program which implements CRUD::

    from flask import Flask, request
    app = Flask(__name__) 

    @app.route('/create')
    def create():

    @app.route('/read')
    def read():

    @app.route('/update')
    def update():

    @app.route('/delete')
    def delete():

    if __name__ == "__main__":
        app.debug = True
        app.run(port=9000)

.. note:: Notice that request object uses request.form to retrieve data that it expects to get from a form.



File Uploads
------------------------------------
File uploads need a few more considerations when integrating them with your forms

Adding a form to your template
----------------------------------
Example with multi part form and using the
request.files

