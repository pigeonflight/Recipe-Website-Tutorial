.. index::
   single: jquery
   single: ajax
   single: jsonify
   single: json
   single: jsonp

.. _jquery_ajax_chapter:

Part 8 - Jquery and Ajax
============================================================================

In this section we look at working with jQuery and see how we can integrate it with Flask, we will review some important concepts such as:

- Flask and requests
- Ajax
- jsonify in Flask
- jQuery, JSON and JSONP

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

.. note:: Notice that request.args.get has an additional parameter, if there is no key 'q' it will set an empty result to ''. Also if the value of 'q' does not match any of the keys in the 'fruits' dictionary then the result will be set to "no fruit found".

.. note:: We have also customized the default port to listen on 9000 and enabled debugging, in case we need to troubleshoot.




Javascript and Jquery Tools
------------------------------------
The following is a list of resources that you will use regularly when working with jQuery and javascript in general.

`jQuerify Bookmarklet`_
    A bookmark which, when clicked, will install jquery on the current page. 

.. image:: ../images/google-jquerified.png


**Firebug or Chrome/Safari Developer Tools**
    Interactive inspector and console for testing out code.

**console.log()**
     This command sends output to the javascript console

**jsfiddle.net**
      Online service that allows you to 'fiddle' with javascript

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

.. note:: Be sure that you're familiar with the JQuery AJAX convenience method: ``$.getJSON``. It is worth reading http://jqfundamentals.com/#chapter-7 even just skimming to make sure you understand how getJSON fits into the picture.

Let's put everything together::

   wget http://dl.dropbox.com/u/1004432/flask_starter.zip
   unzip flask_starter.zip
   cp -r flask_starter myjson
   cd myjson
   python bootstrapflask.py
   source venv/bin/activate

Edit the ``app.py`` file and add the jsonify code that we discussed above (remember to import jsonify).

Remember to import request and jsonify::

   from flask import Flask,jsonify,request

Run it::

   python app.py



JSONP to defeat the same-origin policy limitation
---------------------------------------------------------------------
A normal JSON request, made to a service on another domain will fail.

.. note:: What do you know about the same-origin policy limitation. Google for it if you're not sure about it.

Browsers don't prevent the loading of external scripts from a different location into an HTML page. JSON + Padding (JSONP), is a mechanism to dynamically take advantage of this behaviour.

Using a javascript templating system with a jsonp based service
--------------------------------------------------------------------
The example below demonstrates the use of a JSONP service provided by Flickr.

It also demonstrates the use of a javascript/json templating solution called tempo.
Visit http://api.flickr.com/services/feeds/photos_public.gne?format=json and you will see something like this:

.. image:: /images/jsonpflickr.png

.. note:: The request included `format=json` but the output is a bit more than just plain JSON it is actually a JSONP response. The JSON data is 'wrapped' in what looks like a function in this case called ``jsonFlickrFeed()``.

Download the working example from http://dl.dropbox.com/u/1004432/tempo.demo.zip
::

  wget http://dl.dropbox.com/u/1004432/tempo.demo.zip
  unzip tempo.demo.zip

Open ``tempo-flickrdemo.html``, The code will look like this::

    <html>
    <head>
        <script src="jquery.js"></script>
        <script src="tempo.min.js"></script>
    </head>
    <body>

      <script>
       function jsonFlickrFeed(jsonData) {
                    //  uncomment to see jsonData in your
                    //  javascript console
                    //  console.log(jsonData);

                    //use element with id 'my-pics'
                   Tempo.prepare('my-pics').render(jsonData.items);
                  }
                  var URL = "http://api.flickr.com/services/feeds/photos_public.gne?format=json"


       $.ajax({
                      url: URL,
                      dataType: 'jsonp',
                      jsonpCallback: 'jsonFlickrFeed',
       });
      </script>


    <ol id="my-pics">
        <li data-template>{{link}} <img src="{{media.m}}" /></li>
    </ol>
    </body>
    </html>


.. note:: Notice the function named ``jsonFlickrFeed()`` 

.. note:: How do {{link}} and {{media.m}} relate to the function and the data? Hint: pay attention to the use of ``Tempo.prepare()``.

  
Next Lab
--------------
In the upcoming lab we will be implementing our very own webAPI expect to be doing the following:

- Integrate Tempo based templates with Flask
- Create a webservice that serves both JSON and JSONP


.. _jQuerify Bookmarklet: http://www.learningjquery.com/2006/12/jquerify-bookmarklet
