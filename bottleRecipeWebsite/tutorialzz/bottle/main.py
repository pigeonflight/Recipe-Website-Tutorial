#!/usr/bin/env python

import sys, os
package_dir = "packages"
package_dir_path = os.path.join(os.path.dirname(__file__), package_dir)
sys.path.insert(0, package_dir_path)

import bottle
from app import views

bottle.debug(True)
bottle.run(server='gae',port='3080')
