.. index::
   single: views
   single: macros

.. _additional_views_chapter:

Building out additional views
===========================================

In this tutorial we will explore how to use teh `views.py` file to 
define new views and associate new templates and contexts with these new views.

Views for our application
--------------------------

Based on the nature of our application we can predict some of the common views
that we may need.

Views that we will need include:

homepage
    a view which shows the home page, it is associated with the roote of the website.

recipe
    when viewing an individual recipe, this view will be used to display all the information for that recipe.

ingredient
    search by ingredient, this view will return a list of recipes that have the particular ingredient.

submitrecipe
    It should be possible to add a new recipe using the 'submit a recipe' link.

registration
    There needs to be a registration page, so that new users can sign up

faq
     This will be a simple view that lists common questions about the web application
