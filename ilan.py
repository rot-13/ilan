#!/usr/bin/python

import cherrypy
import haml
import mako.template
import templates
import os
import glob
import staging
import urllib

class Main:
  @cherrypy.expose
  def index(self):
    return templates.get_template("layout.haml").render()

  @cherrypy.expose
  def staging(self):
    staging_files = staging.staging("/home/asafg/staging").list_files()
    thumbnails = map(self.make_thumbnail, staging_files)
    return templates.get_template("staging.haml").render(files=thumbnails)

  def make_thumbnail(self, path):
    return "/thumbnail/" + urllib.quote(path, '')

  @cherrypy.expose
  def thumbnail(self, path):
    staging_file = staging.file(path)
    thumbnail = staging_file.load_image()
    cherrypy.response.headers['Content-Type'] = "image/" + thumbnail['filetype']
    return thumbnail['content']

cherrypy.quickstart(Main())
