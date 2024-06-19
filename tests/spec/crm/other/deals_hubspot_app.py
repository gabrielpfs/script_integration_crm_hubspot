from hubspot import HubSpot
from pprint import pprint

client = HubSpot(api_key="YOUR_API_KEY")

try:
    api_response = client.crm.deals.basic_api.get_page(limit=10, archived=False)
    pprint(api_response)
except Exception as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)

# Now I am getting the following error: SyntaxError: You must include a hapi_key or access_token attribute when initalizing the API
# update the package using: pip install --upgrade hubspot-api-client