.. index::
   single: windows
   single: development
   single: setup

.. _setting_up_windows_dev_chapter:

Installing Pyramid and Virtualenv on Windows behind the UWI proxy
==================================================================

Before attempting any of the instructions below, `download and install python2.7`_. 

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

Below is sample output from a command line session with a virtualenv named `venv` activated.

.. note:: 

    Notice the (venv) in brackets at the beginning of the command line prompt. This is how you can know that your virtual enviroment is active.

You can now install pyramid using the following commands:
::
 
	pip install pyramid

It is recommended that you do all your development in a folder on your Desktop, Create a folder called `code`. This is where you will create your custom packages.

.. image:: ../images/createcodefolder.jpg

 
Creating and activating a new application
------------------------------------------

Do this in your code folder.

You can do this by launching the commandline and running the following commands:
::

	cd Desktop\code
	pcreate -s zodb MyRecipe

Then activate the new package using the following commands:
::

	cd MyRecipe
	python setup.py develop

View the result in your file browser:
::

	explorer .\

.. image:: ../images/explorerview.png

To launch the new application run the following command:
::

	pserve development.ini 

Then visit http://localhost:6543 in your webbrowser. The application will look like this::

.. image:: ../images/pyramidonwindows.png

Important notes about Windows
--------------------------------

The set http_proxy command is very important on campus
`set http_proxy=scalpel:8080` (or other proxy) is VERY IMPORTANT!!


Use your 'Desktop' as recommended, NOT 'My Documents', we don't want to have any issues 
due to working with paths that have spaces, we haven't confirmed this to be an issue, but 
we don't recommend that you test it.

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

.. _download and install python2.7: http://python.org/download/
