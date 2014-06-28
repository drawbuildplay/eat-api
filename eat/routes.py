import falcon
import requests
import json
import health
import recipes
import userbookmarks
import userqueues
import userratings
import userrecommendations
import users
import v1

class Routes:
	def __init__(self):
		self._init_routes()

	def _init_routes(self):

		# falcon.API instances are callable WSGI apps
		self.app = falcon.API()

		# Resources are represented by long-lived class instances
		home = v1.Resource()
		healthStatus = health.Resource()

		recipeCollection = recipes.CollectionResource()
		recipe = recipes.Resource()

		userCollection = users.CollectionResource()
		user = users.Resource()

		userBookmarkCollection = userbookmarks.CollectionResource()
		userBookmark = userbookmarks.Resource()

		userRecipeRating = userratings.Resource()

		userRecipeRecommendationsCollection = userrecommendations.CollectionResource()

		userQueuesCollection = userqueues.CollectionResource()
		userQueues = userqueues.Resource()



		# Base Endpoints
		self.app.add_route('/v1', home)
		self.app.add_route('/v1/health', healthStatus)

		# Recipes
		self.app.add_route('/v1/recipes', recipeCollection)
		self.app.add_route('/v1/recipes/{recipe_name}', recipe)

		# Users
		self.app.add_route('/v1/users', userCollection)
		self.app.add_route('/v1/users/{user_name}', user)

		# User Bookmarks
		self.app.add_route('/v1/users/{user_name}/recipes', userBookmarkCollection)
		self.app.add_route('/v1/users/{user_name}/recipes/{recipe_name}', userBookmark)

		# User Ratings
		self.app.add_route('/v1/users/{user_name}/recipes/{recipe_name}/rating', userRecipeRating)

		# User Recommendations
		self.app.add_route('/v1/users/{user_name}/recommendations', userRecipeRecommendationsCollection)

		# User Queues
		self.app.add_route('/v1/users/{user_name}/queues/instant', userQueuesCollection)
		self.app.add_route('/v1/users/{user_name}/queues/instant/{recipe_name}', userQueues)

	



