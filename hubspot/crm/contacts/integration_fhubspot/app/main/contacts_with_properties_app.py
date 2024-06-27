import requests
import json
import pandas as pd
import time
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# The Private HubSpot Access Token of HubSpot
access_token = 'your_access_token'

# HubSpot API endpoint URL for contacts
url = 'https://api.hubapi.com/crm/v3/objects/contacts'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

properties = {
    "firstname",
    "lastname",
    "email",
    "hs_email_domain",
    "phone",
    "hs_lead_status",
    "hubspot_owner_id",
    "createdate",
    "hs_lifecyclestage_marketingqualifiedlead_date",
    "hs_lifecyclestage_salesqualifiedlead_date",
    "notes_last_updated",
    "lastmodifieddate",
    "lead_source",
    "lifecyclestage",
    "company_type",
    "company",
    "property_size",
    "hs_analytics_source",
    "lead_origin",
    "hs_content_membership_status",
    "attribution"
}
# To discover how is the right way to describe the properties is the following steps: Setting > Data Management > Properties > Click on Specific Property > Click on the (</>) Icon

def get_all_contacts(url, headers, properties):
    print("Starting to fetch and collect all the contacts from HubSpot:")
    contacts = []
    has_more = True
    after = None
    properties_param = ','.join(properties)

    while has_more:
        print("Searching for more contacts (pagging) or Requesting data from API:")
        params = {
            'properties': properties_param,
            'limit': 100  # You can adjust the limit as needed
        }
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
    
    print("All contacts have been fecthed or Collect of the contacts was successful.")
    return contacts

def send_email():
    # Configuring the SMTP server
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587 # 465 used to SMTP with SSL
    sender_email = 'your_email_sender'
    sender_password = 'your_password'
    # recipient_email = 'recipient_email@example.com'

    # Configuring the Email
    recipient_email = 'your_recipient_email'
    subject = "Automatic email in python"
    body = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Teste</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f2f2f2;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f2f2f2;">
            <tr>
                <td align="center">
                    <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff;">
                        <tr>
                            <td align="center" style="padding: 40px 0;">
                                <img src="https://img.freepik.com/fotos-gratis/paisagem-de-nevoeiro-matinal-e-montanhas-com-baloes-de-ar-quente-ao-nascer-do-sol_335224-794.jpg" alt="Paisagem" width="400" style="display: block; margin: 0 auto;">
                                <p style="margin-top: 20px; text-align: center;">Olá,</p>
                                <p style="text-align: center;">Este é um e-mail de teste com uma imagem anexada.</p>
                                <p style="text-align: center;">Agradecemos por ter recebido este e-mail de teste.</p>
                                <p style="text-align: center;">Este e-mail foi enviado apenas para fins de demonstração e teste.</p>
                            </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""
    
    # Creating the message
    message = MIMEMultipart()
    message['from'] = sender_email
    message['to'] = recipient_email
    message['subject'] = subject
    # message['Subject'] = 'Script Executado com Sucesso'
    # body = 'O script foi executado com sucesso e os dados foram exportados.'
    message.attach(MIMEText(body, 'html'))

    # Connecting to SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(send_email, sender_password)
        # text = message.as_string()
        server.sendmail(send_email, recipient_email, message.as_string())
        print("Email enviado com sucesso")
    except Exception as e:
        print(f'Houve algum erro:{e}')
    finally:
        server.quit()

print("Fetching all contacts or Starting the Script")
def main ():
    contacts = get_all_contacts(url, headers, properties)

    # Export the dataframe contacts for a JSON file
    print("Exporting the contacts to a JSON file:")
    with open('path_where_you_want_to_save_the_generated_file', 'w') as f:
        json.dump(contacts, f, indent=4)

    # Convert the contact list into a pandas DataFrame
    df = pd.json_normalize(contacts)

    # df = pd.dataframe (contacts) # Create a dataframe of pandas by the contacts

    # Export the dataframe contacts for a CSV file
    print("Exporting the contacts to a CSV file")
    df.to_csv('path_where_you_want_to_save_the_generated_file', index=False)

    # Export the dataframe contacts for a Excel file
    print("Exporting the contacts to a Excel file")
    df.to_excel('path_where_you_want_to_save_the_generated_file', index=False)

    print(f'Exportados {len(contacts)} contatos para contacts_with_properties_app.json, contacts_with_properties_app.csv e contacts_with_properties_app.xlsx')
    print("Script completed.")

    # Add a timer of 5 seconds before it close
    time.sleep(5)

# The verification of 'if __name__ == '__main__':': It guarantee that the function main () will be started only when the script will be directly executed.
if __name__ == '__main__': 
    main()