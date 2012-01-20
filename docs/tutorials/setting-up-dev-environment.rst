.. index::
   single: development
   single: setup

.. _setting_up_dev_chapter:

Setting up your development environment
===========================================

In this tutorial we gather our tools. We assume that you already have a trusted text editor.
So we will focus on the tools needed to build out the new application.
It is recommended that you use a UNIX/Linux environment.
If you would like to try Pyramid on Windows, read the article 
:ref:`setting_up_windows_dev_chapter`, while Pyramid works on Windows
there is far more documentation and support related to using it on UNIX/Linux.

Installing the Pyramid Webframework
-----------------------------------------

You will need the following:

- A python interpreter

- The ability to compile source code

- and the python virtualenv package

.. note:: This is well documented in the Pyramid Documentation so head over to 
   the `Pyramid Installation Documentation`_ for more details.
   Then come back when you're finished. 

If you are on a network with a proxy then pay careful attention to the next section.

.. _Pyramid Installation Documentation: http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html

Dealing with on campus proxies
-------------------------------

.. note: All the examples below are specific to the UWI Mona network, but should be applicable to other 
locations that use a proxy on their network.

**Known UWI proxies** 
	scalpel, proxy-cluster, proxy1, proxy3, sword

- All proxies are configured to run on port 8080. 

After launching the terminal (or commandline) it is important to set the http_proxy
environmental variable, before running any other command

**On Unix** 

::

   export http_proxy=proxy3:8080

**On Windows** 

the same can be acheived by using `set` instead of `export`::


   set http_proxy=proxy3:8080

Using Virtualenv
------------------

To install Pyramid, create a virtualenv::

   mkdir pyramidenv
   cd pyramidenv
   virtualenv --no-site-packages .

When ever you need to use this environment use the command::

   source bin/activate

Then install pyramid using the pip command::

    pip install pyramid

Quick Tour of common Pyramid commands
----------------------------------------

`pcreate`
	Create a new Pyramid project

`pserve`
	Serve a pyramid application

`pshell`
	Launch an interactive REPL type shell (useful for troubleshooting)

For more information about these tools visit `commandline pyramid`_
Other tools which you may find useful are `proutes`, `pviews` and `ptweens`.

Creating the scaffolds for our project
-----------------------------------------

Establishing conventions help to make source code more maintainable, Pyramid provides
a handful of starting templates, which it calls `scaffolds`. We will use one
of these templates to generate the directory structure of our application. 

Let's create a quick project.
::
    bin/pcreate -s zodb RecipeWebsite

You will see output similar to this (the output has been truncated)::

    Creating directory ...
      Recursing into +package+
    ...
    Welcome to Pyramid.  Sorry for the convenience.

The result will be a directory structure like this::
    
	RecipeWebsite/
	├── CHANGES.txt
	├── MANIFEST.in
	├── README.txt
	├── development.ini
	├── production.ini
	├── recipewebsite
	│   ├── __init__.py
	│   ├── models.py
	│   ├── static
	│   │   ├── favicon.ico
	│   │   ├── footerbg.png
	│   │   ├── headerbg.png
	│   │   ├── ie6.css
	│   │   ├── middlebg.png
	│   │   ├── pylons.css
	│   │   ├── pyramid-small.png
	│   │   ├── pyramid.png
	│   │   └── transparent.gif
	│   ├── templates
	│   │   └── mytemplate.pt
	│   ├── tests.py
	│   └── views.py
	├── setup.cfg
	└── setup.py

Enter the `RecipeWebsite` folder and install the new package::

    pip install -e .

.. note:: an older alternative approach is to run `python setup.py develop`.

The result will be output similar to this (output truncated)::

    ...
    Finished processing dependencies for RecipeWebsite==0.0

To view the new application your browser run the following command::

    pserve development.ini

The result will be output like this::

    ...
    Starting server in PID 24374.
    serving on http://0.0.0.0:6543


Visiting http://localhost:6543 in your browser will display something like the image below

.. image:: ../images/pyramid_app_running.jpg

Requirements and setup.py
--------------------------

If you need new functionality you can declare a requirement in your 
new package. This will prove very useful in the future.

Take a look at `setup.py` 
Note the `requires` lines::

	requires = [
	    'pyramid',
	    'pyramid_zodbconn',
	    'pyramid_tm',
	    'pyramid_debugtoolbar',
	    'ZODB3',
	    'waitress',
	    ]

Each of these refers to a package that our `RecipeWebsite` applications depends on.
When the `python setup.py develop` command is invoked the required dependencies are installed. 

Where the code lives
------------------------

Throughout this project, most of your code and customizations will be done 
in the `recipewebsite` subdirectory.
Note that the subdirectory is all lowercase, even though the package 
directory is `RecipeWebsite`.

.. image:: ../images/location.png

Discussion
-----------

- What is the benefit of using the `pcreate` command to create a directory structure.

- In what way do conventions make source code more maintainable?

- Any thoughts on what happens when you use virtualenv and the `source bin/activate` command?

- What might cause an error like this: 
       `socket.error: [Errno 48] Address already in use`

.. _commandline pyramid: http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/commandline.html
