# Design Details 🍦
## Table of Contents
* [Deliverable 1](#deliverable1)
  1. [API Module Development](#apidev)
  2. [Module Interactions](#modint)
  3. [Development Stack](#devstack)
* [Deliverable 2](#deliverable2)
  1. [Final Architecture](#finarch)
  2. [Implementation Justification](#justif)
  3. [Challenges](#challenges)
## Deliverable 1 🥓 <a name="deliverable1"></a>
### API Module Development <a name="apidev"></a>
Question: *Describe how you intend to develop the API module and provide the ability to run it in Web service mode*

The first step is to make a detailed list of endpoints, describing exactly what format the response will be in and what information is being passed back by each endpoint. If we’re unclear about what each endpoint of the API does then in development we may run into issues such as redundant endpoints or confusing parameters. This step can be broken down a bit more:
1. Figure out what the broad scope of our API and app will be
2. List all the information we want to provide and actions we want to make possible for API users (identify all the endpoints)
3. Design the schema for the parameters and response of each endpoint
4. Make example data to show how it can be used and what type of information will be passed back
5. Fill out the documentation on Stoplight in a way that’s useable by others

Once our documentation is sorted out, we can begin actually creating these endpoints. At first, we will only return dummy data or perform superficial operations, but once every endpoint exists, we can go into making each one fully functional. After the design phase it will become apparent that some endpoints should be made before others, either because they are more useful or they are a base we can work off of for harder endpoints. The endpoints can be split up between group members, and each one can work on a set of related endpoints. The first few can also be done as a group, so we can establish a style and consistency in our code.

Stoplight lets us run a mock server that will provide example responses to api calls. When we create our API we’ll also need to run it on a live server to allow other teams to access it. Our team will make use of Amazon Web Services for easy and convenient hosting of our API, in particular using AWS Lambda. This service lets us host an API cheaply, only charging us for calls made to it, and is designed for small APIs like ours.

### Module Interactions <a name="modint"></a>
Question: *Discuss your current thinking about how parameters can be passed to your module and how results are collected. Show an example of a possible interaction. (e.g.- sample HTTP calls with URL and parameters)*
#### Request Details
**GET** http://sengmcnuggets.com/query
| Field      | Description                                                                                                 | Example             |
| ---------- | ----------------------------------------------------------------------------------------------------------- | ------------------- |
| start_date | The earliest date for which the user wants disease reports to be returned in the format yyyy-MM-ddTHH:mm:ss | 2015-10-01T08:45:10 |
| end_date   | The latest date for which the user wants disease reports to be returned in the format yyyy-MM-ddTHH:mm:ss   | 2015-11-01T19:37:12 |
| key_terms  | A comma separated list of all the key terms the user wants diseases reports about                           | Anthrax,Zika        |
| location   | Location name (city/country/state), which is a string to be matched with the content in the disease report  | Sydney              |

#### Respone Details
Overall Response:
```javascript
{
	articles: [<object::article>] // An array of article objects
}
```
Article Object:
```javascript
{
	url: <string>, // The url of the article
	date_of_publication: <string>, // The date the article was published
	headline: <string>, // The headline of the article
	main_text: <string>, // The main body of the article
	reports: [<object::report>] // An array of report objects
}
```

Report Object:
```javascript
{
	diseases: [<string::disease>], // the diseases relating to the report
	syndromes: [<string::syndrome>], // the syndromes relating to the report
	event_date: [<string>], // the date on which the case occurred
	locations: [<object::location>] // all the locations mentioned in the report referring to the case
}
```

Location Object:
```javascript
{
	geonames_id: <number> // the id of the location from the geonames database
}
```

event_date and date_of_publication dates are in one of two formats:
1. In the case of a single date, the format “yyyy-mm-dd hh:mm:ss” with the year always being present while every other segment is optional and uses ‘x’ if the character is missing
2. In the case of a date range, the format “yyyy-mm-dd hh:mm:ss to yyyy-mm-dd hh:mm:ss” is used with the years always being present while every other segment is optional and uses ‘x’ if the character is missing. The first date must be earlier than the second date

Example request:
> http://sengmcnuggets.com/query?start_date=2015-10-01T08:45:10&end_date=2015-11-01T19:37:12&keyterms=Anthrax,Zika&location=Sydney

Example Response (*Note:  this response is not related to the example request and is just an example of what a response would look like*)
```javascript
{
   "articles": [
       {
           "url": "https://www.cbsnews.com/news/ebola-monitoring-program-u-s-considering-as-new-cases-reported-in-africa/",
           "date_of_publication": "2021-02-26 21:17:xx",
           "headline": "U.S. to implement Ebola monitoring program at airports as new cases reported in Africa",
           "main_text": "The U.S. will soon be monitoring travelers coming into the country from two nations impacted by the Ebola virus, the Centers for Disease Control and Prevention announced Friday. The CDC confirmed these plans after CBS News first reported the details on Friday night.",
           "reports": [
               {
                   "diseases": ["ebola haemorrhagic fever", "zika"],
                   "syndromes": ["Haemorrhagic Fever"],
                   "event_date": "2021-01-19 xx:xx:xx to 2021-02-12 xx:xx:xx",
                   "locations": [6354908,2154855]
               }
           ]
       },
       {
           "url": "https://www.sample.com/news/influenza-outbreak",
           "date_of_publication": "2020-xx-xx xx:xx:xx",
           "headline": "Influenza Outbreak in Tokyo",
           "main_text": "Tokyo suffering from worst Influenza epidemic in recorded history",
           "reports": [
               {
                   "diseases": ["influenza a/h5n1"],
                   "syndromes": ["Haemorrhagic Fever", "Acute Flacid Paralysis"],
                   "event_date": "2020-xx-xx xx:xx:xx",
                   "locations": [1850147]
               }
           ]
       }
   ]
}
```

### Development Stack <a name="devstack"></a>
Question: *Present and justify implementation language, development and deployment environment (e.g. Linux, Windows) and specific libraries that you plan to use.*
#### Languages
These are the languages we have experience in:
| Name | James | Luke | Kenneth | Liam |
|------|-------|------|---------|------|
| Languages | <ul><li>Java</li><li>Python</li><li>C</li><li>HTML5/JavaScript</li><li>C#</li><li>C++</li><li>SQL</li><li>Bash</li></ul> | <ul><li>C#</li><li>Python</li><li>C</li><li>JavaScript</li></ul> | <ul><li>Python</li><li>C</li><li>Perl</li><li>Java</li><li>MIPS</li><li>Shell</li><li>SQL</li></ul> | <ul><li>Python</li><li>Java</li><li>Perl</li><li>JavaScript</li><li>C</li></ul> |

Pros and Cons of Languages for APIs:
| Language | Pros | Cons |
|----------|------|------|
| Python | <ul><li>Easy API calls through web development frameworks such as Flask</li><li>Readability - easy to learn and understand</li><li>Supports both procedural and object-oriented programming</li><li>Can be run on multiple platforms</li><li>Automatic memory management</li><li>Simplified unit testing</li></ul> | <ul><li>Relatively slow performance</li><li>High memory consumption due to flexibility of data types</li><li>Has errors that only show up in runtime as language is dynamically typed</li><li>Needs large degree of unit testing</li></ul> |
| Java/C# | <ul><li>Relatively high performance</li><li>Compiled</li><li>Statically typed so errors can be detected during runtime</li><li>Object oriented - offers maintainability and modularity</li></ul> | <ul><li>Not as readable and beginner friendly as python</li></ul> |
| JavaScript (Full Stack) | <ul><li>Covers full stack of development</li><li>Manages backend and frontend</li><li>Common language allows for better team efficiency with less resources</li><li>Extensive code reusability</li><li>Relatively high performance</li></ul> | <ul><li>Insufficiency with computation-heavy back end</li><li>The drawback of each item in the stack causes framework to have to inherit the flaws of each part</li></ul> |
| C/C++ | <ul><li>High performance and efficient</li><li>Statically typed so errors can be detected during runtime</li></ul> | <ul><li>Need to manually manage memory</li><li>Commonly used to be platform specific</li><li>Can be more complex and therefore harder to use</li></ul> |
| SQL | <ul><li>Fast data lookup once it is stored</li></ul> | <ul><li>Backend database</li><li>Not for frontend use</li><li>Not used to crawl internet directly</li></ul> |

After evaluating the possible languages we could use for developing our API and Web App, we decided to use Python as it was the language that everyone in the team was relatively familiar with, and thus would allow all team members to contribute in the development of the program. Furthermore, with how Python filing works, it is very easy to import packages, allowing us to easily work on separate functions without reliance on others work.

Additionally, Python’s ease of use arising from its simple syntax and dynamic typing makes it easier to maintain and collaborate on, especially between five team members who have not worked together on a project of this scale before. With Python being interpreted rather than compiled, it is slower compared to languages such as C, C# or Java, however, due to the relatively small scale of this project, we believe the difference in performance would not be significant enough to outweigh the benefits Python brings. 
Additionally, python also has a large community of users as well as extensive libraries which will speed up the development process. 
Some of the libraries we will be using in this project include:
* **json**: a library for reading and producing JSON data. This is a common format for API input and output, meaning it will be an essential library during our development.
* **flask**: one of two major options for server development in Python. Due to this server only being a backend server, Flask will be a simple option and preferable to Django.
* **pytest**: one of the best options for unit testing in Python.
* **psycopg2**: if we use an SQL database, this will be how we connect to it and run associated code on it.
* **datetime**: for dates and/or times.
* **requests**: for making requests to websites and/or pages and/or other API’s.
* **selenium**: for requesting HTML from dynamic websites.

#### Operating System
| Operating System | Pros | Cons |
|----------|------|------|
| Linux | <ul><li>Linux being free and dominance of Unix on the internet lead to there being more Linux hosting, which leads to more web apps being written which may purposely or accidentally favour Linux</li><li>Available documentation, resources for support and problem solving reflect disproportionate use of Linux</li><li>Industry Standard OS</li><li>Linux is FOSS</li></ul> | <ul><li>Open source leads to more opportunity for attack and abuse</li><li>Can’t host any .NET or ASP programs</li></ul> |
| OS-X Server | <ul><li>Benefits for apple users</li><li>Access to some apple specific programs</li></ul> | <ul><li>Can’t host any .NET or ASP programs</li><li>On top of the cost of the macintosh OS, you then have to purchase the server program from the app store</li><li>Mostly used for small scale business organization</li></ul> |
| Windows Server | <ul><li>Proprietary and constantly getting security updates</li><li>Applications written in Windows-only languages like .NET or ASP must be run from a Windows server</li><li>Good all rounder</li></ul> | <ul><li>All rounder, but sometimes can’t do the same specifics that can be done on a linux host</li><li>Much harder to work with for the inexperienced</li><li>Proprietary, so costs money to set up and use, alongside the extra costs of server</li></ul> |

We have decided that we will be using Linux for our hosting system. Alongside being an industry standard, it is free and can be run in a VM or as a machine itself. Furthermore, with all of us having access to the CSE computers via VNC or UNSW computer labs, we can be certain that we all have the same local setup and ensure there won’t be any compatibility issues.

Furthermore, we are using a virtual env so that we are all working in the same area. To use this, a person must first install venv. Follow the instructions below:
* python3 -m pip install --upgrade pip
* python3 -m pip install virtualenv
* Whilst in the API folder, run this command: 
  * source SENG3011/bin/activate
* This will activate the environment. To check you’re in the correct env, check it with this command:
  * which python
  * Should output your current directory + API/SENG3011/bin/python
* To exit the environment, run the command deactivate

Instructions found here for other operating systems:
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Deliverable 2 🥓 <a name="deliverable2"></a>
### Software Architecture <a name="finarch"></a>

![](https://lh3.googleusercontent.com/1-ryL9QM9Tf7DiXG1yUqZ9E9CxdDiNyeRaJbtFzIncNLkqKLmctu_1jgObk4zpguiEKoBfBROSSUe5tSnZL0_tv2kIJJD4YPuvUrtvDQTEgl-AMV_gKHgfDo3ngE1rRoh3auRmqp)

### Database Schema

![](https://lh4.googleusercontent.com/LFRgwUVtQkB1_03oa7-DMJq0Crb-KAmgGrQaHXUD7dlQO1H-gvW9NWODo1yKsOxwM7nUGt7NcFdR8_kGQABEETeEuaafSfeD67f7lil2HdwTqSLO5Fyik-n1jQSadlKpNH8matec)

### Justification of Implementation <a name="justif"></a>

Prior to our final formulation of our API architecture, we had outlined many components that we had planned to use for our development stack here: <https://github.com/KennethMejico/SENG3011_McNuggets/blob/main/Reports/Design%20Details.md#devstack>

As detailed above, the planned architecture differs slightly from our final architecture, most notably we had changes in the following categories:

| Category | Planned | Final |
|----------|------|------|
|SQL Database| DB on AWS services|RDS DB on AWS Lambda|
|Online Backend|AWS Lambda/Elastic Beanstalk|AWS Lambda|
|Database Management System|PostgreSQL (psycopg2)|mySQL (mysql.connector)|
|Scraping|Requests/Selenium|Requests/BeautifulSoup|

-   SQL Database: We had initially planned on using an AWS database but were unsure of the limitations that other changes could impose. In completing further research and attempts at implementation, we had decided to go with Amazon Relational Database Service (RDS), as opposed to other AWS databases:

-   Relational (Aurora, RDS, Redshift): Used for traditional applications, ERP, CRM, e-commerce

-   Key-value (DynamoDB): High-traffic web apps, e-commerce systems, gaming applications

-   In-memory (ElastiCache): Caching, session management, gaming leaderboards, geospatial applications

-   Document (DocumentDB): Content management, catalogs, user profiles

-   Wide Column (Keyspaced): High scale industrial apps for equipment maintenance, fleet management, and route optimization

-   Graph (Neptune): Fraud detection, social networking, recommendation engines

-   Time series (Timestream): IoT applications, DevOps, industrial telemetry

-   Ledger (QLDB): Systems of record, supply chain, registrations, banking transactions

With respect to all use cases for each type of database, we believe that our API would best fall under the relational category as a 'traditional application', as well as for the fact that our database would be stored in SQL form. In comparison to other options under the relation database type, we chose RDS due to its ease of use and free tier availability. RDS is more cost effective in comparison to Aurora, where although Redshift does have a 2-month free trial, RDS and it's ease of use outweighs Redshift for our project's timeframe.

-   Web Server Hosting: Our team had initially attempted to use AWS Elastic Beanstalk but found that the number of errors and difficulty of working with uploaded code made this approach sustainable. With this in mind, we opted to use AWS Lambda as it was much easier to set up and utilise.

-   Database Management System: The main reason for a change in our database system was mainly the result of developer preference, i.e. the group member working on the SQL database had more experience using MySQL as opposed to PostgreSQL, and therefore a greater preference for the former.

-   Scraping: Our initial plan had involved using requests and Selenium, though through further development on the scraper, there was better familiarity and ease in mainly using requests, as well as BeautifulSoup for HTML parsing.\
Here is the final architecture of our development stack:

#### Final Architecture:
|Category|Used Component|
|----------|------|
|Data Source|ProMedMail.org|
|Backend Language|Python|
|Web Scraping|Requests/BeautifulSoup Libraries|
|Web Framework (Local hosting only)|Flask|
|Operating System|Linux|
|Online Backend|AWS Lambda|
|Database Management System|MySQL|
|MySQL Database|AWS Relational Database Service (RDS)|
|Data Formatting|JSON|
|Testing|Pytest library|
|Misc. Libraries|datetime, mysql.connector, relativedelta, time, re, sys, os|\

Due to their respective components being given as default or necessary for the project, the following categories have not been given a comparison:

-   Data Source
-   Data Formatting
-   Misc. Libraries
-   Web Framework
-   Operating System

#### Backend Language
|Language|Pros|Cons|
|----------|------|------|
|**Python**|<ul><li>Easy API calls</li><li>Readability</li><li>Supports procedural and object-oriented programming</li><li>Can be run on multiple platforms</li><li>Automatic memory management</li><li>Simplified unit testing</li></ul>|<ul><li>Relatively slow performance</li><li>High memory consumption due to flexibility of data types</li><li>Has errors that only show up in runtime as language is dynamically typed</li><li>Needs large degree of unit testing</li></ul>|
|Java/C#|<ul><li>Relatively high performance</li><li>Compiled</li><li>Statically typed so errors can be detected during runtime</li><li>Object oriented - offers maintainability and modularity</li></ul>|<ul><li>Not as readable and beginner friendly as python</li></ul>|
|JavaScript|<ul><li>Covers full stack of development</li><li>Manages backend and frontend</li><li>Common language allows for better team efficiency with less resources</li><li>Extensive code reusability</li><li>Relatively high performance</li></ul>|<ul><li>Insufficiency with computation-heavy back end</li><li>The drawback of each item in the stack causes framework to have to inherit the flaws of each part</li></ul>|
|C/C++|<ul><li>High performance and efficient</li><li>Statically typed so errors can be detected during runtime</li></ul>|<ul><li>Need to manually manage memory</li><li>Commonly used to be platform specific</li><li>Can be more complex and therefore harder to use</li></ul>|
|SQL|<ul><li>Fast data lookup once it is stored</li></ul>|<ul><li>Backend database</li><li>Not for frontend use</li><li>Not used to crawl internet directly</li></ul>|

Justification: We had decided to use Python as our main programming language in developing our API and Web App, as it was the most familiar language for everyone. For the timeframe of the project, the ease of importing packages, less time spent on learning the language, and simple syntax of Python would provide a major advantage for much needed efficiency in the development stages.

#### Web Scraping
|Scraper|Pros|Cons|
|----------|------|------|
|Scrapy|<ul><li>Relatively fast - asynchronous</li></ul>|<ul><li>High learning curve</li><li>Unable to handle JavaScript by default</li></ul>|
|Selenium|<ul><li>Renders web pages for test automation</li><li>Useful in cases where websites rely on JavaScript</li></ul>|<ul><li> Wasn't originally designed for web scraping</li><li>Slower than HTTP requests</li></ul>|
|**Requests**|<ul><li>Low overhead</li><li>Makes simplified HTTP requests that are fast and use smaller amounts of data</li><li>Can query databases and web pages</li></ul>|<ul><li>Not very user friendly</li></ul>|

Justification: Using requests was a much easier option, despite Scrapy being much faster, and Selenium being able to work with the JavaScript used on the ProMedMail.org site. Being able to access the AJAX data of the website, we were able to use requests with much more efficiency.

#### Online Backend
|Backend|Pros|Cons|
|----------|------|------|
|**AWS Lambda**|<ul><li>Reduced cost of execution - only pay for computing costs</li><li>Improved resiliency - code is more resilient under load</li></ul>|<ul><li>No control over environment - unable to install packages or software on the environment</li><li>More complex call patterns - functions are timeboxed with timeouts</li></ul>|
|AWS Elastic Beanstalk|<ul><li>Completely automatic</li><li>Well integrated with AWS services</li><li>Good technical support from docs</li></ul>|<ul><li>Troubleshooting is difficult - unable to see where errors occur</li></ul>|

Justification: As mentioned above, we had chosen to use the AWS RDS as our form of database hosting, and as a result, we had two main choices between AWS Lambda, and AWS Elastic Beanstalk. Elastic Beanstalk was our first choice, as it has the ability to upload whole packages of code, have it run on a preconfigured server, and has a fairly long free trial. However, due to problems regarding configuration, we had decided to abandon Elastic Beanstalk and use Lambda instead, further can be read here: INSERT LINK TO CHALLENGES AND SHORTCOMINGS. 

#### Database Management System
|DBMS|Pros|Cons|
|----------|------|------|
|**MySQL**|<ul><li>Support for multi-user features</li><li>Simple read-heavy operations</li><li>Simple to install and use with broad community</li></ul>|<ul><li>Moves old data to rollback segments, performance is impacted with bulk INSERTs</li><li>Does not work well with long-running SELECTs</li><li>Lack of full-text search and slow concurrent read-writes</li></ul>|
|PostgreSQL|<ul><li>Parallel processing capability - can run long SELECTs unlike MySQL</li><li>Multi-user features</li></ul>|<ul><li>Storage engine needs extensive work</li><li>More power hungry</li></ul>|
|SQLite|<ul><li>Small footprint - compact with library under 600KB</li><li>Cache data from client/server locally</li></ul>|<ul><li>Lack of multi-user capabilities</li><li>Is file-based, can cause issues with larger datasets</li></ul>|

Justification: Despite the parallel processing capability of PostgreSQL, we had chosen to use MySQL as it was more familiar to us as a group. It would also be more time efficient, as members already had knowledge on how to set up MySQL databases, whereas precious time to learn to set up PostgreSQL would be wasted.

#### Database Hosting
|SQL DB|Pros|Cons|
|----------|------|------|
|**AWS RDS**|<ul><li>is cheaper because of its simplicity and lower scaling capabilities</li><li>no significant application changes are required </li></ul>|<ul><li>lower scaling capabilities</li><li>Shell access to the underlying operating system is disabled</li><li>access to MySQL user accounts with "SUPER" privilege isn't allowed</li></ul>|
|AWS Aurora|<ul><li>with Aurora there is no need for capacity planning. Aurora storage will automatically grow, from the minimum of 10 GB up to 64 TiB</li><li>With Aurora, you can provision up to fifteen replicas compared to just five in RDS MySQL</li></ul>|<ul><li>There is a big performance penalty in workloads where heavy writes that update secondary indexes are performed</li><li>Aurora Serverless is better for dev environments or systems which are needed for just a few hours/day or a short period of time</li><li>Aurora instances will cost you ~20% more than RDS MySQL. </li></ul>|
|AWS Redshift|<ul><li>Very strong load control</li><li>Petabyte scale data storage</li></ul>|<ul><li>Pricing is relatively very expensive</li><li>High maintenance because of its complex architecture</li><li>Redshift needs some administrative tasks to be executed manually by the cluster administrator. </li><li>Relatively slow results</li></ul>|

Justification: Our group had chosen RDS as it was the cheapest option, where Aurora instances would cost 20% more than RDS, and Redshift prices would be very expensive, despite there being a free trial. Redshift seems to require high maintenance and has slow results, so choosing RDS was our best option.

#### Testing
|Testing Tool|Pros|Cons|
|----------|------|------|
|**PyTest**|<ul><li>Prior experience</li><li>Intuitive yet flexible with decorators</li><li>Is actively developed and maintained. </li><li>It is compatible with both unittest and nose test suites</li><li>Has built-in test discovery </li><li>Has a large number of plugins available for use</li></ul>|<ul><li>Low compatibility with testing frameworks outside of the mentioned ones</li></ul>|
|Robot|<ul><li>Simple to use</li><li>Fast to write</li><li>Extendable</li><li>Open Source</li><li>Good for testing networked applications</li></ul>|<ul><li>Large overhead</li><li>Low Flexibility</li></ul>|
|unittest|<ul><li>Comes with Python</li></ul>|<ul><li>Simple. Very basic</li></ul>|
|DocTest|<ul><li>Comes with Python</li><li>Doctests often contain usage examples</li><li>You use the API of your code in the doctest before you actually use it for real</li></ul>|<ul><li>You can't run a subset of the tests.</li><li>If a failure happens in the middle of the doctest, the whole thing stops.</li><li>The coding style is stylized, and has to have printable results.</li><li>Your code is executed in a special way, so it's harder to reason about how it will be executed, harder to add helpers, and harder to program around the tests</li></ul>|

Justification: We had chosen to use PyTest as we all had experience using it during previous software engineering courses.

### Challenges Addressed and Shortcomings <a name="challenges"></a>

#### Multiple Reports per Article

One of the challenges we faced during the development of the API was how to store and process reports which have multiple locations, diseases and syndromes. Initially our solution involved having a Reports table that stored everything (locations, diseases, syndromes, keywords). However, we soon realised that this would result in multiple rows of the same report with the only difference being one disease, one syndrome, one location, or one keyword. To reduce the amount of redundant data we had to store, we decided to create joining tables Report_Locations, Report_Diseases, Report_Syndromes, and Report_Keywords which would only require us to store the ReportID and the other corresponding Id, reducing the amount of data we had to store. Additionally, these tables allow for flexibility in the future as it provides an easy way to isolate one field of a report. The shortcoming or downside associated with this is that it may result in slower performance as more joins are required, however, we did not see this as a significant issue as speed is not required for the purpose of our API as long as the request could be processed in a reasonable amount of time.

Furthermore, to properly generate multiple reports for a given article would involve natural text processing. This is not a feasible task to achieve on upwards of 20,000 individual articles, let alone write a script that could achieve this in a timely manner. Hence we had to look at other methods of generating reports from articles and collecting information about them.This lead to large amounts of problem solving that culminated in our final architecture and scraper operation.

#### Publishing the API

Our team encountered multiple issues while attempting to deploy the API publicly. Our initial plan was to create the API using Flask, and deploy it completely on AWS Elastic Beanstalk. The promises of using Elastic Beanstalk looked enticing - the ability to upload whole packages of code, have it run on a preconfigured server, and a fairly long free trial. However, like a mirage these hopes faded quickly when we ran into numerous issues configuring environment variables, importing external packages and even getting Elastic Beanstalk to identify our main file. When these issues were compounded with the inability to change code in any way other than completely reuploading the whole codebase, several minute long deployment times and a lack of documentation, we gave up on Elastic Beanstalk and looked to another Amazon Webservice, Lambda. We had previously experimented with Lambda in case we ran into issues with Elastic Beanstalk, so we were able to get Lambda working quickly enough to show off an example endpoint for our week five mentor session. We also found that during the switch to Lambda, it was easier to manually direct code to the appropriate endpoints (Using Amazon's API Gateway) than it was to figure out how to integrate Flask, and so the use of Flask was dropped when deploying to Lambda. This, along with a reorganisation of functions, is why we have included a zipped version of the code published to Lambda in our git repository, under the paths "Phase_1/API_SourceCode/lambda_endpoints.zip" and "Phase_1/API_SourceCode/lambda_database_updater.zip." This code integrates with Amazon's API Gateway and environment to receive event information and redirect it to the appropriate functions.
