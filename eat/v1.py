import falcon
import requests
import json

class Resource:
	def on_get(self, req, resp):
		"""Get the Home Service Catalog"""

		# return the home document

		home_doc = [
			{
				"resources" : [
					{
						"/v1/recipes" : {
							"href" : "/recipes",
							"hints" : {
								"allow":["GET"],
								"formats" : { 
									"application/json" : {}
								}
							}
						}
					},
					{
						"/v1/recipe" : {
							"href-template" : "/recipes/{recipe_name}",
							"href-vars" : {
								"recipe_name" : "/v1/recipes"
							},
							"hints" : {
								"allow":["GET", "PUT", "DELETE"],
								"formats" : { 
									"application/json" : {}
								}
							}
						}
					}
				]
			}
		]


		resp.status = falcon.HTTP_200  # This is the default status
		resp.body = json.dumps(home_doc)
