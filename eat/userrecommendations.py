import falcon
import requests
import json

class CollectionResource:
	def on_get(self, req, resp, user_name):
		"""Get a list of recipe recommendations for user"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Get recipe recommendations for user\n')