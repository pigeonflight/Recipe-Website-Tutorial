.. index::
   single: development
   single: app engine
   single: gae

.. _setting_gae_chapter:

Part 6 - Deploying on Google App Engine
===========================================

Google App Engine (GAE) is sometimes called a 
platform as a service (PAAS) because it provides specific utilities for things like data persistence, authentication and user management. 

.. note:: If you don't mind following "the App Engine way" the benefit is a free platform for deploying webscale applications on infrastructure managed by Google. App Engine has a threshold at which point you will need to pay about USD $9 per month, this fee increases as you consume more resources.
While App Engine is great for some application there has been `discussion about App Engine charges`_ which suggest some applications are not economical on GAE.

Setting up the Bottle GAE Scaffold 
--------------------------------------------

For working with App Engine we will use 
a directory structure inspired by this `blog post about using bottle on GAE`_. 
This will be our standard way of arranging directories for applications that we will deploy to GAE.
The scaffold also includes the App Engine Software Development Kit (SDK).

We will refer to this as the **GAE scaffold**. Download it from http://dl.dropbox.com/u/1004432/bottle_gae.zip

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


What you will need:

- An account with App Engine (visit http://appengine.google.com to sign up)
- The Bottle GAE Scaffold http://dl.dropbox.com/u/1004432/bottle_gae.zip
- Python 2.5 
    Google App Engine is designed to work with Python 2.5 newer versions of Python are known to have issues. Ensure that you have this installed, on Windows you may consider using `Portable Python 2.5 <http://www.portablepython.com/wiki/PortablePython1.1Py2.5.4>`_.
- bootstrapbot.py http://dl.dropbox.com/u/1004432/bootstrapbot.py

Sign up with App Engine
------------------------

Visit http://appengine.google.com and sign up by creating a new application.

.. image:: ../images/appenginestart.png

For each application that you create on App Engine there is an ``Administration`` section where you can manage 
``Application Settings``. The most import setting for us is the ``Application Identifier``, we will need to know this name.

Use Python 2.5 to bootstrap bottle
------------------------------------

To install bottle  and virtualenv place bootstrapbot.py in the target folder of your choice and run, be sure
to use Python 2.5::

   python2.5 bootstrapbot.py

This creates a virtual environment called ``venv``.
When ever you need to use this environment it can be activated using the following commands::

   source venv/bin/activate

.. warning:: Are you sure you used Python 2.5? There will be issues is you didn't!

Summary of develop/deploy cycle
-------------------------------------

Download the Bottle GAE Scaffold to the target folder (the same one target folder used above) and unzip it.

The instructions below are for Unix, we assume that `bottle_gae` and `venv` are in the same target folder.
Start in your target folder (the folder containing both venv and bottle_gae).

#. Activate the Python 2.5 virtual environment

       venv/bin/activate

#. Copy `app_template` to `MyApp`::

       cp -r bottle_gae/app_template bottle_gae/MyApp

#. Test that it is working by running the run.sh script::

       cd bottle_gae/MyApp
       sh run.sh 

#. Edit the `app.yaml` file (ensure that the value for ``application`` matches your ``Application Identifier``.

#. Deploy your application to Google App Engine 

        sh deploy.sh

.. note:: Proxy issues? check out :ref:`dealing_with_proxies`

app.yaml and App Engine Versions
----------------------------------

Your applications can be given new version numbers by configuring them in the ``app.yaml`` file.

After deploying a new version you will need to set it to be the default version, in order to see the changes.

.. image:: ../images/appengineversions.png

Taking advantage of the GAE users api and Datastore api
---------------------------------------------------------

Since we will be deploying to GAE, we might as well take advantage of features that GAE provides, especially those
features that Bottle does not provide, specifically:

- User account management (Authentication, Sessions, Login)
- Database backend

We will use App Engine's ``Datastore`` and ``Users`` API, read about both in `getting started with App Engine`_.

Adding Third Party Auth
--------------------------

http://engineauth.readthedocs.org


Discussion
-----------

- What does PAAS mean? How is a PAAS different from normal webhosting? 

- One feature of App Engine is application version management. What would you use this for?

.. _discussion about App Engine charges: http://news.ycombinator.com/item?id=3431132
.. _blog post about using bottle on GAE: http://www.joemartaganna.com/web-development/how-to-build-a-web-app-using-bottle-with-jinja2-in-google-app-engine/
.. _getting started with App Engine: http://code.google.com/appengine/docs/python/gettingstarted/
