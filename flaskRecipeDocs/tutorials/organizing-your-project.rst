.. index::
   single: convention
   single: best practice

.. _organizing_project_chapter:

Part 4 - Organizing your Project / UI and Simple Templating
===============================================================

At this point we have covered the following

:ref:`planning_mockups_chapter`
    Where we looked at process of planning the user interface (UI) of your application
:ref:`setting_up_dev_chapter`
    This looked at what we needed on our computer to get started.
    We also gained some experience with configuring views (routes) and templates by working on a simple application.
:ref:`deploying_application_chapter`
    We have explored the details of publishing your application to the web

You should now know enough to begin working on the prototype for our Recipe Website.

Setting up the Flask Starter Scaffold 
--------------------------------------------

A scaffold refers to a predetermined structure around which you will build your applications.

.. note:: **Why Scaffolds?** Glad you asked! Over the next couple weeks you will be submitting work to be assessed, to simplify things 
    We've developed a standard way of starting and organizing your projects. Maintaining a standard approach means there is one less decision to make when building your applications. 

There are two scaffolds to be used in this course the names are listed below:

**Starter Scaffold**
    This is a simple approach, just enough folders to keep things organized

**GAE Scaffold**
    This arrangement is meant to accomodate projects that will be deployed to Google App Engine, due to the nature of GAE it is necessary to bundles more utilities in our package.

Today we will focus on the ``Starter Scaffold``.

.. note:: This section assumes that you have Virtualenv installed. You may find it helpful to 
          review the section entitled :ref:`virtualenv_section`

.. note:: You will need to download the Flask Starter Scaffold http://dl.dropbox.com/u/1004432/flask_starter.zip. If you are using Windows, just download it with your webbrowser.

1. Download and unzip the starter scaffold http://dl.dropbox.com/u/1004432/flask_starter.zip
copy `flask_starter` to `recipe_website` this effectively uses the flask_starter folder as a template::

   wget http://dl.dropbox.com/u/1004432/flask_starter.zip
   unzip flask_starter
   cp flask_starter recipe_website

1. Enter the new `recipe_website` folder, bootstrap flask and activate your virtual environment::

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

Visit your browser at http://localhost:6543, you should see something like the
image below:

.. image:: ../images/scaffoldview.png

If you are on a network with a proxy you will need to review :ref:`dealing_with_proxies` for setting your http_proxy environment variable.

Creating the views for our RecipeWebsite application
-------------------------------------------------------

Based on the nature of our application we can predict some of our required views.

The names below represent reasonably descriptive choices for our Views, (later on, we may choose to use different names for our views):


welcome
    a view which shows a welcome or home page, it is associated with the root of the website.

recipe
    when viewing an individual recipe, this view will be used to display all the information for that recipe.

queryby_ingredient
    search by ingredient, this view will return a list of recipes that have the particular ingredient.

submitrecipe
    It should be possible to add a new recipe using the 'submit a recipe' link.

registration
    There needs to be a registration page, so that new users can sign up

faq
     This will be a simple view that lists common questions about the web application

.. note:: Point of Interest - the term "scaffold" comes from the construction industry and roughly means "structure".


Adding a template in the `templates` folder
--------------------------------------------

.. note:: Templates go in the `templates` directory ``by convention``, it is not necessary to declare this anywhere in your code or configuration. Placing your templates in the the `templates` folder is enough.

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

Then visit localhost:6543/recipe, you should see something like the image below.

    .. image:: ../images/recipetemplate.jpg

Template inheritance
-----------------------------------

A common pattern seen in application development, is to have a layout or master template. The other templates can then be configured to inherit from this global layout.

You can read more about the `template inheritance pattern`_ at the Flask website.

Passing variables to the template
-----------------------------------

Flask uses Jinja2 templates by default.
Variables are generally passed to Jinja2 templates as key value pairs of a python dictionary.
Notice how this approach is used in the app.py file to pass the value of `name` to the index.html template. 
::

	@app.route('/')
	@app.route('/<name>')
	def index(name='Earth'):
	    return template('index.html',name=name)


Defining macros and slots, creating a master template
--------------------------------------------------------

After a while we begin to see things that are common to all templates. Instead of repeating these elements
across different templates, we can share these elements by creating a global or master template.
New templates can be made to inherit from the master template.
In our case the `index.html` template is a good starting point.


Based on our mockups, most pages will be simpler than the front page so we will create a more generic template
based on the `index.html` template. 

.. image:: ../images/recipewebsite-template-innerpage.png

We'll create a new master template called 'global.html' in the `templates` folder. We can use the `index.html` template as the starting point.

The simpler global template can be implemented with 3 rows instead of 5 in the welcome template.

.. image:: ../images/simpletemplate.jpg


XXX Fix me
need to say something about template inheritance

We will pull this off using template inheritance

see: http://flask.pocoo.org/docs/patterns/templateinheritance/

We name our template `global.html`::

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
		   <div class ="cell position-0 width-3">
		       LOGO will go here
		   </div>


Discussion
-----------

- Did we need to declare where to look for templates and static files?

- What does the phrase "by convention" mean? What conventions have we seen today? What's the purpose of having conventions?

- In what way do conventions make source code more maintainable?



.. _the new hotness: http://s3.pixane.com/pip_distribute.png
.. _flask starter scaffold: http://dl.dropbox.com/u/1004432/flask_starter.zip
.. _article about App Engine charges: http://news.ycombinator.com/item?id=3431132
.. _blog post about using flask on GAE: http://www.joemartaganna.com/web-development/how-to-build-a-web-app-using-flask-with-jinja2-in-google-app-engine/
.. _template inheritance pattern: http://flask.pocoo.org/docs/patterns/templateinheritance/
