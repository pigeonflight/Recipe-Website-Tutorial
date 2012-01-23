.. index::
   single: development
   single: app engine
   single: gae

.. _setting_gae_chapter:

Part 6 - Deploying on Google App Engine
===========================================

Google App Engine (GAE) is sometimes called a 
platform as a service (PAAS) because it provides specific utilities for things like data persistence, authentication and user management. If you don't mind following "the App Engine way" the benefit is a free platform for deploying webscale applications on infrastructure managed by Google. App Engine has a threshold at which point you will need to pay about USD $9 per month, this fee increases as you consume more resources.

.. attention:: App Engine is not perfect for every type of solution this `discussion about App Engine charges`_ illustrates clearly that some applications don't match very well with GAE.

Setting up the Bottle GAE Scaffold 
--------------------------------------------

The directory structure that we use is borrowed from this `blog post about using bottle on GAE`_. 
It provides a standard way of arranging directories for applications that will be deployed to GAE.
We also include the App Engine Software Development Kit (SDK).

We will refer to this as the **bottle_gae scaffold**. Download it from http://dl.dropbox.com/u/1004432/bottle_gae.zip

The unzipped directory structure looks something like this::

	bottle_gae
	├── app_template
	│   ├── app
	│   ├── media
	│   └── packages
	└── google_appengine
	    ├── demos
	    ├── google
	    ├── lib
	    ├── new_project_template
	    └── tools


What you will need
-------------------

- The Bottle GAE Scaffold http://dl.dropbox.com/u/1004432/bottle_gae.zip
- Python 2.5 
    Google App Engine is designed to work with Python 2.5 newer versions of Python are known to have issues. Ensure that you have this installed, on Windows you may consider using `Portable Python 2.5 <http://www.portablepython.com/wiki/PortablePython1.1Py2.5.4>`_.
- Virtualenv

Summary of develop/deploy cycle
-------------------------------------

Download the Bottle GAE Scaffold and Unzip it.
Here is how we will work with the Bottle GAE Scaffold. The instructions below are for Unix, but
similar steps can be taken on Windows.

#. Copy `app_template` to `MyApp`::

       cp app_template MyApp

#. Activate your Python 2.5 virtual environment::

       . ~/Code/py25env/bin/activate

#. Test that it is working by running the run.sh script::

       sh run.sh 

If you are on a network with a proxy then pay careful attention to the next section.

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

Using Virtualenv
------------------

Virtualenv allows you to create complete python environment without the need for administrative access.

To install Bottle, create a virtualenv::

   mkdir venv
   cd venv
   virtualenv --no-site-packages .

When ever you need to use this environment use the command::

   cd venv
   source bin/activate

On Windows the following is enough::

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

Using the bottle starter app
-----------------------------------------

Establishing conventions help to make source code more maintainable, while bottle does not provide a standard approach to managing our code. We will use a standard folder structure. 

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

.. literalinclude:: ../bottleRecipeWebsite/tutorial1/RecipeWebsite/recipewebsite/app.py


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
.. _bottle starter app: http://dl.dropbox.com/u/1004432/bottle-app.zip
.. _discussion about App Engine charges: http://news.ycombinator.com/item?id=3431132
.. _blog post about using bottle on GAE: http://www.joemartaganna.com/web-development/how-to-build-a-web-app-using-bottle-with-jinja2-in-google-app-engine/
