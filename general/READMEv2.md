<h1 align="center">
  <br>
  <a href="[https://drive.google.com/file/d/1Az5HHjbJygWJgpLpZh4MPJ6L173-kYUo/view?usp=drive_link](https://github.com/gabrielpsf/integration-crm/blob/main/assets/image.png)"><img src="https://github.com/gabrielpsf/integration-crm/blob/main/assets/image.png" alt="CRM Hubspot" width="200"></a>
  <br>
  CRM Hubspot
  <br>
</h1>

# HubSpot Contact Fetcher
Welcome to the documentation for the HubSpot Contact Fetcher project. This Python script is designed to automate the process of fetching contact data from HubSpot, converting the data into different formats (JSON, CSV, and Excel), and sending an email notification once the process is completed.

## Overview
The script uses the HubSpot API to fetch contact data based on specified properties. The fetched data is then converted into a pandas DataFrame and exported as a JSON file, a CSV file, and an Excel file. After the data export is completed, the script sends an email notification with a custom HTML body.

## Key Features
- **Fetch Contact Data:** The script connects to the HubSpot API, retrieves contact information based on specified properties, and handles pagination to ensure all contacts are fetched.
- **Data Conversion:** The fetched data is converted into a pandas DataFrame and exported in three different formats: JSON, CSV, and Excel.
- **Email Notification:** An email notification is sent after the data export is completed. The email is configured with SMTP and includes a custom HTML body.

This script is a powerful tool for automating data export tasks and can be customized to fit your specific needs. Whether you need to regularly export contact data or want to automate email notifications, this script has you covered. Enjoy exploring its capabilities and making it your own!

- **News:** You can make your own requests with this project to extract other information from the crm making a little changes.

## Authors

- [@gabrielpfs](https://www.github.com/gabrielpfs)

## Used By

This project is used by the following companies:

- Group Software
- Vinteum Software

## Tech Stack

**Client:** Python

**Server:** HubSpot API RESTful 

<details>
<summary>
  Languages:
</summary> <br />

  - Pythons 3.12.3
  
- HTML
</details>

<details>
<summary>
  Libraries:
</summary> <br />
  
- requests (HTTP requests)

- pandas
  
- smtplib (SMTP email sending)
  
- os
  
- json
  
- time
</details>

**Dependencies:** requests, pandas, pytest

<details>
<summary>
  Requirements:
</summary> <br />
  
- [Python 3.5+](https://docs.python.org/3/)

- [pip](https://pypi.org/project/pip/)
</details>

## Support

For support, email contactgabriel@gmail.com or join our Slack channel.

## Project Visualization

![Burnup Dashboard]()

## Usage - How To Use on your Own

Clone the project

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
- **[Twitter](https://twitter.com/dataventures)** for the latest updates on the product and published blogs.
- **[YouTube](https://www.youtube.com/c/dataventures)** for guides and technical talks.

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
<a href="https://github.com/gabrielpsf"><img src="https://avatars.githubusercontent.com/u/138036928?v=4" title="gabrielpsf" width="50" height="50"></a>

[//]: contributor-faces


## Feedback

If you have any feedback, please reach out to us at contactgabriel@gmail.com


## License

[MIT](https://choosealicense.com/licenses/mit/)


## 🔗 Links
[![portfolio](https://beacons.ai/gabrielpfsantos)](https://katherineoelsner.com/)
[![linkedin](https://www.linkedin.com/in/gabprates/)](https://www.linkedin.com/)