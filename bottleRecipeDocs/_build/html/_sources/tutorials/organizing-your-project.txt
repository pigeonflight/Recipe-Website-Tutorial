.. index::
   single: convention
   single: best practice

.. _organizing_project_chapter:

Part 4 - Organizing your Project
===========================================

At this point we have covered the following

:ref:`planning_mockups_chapter`
    Where we looked at process of planning the user interface (UI) of your application
:ref:`setting_up_dev_chapter`
    This looked at things we may need on our computer to get started 
:ref:`basic_application_chapter`
    Here we gained some experience with the framework by creating a simple application 

You should feel comfortable creating a simple application now.


The Scaffolds
----------------

In the context of this course, a scaffold refers to a predetermined structure around which you will build your applications.

.. note:: **Why Scaffolds?** Glad you asked! Over the next couple weeks you will be submitting work to be assessed, to simplify things 
    we've developed a standard approach for organizing your projects which we will call the `bottle starter scaffold`. By agreeing on a standard approach it means there is one less decision to make when building your applications. 

There are two scaffolds to be used in this course we will be looking at the first today, the `bottle starter scaffold`. 
In additon to the `bottle starter scaffold` future projects will be arranged around the `bottle gae scaffold`, these names will make more sense in time. 

Starter Scaffold
    This is a simple approach, just enough folders to keep things organized

GAE Scaffold
    This arrangement is meant to accomodate projects that will be deployed to Google App Engine, it will seem to be lots of folders, most of them play a supporting role, but all are useful.

Today we will focus on the following:

- Virtualenv
- the Bottle Starter Scaffold

Using Virtualenv
------------------

.. note:: This section assumes that you have Virtualenv installed. You may find it helpful to review the section entitled 
:ref:`virtualenv_section`

To install Bottle, create a virtualenv::

   mkdir venv
   cd venv
   virtualenv --no-site-packages .

When ever you need to use this environment use the command::

   cd venv
   source bin/activate

On Windows there should be a `Scripts` directory not a `bin` directory, also there is no need for the
`source` command, the following is enough::

   cd venv
   Scripts/activate

.. note::  

   Remember to activate your virtual environment!
       .. image:: ../images/activate.gif

   If you neglect this, `pip` will behave in unpredictable ways,
   you will get permission errors
   and other strange behaviour.

Then install bottle using the pip command::

    pip install bottle

.. note:: `pip` stands for "Pip Installs Packages", it is a package installer designed to install python packages (similar to apt-get on Debian or Ubuntu).
        It has been affectionately referred to as `the new hotness`_.

Setting up the Bottle Starter Scaffold 
--------------------------------------------

You will need

- The Bottle GAE Scaffold http://dl.dropbox.com/u/1004432/bottle_starter.zip
- Virtualenv

Activate your virtual environment and, if you haven't done so yet, install Bottle::

   cd venv
   source bin/activate
   pip install bottle

Download and unzip the starter scaffold http://dl.dropbox.com/u/1004432/bottle_starter.zip:

The unzipped directory structure looks something like this (for the sake of simplicity, only the key files and folders are listed below)::

	bottle_starter
	├── app.py
	├── ez_setup.py
	├── static
	│   ├── css
	│   ├── images
	│   └── js
	└── templates
	    └── index.tpl

Check to see that the scaffold is working by running the following inside the `bottle_starter`::


Summary of develop/deploy cycle
-------------------------------------

By now you will have downloaded the starter scaffold and unzipped in to a convenient location.

The instructions below are for Unix, but
similar steps can be taken on Windows.

#. Copy `bottle_starter` to `MyApp`::

       cp bottle_starter MyApp

#. Activate your Python virtual environment::

       source venv/bin/activate

#. Test that it is working by running launching the app::

       cd MyApp
       python app.py

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


Beginning our RecipeWebsite application
-----------------------------------------

Establishing conventions help to make source code more maintainable, while Bottle does not provide a standard approach to managing our code. Thanks to `bottle starter scaffold`_ we will have a standard folder structure. 

You can download our `bottle starter app`_ to get going.

.. note:: the term "scaffold" comes from the construction industry and roughly means "structure".


We will use the following directory structure::
    
	RecipeWebsite/
	└── recipewebsite
	    ├── static
	    └── templates

This structure will be very useful if we later on decided to make our site into a full python packages.

Enter the `RecipeWebsite/recipewebsite` folder

.. note::   .. image:: ../images/activate.gif
   Remember to activate your virtual environment!

Create a file called `app.py`
Your directory will now look like this
::

	RecipeWebsite/
	└── recipewebsite
	    ├── app.py
	    ├── static
	    └── templates

To view the new application in your browser run the following command::

    python app.py

.. literalblock:: ../bottleRecipeWebsite/app.py


.. warning:: sometimes this will will fail because another service on your machine may already be running on the port  (you can change the port in the `app.py` file or stop the conflicting service).


Visiting http://localhost:8080 in your browser will display the following text in your browser::

Discussion
-----------

- What is the benefit have a standard directory structure?

- We used pip to install the Bottle package, in python circles packages are often called `eggs`, can you guess why?

- In what way do conventions make source code more maintainable?

- Any thoughts on what happens when you use virtualenv and the `source bin/activate` command? 

- What do you think happens when you set the `http_proxy` environment variable.?

.. _the new hotness: http://s3.pixane.com/pip_distribute.png
.. _bottle starter scaffold: http://dl.dropbox.com/u/1004432/bottle_starter.zip
.. _article about App Engine charges: http://news.ycombinator.com/item?id=3431132
.. _blog post about using bottle on GAE: http://www.joemartaganna.com/web-development/how-to-build-a-web-app-using-bottle-with-jinja2-in-google-app-engine/
