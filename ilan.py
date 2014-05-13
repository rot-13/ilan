#!/usr/bin/python

import cherrypy
import haml
import mako.template
import templates

class Main(object):
    @cherrypy.expose
    def index(self):
        return templates.get_template("layout.haml").render()

    @cherrypy.expose
    def staging(self):
        return templates.get_template("staging.haml").render()

cherrypy.quickstart(Main())
