import falcon
import requests
import json

class CollectionResource:
	def on_get(self, req, resp, user_name):
		"""Get user recipe queue"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('List of recipe queues for: ' + user_name + '\n')

class Resource:
	def on_post(self, req, resp, user_name, recipe_name):
		"""Add recipe to a user queue"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Add recipe to queue for : ' + user_name + '\n')

	def on_delete(self, req, resp, user_name, recipe_name):
		"""Delete the recipe from the user queue"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Delete recipe from queue for : ' + user_name + '\n')