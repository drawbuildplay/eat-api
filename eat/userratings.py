import falcon
import requests
import json

class Resource:
	def on_get(self, req, resp, user_name, recipe_name):
		"""Get a rating for a recipe for this user"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Get recipe rating\n')

	def on_put(self, req, resp, user_name, recipe_name):
		"""Set the user rating for the recipe"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Set recipe rating for : ' + user_name + '\n')

	def on_delete(self, req, resp, user_name, recipe_name):
		"""Delete the user rating for the recipe"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Delete recipe rating for : ' + user_name + '\n')