import falcon
import requests
import json

class Resource:
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200
