# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from collections import namedtuple
import jinja2
import webapp2
from models.models import *
import json
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), "dist/static") 
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
	autoescape=True,
	extensions=['jinja2.ext.autoescape'])

class Handler(webapp2.RequestHandler):
	def initialize(self, request, response):
		super(Handler, self).initialize(request, response)
		request.is_ajax = lambda:request.environ.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
	def write(self, * a, ** kw):
		self.response.out.write( * a, ** kw)
	def render_str(self, template, ** params):
		t = jinja_env.get_template(template)
		return t.render(params)
	def render(self, template, ** kw):
 		self.write(self.render_str(template, ** kw))

class Index(Handler):
	def get(self):
		self.render("index.html")


application  = webapp2.WSGIApplication([
    ('/', Index),
], debug=True)