.. _index:

=================================================
Recipe Website Tutorial
=================================================

This tutorial is based on the `Pyramid` web application
development framework.  Pyramid is an open source framework written 
in Python and is part of the 
`Pylons Project
<http://docs.pylonsproject.org/>`_.  

According to the Pyramid documentation the following is the simplest pyramid application that you can make:

.. literalinclude:: ../code/snippets/helloworld.py

When saved to ``helloworld.py``, the above application can be run via:

.. code-block:: text

   $ easy_install pyramid
   $ python helloworld.py

When you visit ``http://localhost:8080/hello/world`` in a browser, you will
see the text ``Hello, world!``.

This is a simple single file application. As our tasks become more complex there comes a point
when an application may be spread accross several files and possibly several packages. This tutorial
will focus on building a "Recipe Website" following the conventions of a URL Traversal type Pyramid application.


Tutorials
=======================

Each tutorial includes discussion questions. It should be possible to work through the tutorial within 30 - 35 minutes and then spend 15 to 20 minutes in discussion, guided by the discussion questions.

.. toctree::
   :maxdepth: 2

   tutorials/planning-and-mockups
   tutorials/setting-up-dev-environment
   tutorials/adding-custom-views
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

