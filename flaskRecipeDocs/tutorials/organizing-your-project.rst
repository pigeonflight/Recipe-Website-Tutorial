.. index::
   single: convention
   single: best practice

.. _organizing_project_chapter:

Part 3 - Organizing your Project / UI and Simple Templating
===============================================================

At this point we have covered the following

:ref:`planning_mockups_chapter`
    Where we looked at process of planning the user interface (UI) of your application
:ref:`setting_up_dev_chapter`
    This looked at what we needed on our computer to get started.
    We also gained some experience with the framework by creating a simple application.

You should be able to create a simple web application now.

Setting up the Flask Starter Scaffold 
--------------------------------------------

A scaffold refers to a predetermined structure around which you will build your applications.

.. note:: **Why Scaffolds?** Glad you asked! Over the next couple weeks you will be submitting work to be assessed, to simplify things 
    We've developed a standard way of organizing your projects. Maintaining a standard approach means there is one less decision to make when building your applications. 

There are two scaffolds to be used in this course the names are listed below:

**Starter Scaffold**
    This is a simple approach, just enough folders to keep things organized

**GAE Scaffold**
    This arrangement is meant to accomodate projects that will be deployed to Google App Engine, it will seem to be lots of folders, most of them play a supporting role, but all are useful.

Today we will focus on the ``Starter Scaffold``.

.. note:: This section assumes that you have Virtualenv installed. You may find it helpful to 
          review the section entitled :ref:`virtualenv_section`

You will need to download the Flask Starter Scaffold http://dl.dropbox.com/u/1004432/flask_starter.zip
It is best to place it in the same folder where you have your `venv` folder.

Activate your virtual environment (we're assuming that you already installed Flask)::

   source venv/bin/activate

Download and unzip the starter scaffold http://dl.dropbox.com/u/1004432/flask_starter.zip:

The unzipped directory structure looks something like this (for the sake of simplicity, only the key files and folders are listed below)::

	flask_starter
	├── app.py
	├── static
	│   ├── css
	│   ├── images
	│   └── js
	└── templates
	    └── index.tpl

Check to see that the scaffold is working by running the following::

The instructions below are for Unix, but
similar steps can be taken on Windows.

#. Copy `flask_starter` to `MyApp`::

       cp -r flask_starter MyApp

#. Activate your Python virtual environment (if you haven't done so already)::

       source venv/bin/activate

#. Test that it is working by launching the default app::

       cd MyApp
       python app.py

Visit your browser at http://localhost:6543, you should see something like the
image below:

.. image:: ../images/scaffoldview.png

If you are on a network with a proxy then pay careful attention to the next section.

.. _campus_proxies:

Dealing with on campus proxies
-------------------------------

.. note: All the examples below are specific to the UWI Mona network, but should be applicable to other 
locations that use a proxy on their network.

**Known UWI proxies** 
	scalpel, proxy-cluster, proxy1, proxy3, sword
        while we use `scalpel` in our examples
        any of the ones listed should work

- All proxies are configured to run on port 8080. 

After launching the terminal (or commandline) it is important to set the http_proxy
environmental variable, BEFORE running any other command

**On Unix** 

::

   export http_proxy=proxy3:8080

**On Windows** 

the same can be acheived by using `set` instead of `export`::


   set http_proxy=proxy3:8080

.. note:: For persons using `sudo` on Unix. Be careful if you use `sudo` on Unix, `sudo` may not inherit the http_proxy environment variable if you set it without `sudo`.


Creating the views for our RecipeWebsite application
-------------------------------------------------------

Based on the nature of our application we can predict some of views
that we will need.

The names below represent reasonable descriptive choices for our Views:

welcome
    a view which shows a welcome or home page, it is associated with the root of the website.

recipe
    when viewing an individual recipe, this view will be used to display all the information for that recipe.

ingredient
    search by ingredient, this view will return a list of recipes that have the particular ingredient.

submitrecipe
    It should be possible to add a new recipe using the 'submit a recipe' link.

registration
    There needs to be a registration page, so that new users can sign up

faq
     This will be a simple view that lists common questions about the web application

Flask does not provide a standard way to manage our code, so we will rely on our `flask starter scaffold`_ to ensure that our applications have a standard and predictable folder structure. 

Our application will have the following sections

You can download our `flask starter app`_ to get going.

.. note:: the term "scaffold" comes from the construction industry and roughly means "structure".


Copy the flask_starter folder to RecipeWebsite::

       cp -r flask_starter RecipeWebsite
    
Enter the `RecipeWebsite` folder

The 

Adding a template in the `templates` folder
--------------------------------------------

In the `templates` folder we will add a new template called `recipe.pt`. To make it very 
simple we will just put the phrase, "I am the recipe template".

::

    <h1>I am the recipe template</h1>

View the new view in your browser
----------------------------------------

Start the application::

    pserve development.ini

Then visit localhost:6543/recipe_view, you should see something like the image below.

    .. image:: ../images/recipetemplate.jpg

Passing variables to the template
-----------------------------------

Variables are generally passed to Chameleon templates as key value pairs of a python dictionary.
Notice how this approach is used to define the 'project' in the root template `my_view`.

::

	@view_config(context=RecipeSite, renderer='templates/welcome.pt')
		def my_view(request):
		    return {'project':'RecipeWebsite'}

Defining macros and slots, creating a master template
--------------------------------------------------------

After a while we begin to see things that are common to all templates. Instead of repeating these elements
across different templates, we can share these elements by creating a global or master template.
New templates can be made to inherit from the master template.
In our case the `welcome.pt` template is a good starting point.


Based on our mockups, most pages will be simpler than the front page so we will create a more generic template
based on the `welcome.pt` template. 

.. image:: ../images/recipewebsite-template-innerpage.png

We'll create a new master template called 'global.pt' in the `templates` folder. We can use the `welcome.pt` template as the starting point.

The simpler global template can be implemented with 3 rows instead of 5 in the welcome template.

.. image:: ../images/simpletemplate.jpg


Pay attention to the following changes:

- the addition of a `metal:define-macro` line

- the addition of a `define-slot` which will act as a replaceable region.

- in general this template is more generic

We name our template `global.pt`::

	<!DOCTYPE html>
	<html
	      xmlns:metal="http://xml.zope.org/namespaces/metal"
	      xmlns:tal="http://xml.zope.org/namespaces/tal"
	      metal:define-macro="layout">
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

- What is the benefit have a standard directory structure?

- We used pip to install the Flask package, in python circles packages are often called `eggs`, can you guess why?

- In what way do conventions make source code more maintainable?

- Any thoughts on what happens when you use virtualenv and the `source bin/activate` command? 

- What do you think happens when you set the `http_proxy` environment variable.?

.. _the new hotness: http://s3.pixane.com/pip_distribute.png
.. _flask starter scaffold: http://dl.dropbox.com/u/1004432/flask_starter.zip
.. _article about App Engine charges: http://news.ycombinator.com/item?id=3431132
.. _blog post about using flask on GAE: http://www.joemartaganna.com/web-development/how-to-build-a-web-app-using-flask-with-jinja2-in-google-app-engine/
