#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2
from google.appengine.ext import db
import markdown

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
markdown_dir = os.path.join(os.path.dirname(__file__), 'markdowns')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = False)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
    	self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
    	t = jinja_env.get_template(template)
    	return t.render(params)

    def render(self, template, **kw):
    	self.write(self.render_str(template, **kw))


class MainHandler(Handler):
    def get(self):
        self.render('main-page.html')

class Programming(Handler):
    def get(self):
        self.render('programming-banners.html')

class Tutorials(Handler):
    def get(self, number):
        # needed_file = open(markdown_dir+'/prog_tutorial'+number+'.md', 'rb')
        # content = needed_file.read()
        # content = unicode(content, "utf-8")
        # needed_file.close()
        # html = markdown.markdown(content)
        # self.render('same-content.html', article_content = html)
        # needed_file = open(markdown_dir+'/prog_tutorial'+number+'.md', 'rb')
        # content = needed_file.read()
        # content = unicode(content, "utf-8")
        # needed_file.close()
        # html = markdown.markdown(content)
        self.render('programming' + str(number) + ".html")




app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/programming', Programming), (r'/programming(\d+)', Tutorials)
], debug=True)