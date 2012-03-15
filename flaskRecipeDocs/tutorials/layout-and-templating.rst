.. index::
   single: convention
   single: best practice
   single: authentication

.. _layout_and_templating_chapter:

Part 8  - Layout and Templating
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

You should now know enough to begin working on the prototype for our Recipe Website.
The prototype will implement the layout. 

We only want to worry about putting placeholder text in in the grids.
We will NOT concern ourselves with fancy css or images yet.

By the end of this tutorial you will have reviewed the following topics:

- Use the starter scaffold as a starting point for our application
- Create a global layout using the jinja2 templating language
- Retrieve a recipe by id from the database
- Implement a simple user login system

We will focus today on building this page:

.. image:: /images/viewrecipe.png


Setting up the Flask Starter Scaffold 
--------------------------------------------

A scaffold refers to a predetermined structure around which you can build an application.

.. note:: **Why Scaffolds?** Glad you asked! Over the next couple weeks you will be submitting work to be assessed, to simplify things 
    we've developed a standard way of starting and organizing your projects. Maintaining a standard approach means there is one less decision to make when building your applications. 

There are two scaffolds to be used in this course the names are listed below:

**Starter Scaffold**
    This is a simple approach, just enough folders to keep things organized

**GAE Scaffold**
    This arrangement is meant to accomodate projects that will be deployed to Google App Engine, due to the nature of GAE it is necessary to bundle more utilities in our package.

Today we will focus on the ``Starter Scaffold``.

.. note:: This section assumes that you have Virtualenv installed. You may find it helpful to 
          review the section entitled :ref:`virtualenv_section`

.. note:: You will need to download the Flask Starter Scaffold http://dl.dropbox.com/u/1004432/flask_starter.zip. If you are using Windows, just download it with your webbrowser.

1. Download and unzip the starter scaffold http://dl.dropbox.com/u/1004432/flask_starter.zip
copy `flask_starter` to `recipe_website` this effectively uses the flask_starter folder as the "blueprint" for your projects::

   wget http://dl.dropbox.com/u/1004432/flask_starter.zip
   unzip flask_starter
   cp -r flask_starter recipe_website

2. Enter the new `recipe_website` folder, bootstrap flask and activate your virtual environment
::

    cd recipe_website
    python bootstrapflask.py
    source venv/bin/activate

The unzipped directory structure looks something like this (for the sake of simplicity, only the key files and folders are listed below)::

	recipe_website
	├── app.py
	├── static
	│   ├── css
	│   ├── images
	│   └── js
	├── templates
	└── venv

Check to see that everything is working by running the following::

       python app.py

Visit your browser at http://localhost:5000, you should see something like the
image below:

.. image:: ../images/scaffoldview.png

.. note:: Point of Interest - the term "scaffold" comes from the construction industry and roughly means "structure".

If you are on a network with a proxy you will need to review :ref:`dealing_with_proxies` for setting your http_proxy environment variable.

Creating the routes (views) for our RecipeWebsite application
-------------------------------------------------------------------

Based on what we know about our application we can predict some of our required views.

The names below represent reasonably descriptive choices for our views, (later on, we may choose to use different names for our views):


/ or /frontpage
    a view which shows a home page, it is associated with the root of the website.

/recipe/<id>
    when viewing an individual recipe identified by its `id`, this view will be used to display all the information for that recipe.

/ingredient/<ingredient>
    search by ingredient, this view will return a list of recipes that have the particular ingredient.

/add/recipe
    It should be possible to add a new recipe using the 'submit a recipe' link.

/registration
    There needs to be a registration page, so that new users can sign up

/login
     This will be the view used for logging into the web application

The code for this might look something like:
::

    from flask import Flask, request, g,render_template, \ 
               url_for, redirect, flash
    import sqlite3, os

    SECRET_KEY = "the global object 'g' needs this"

    app = Flask(__name__) 
    app.config.from_object(__name__)


    # database method, which is triggered
    # before each request
    def connect_db():
        return sqlite3.connect('./recipes.db')

    @app.before_request
    def before_request():
        g.db = connect_db()

    @app.teardown_request
    def teardown_request(exception):
        g.db.close()

    @app.route('/frontpage')
    @app.route('/')
    def frontpage():
        # A query that returns recent recipes

        return render_template('frontpage.html',recipes=recipes) 

    @app.route('/recipe/<id>')
    def recipe(id):
        # A query to retrieve a recipe based on id
        return render_template('recipe.html',recipe=recipe) 

    @app.route('/ingredient/<ingredient>')
    def ingredient(ingredient):
        # A query to retrieve all recipes that match this ingredient
        return render_template('results.html',recipes=recipes) 


    @app.route('/add/recipe', methods=['POST'])
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
        

Adding a template in the `templates` folder
--------------------------------------------

.. note:: Templates go in the `templates` directory ``by convention``, it is not necessary to declare this anywhere in your code or configuration. Placing your templates in the the `templates` folder is enough.

.. note:: What do you think the phrase ``by convention`` means? What's the benefit of having conventions?

We will start by adding a new template called `recipe.html`. To make it very 
simple we will just put the phrase, "I am the recipe template".

::

    <h1>I am the recipe template</h1>

We will need a new route before this will work::

	@app.route('/recipe')
	def recipe():
	    return template('recipe.html')


View the new view in your browser
----------------------------------------

Start the application::

    python app.py

Then visit localhost:5000/recipe, you should see something like the image below.

    .. image:: ../images/recipetemplate.jpg

Passing variables to the template
-----------------------------------

By default, Flask uses Jinja2 as its templating system.

.. note:: Flask can use other templating systems such as Mako

Variables are generally passed to Jinja2 templates as key value pairs of a python dictionary.
Notice how this approach is used in the app.py file to pass the value of `name` to the index.html template. 
::

	@app.route('/')
	@app.route('/<name>')
	def index(name='Earth'):
	    return template('index.html',name=name)

We will find this useful later.

Template inheritance and a master (layout) template
-------------------------------------------------------

After a while we begin to see things that are common to all templates. Instead of repeating these elements
across different templates, we can share these elements by creating a global or master template.

A common pattern seen in application development, is to have a layout or master template. The other templates can then be configured to inherit from this global layout.

You can read more about the `template inheritance pattern`_ at the Flask website. 

In this step, we will create a master template called ``layout.html``. Our other templates will inherit common elements from the layout template.

Based on our mockups, most pages will be simpler than the front page so we will create a more generic template
based on the `index.html` template. 

.. image:: ../images/recipewebsite-template-innerpage.png

We'll create a new master template called 'layout.html' in the `templates` folder. We can use the `index.html` template as the starting point.

The simpler global template can be implemented with 3 rows instead of the 5 that we identified for the welcome page.

.. image:: ../images/simpletemplate.jpg

We will focus on row 2, we'll call the area highlighted in yellow ``content``. We add a replaceable ``block`` to our template.

We name our template `layout.html`::

	<!DOCTYPE html>
	<html>
	<head>
	<head>
	     <style>
		<!--
		@import url(http://dl.dropbox.com/u/1004432/decogrids-12-gapless.css);
		-->
	      </style>
	</head>
	<body>

		<div id="row-1" class="row">
		      <div class ="cell position-0 width-3">logo</div>
		      <div class ="cell position-3 width-6">the menu</div>
		      <div class ="cell position-9 width-3">search</div>
		</div>
		<div id="row-2" class="row">
		      <div class ="cell position-0 width-3">recipe sidebar</div>
		      <div class ="cell position-3 width-9">{% block content %}content goes here{% endblock %}</div>
		</div>
		<div id="row-3" class="row">
		      <div class ="cell position-0 width-3">popular ingredients</div>
		      <div class ="cell position-3 width-4">new recipes box</div>
		      <div class ="cell position-7 width-5">popular recipes box</div>
		</div>

	</body>
	</html>


We now have a ``content`` block.

Child templates - using our template
-------------------------------------
A child template inherits from the global template using a special ``extends`` tag.

Our recipe template can now be implemented like this
::

    {% extends "layout.html" %}

	    {% block content %}
	    <h1>I am the recipe template</h1>
	    {% endblock %}

.. note:: the indentation is optional but helps to make the child template more readable

It will look like this:

.. image:: ../images/recipetemplate-child.png

Notice how the ``content`` block of the child, overrides the original content block.

Adding AJAX to the template
---------------------------------
 We are now going to add some ajax functionality. For this we'll use jQuery.load() to load new page content without doing a full browser refresh. 

The pjax library takes advantage of the HTML history api, specifically the pushState and is able to load new content using ajax.

XXX we could use the github style page load

What's Next
----------------

- We will need an administrative interface so that administrators can easily add new users


- In what way do conventions make source code more maintainable?

- Read the import statements in the app.py file, what's the original name of the the ``template`` method? Can all of this be rewritten as a single import statement?



.. _the new hotness: http://s3.pixane.com/pip_distribute.png
.. _flask starter scaffold: http://dl.dropbox.com/u/1004432/flask_starter.zip
.. _article about App Engine charges: http://news.ycombinator.com/item?id=3431132
.. _blog post about using flask on GAE: http://www.joemartaganna.com/web-development/how-to-build-a-web-app-using-flask-with-jinja2-in-google-app-engine/
.. _template inheritance pattern: http://flask.pocoo.org/docs/patterns/templateinheritance/
.. _pjax: https://github.com/defunkt/jquery-pjax


