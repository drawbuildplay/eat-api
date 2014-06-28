import falcon
import requests
import json

class CollectionResource:
	def on_get(self, req, resp):
		"""Get a list of users"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Retrieved a list of users\n')

class Resource:
	def on_get(self, req, resp, user_name):
		"""Get a user"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Retrieved a user: ' + user_name + '\n')

	def on_put(self, req, resp, user_name):
		"""Upsert a user"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Updated user: ' + user_name + '\n')

	def on_delete(self, req, resp, user_name):
		"""Delete a user"""

		# return the list of recipes
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = ('Removed a User\n')