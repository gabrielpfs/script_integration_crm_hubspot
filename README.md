<h1 align="center">
  <br>
  <a href="https://github.com/user-attachments/assets/61250cf8-9b95-4770-ba91-07c3bdd87754"><img src="https://github.com/user-attachments/assets/61250cf8-9b95-4770-ba91-07c3bdd87754" alt="logo" width="80"></a>
  <a href="https://github.com/user-attachments/assets/8188f8ab-f0b5-4c0c-b639-e6d4a0b51128"><img src="https://github.com/user-attachments/assets/8188f8ab-f0b5-4c0c-b639-e6d4a0b51128" alt="hubspot" width="80"></a>
  <br>
  CRM Hubspot
  <br>

</h1>
<a href="https://github.com/Vinteum-Software/integration_collaboration_airtable/assets/88781022/f2805712-3a35-49de-b95b-4c3e5e266392"><img src="https://github.com/Vinteum-Software/integration_collaboration_airtable/assets/88781022/f2805712-3a35-49de-b95b-4c3e5e266392" width="80"></a>
<br>

# HubSpot Integration Contact Fetcher

Welcome to the documentation for the HubSpot Contact Fetcher project. This Python script is designed to automate the process of fetching contact data from HubSpot, converting the data into different formats (JSON, CSV, and Excel), and sending an email notification once the process is completed.

This project is a Python script that interacts with the HubSpot CRM to fetch contact data, process it, and export it in JSON, CSV, and Excel formats. Additionally, it has functionality to send an email notification using the SMTP protocol.
 
**HubSpot Integration** is a Python-based application that interfaces with the HubSpot CRM to retrieve and manipulate contact information. It has the capability to export the processed data in various formats including JSON, CSV, and Excel. Furthermore, it incorporates an email notification feature that utilizes the SMTP protocol to send updates.

## Overview

The script uses the HubSpot API to fetch contact data based on specified properties. The fetched data is then converted into a pandas DataFrame and exported as a JSON file, a CSV file, and an Excel file. After the data export is completed, the script sends an email notification with a custom HTML body.

This project involves fetching contact data from HubSpot, manipulating the data, and sending an email with the exported data. Here’s a detailed overview of the tech stack, including the client, server, and database components:

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://python.org/">Python</a></li>
    <li><a href="https://pypi.org/project/requests/">requests</a></li>
    <li><a href="https://docs.python.org/3/library/json.html">json</a></li>
    <li><a href="https://pandas.pydata.org/">pandas</a></li>
    <li><a href="https://pypi.org/project/openpyxl/">openpyxl</a></li>
    <li><a href="https://docs.python.org/3/library/time.html">time</a></li>
    <li><a href="https://docs.python.org/3/library/smtplib.html">smtplib</a></li>
    <li><a href="https://docs.python.org/3/library/email.mime.html">email.mime.multipart</a></li>
    <li><a href="https://docs.python.org/3/library/email.mime.html">email.mime.text</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://developers.hubspot.com/docs/api/crm/contacts">Endpoint</a></li>
    <li><a href="https://developers.hubspot.com/docs/api/private-apps#make-api-calls-with-your-app-s-access-token">Access Token</a></li>
    <li><a href="https://developers.hubspot.com/docs/api/oauth/tokens">Access Token 2.0</a></li>
    <li><a href="https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040">SMTP Configuration</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://knowledge.hubspot.com/get-started/manage-your-crm-database?utm_campaign=UserGuides&utm_source=Developers&_ga=2.210980821.190745408.1718018636-1581166926.1715862096&_gl=1*1rwddz8*_gcl_au*ODY3OTkzMjk0LjE3MTU4NjIwOTU.*_ga*MTU4MTE2NjkyNi4xNzE1ODYyMDk2*_ga_LXTM6CQ0XK*MTcxODAzODgzMC4xNi4xLjE3MTgwMzkzNjAuMTkuMC4w#3-get-started-with-your-crm">HubSpot Database</a></li>
  </ul>
</details>

## Key Features
- **Fetch Contact Data:** The script connects to the HubSpot API, retrieves contact information based on specified properties, and handles pagination to ensure all contacts are fetched.
- **Data Conversion:** The fetched data is converted into a pandas DataFrame and exported in three different formats: JSON, CSV, and Excel.
- **Email Notification:** An email notification is sent after the data export is completed. The email is configured with SMTP and includes a custom HTML body.

> The application utilizes the HubSpot API to automatically fetch contact data. By specifying the desired contact properties, the application can retrieve comprehensive information about contacts stored in the HubSpot CRM. The data is fetched in a paginated manner, ensuring that even large datasets are handled efficiently without manual intervention.

> Once the contact data is fetched, the application converts and exports this data into three different formats: JSON, CSV, and Excel. This flexibility allows users to utilize the data in various applications and workflows. JSON is ideal for integration with other software systems, CSV is widely used for data analysis and import into databases, and Excel is perfect for detailed reporting and data manipulation.

> After exporting the data, the application sends an automated email notification. This email includes the exported files as attachments and a custom HTML message body. The email functionality is powered by the SMTP protocol, making it versatile for integration with various email services. This feature ensures that stakeholders are immediately informed of the availability of the latest data, enhancing collaboration and decision-making processes.


This script is a powerful tool for automating data export tasks and can be customized to fit your specific needs. Whether you need to regularly export contact data or want to automate email notifications, this script has you covered. Enjoy exploring its capabilities and making it your own!

- **News:** You can make your own requests with this project to extract other information from the crm making a little changes.

## Authors

- [@gabrielpfs](https://www.github.com/gabrielpfs)

## Used By

This project is used by the following companies:

- Group Software
- Vinteum Software

## Tech Stack

> This project involves fetching contact data from HubSpot, manipulating the data, and sending an email with the exported data. Here’s a detailed overview of the tech stack, including the client, server, and database components:

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://python.org/">Python</a></li>
    <li><a href="https://pypi.org/project/requests/">requests</a></li>
    <li><a href="https://docs.python.org/3/library/json.html">json</a></li>
    <li><a href="https://pandas.pydata.org/">pandas</a></li>
    <li><a href="https://pypi.org/project/openpyxl/">openpyxl</a></li>
    <li><a href="https://docs.python.org/3/library/time.html">time</a></li>
    <li><a href="https://docs.python.org/3/library/smtplib.html">smtplib</a></li>
    <li><a href="https://docs.python.org/3/library/email.mime.html">email.mime.multipart</a></li>
    <li><a href="https://docs.python.org/3/library/email.mime.html">email.mime.text</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://developers.hubspot.com/docs/api/crm/contacts">Endpoint</a></li>
    <li><a href="https://developers.hubspot.com/docs/api/private-apps#make-api-calls-with-your-app-s-access-token">Access Token</a></li>
    <li><a href="https://developers.hubspot.com/docs/api/oauth/tokens">Access Token 2.0</a></li>
    <li><a href="https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040">SMTP Configuration</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://knowledge.hubspot.com/get-started/manage-your-crm-database?utm_campaign=UserGuides&utm_source=Developers&_ga=2.210980821.190745408.1718018636-1581166926.1715862096&_gl=1*1rwddz8*_gcl_au*ODY3OTkzMjk0LjE3MTU4NjIwOTU.*_ga*MTU4MTE2NjkyNi4xNzE1ODYyMDk2*_ga_LXTM6CQ0XK*MTcxODAzODgzMC4xNi4xLjE3MTgwMzkzNjAuMTkuMC4w#3-get-started-with-your-crm">HubSpot Database</a></li>
  </ul>
</details>

## Support

For support, email contactgabriel@gmail.com or join our Slack channel.

## Project Visualization
![burnup_dashboard](burnup_dashboard.png)

## Usage - How To Use on your Own

### Prerequisites

In order to run this project you need:

```bash
pip install python
```

```bash
python install pyinstaller
```

```bash
pip install requests
```

```bash
pip install pandas
```

```bash
pip install openpyxl
```

or you can run all of them:

```bash
pip install requests pandas openpyxl
```

Clone the project, to get a local copy up and running, follow these steps:

```bash
  git clone https://github.com/gabrielpsf/integration-crm-hubspot
```

Go to the project directory

```bash
  cd integration-crm-hubspot
```

Install dependencies

```bash
  npm install
```

Start the server or Run the App

```bash
  npm run start
```

Clone this repository to your desired folder:

```bash
git clone https://github.com/your-username/hubspot-data-fetch.git
cd hubspot-data-fetch
```

HubSpot Access Token:
```bash
access_token = 'your_hubspot_access_token'
```

SMTP Email Configuration:
```bash
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
sender_email = 'your_email@example.com'
sender_password = 'your_password'
recipient_email = 'recipient_email@example.com'
```

### Usage

To run the project, execute the following command:

```bash
python contacts_with_properties_app.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

# Demo
in development (Insert gif or link to demo)

# Deployment Project on GitHub

Deploying a project on GitHub involves several steps, including creating a repository, adding your project files, committing your changes, and pushing them to GitHub. Here’s a step-by-step guide:

## Set Up Git

### Install Git
- Download and install Git from [git](https://git-scm.com/).
- Configure Git with your username and email:

```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
```

## Create a Repository on GitHub
### Log in to GitHub
- Go to [GitHub](https://github.com/) and log in to your account.

### Create a New Repository
- Click the "+" icon in the top right corner and select "New repository".
- Enter a repository name, provide a description (optional), choose public or private, and optionally initialize with a README.
- Click "Create repository".

## Initialize Local Repository
### Navigate to your project directory:

```bash
    cd /path/to/your/project
```

### Initialize a Git repository:

```bash
    git init
```

## Add Your Project Files
### Add all files to the repository:

```bash
    git add .
```

### Commit your changes:

```bash
    git commit -m "Initial commit"
```

## Connect to GitHub Repository
### Add the remote repository:
- Copy the URL of your GitHub repository (e.g., https://github.com/yourusername/your-repo.git).
- Add it as a remote:

```bash
    git remote add origin https://github.com/yourusername/your-repo.git
```

## Push to GitHub
### Push your changes to GitHub:

```bash
    git push -u origin master
```

## Verify Your Repository
### Go to your GitHub repository URL:
- Verify that your files are now available in the repository.

## Optional: Update Your Repository
- Make changes to your files locally.
- Stage the changes:

```bash
    git add .
```

- Commit your changes:

```bash
    git commit -m "Describe your changes"
```

- Push the changes:

```bash
    git push
```

## Publishing on GitHub in Differents Accounts - Git Bash
### Verify if is logged with the correct account

```bash
    git config --global user.name
    git config --global user.email
```

### SSH Authentication (if you don't have one yet)

```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

### Add a SSH key to ssh-agent:

```bash
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_rsa
```

### Add the SSH key to your Github account

```bash
    cat ~/.ssh/id_rsa.pub
```

### Add to your remote repository by SSH

```bash
    git remote set-url origin git@github.com:your_github_username/github_project_name.git
```

### Do the Push again

```bash
    git push -u origin main
```

## Publishing on GitHub with Different Accounts

To work with two different GitHub repositories using different accounts on the same system, you can use various approaches. Below is a step-by-step guide to configuring your Git environment to handle this situation.

### Use Different SSH Keys

This approach involves creating separate SSH keys for each GitHub account and configuring Git to use the appropriate key for each repository.

### Generate SSH Key
- First Account

```bash
    ssh-keygen -t rsa -b 4096 -C "first_email@example.com" -f ~/.ssh/id_rsa_first_account
```

- Second Account

```bash
    ssh-keygen -t rsa -b 4096 -C "second_email@example.com" -f ~/.ssh/id_rsa_second_account
```

### Generate sssh-agent Key

- Start the ssh-agent:

```bash
    eval "$(ssh-agent -s)"
```

- Add the first key

```bash
    ssh-add ~/.ssh/id_rsa_first_account
```

- Add the second key

```bash
    ssh-add ~/.ssh/id_rsa_second_account
```

### Add the keys to GitHub
- Get the public keys

```bash
    cat ~/.ssh/id_rsa_first_account.pub
    cat ~/.ssh/id_rsa_second_account.pub
```

- To add each public key to the respective GitHub account:
  - Go to "SSH and GPG keys" in the settings of each GitHub account.
  - Click on "New SSH key" and paste the corresponding public key.

### Config the SSH Config File
- Edit the file `~/.ssh/config` or create it if does't exist

```bash
    nano ~/.ssh/config
```

- Add the following configurations:

```bash
# Config to First Account
Host github-conta1
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa_conta1

# Config to Second Account
Host github-conta2
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa_conta2
```

## Clone the Repository
### To clone a repository using the first account

```bash
    git clone git@github-first_account:first_user/repository2.git
```

### To clone a repository using the second account

```bash
    git clone git@github-second_account:second_user/repository2.git
```

## Config the Remote in the Existing Repositories
### To a Repository cloned with the first account

```bash
    git remote set-url origin git@github-first_account:user
```

### To a Repository cloned with the second account

```bash
    git remote set-url origin git@github-second_account:user
```
# Using HTTPS Key

## Using Personal Access Token (PAT) for HTTPS

### Generate a Personal Access Token:

- Go to [GitHub](https://github.com/) and log in to your account.
- In the upper right corner, click on your profile photo and select Settings.
- In the left sidebar, click on Developer settings.
- Then click on Personal access tokens.
- Click on Generate new token.
- Give your token a descriptive name, such as "Cloning Private Repo".
- Select the repo scope to grant full control of private repositories.
- Click Generate token and copy the token. Store it securely.

### Clone the Repository Using the Token:

- Open Git Bash or another terminal of your choice.
- Navigate to the directory where you want to clone the repository:

```
cd "C:\Gabriel Prates\New folder"
```

- Use the git clone command with the repository URL, including the personal access token for authentication:

```
git clone https://YOUR_USERNAME:YOUR_PERSONAL_ACCESS_TOKEN@github.com/gabrielpfs/development_financial_portfolio.git
```

Replace YOUR_USERNAME with your GitHub username and YOUR_PERSONAL_ACCESS_TOKEN with the token you generated.

# Using SSH Key

## Generate an SSH Key (if you don't already have one):

- Open Git Bash or another terminal of your choice and generate an SSH key:

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

- Press Enter to accept the default file location.
- Enter a strong passphrase (or press Enter to leave it empty).

## Add the SSH Key to the SSH Agent:

- Start the SSH agent:

```
eval "$(ssh-agent -s)"
```

- Add your private SSH key to the SSH agent:

```
ssh-add ~/.ssh/id_rsa
```

## Add the SSH Key to Your GitHub Account:

- Copy the public SSH key to your clipboard:

```
cat ~/.ssh/id_rsa.pub
```

- Go to [GitHub](https://github.com/) and log in to your account.
- In the upper right corner, click on your profile photo and select Settings.
- In the left sidebar, select SSH and GPG keys.
- Click on New SSH key, paste your public key, and click Add SSH key.

## Clone the Repository Using SSH:

- Navigate to the directory where you want to clone the repository:

```
cd "C:\Gabriel Prates\New folder"
```

- Use the git clone command with the SSH URL of the repository:

```
git clone git@github.com:gabrielpfs/development_financial_portfolio.git
```
## Summary

### Using Personal Access Token (HTTPS)

```
cd "C:\Gabriel Prates\New folder"
git clone https://YOUR_USERNAME:YOUR_PERSONAL_ACCESS_TOKEN@github.com/gabrielpfs/development_financial_portfolio.git
```

### Using SSH

```
cd "C:\Gabriel Prates\New folder"
git clone git@github.com:gabrielpfs/development_financial_portfolio.git
```

## Configurations

```bash
    $ cd ~/.ssh/
```

```bash
    $ ls
    $ ls ~/.ssh/
```

```bash
    $ cd ../
```

```bash
    $ git push -u origin main
```

```bash
    $ git remote set-url origin git@github.com:github_personal/https://github.com/github_username/project_name.git
```

```bash
    $ git remote set-url origin git@github.com:github_username/https://github.com/github_username/project_name.git
```

```bash
    $ cat ~/.ssh/id_rsa_personal_account.pub
```

```bash
    $ cat ~/.ssh/id_rsa_personal_account.pub
```

```bash
    $ ssh -T git@github_personal
```

```bash
    $ git remote set-url origin git@github.com:github_username/https://github.com/github_username/project_name.git
```

```bash
    $ git push -u origin main
```

## Resources

- **[Website](https://dataventures.com)** overview of the product.
- **[Docs](https://docs.dataventures.com)** for comprehensive documentation.
- **[Blog](https://dataventures.com/blog)** for guides and technical comparisons.
- **[Discord](https://dataventures.com/discord)** for support and discussions with the community and the team.
- **[GitHub](https://github.com/gabrielpsf/gabrielpsf)** for source code, project board, issues, and pull requests.
<!-- - **[Twitter](https://twitter.com/dataventures)** for the latest updates on the product and published blogs.-->
<!-- - **[YouTube](https://www.youtube.com/c/dataventures)** for guides and technical talks.-->

<a name="contributing_anchor"></a>

## Contributing

The majority of HubSpot Integration CRM code is open-source. We are committed to a transparent development process and highly appreciate any contributions. Whether you are helping us fix bugs, proposing new features, improving our documentation or spreading the word - we would love to have you as a part of the Integration of CRMs community.
- Bug Report: If you see an error message or encounter an issue while using this code in your application to connect with any crm to get contacts or others categories, please create a [bug report]().

- Feature Request: If you have an idea or if there is a capability that is missing and would make development easier and more robust, please submit a [feature request]().

- Documentation Request: If you're reading the Amplication docs and feel like you're missing something, please submit a [documentation request]().

Not sure where to start? Join our discord and we will help you get started!

<a href="https:/dataventures/.com/discord"><img src="https://amplication.com/images/discord_banner_purple.svg" /></a>

## Contributors

[//]: contributor-faces
<a href="https://github.com/gabrielpfs"><img src="https://avatars.githubusercontent.com/u/88781022?s=96&v=4" title="gabrielpsf" width="50" height="50"></a>

[//]: contributor-faces


## Feedback

If you have any feedback, please reach out to us at contatogabrielsantosgs@gmail.com


## License

[MIT](https://choosealicense.com/licenses/mit/)


<h3>🔗 Connections</h3>
<p>
<a href="https://beacons.ai/gabrielpfsantos" target="blank"><img src="https://iili.io/HQZDQCQ.png" alt="test" height="30" width="30" /></a>
<a href="https://www.linkedin.com/in/gabprates/" target="_blank"><img src="https://t.ctcdn.com.br/IwwDh-BajTE4ZwE4zuIcvz9Q2ZY=/i490027.jpeg" alt="test" height="30" width="30" /></a>
</p>
