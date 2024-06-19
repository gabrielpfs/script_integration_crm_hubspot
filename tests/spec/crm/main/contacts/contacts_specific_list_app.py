import requests
import json

# Your HubSpot private app access token
access_token = 'YOUR_ACCESS_TOKEN'

# HubSpot API endpoint for getting contacts from a list
list_id = 'YOUR_LIST_ID'  # Substitua pelo ID da lista que você quer acessar
url = f'https://api.hubapi.com/contacts/v1/lists/{list_id}/contacts/all'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

def get_list_contacts(url, headers):
    contacts = []
    has_more = True
    offset = 0

    while has_more:
        params = {
            'count': 100,  # Número de contatos por página (máximo é 100)
            'vidOffset': offset
        }

        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()

        contacts.extend(response_data.get('contacts', []))

        # Check if there are more pages
        has_more = response_data.get('has-more')
        if has_more:
            offset = response_data.get('vid-offset')
        else:
            has_more = False

    return contacts

contacts = get_list_contacts(url, headers)

# Export contacts to a JSON file
with open('contacts_especific_list_app.json', 'w') as f:
    json.dump(contacts, f, indent=4)

print(f'Exported {len(contacts)} contacts to contacts_especific_list_app.json')