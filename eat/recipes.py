import falcon
import requests
import json

class CollectionResource:
	def on_get(self, req, resp):
		"""Get a list of recipes belonging to the user"""

		# return the list of recipes

		recipes = {
			'links': [
				{
				  'rel': 'next',
				  'href': '/v1/recipes/'
				}
			],
			'recipes': [
				{ 
					'name': 'chicken curry', 
					'href': '/v1/recipes/chickencurry',
					'cover_image': 'http://cdn.eat.com/12345/cover/chickencurry.jpg',
					'thumb_image' : 'http://cdn.eat.com/12345/thumb/chickencurry.jpg'
				},
				{ 
					'name': 'roast beef', 
					'href': '/v1/recipes/roastbeef',
					'cover_image': 'http://cdn.eat.com/12345/cover/roastbeef.jpg',
					'thumb_image' : 'http://cdn.eat.com/12345/thumb/roastbeef.jpg'
				},
				{ 
					'name': 'braised carrots',  
					'href': '/v1/recipes/braisedcarrots',
					'cover_image': 'http://cdn.eat.com/12345/cover/braisedcarrots.jpg',
					'thumb_image' : 'http://cdn.eat.com/12345/thumb/braisedcarrots.jpg'
				}
			]
		}


		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = json.dumps(recipes)

class Resource:
	def on_get(self, req, resp, recipe_name):
		"""Get a recipe"""

		# recipe sample
		recipe = {
			'name' : 'chicken curry',
			'href': '/v1/recipes/chickencurry',
			'ingredients' : [
				'oil', 
				'chopped yellow onion', 
				'garlic', 
				'tumeric', 
				'chilli powder', 
				'ground cumin', 
				'ground coriander',
				'chicken thighs'
			],
			'cover_image' : 'http://cdn.eat.com/12345/cover/chickencurry.jpg',
			'thumb_image' : 'http://cdn.eat.com/12345/thumb/chickencurry.jpg',
			'instructions' : [
				'Sweat the onions in the oil with the garlic for 2 minutes until soft.',
				'Add the spices and stir',
				'Add the chicken and fry until golden brown.',
				'Add water, stir, and cover for 30 minutes.'
			]
		}

		# return a recipe
		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = json.dumps(recipe)

	def on_put(self, req, resp, recipe_name):
		"""Upsert a recipe"""

		# upsert a recipe
		resp.status = falcon.HTTP_201
		resp.body = ('Recipe Created: ' + recipe_name + '\n')

	def on_delete(self, req, resp, recipe_name):
		"""Delete a recipe"""

		# delete a recipe
		resp.status = falcon.HTTP_200
		resp.body = ('Recipe Deleted: ' + recipe_name + '\n')