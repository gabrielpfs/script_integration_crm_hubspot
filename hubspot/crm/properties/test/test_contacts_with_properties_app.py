# import requests
# import json

# # Seu token de acesso privado do HubSpot
# access_token = 'your_access_token'

# # URL do endpoint da API do HubSpot para pegar uma propriedade Individual de um objeto
# # url = 'https://api.hubapi.com/crm/v3/properties/{object}/{propertyName}'

# # URL do endpoint da API do HubSpot para pegar todas as propriedades de um objeto
# # url = 'https://api.hubapi.com/crm/v3/properties/{objectType}'

# properties_url = 'https://api.hubapi.com/properties/v1/contacts/properties'

# headers = {
#     'Authorization': f'Bearer {access_token}',
#     'Content-Type': 'application/json'
# }

# # Obtém todas as propriedades disponíveis para contatos
# response = requests.get(properties_url, headers=headers)
# properties_data = response.json()
# all_properties = [prop['name'] for prop in properties_data]

# # URL do endpoint da API do HubSpot para contatos
# contacts_url = 'https://api.hubapi.com/crm/v3/objects/contacts'

# def get_all_contacts_with_properties(url, headers):
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

# contacts = get_all_contacts_with_properties(contacts_url, headers, all_properties)

# # Exporta contatos para um arquivo JSON
# with open('get_all_contacts_with_properties.json', 'w') as f:
#     json.dump(contacts, f, indent=4)

# print(f'Exportados {len(contacts)} contatos para get_all_contacts_with_properties.json')

# # Para obter todas as colunas que voce adicionou a visualizacao All Contacts, precisa-se especificar essas propriedades na solicitacao a API do HubSpot.

# # Para obter todas as colunas (propriedades) que você adicionou na visualização "All contacts" no HubSpot, você precisa especificar quais propriedades deseja incluir na solicitação para a API.

# # A API do HubSpot permite que você especifique as propriedades que deseja retornar usando o parâmetro properties na URL da sua solicitação. Você pode adicionar este parâmetro várias vezes para solicitar várias propriedades.


# # Note: O limite de 100 registros por solicitação é definido pela API do HubSpot. Se você precisar de mais registros por solicitação, pode ajustar o parâmetro limit.

# import requests
# import json

# # Seu token de acesso privado do HubSpot
# access_token = 'pat-na1-2ea9272f-c006-488a-bc12-07af0c27385f'

# # URL do endpoint da API do HubSpot para propriedades de contatos
# properties_url = 'https://api.hubapi.com/properties/v1/contacts/properties'

# headers = {
#     'Authorization': f'Bearer {access_token}',
#     'Content-Type': 'application/json'
# }

# # Obtém todas as propriedades disponíveis para contatos
# response = requests.get(properties_url, headers=headers)
# if response.status_code == 200:
#     properties_data = response.json()
#     all_properties = [prop['name'] for prop in properties_data]
# else:
#     print("Erro ao obter propriedades dos contatos:", response.status_code, response.text)
#     all_properties = []
#     # O script primeiro obtém todas as propriedades disponíveis para os contatos e as utiliza para definir quais propriedades serão solicitadas para cada contato.

# # URL do endpoint da API do HubSpot para contatos
# contacts_url = 'https://api.hubapi.com/crm/v3/objects/contacts'

# def get_all_contacts(url, headers, properties):
#     contacts = []
#     has_more = True
#     after = None
#     properties_param = ','.join(properties)

#     while has_more:
#         params = {
#             'properties': properties_param,
#             'limit': 100  # Este é o limite padrão por solicitação da API do HubSpot
#         }
#         if after:
#             params['after'] = after

#         response = requests.get(url, headers=headers, params=params)
#         if response.status_code == 200:
#             response_data = response.json()
#             contacts.extend(response_data.get('results', []))

#             # Verifica se há mais páginas
#             paging = response_data.get('paging')
#             if paging and 'next' in paging:
#                 after = paging['next']['after']
#             else:
#                 has_more = False
#                 # O script utiliza a paginação fornecida pela API do HubSpot para iterar através de todos os contatos. O parâmetro after é usado para continuar obtendo registros onde a última solicitação parou.
#         else:
#             print("Erro ao obter contatos:", response.status_code, response.text)
#             has_more = False

#     return contacts

# contacts = get_all_contacts(contacts_url, headers, all_properties)

# # Exporta contatos para um arquivo JSON
# with open('get_all_contacts_with_properties.json', 'w') as f:
#     json.dump(contacts, f, indent=4)

# print(f'Exportados {len(contacts)} contatos para get_all_contacts_with_properties.json')
