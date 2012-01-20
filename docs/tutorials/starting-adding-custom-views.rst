.. index::
   single: views

.. _custom_views_chapter:

Starting the Project, Adding Custom Views
===========================================

Key concepts
---------------

**resource tree**
    The collection of traversable resources within an application. It is most comparable to a filesystem. The diagram
    below demonstrates a graphical representation of a simple resource tree of recipes.

    .. image:: ../images/reciperesourcetree.jpg
    The traversal path highlighted in pink could also be represented as the following path **/recipe/preparationtime**

**traversal**
   The act of stepping through a resource tree. Traversal is similar to navigating through
a folder hierarchy in a filesystem. Depending on the type of object being viewed   

**context**
    The context refers to  a resource in the resource tree which is accessed during traversal. The properties associated with the current context will vary but can include properties such as
the location in the resource tree, the object type etc..

**root**
    This refers to the object at the top of the resource tree. This object is usually configured to provide a `root factory`, all other objects are added below the root. This is analagous to the root of a filesystem.

**view**
    Properly known as a 'view callable' is callable python code that accepts a request as an argument and returns a response. Some view callables also accept an additional `context` argument. 

Since context is important when traversal is involved, most of the views that we work with on this project will be "context sensitive".



Creating the project with pcreate
-----------------------------------------

In case you didn't get it working last time, this is a quick reminder of getting started.
We'll create a project called `RecipeWebsite`.

.. note:: If you are on campus, remember to declare the http_proxy BEFORE doing anything else.

       for Unix
            export http_proxy=scalpel:8080

       for Windows
            set http_proxy=scalpel:8080

::

    bin/pcreate -s zodb RecipeWebsite

You will see output similar to this (the output has been truncated)::

    Creating directory ...
      Recursing into +package+
    ...
    Welcome to Pyramid.  Sorry for the convenience.

The result will be a directory structure like this (we've left out the files, this just lists the directories::
    
	RecipeWebsite/
	├── recipewebsite
	│   ├── static
	│   ├── templates

Enter the `RecipeWebsite` folder and install the new package::

    pip install -e .


Configuring the root
----------------------

Look under the `recipewebsite` directory
(I've added a '*' at the end of important files).
::

	RecipeWebsite/recipewebsite/
	├── __init__.py
	├── models.py*
	├── static
	│   ├── favicon.ico
	│   ├── footerbg.png
	│   ├── headerbg.png
	│   ├── ie6.css
	│   ├── middlebg.png
	│   ├── pylons.css
	│   ├── pyramid-small.png
	│   ├── pyramid.png
	│   └── transparent.gif
	├── templates
	│   └── mytemplate.pt*
	├── tests.py
	├── views.py*

The `root` object is configured in the `models.py` file.

Instead of the name `MyModel`, we want to give our root the more descriptive name `RecipeSite`.

This is a cosmetic change, but the new name makes more sense for a recipe website.

The new models.py file will look like this.
::

	from persistent.mapping import PersistentMapping

	class RecipeSite(PersistentMapping):
	    __parent__ = __name__ = None

	def appmaker(zodb_root):
	    if not 'app_root' in zodb_root:
		app_root = RecipeSite()
		zodb_root['app_root'] = app_root
		import transaction
		transaction.commit()
	    return zodb_root['app_root']

.. note:: The `views.py` file depends on the `models.py` file so before we can use our new model. We need to make appropriate adjustments to the `views.py` file. Read the next section and see if you can figure out what needs to be fixed.
 

Introducting Views
----------------------

A `view` (or view callable) is **python code that accepts a request and returns a response**. 

Views are often associated with templates. These templates work with the views to provide a user interface.
The user experience for an application is based around a collection of views.

In a Pyramid application views and their templates are normally managed in the `views.py` file.

Below is what our `views.py` file should look like at this time::

	from pyramid.view import view_config
	from .models import RecipeSite

	@view_config(context=RecipeSite, renderer='templates/mytemplate.pt')
	def my_view(request):
	    return {'project':'RecipeWebsite'}

The `@view_config` decorator is placed just before the view and is used to tell the view its
`context` and `renderer`, which in this case is the `mytemplate.pt` template.




Replacing the default template
----------------------------------

The `views.py` file contains configuration information which makes reference to the default template.
We will replace the current template called `mytemplate.pt` with `the code from the previous tutorial`_

If we look at the `mytemplate.pt` file there is only one dynamic variable called ${project}. Here is the snippet from
the template::

    <div id="middle">
      <div class="middle align-center">
        <p class="app-welcome">
          Welcome to <span class="app-name">${project}</span>, an application generated by<br/>
          the Pyramid web application development framework.
        </p>
      </div>
    </div>

Let's create a template of our own based on `the code from the previous tutorial`_, this time around 
we will also add proper doctypes and make it a fully valid html file.
We just want to keep the welcome content::

        <p class="app-welcome">
          Welcome to <span class="app-name">${project}</span>, an application generated by<br/>
          the Pyramid web application development framework.
        </p>

Using our previous grid we'll create a new template in the `templates` folder
 called `welcome.pt` which will look
something like this::

       <!DOCTYPE html>
	<html>
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
			<p class="app-welcome">
			  Welcome to <span class="app-name">${project}</span>, 
                          an application generated by<br/>
			  the Pyramid web application development framework.
			</p>
		</div>
		  <div class ="cell position-3 width-6">the menu</div>
		  <div class ="cell position-9 width-3">search</div>
	    </div>
	    <div id="row-2" class="row">
		  <div class ="cell position-0 width-3">submit a recipe</div>
		  <div class ="cell position-3 width-9">highlight recipes</div>
	    </div>
	    <div id="row-3" class="row">
		  <div class ="cell position-0 width-3">popular ingredients</div>
		  <div class ="cell position-3 width-4">new recipes box</div>
		  <div class ="cell position-7 width-5">popular recipes box</div>
	    </div>
	    <div id="row-4" class="row">

		  <div class ="cell position-3 width-9">Recipe Categories</div>
	    </div>
	    <div id="row-5" class="row">
		  <div class ="cell position-0 width-3">I heart Recipes</div>
		  <div class ="cell position-3 width-4">footer stuff</div>
		  <div class ="cell position-7 width-5">social stuff</div>
	    </div>
            </body>

We need to edit the `views.py` file so that our new `welcome.pt` template is used instead of
the `mytemplate.pt` template.
::

	from pyramid.view import view_config
	from .models import RecipeSite

	@view_config(context=RecipeSite, renderer='templates/welcome.pt')
	def my_view(request):
	    return {'project':'RecipeWebsite'}
	

.. _the code from the previous tutorial: https://gist.github.com/1636270

Try it out
------------
It is recommended that you delete the Data.fs file if it exists. This is ZODB file where the resource tree is stored. Otherwise it is possible that the old version of the resource tree with the 'MyModel' root object will persist and cause errors.

Go to the application directory and run::

   pserve development.ini

I got the following view (the dynamic part of the template has been highlighted):

.. image:: ../images/recipewebsite-template.jpg

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
