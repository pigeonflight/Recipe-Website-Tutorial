.. index::
   single: views

.. _custom_views_chapter:

Starting the Project, Routes and Static Resources
==================================================

.. note:: If you are on campus, remember to declare the http_proxy BEFORE doing anything else.

       for Unix
            export http_proxy=scalpel:8080

       for Windows
            set http_proxy=scalpel:8080

In case you didn't get it working last time, this is a quick reminder of getting started.

We'll create a project called `RecipeWebsite`.

We will use the following directory structure::
    
	RecipeWebsite/
	└── recipewebsite
	    ├── static
	    └── templates

This structure will be especially valuable if we later decide to distribute our application as a python package.

Enter the `RecipeWebsite/recipewebsite` folder

Create a file called `app.py`
Your directory will now look like this
::

	RecipeWebsite/
	└── recipewebsite
	    ├── app.py
	    ├── static
	    └── templates

.. note::   .. image:: ../images/activate.gif
   Remember to activate your virtual environment!
   This will ensure that you are using an instance of python
   that is "aware" of the bottle package.

To view the new application in your browser run the following command::

    python app.py



Introducing Routes
----------------------

A route is a URL path and its associated method.

The following snippet is an example of a route named hello. The route is
the combination of a method called hello() and a @route decorated URL path.
::

	@route('/hello')
	def hello():
	    return "Hello World!"


Below is what our `app.py` file should look like at this time::

.. literalinclude:: ../../bottleRecipeWebsite/recipewebsite/app.py

The `@route` decorator is used to associate a metod to a URL path.


Associating templates with routes
----------------------------------

XXX FIXME discuss templates and routes



Static resources
----------------------------------
For our purposes we will want to have static files for css, javascript and image resources. By convention these resources are stored in the `static` folder.

Here are some things we can do:

- Add our own custom images to the static folder

- Move all css to the static folder, in our case we have an external link for our grid framework
  we will choose to host the grid css in our own static folder.


Discussion
------------

- What is a request?

- What is a response?

- The `root factory` (as the name implies) is what actually makes our new application root. Can you figure out where
  (meaning in what file) the `root factory` is declared and how it relates to the `models.py` file?

Lab Exercises
--------------

#. Create a new css file in the `static` folder, name it style.css

#. Link to the style.css file from the welcome.pt.

#. Make changes to the style.css
   so that the welcome.pt view looks more like the mockup. 

#. Add the css file that imports the grid styles to the `static` folder also and make sure that the grid
   system still works.
