.. index::
   single: development
   single: setup

.. _setting_up_dev_chapter:

Part 2 - Setting up your development environment
===========================================

We have a lot to cover today including:

It is recommended that you use a UNIX/Linux environment, though everything should also work on Windows.

- Installing Flask using our bootstrapflask.py method
- 

.. note:: **Deployment** - We will deploy our earlier projects on Fluxflex (a cloud hosting platform) and later we will use Google App Engine (GAE). Google App Engine is sometimes called a 
 platform as a service (PAAS) because it provides specific utilities for things like data persistence, authentication and user management. If you don't mind following "the Google way" the benefit is a free option for getting started on infrastructure provided by Google. 

.. attention:: App Engine is not perfect for every type of solution, a recent `discussion about App Engine charges`_ illustrates clearly that some applications don't match very well with GAE.

Installing the Flask web framework
-----------------------------------------

You will need the following:


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

Using Bootstrapflask.py to setup a Virtualenv
----------------------------------------------

Bootstrapflask.py is a single file which creates a complete python environment with the 
flask package installed without the need for administrative access.

The only assumption is that you have a working python interpreter already installed.

.. note:: On OS X you will also need to install Xcode so that you have developertools 

Download http://dl.dropbox.com/u/1004432/bootstrapflask.py

Then follow the instructions below:

To install flask  and virtualenv place bootstrapflask.py in the target folder of your choice and run (set your `http_proxy` if you need to do that)::

   python bootstrapflask.py

This creates a virtual environment called ``venv``.
When ever you need to use this environment it can be activated using the following commands::

   source venv/bin/activate

On Windows the following is enough::

   venv\Scripts\activate

.. note::  

   Remember to activate your virtual environment!
       .. image:: ../images/activate.gif

   If you don't use an active virtual environment
   things may deviate from behaviour outlined in this documentation
   for example you will get permission errors and other strange behaviour.

Trying out Flask
-----------------------------------------

Now that you have flask in a virtual environment (venv from running bootstrapflask.py above).

.. note::   .. image:: ../images/activate.gif
   Remember to activate your virtual environment!

.. .. note:: `pip` stands for "Pip Installs Packages", it is a package installer designed to install python packages (similar to apt-get on Debian or Ubuntu).
        It has been affectionately referred to as `the new hotness`_.

Let's see that everything is working.

Create a file called `app.py`
And make it look like this:

.. literalinclude:: ../hello.py

To view the new application in your browser run the following command::

    python app.py

.. warning:: sometimes this will will fail because another service on your machine may already be running on the port  (you can change the port in the `app.py` file or stop the conflicting service).

Visiting http://localhost:8080 in your browser will show the result of the code.


Building A Basic Application
------------------------------

Now it's time to build your first simple application.

Follow the tutorial at http://flask.pocoo.org/docs/tutorial/

Then come back to discuss what you've learnt.

Discussion
-----------

- Where's the webserver? How is it possible to access our application even though we haven't set up a webserver?

- What is an environment variable?

- By now you should know how to set environment variables, how do you use the terminal (on UNIX or Windows) to display environment variables?

- What do you think happens when you set the `http_proxy` environment variable.?

- Notice the effect of introducing the templating system, the application is now broken up into .py files and .tpl templates. What are your thoughts regarding this approach, compared to what you may know from using PHP?

- How would create a login and logout system without a framework? What are the key ingredients of a login/logout system?

.. _the new hotness: http://s3.pixane.com/pip_distribute.png
.. _flask starter app: http://dl.dropbox.com/u/1004432/flask-app.zip
.. _discussion about App Engine charges: http://news.ycombinator.com/item?id=3431132
