# SENG3011_McNuggets 🐔
## Table of Contents
* [Project Overview](#projoverview)
* [Deliverable 1](#deliverable1)
  1. [Design Details](#designdetails)
  2. [Management Information](#maninfo)
* [Deliverable 2](#deliverable2)
  1. [API Design Details](#apides)
  2. [API Testing](#apites)
  3. [API Documentation](#apidoc)
  4. [API Implementation](#apiimp)
* [Deliverable 3](#deliverable3)
* [Deliverable 4](#deliverable4)
  1. [Use Cases and Requirements](#usecases)
  2. [System Design and Implementation](#desandimp)
  3. [Management Information](#maninfo1)

## Project Overview 🍟 <a name="projoverview"></a>
Ever since COVID-19's breakout, more awareness and emphasis has been placed on the effectiveness of communication and knowledge of disease and outbreaks. The **McNuggets** aim to to develop a platform that would contribute to an alert society with complete access to vital health information. This platform will automate the extraction of data from available sources in order to produce the following information for the public:
* Outbreak alerts: Important notifications regarding outbreaks of a new disease, existing disease in a new area, etc.
* Watching briefs: Analysis on serious outbreaks, involving origins, symptoms, treatments, fatality rate, etc.
* Digest: Newsletters available to inform policy makers, government and other stakeholders about outbreaks.
### Members:
| Name               | zID      |
| ------------------ |----------|
| James Miller       | z5257531 |
| Kenneth Mejico     | z5257133 |
| Liam Staples       | z5254570 |
| Luke Junsuo Chen   | z5264602 |

## Deliverable 1 🍟 <a name="deliverable1"></a>
### Design Details <a name="designdetails"></a>
The overall development stack has been decided, but is flexible and subject to change. After collating a list of languages everyone is familiar with, we have decided to use Python for our API. This will most likely be used in conjunction with json and flask libraries. The operating system of choice for development and deployment will be Linux. We have also created a plan of action on how we are to develop the API module, which involves the scope of the API, identifying all endpoints, schema for parameters and responses, and more. Additionally, we have discussed the passing of parameters to the module and how the results should be collected. All of the above can be found more depth in our [Design Details Report](https://github.com/KennethMejico/SENG3011_McNuggets/blob/main/Reports/Design%20Details.md).

### Management Information <a name="maninfo"></a>
During deliverable 1, the **McNuggets** have assigned proper meeting times for standups, peer programming, admin work, etc. These meeting times will mainly take place on Tuesdays 13:00 - 14:20, and Sundays 21:00 - 22:00.
Team member responsibilities for Stage 1 (API Development, Webscraping, Documentation) were assigned, along with work arrangements for the first deliverable (Reports, GitHub repository). 

Our main software tools currently in use to assist project management are:
* Messenger Group Chat
* Microsoft Teams
* Github
* Stoplight
* Virtual Environments
* Google Docs
* Selenium / Requests

More information can be found in our [Management Information Report](https://github.com/KennethMejico/SENG3011_McNuggets/blob/main/Reports/Management%20Information.md).

## Deliverable 2 🍟 <a name="deliverable2"></a>
### API Design Details <a name="apides"></a>
The final architecture, justification of implementation, and challenges addressed for our project can be found here: [Design Details Report: Deliverable 2](https://github.com/KennethMejico/SENG3011_McNuggets/blob/main/Reports/Design%20Details.md#deliverable2)

Our architecture begins with a scraper that scrapes data from ProMedMail.org, which then stores that data into a MySQL database, (AWS Relational Database Service). We have a Python backend API that is run on AWS Lambda, which then takes user input (HTTP requests) from the Amazon API gateway and uses queries to retrieve data from RDS. It then formats it and returns a JSON response to the user.
### API Testing <a name="apites"></a>
A complete guide to our testing methodology can be found here: [Testing Documentation](https://github.com/KennethMejico/SENG3011_McNuggets/blob/main/Reports/Testing%20Documentation.md)
### API Documentation <a name="apidoc"></a>
Our API Documentation was completed on Stoplight, and can be found here: [McNuggets Stoplight](https://unsw-seng-mcnuggets.stoplight.io/docs/seng3011-mcnuggets)
### API Implementation <a name="apiimp"></a>
The API has been implemented on AWS Lambda, and can be called using our Stoplight's try it out feature. Log files have also been implemented, including details such as team name, accessed time, and data source.

## Deliverable 3 🍟 <a name="deliverable3"></a>

## Deliverable 4 🍟 <a name="deliverable4"></a>
Our web application, 'NugSearch', has been developed to work as a visualised search engine for disease reports found on [ProMedMail.org](https://promedmail.org/). Users can see the reports on diseases of interest and visualise that data in a graph to track the growth of infection and a map to see the areas threatened. They can also sign up to a mailing list to receive notifications if our system detects a lockdown, and gain an edge that allows them to prepare to weather the oncoming events.
### Use Cases and Requirements <a name="usecases"></a>
More information about the use cases and requirements of our web application can be found here: [Use Cases and Requirements](https://github.com/KennethMejico/SENG3011_McNuggets/blob/main/Reports/Design%20Details.md#usecases)
### System Design and Implementation <a name="desandimp"></a>
More information about our system design and implementation can be found here: [System Design and Implementation](https://github.com/KennethMejico/SENG3011_McNuggets/blob/main/Reports/Design%20Details.md#system-design-and-implementation-)
### Management Information <a name="maninfo1"></a>
Information regarding team organisation and appraisal of work can be found here: [Management Information](https://github.com/KennethMejico/SENG3011_McNuggets/blob/main/Reports/Management%20Information.md#deliverable4)
