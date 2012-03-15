.. index::
   single: jquery
   single: ajax
   single: jsonify

.. _jquery_ajax_chapter:

Part 9 - Jquery and Ajax
============================================================================

In this section we look at working with jQuery and see how we can integrate it with Flask, we will review some important concepts such as:

- Flask and requests
- Ajax
- jQuery and selectors
- chaining
- jsonify in Flask
- jQuery and JSON

Flask and HTTP requests
-------------------------------
The example below demonstrates using Flask to listen for a query
it expects the key 'q'. 

::

    from flask import Flask, request
    app = Flask(__name__) 

    @app.route('/')
    def getquery():
        q = request.args.get('q','')
        fruits = {'1':"Naseberry",'2':"Mango"}
        if q not in fruits.keys():
            result = "no fruit found"
        else:
            result = fruits[q]
        return result

    if __name__ == "__main__":
        app.debug = True
        app.run(port=9000)

.. note:: Notice that request.args.get has an additional parameter, if there is no key 'q' it will set the result to ''. Also if the value of 'q' does not match any of the keys in the 'fruits' dictionary then the result will be set to "no fruit found".

.. note:: We have also customized the default port to listen on 9000 and enabled debugging, in case we need to troubleshoot.


Javascript and Jquery Tools
------------------------------------
The following is a list of resources that you will use regularly when working with jQuery and javascript in general.

`jQuerify Bookmarklet`_
    A bookmark which, when clicked, will jquery enable any page. 

.. image:: ../images/google-jquerified.png

Firebug or Chrome/Safari Developer Tools
    Interactive inspector and console for testing out code.

console.log()
- jsfiddle.net

Flask and jsonify()
---------------------
Flask provides a special method called jsonify() which accepts key value pairs which are passed as a JSON style response to the browser.
::

    from flask import Flask, request, jsonify
    app = Flask(__name__) 

    @app.route('/_json_data')
    def getquery():
        q = request.args.get('q','')
        fruits = {'1':"Naseberry",'2':"Mango"}
        if q not in fruits.keys():
            result = "no fruit found"
        else:
            result = fruits[q]
        return jsonify(result=result)

    if __name__ == "__main__":
        app.debug = True
        app.run(port=9000)

Ajax a quick demo
-------------------------------
In this exercise we will create a demo application that takes advantage of the ajax methods provided by jQuery.



.. _jQuerify Bookmarklet: http://www.learningjquery.com/2006/12/jquerify-bookmarklet
