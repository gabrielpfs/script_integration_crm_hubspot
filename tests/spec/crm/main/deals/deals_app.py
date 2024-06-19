import requests
import json

# Your HubSpot private app access token
access_token = 'YOUR_ACCESS_TOKEN'

# HubSpot API endpoint for deals
url = 'https://api.hubapi.com/crm/v3/objects/deals'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

def get_all_deals(url, headers):
    deals = []
    has_more = True
    after = None

    while has_more:
        params = {}
        if after:
            params['after'] = after

        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()

        deals.extend(response_data.get('results', []))

        # Check if there are more pages
        paging = response_data.get('paging')
        if paging and 'next' in paging:
            after = paging['next']['after']
        else:
            has_more = False

    return deals

deals = get_all_deals(url, headers)

# # Formatting decimal values before exporting to JSON
# for deal in deals:
#     if 'properties.amount' in deal:
#         deal['properties.amount'] = f"{deal['properties.amount']:.2f}" # Format to two decimal places

# Export deals to a JSON file
with open('deals_app.json', 'w') as f:
    json.dump(deals, f, indent=4)

print(f'Exported {len(deals)} deals to deals_app.json')