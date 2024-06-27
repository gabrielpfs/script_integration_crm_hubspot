<a name="readme-top"></a>

<!--
HOW TO USE:
This is an example of how you may give instructions on setting up your project locally.

Modify this file to match your project and remove sections that don't apply.

REQUIRED SECTIONS:
- Table of Contents
- About the Project
  - Built With
  - Live Demo
- Getting Started
- Authors
- Future Features
- Contributing
- Show your support
- Acknowledgements
- License

OPTIONAL SECTIONS:
- FAQ

After you're finished please remove all the comments and instructions!
-->

<div align="center">
  <!-- You are encouraged to replace this logo with your own! Otherwise you can also remove it. -->
  <img src="python_integration.png" alt="logo" width="140"  height="auto" />
  <br/>

  <h3><b>HubSpot Integration</b></h3>

</div>

<!-- TABLE OF CONTENTS -->

# Table of Contents

- [About the Project](#about-project)
  - [Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [Live Demo](#live-demo)
- [Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#triangular_flag_on_post-deployment)
- [Authors](#authors)
- [Future Features](#future-features)
- [Contributing](#contributing)
- [Show your support](#support)
- [Acknowledgements](#acknowledgements)
- [FAQ (OPTIONAL)](#faq)
- [License](#license)

<!-- PROJECT DESCRIPTION -->

# HubSpot Integration <a name="about-project"></a>

> This project is a Python script that interacts with the HubSpot CRM to fetch contact data, process it, and export it in JSON, CSV, and Excel formats. Additionally, it has functionality to send an email notification using the SMTP protocol.

**[HubSpot Integration]** is a Python-based application that interfaces with the HubSpot CRM to retrieve and manipulate contact information. It has the capability to export the processed data in various formats including JSON, CSV, and Excel. Furthermore, it incorporates an email notification feature that utilizes the SMTP protocol to send updates.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

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

<!-- Features -->

### Key Features <a name="key-features"></a>

- **Automated_Data_Fetching_from_HubSpot**
- **Data_Export_in_Multiple_Formats**
- **Automated_Email_Notifications**

> The application utilizes the HubSpot API to automatically fetch contact data. By specifying the desired contact properties, the application can retrieve comprehensive information about contacts stored in the HubSpot CRM. The data is fetched in a paginated manner, ensuring that even large datasets are handled efficiently without manual intervention.

> Once the contact data is fetched, the application converts and exports this data into three different formats: JSON, CSV, and Excel. This flexibility allows users to utilize the data in various applications and workflows. JSON is ideal for integration with other software systems, CSV is widely used for data analysis and import into databases, and Excel is perfect for detailed reporting and data manipulation.

> After exporting the data, the application sends an automated email notification. This email includes the exported files as attachments and a custom HTML message body. The email functionality is powered by the SMTP protocol, making it versatile for integration with various email services. This feature ensures that stakeholders are immediately informed of the availability of the latest data, enhancing collaboration and decision-making processes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

> Welcome to the HubSpot Data Fetching and Exporting project! This guide will help new developers get up and running with the project, including installation, configuration, and usage instructions.

To get a local copy up and running, follow these steps:

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

<!--
Example command:

```sh
 gem install rails
```
 -->

### Setup

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

<!--
Example commands:

```sh
  cd my-folder
  git clone git@github.com:myaccount/my-project.git
```
--->

### Usage

To run the project, execute the following command:

```bash
python contacts_with_properties_app.py
```

<!--
Example command:

```sh
  rails server
```
--->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./licence) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->