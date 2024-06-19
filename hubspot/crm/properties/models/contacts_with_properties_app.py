# import requests
# import json
# import pandas as pd # pandas utilizado para manipulacao de dados de dataframes # Openpyxl utilizado por pandas para exportar dataframes em arquivos excel
# # pip install pandas openpyxl # Instalar a biblioteca pandas e openpyxl (necessária para escrever arquivos Excel)
# import time # The time library is a module in Python provides functions for handling time-related tasks.
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # My Private HubSpot Access Token - Seu token de acesso privado do HubSpot
# access_token = 'your_access_token'

# # HubSpot API endpoint URL for contacts - URL do endpoint da API do HubSpot para contatos
# url = 'https://api.hubapi.com/crm/v3/objects/contacts'

# headers = {
#     'Authorization': f'Bearer {access_token}',
#     'Content-Type': 'application/json'
# }

# # Lista de propriedades específicas que você quer incluir
# # properties = [
# #     "firstname",
# #     "lastname",
# #     "email",
# #     "email_domain",
# #     "phone",
# #     "lead_status",
# #     "hubspot_owner_id",
# #     "createdate",
# #     "hs_lifecyclestage_marketingqualifiedlead_date",
# #     "hs_lifecyclestage_salesqualifiedlead_date",
# #     "last_activity_date",
# #     "lastmodifieddate",
# #     "source",
# #     "lifecyclestage",
# #     "company_type",
# #     "company_name",
# #     "property_size",
# #     "hs_analytics_source",
# #     "hs_analytics_utm_campaign",
# #     "status",
# #     "attribution"

# properties = {
#     "firstname",
#     "lastname",
#     "email",
#     "hs_email_domain",
#     "phone",
#     "hs_lead_status",
#     "hubspot_owner_id",
#     "createdate",
#     "hs_lifecyclestage_marketingqualifiedlead_date",
#     "hs_lifecyclestage_salesqualifiedlead_date",
#     "notes_last_updated",
#     "lastmodifieddate",
#     "lead_source",
#     "lifecyclestage",
#     "company_type",
#     "company",
#     "property_size",
#     "hs_analytics_source",
#     "lead_origin",
#     "hs_content_membership_status",
#     "attribution"
# }
# # To discover how is the right way to describe the properties is the following steps: Setting > Data Management > Properties > Click on Specific Property > Click on the (</>) Icon

# def get_all_contacts(url, headers, properties):
#     print("Starting to fetch and collect all the contacts from HubSpot:")
#     contacts = []
#     has_more = True
#     after = None
#     properties_param = ','.join(properties)

#     while has_more:
#         print("Searching for more contacts (pagging) or Requesting data from API:")
#         params = {
#             'properties': properties_param,
#             'limit': 100  # You can adjust the limit as needed - Você pode ajustar o limite conforme necessário
#         }
#         if after:
#             params['after'] = after

#         response = requests.get(url, headers=headers, params=params)
#         response_data = response.json()

#         contacts.extend(response_data.get('results', []))

#         # Check if there are more pages - Verifica se há mais páginas
#         paging = response_data.get('paging')
#         if paging and 'next' in paging:
#             after = paging['next']['after']
#         else:
#             has_more = False
    
#     print("All contacts have been fecthed or Collect of the contacts was successful.")
#     return contacts

# def send_email():
#     # Configuring the SMTP server
#     smtp_server = 'smtp-mail.outlook.com'
#     smtp_port = 587 # 465 used to SMTP with SSL
#     sender_email = 'sender_email'
#     sender_password = 'your_password'
#     # recipient_email = 'recipient_email@example.com'

#     # Configuring the Email
#     recipient_email = 'recipient_email'
#     subject = "Automatic email in python"
#     body = """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta http-equiv="X-UA-Compatible" content="IE=edge">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Email Teste</title>
#     </head>
#     <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f2f2f2;">
#         <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f2f2f2;">
#             <tr>
#                 <td align="center">
#                     <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff;">
#                         <tr>
#                             <td align="center" style="padding: 40px 0;">
#                                 <img src="https://img.freepik.com/fotos-gratis/paisagem-de-nevoeiro-matinal-e-montanhas-com-baloes-de-ar-quente-ao-nascer-do-sol_335224-794.jpg" alt="Paisagem" width="400" style="display: block; margin: 0 auto;">
#                                 <p style="margin-top: 20px; text-align: center;">Olá,</p>
#                                 <p style="text-align: center;">Este é um e-mail de teste com uma imagem anexada.</p>
#                                 <p style="text-align: center;">Agradecemos por ter recebido este e-mail de teste.</p>
#                                 <p style="text-align: center;">Este e-mail foi enviado apenas para fins de demonstração e teste.</p>
#                             </td>
#                     </tr>
#                 </table>
#             </td>
#         </tr>
#     </table>
# </body>
# </html>"""
    
#     # Creating the message
#     message = MIMEMultipart()
#     message['from'] = sender_email
#     message['to'] = recipient_email
#     message['subject'] = subject
#     # message['Subject'] = 'Script Executado com Sucesso'
#     # body = 'O script foi executado com sucesso e os dados foram exportados.'
#     message.attach(MIMEText(body, 'html'))

#     # Connecting to SMTP server
#     try:
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(send_email, sender_password)
#         # text = message.as_string()
#         server.sendmail(send_email, recipient_email, message.as_string())
#         print("Email enviado com sucesso")
#     except Exception as e:
#         print(f'Houve algum erro:{e}')
#     finally:
#         server.quit()

# print("Fetching all contacts or Starting the Script")
# def main (): # Definicao da Funcao 'main()': A funcao main() é definida para conter o fluxo principal do seu script. Ela chama a função get_all_contacts para buscar os contatos, e então exporta os dados em formatos JSON, CSV e Excel.
#     contacts = get_all_contacts(url, headers, properties)

#     # Exporta contatos para um arquivo JSON
#     print("Exporting the contacts to a JSON file:")
#     with open('contacts_with_properties_app.json', 'w') as f:
#         json.dump(contacts, f, indent=4)

#     # Converte a lista de contatos em um DataFrame do pandas
#     df = pd.json_normalize(contacts) # utilizado para transformar a lista de contatos em um dataframe do pandas

#     # df = pd.dataframe (contacts) # cria um dataframe do pandas a partir dos contatos

#     # Exporta o dataframe contatos para um arquivo CSV
#     print("Exporting the contacts to a CSV file")
#     df.to_csv('ncontacts_with_properties_appew.csv', index=False)

#     # Exporta o dataframe contatos para um arquivo Excel
#     print("Exporting the contacts to a Excel file")
#     df.to_excel('contacts_with_properties_app.xlsx', index=False)

#     print(f'Exportados {len(contacts)} contatos para contacts_with_properties_app.json, contacts_with_properties_app.csv e contacts_with_properties_app.xlsx')
#     print("Script completed.")

#     # Add a timer of 5 seconds before it close
#     time.sleep(5) # 'time.sleep(10)' é usado no final da função 'main()' para pausar a execução do script por 10 segundos antes de terminar. Isso dará tempo para o usuário ver a mensagem final antes do terminal fechar.

# if __name__ == '__main__': # Verificacao 'if __name__ == '__main__':': Esta linha garante que a função main() será executada apenas quando o script for executado diretamente (e não quando ele for importado como um módulo em outro script).
#     main()