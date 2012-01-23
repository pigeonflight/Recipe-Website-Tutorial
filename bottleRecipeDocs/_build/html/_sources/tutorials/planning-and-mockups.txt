.. index::
   single: planning
   single: mockups
   single: css
   single: layout
   single: convience class
   single: grid framework

.. _planning_mockups_chapter:

Part 1 - Planning and Mockups
=====================

Why do this?
--------------

Because most customers are visual, we work with them to develop something that will give them a good idea of how their application will behave. This course focuses mostly on development not design, so we will use "shortcuts" for our design work. For a full project there will be need for a UI designer to
layout the look to the satisfaction of the customer.

Mockup up tools
------------------

Some tools that I have worked with are:

 - LucidChart_  - an HTML5 based diagram tool

 - Cacoo_ - a Flash based diagram tool (has a nice sketchy style for mockups)

 - Mockingbird_ - an HTML5 based diagram tool

Browse their websites and sign up for one of the services (the first two allow
you to log in with your google account, which means you will have one less 
password to worry about)

The Design
------------

Our UI person (me in this case) has decided to use Cacoo to come up with the following layout:

.. image:: /images/recipe-website-wireframe.png

You can also see the `live version of the mockup`_ at the Cacoo website.
Notice the use of a sketchy style.

Layout using a CSS Framework
------------------------------

There are several CSS Frameworks which help to simplify the task of creating an HTML layout. 
For this layout I've decided to use the deco.gs_ framework.
In addition to these frameworks new applications like Initializr_ help to get you started quickly.

The deco.gs system uses a combination of two CSS classes ".row" and ".cell" to acheive layout. The cells are supplemented by special `position-` and `width-` ``convenience classes``, which determine **where** within a row a cell will be placed as well as **how much space** that cell takes up.

In the example below we use two different cell widths [#]_, `width-4` and `width-12` to create our layout. 

::

    <div class="row">
	  <div class ="cell position-0 width-4">This cell is four units wide</div>
	  <div class ="cell position-4 width-12">This cell is twelve units wide</div>
    </div>

The resulting layout:

.. image:: /images/2deco-cells.png

After looking at the mockup, we've determined that the UI could be divided into
5 rows, each row will have a varied number of cells and the width of each cell will vary.

.. image:: /images/mockup-grid.jpg

If each row gets a unique id from row-1 to row-5 we could recreate the structure
of the mockup with deco.gs using the following code.
::

    <div id="row-1" class="row">
	  <div class ="cell position-0 width-3">logo</div>
	  <div class ="cell position-3 width-6">the menu</div>
	  <div class ="cell position-9 width-3">search</div>
    </div>
    <div id="row-2" class="row">
	  <div class ="cell position-0 width-3">submit a recipe</div>
	  <div class ="cell position-3 width-9">highlight recipes</div>
    </div>
    <div id="row-3" class="row">
	  <div class ="cell position-0 width-3">popular ingredients</div>
	  <div class ="cell position-3 width-4">new recipes box</div>
	  <div class ="cell position-7 width-5">popular recipes box</div>
    </div>
    <div id="row-4" class="row">

	  <div class ="cell position-3 width-9">Recipe Categories</div>
    </div>
    <div id="row-5" class="row">
	  <div class ="cell position-0 width-3">I heart Recipes</div>
	  <div class ="cell position-3 width-4">footer stuff</div>
	  <div class ="cell position-7 width-5">social stuff</div>
    </div>

View `the result of this code at dabblet`_

Try `the code at dabblet`_

Get `the code from github.com`_

Discussion 
------------

- What might be some pros and cons to presenting the mockup in a "sketchy" style?

- The HTML snippets above are not complete HTML documents, what would we need to add to make them complete?

- Why use a css grid framework when you can hand code everything yourself?

- Most grid frameworks focus on organizing things into rows and cells, NOT rows and columns, what's the difference?

- What does the term convenience class suggest?

- Look at the proposed html code, do you notice anything different about the contents of 'row-4'?

Lab
----

- Using one of the tools mentioned above, create a mockup for a website.
  While making the mockup, try to think about how many rows will be needed if
  you were implementing the site using a grid framework.

- Using Deco.gs (or a framework of your choice), implement a rough HTML version of that mockup.


.. _deco.gs: http://limi.net/deco.gs
.. _LucidChart: http://www.lucidchart.com
.. _Cacoo: http://cacoo.com
.. _Mockingbird: http://www.gomockingbird.com
.. _Initializr: http://www.initializr.com
.. [#] Note that the cell convenience classes are added to the same div tag as the cell.
.. _the result of this code at dabblet: http://dabblet.com/result/gist/1636270
.. _the code at dabblet: http://dabblet.com/1636270
.. _the code from github.com: https://gist.github.com/1636270
.. _live version of the mockup: https://cacoo.com/diagrams/qb2bRi32AHGvzlef
