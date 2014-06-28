import falcon
import requests
import json

class CollectionResource:
	def on_get(self, req, resp, user_name):
		"""Get a list of recipes bookmarked by the user"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Retrieved a list of Recipes for user: ' + user_name + '\n')

class Resource:
	def on_put(self, req, resp, user_name, recipe_name):
		"""Bookmark a recipe for the user"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Retrieved a list of Recipes for user: ' + user_name + '\n')

	def on_delete(self, req, resp, user_name, recipe_name):
		"""Delete a Bookmarked recipe from the user"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Removed a bookmarked recipe\n')