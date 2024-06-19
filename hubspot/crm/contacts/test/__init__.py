# import requests
# import json

# # Seu token de acesso privado do HubSpot
# access_token = 'your_access_token'

# # URL do endpoint da API do HubSpot para pegar uma propriedade Individual de um objeto
# # url = 'https://api.hubapi.com/crm/v3/properties/{object}/{propertyName}'

# # URL do endpoint da API do HubSpot para pegar todas as propriedades de um objeto
# # url = 'https://api.hubapi.com/crm/v3/properties/{objectType}'

# properties_url = 'https://api.hubapi.com/properties/v1/deals/properties'

# headers = {
#     'Authorization': f'Bearer {access_token}',
#     'Content-Type': 'application/json'
# }

# # Obtém todas as propriedades disponíveis para contatos
# response = requests.get(properties_url, headers=headers)
# properties_data = response.json()
# all_properties = [prop['name'] for prop in properties_data]

# # URL do endpoint da API do HubSpot para contatos
# contacts_url = 'https://api.hubapi.com/crm/v3/objects/deals'

# def get_all_deals_with_properties(url, headers):
#     contacts = []
#     has_more = True
#     after = None
#     properties_param = ','.join(properties)

#     while has_more:
#         params = {
#             'properties': properties_param,
#             'limit': 100  # Você pode ajustar o limite conforme necessário
#         }

#         if after:
#             params['after'] = after

#         response = requests.get(url, headers=headers, params=params)
#         response_data = response.json()

#         contacts.extend(response_data.get('results', []))

#         # Verifica se há mais páginas
#         paging = response_data.get('paging')
#         if paging and 'next' in paging:
#             after = paging['next']['after']
#         else:
#             has_more = False

#     return contacts

# contacts = get_all_deals_with_properties(contacts_url, headers, all_properties)

# # Exporta negocios para um arquivo JSON
# with open('get_all_deals_with_properties.json', 'w') as f:
#     json.dump(contacts, f, indent=4)

# print(f'Exportados {len(contacts)} contatos para get_all_deals_with_properties.json')