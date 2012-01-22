.. _index:

=================================================
Recipe Website Tutorials
=================================================

This is a series of tutorials which lay the foundation for using the `Bottle` web application framework
to create a Recipe Website service. 
Learn more about Bottle at `The Bottle Website
<http://bottlepy.org/>`_.  

According to the Bottle documentation the following is the simplest Bottle application that you can make:

.. literalinclude:: hello.py

When saved to ``helloworld.py``. We've bundled all of this into a bootstrp script called `bootstrapbot.sh`, try it out by doing the following:

.. note:: 
	**Want to see this in action now? Use the 'bootstrapbot.sh' script**

	#. Download it if from: http://dl.dropbox.com/u/1004432/bootstrapbot.sh
	#. Run it::

	       sh bootstrapbot.sh 

        #. Launch the script. You should now have a virtualenv called ``venv``, change to the `venv` directory and launch the helloworld.py program::

        	   cd venv
        	   bin/python helloworld.py

	When you visit ``http://localhost:8080/hello/world`` in a browser, you will
	see the text ``Hello world!``.

.. tip::
Having trouble :ref:`dealing_with_proxies`



As our tasks become more complex
we will add supporting templates, CSS, JS and image files.
All examples will be done on Unix/Linux and have not been thoroughly tested on Windows. If you want to use Windows there are notes available on :ref:`setting_up_windows_dev_chapter`.

Tutorials
=======================

Each tutorial includes discussion questions. It should be possible to work through the tutorial within 30 - 35 minutes and then spend 15 to 20 minutes in discussion, guided by the discussion questions.

.. toctree::
   :maxdepth: 2

   tutorials/planning-and-mockups
   tutorials/setting-up-dev-environment
   tutorials/basic-bottle-application
   tutorials/organizing-your-project
   tutorials/deploying-on-google-appengine
   tutorials/starting-routes-static-resources
   tutorials/building-out-additional-views
   tutorials/resources-urls-content-creation


Reference Material
==================

The following will be useful throughout the course.

`The Pyramid API <http://docs.pylonsproject.org/projects/pyramid/en/latest/glossary.html/>`_  
    


Index and Glossary
==================

* :ref:`glossary`
* :ref:`genindex`
* :ref:`search`


.. add glossary, foreword, and latexindex in a hidden toc to avoid warnings

.. toctree::
   :hidden:

   glossary
   foreword.rst
   latexindex.rst

