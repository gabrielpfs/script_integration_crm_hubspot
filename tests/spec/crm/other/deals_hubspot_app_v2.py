# Accessing Deals via API
import hubspot
from pprint import pprint
from hubspot.crm.deals import ApiException

client = hubspot.Client.create(api_key="YOUR_HUBSPOT_API_KEY");

try:
    api_response = client.crm.deals.basic_api.get_page(limit=10, archived=False)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)

# This version of a code to access deals via API does not work
# update the package using: pip install --upgrade hubspot-api-client