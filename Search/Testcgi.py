#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import pycurl
import urllib2
import json
import elasticsearch
import cgi   # NEW

es=elasticsearch.Elasticsearch()

class MainHandler(tornado.web.RequestHandler):
	# standard code for future cgi scripts from here on
	def fileToStr(fileName): 
		"""Return a string containing the contents of the named file."""
		fin = open(fileName); 
		contents = fin.read();  
		fin.close() 
		return contents

	def processInput(self, numStr1, numStr2):  
		'''Process input parameters and return the final page as a string.'''
		num1 = int(numStr1) # transform input to output data
		num2 = int(numStr2)
		total = num1+num2
		return "<html><body>"+str(num1)+" "+str(num2)+" <b>Search for a movie: </body></b><br></br><form action=''><input id='searchbox' type='textbox'></input><input type='submit' value='Submit'></form></html>"

	def get(self):
		#self.write("<html><body><b>Search for a movie: </body></b><br></br><input type='textbox''></input></html>")
		form = cgi.FieldStorage()      # standard cgi script lines to here!

		# use format of next two lines with YOUR names and default data
		numStr1 = form.getfirst("x", "3") # get the form value associated with form
		# name 'x'.  Use default "0" if there is none. 
		numStr2 = form.getfirst("y", "4") # similarly for name 'y'
		contents = self.processInput(numStr1, numStr2)   # process input into a page
		
		form = cgi.FieldStorage()
		
		if "Submit" in form:
			print("Search pressed.")
		else:
			print("Couldn't determine which button was pressed.")

		self.write(contents)

application = tornado.web.Application([
    (r"/", MainHandler),
])

#result = es.search(index='my-index', doc_type='test-type', q='title:"book"')
#print result

if __name__ == "__main__":
	application.listen(8088)
	tornado.ioloop.IOLoop.instance().start()

