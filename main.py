#!/usr/bin/env python

import os
import webapp2
import jinja2
import json

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape = True)
cuenta=0

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(**params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Pagina(Handler):
    def get(self):
        self.render("base.html")

class Sumar(Handler):
    def post(self):
        global cuenta
        cuenta+=1

class Ver(Handler):
    def get(self):
        self.response.out.write(json.dumps(({'cuenta': cuenta})))

app = webapp2.WSGIApplication([
	(r'/', Pagina),
    (r'/sumar', Sumar),
    (r'/ver', Ver)
	], debug = True)
