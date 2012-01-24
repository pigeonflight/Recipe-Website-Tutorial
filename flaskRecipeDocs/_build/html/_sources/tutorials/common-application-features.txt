.. index::
   single: authentication
   single: authorization
   single: database

.. _common_features_chapter:

Part 5 - Common Application Features 
===========================================

Bottle is a very simple micro-framework and as a result it is easy to get started quickly without having to learn
lots of additional concepts. So far we have been able to manage with the functionality that Bottle provides
such as:

- routing
- templating engines (simple template, jinja2 and mako)
- request and response data management

At some point you hit the limitations of working with micro-framework. There are things that Bottle cannot do!
for example if you need to manage users and user accounts or connect to a database Bottle doesn't have that
functionality built in.
Below is a list of some of the common features that Bottle does not `ship` with:

- user accounts (session management, authentication and authorization)
- database connections

For these will have to rely on third-party modules.

We will use the following modules to implement:

- **repoze.who** and **repoze.what** for user account management
- **SQLAlchemy** for database connectivity 


Adding Authentication to an Application
----------------------------------------

XXX Fixme, need

Working with Databases
----------------------------------------

XXX Fixme, need

Discussion
-----------

