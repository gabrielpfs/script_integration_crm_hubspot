import requests
import json

# Your HubSpot private app access token
access_token = 'YOUR_ACCESS_TOKEN'

# HubSpot API endpoint for contacts
url = 'https://api.hubapi.com/crm/v3/objects/contacts'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

def get_all_contacts(url, headers):
    contacts = []
    has_more = True
    after = None

    while has_more:
        params = {}
        if after:
            params['after'] = after

        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()

        contacts.extend(response_data.get('results', []))

        # Check if there are more pages
        paging = response_data.get('paging')
        if paging and 'next' in paging:
            after = paging['next']['after']
        else:
            has_more = False

    return contacts

contacts = get_all_contacts(url, headers)

# Export contacts to a JSON file
with open('contacts_application.json', 'w') as f:
    json.dump(contacts, f, indent=4)

print(f'Exportados {len(contacts)} contatos para contacts_application.json')    