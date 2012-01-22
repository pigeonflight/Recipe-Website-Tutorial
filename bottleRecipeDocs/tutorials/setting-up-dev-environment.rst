.. index::
   single: development
   single: setup

.. _setting_up_dev_chapter:

Part 2 - Setting up your development environment
===========================================

In this tutorial we gather our tools. We assume that you already have a trusted text editor,
so we will focus on the tools needed to build out your web applications.
It is recommended that you use a UNIX/Linux environment, though everything should also work on Windows.

.. note:: **Deployment** - We will deploy our earlier projects on Fluxflex (a cloud hosting platform) and later we will use Google App Engine (GAE). Google App Engine is sometimes called a 
 platform as a service (PAAS) because it provides specific utilities for things like data persistence, authentication and user management. If you don't mind following "the Google way" the benefit is a free option for getting started on infrastructure provided by Google. 

.. attention:: App Engine is not perfect for every type of solution, a recent `discussion about App Engine charges`_ illustrates clearly that some applications don't match very well with GAE.

Installing the Bottle web framework
-----------------------------------------

You will need the following:

- A python interpreter

- and the python virtualenv package

If you are on a network with a proxy then pay careful attention to the next section.

.. _dealing_with_proxies:

Dealing with on campus proxies
-------------------------------

.. note:: All the examples below are specific to the UWI Mona network, but should be applicable to other 
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

.. _virtualenv_section:

Using Bootstrapbot.py to setup a Virtualenv
----------------------------------------------

Bootstrapbot.py is a single file which creates a complete python environment with the 
bottle package installed without the need for administrative access.

Download http://dl.dropbox.com/u/1004432/bootstrapbot.py

Then follow the instructions below:

To install bottle  and virtualenv place bootstrapbot.py in the target folder of your choice and run::

   python bootstrapbot.py

This creates a virtual environment called ``venv``.
When ever you need to use this environment it can be activated using the following commands::

   cd venv
   source bin/activate

On Windows the following is enough::

   cd venv
   Scripts/activate

.. note::  

   Remember to activate your virtual environment!
       .. image:: ../images/activate.gif

   If you don't use an active virtual environment
   things may deviate from behaviour outlined in this documentation
   for example you will get permission errors and other strange behaviour.

Trying out Bottle
-----------------------------------------

Now that you have bottle in a virtual environment (venv from running bootstrapbot.py above).
We can begin try it out. 

.. note::   .. image:: ../images/activate.gif
   Remember to activate your virtual environment!

.. .. note:: `pip` stands for "Pip Installs Packages", it is a package installer designed to install python packages (similar to apt-get on Debian or Ubuntu).
        It has been affectionately referred to as `the new hotness`_.

Let's see that everything is working.

Create a file called `app.py`
And make it look like this:

.. literalinclude:: ../../bottleRecipeWebsite/tutorial1/app.py

To view the new application in your browser run the following command::

    python app.py

.. warning:: sometimes this will will fail because another service on your machine may already be running on the port  (you can change the port in the `app.py` file or stop the conflicting service).

Visiting http://localhost:8080 in your browser will display the following text in your browser::

Discussion
-----------

- Where's the webserver? How is it possible to access our application even though we haven't set up a webserver?

- What is an environment variable?

- By now you should know how to set environment variables, how do you use the terminal (on UNIX or Windows) to display environment variables?

- What do you think happens when you set the `http_proxy` environment variable.?

.. _the new hotness: http://s3.pixane.com/pip_distribute.png
.. _bottle starter app: http://dl.dropbox.com/u/1004432/bottle-app.zip
.. _discussion about App Engine charges: http://news.ycombinator.com/item?id=3431132
