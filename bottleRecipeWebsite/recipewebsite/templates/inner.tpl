<!DOCTYPE html>
 <html>
  <head>
     <title>{{title}}</title>
     <link rel="stylesheet" href="/static/decogrids-12-gapless.css" />
  </head>
   <body>
    <div id="row-1" class="row">
           <div class ="cell position-0 width-3">
               LOGO will go here
           </div>
           <div class ="cell position-3 width-6">the menu</div>
           <div class ="cell position-9 width-3">search</div>
     </div>
     <div id="row-2" class="row">
           <div class ="cell position-0 width-3">side content</div>
           <div class ="cell position-3 width-9">
                     <div metal:define-slot="content">
                      %include
                     </div>
           </div>
     </div>
     <div id="row-3" class="row">
           <div class ="cell position-0 width-3">I heart Recipes</div>
           <div class ="cell position-3 width-4">footer stuff</div>
           <div class ="cell position-7 width-5">social stuff</div>
     </div>

     </body>
