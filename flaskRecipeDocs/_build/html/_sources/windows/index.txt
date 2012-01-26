.. index::
   single: windows
   single: development
   single: setup

.. _setting_up_windows_dev_chapter:

Installing Flask and Virtualenv on Windows behind the UWI proxy
==================================================================

Before attempting any of the instructions below, `download and install python`_. 

1. Open http://peak.telecommunity.com/dist/ez_setup.py in a webbrowser
2. Then save the file. (In Firefox you can select “save page as”). 
3. Save the file to your Desktop.

Open the Windows command line (cmd)

and install virtualenv using the following commands
::
	set http_proxy=scalpel:8080
	python Desktop\ez_setup.py
	D:\Python27\Scripts\easy_install virtualenv

.. warning:: When on campus, the first thing that you should do after launching the command line is to set the http_proxy.

       set http_proxy=scalpel:8080

    Other proxies include proxy3:8080 proxy-cluster:8080

    **If this is NOT set the other commands will fail whenever they need to download items from the internet.**

You will see output similar to this:

.. image:: ../images/installingvirtualenv.png

Create and activate a virtualenv:
::

	D:\Python27\Scripts\virtualenv venv
	venv\Scripts\activate

.. note:: 

    After activating the virtualenv you will notice the name of your environment presented in brackets e.g. (venv) at the beginning of the command line prompt. This is how you can know that your virtual enviroment is active.

.. note::  

   Remember to activate your virtual environment!
       .. image:: ../images/activate.gif

   If you neglect this, `pip` will behave in unpredictable ways,
   you will get permission errors
   and other strange behaviour.

You can now install flask using the following commands:
::
 
	pip install flask

.. note:: The `pip` command depends on the Python Packaging Index (PYPI).
            If the `pip install` command fails try specifying a pypi mirror.
                `pip install -i http://d.pypi.python.org/simple flask`


We recommended that you do all your development in a folder on your Desktop, create a folder called `code`. This is where you will create your custom packages.

.. image:: ../images/createcodefolder.jpg

Important notes about Windows
--------------------------------

The set http_proxy command is very important on campus
`set http_proxy=scalpel:8080` (or other proxy) is VERY IMPORTANT!!


Use your 'Desktop' as recommended, NOT 'My Documents', we don't want to have any issues 
due to working with paths that have spaces, we haven't confirmed this to be an issue, but 
we don't recommend that you test it.

 
Creating and activating a new application
------------------------------------------

XXX Fixme.. need to update these notes

Download it and place it in your code folder.

When you want to start a new flask application unzip and rename the application
You can do this by launching the commandline and running the following commands:
::


Useful tips
----------------

   1. In explorer, open Tools > Folder Options > File Types tab
   2. For Windows XP: Go to NONE / Folder.


   4. For Windows 2000: Press n to scroll to the N/A section.
   5. For Windows NT/98/95: Press f to scroll to the Folders section.
   6. Select the entry labeled Folder
   7. For Windows 2000/XP: Press Advanced button.
   8. For Windows NT/98/95: Press Edit button.
   9. Select New
  10. In the action block type "Command Prompt" without the quotes.
  11. In the app block type "cmd.exe" without the quotes.
  12. Save and exit Folder Options.

Now right click on Start, you should have a new drop down option. Open explorer and right click on a folder, select Command Prompt and a command window opens in that folder.

Read this thread for some information on how to remove the context menu:

.. _download and install python: http://python.org/download/
.. _flask starter app: http://dl.dropbox.com/u/1004432/flask-app.zip
