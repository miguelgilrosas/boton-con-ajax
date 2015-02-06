#!/usr/bin/env python

#Añade módulos necesarios.
import os
import webapp2
import jinja2
import json

#Le dice al servidor Web dónde están las plantillas HTML.
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape = True)
#Esta variable va a hacer de datos de la app.
cuenta=0

#Define clases y métodos necesarios.
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(**params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

#Define el controlador de la ruta base "/".
#Sólo acepta get y envía la página "base.html" al cliente.
class Pagina(Handler):
    def get(self):
        self.render("base.html")

#Define el controlador de la ruta "/suma".
#Sólo acepta post (porque cambia el estado del servidor
#al cambiar sus datos) e incrementa la cuenta.
class Sumar(Handler):
    def post(self):
        global cuenta
        cuenta+=1

#Define el controlador de la ruta "/ver".
#Sólo acepta get y envía el JSON con el valor de la cuenta.
class Ver(Handler):
    def get(self):
        self.response.out.write(json.dumps({'cuenta': cuenta}))

#Define la app y enruta.
#Es el punto de arranque según "app.yaml"
app = webapp2.WSGIApplication([
	(r'/', Pagina),
    	(r'/sumar', Sumar),
    	(r'/ver', Ver)
	], debug = True)
