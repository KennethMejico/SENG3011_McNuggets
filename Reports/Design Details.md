# Design Details 🍦
## Table of Contents
* [Deliverable 1](#deliverable1)
  1. [API Module Development](#apidev)
  2. [Module Interactions](#modint)
  3. [Development Stack](#devstack)
## Deliverable 1 🥓 <a name="deliverable1"></a>
### API Module Development <a name="apidev"></a>
Question: *Describe how you intend to develop the API module and provide the ability to run it in Web service mode*

The first step is to make a detailed list of endpoints, describing exactly what format the response will be in and what information is being passed back by each endpoint. If we’re unclear about what each endpoint of the API does then in development we may run into issues such as redundant endpoints or confusing parameters. This step can be broken down a bit more:
1. Figure out what the broad scope of our API and app will be
2. List all the information we want to provide and actions we want to make possible for API users (identify all the endpoints)
3. Design the schema for the parameters and response of each endpoint
4. Make example data to show how it can be used and what type of information will be passed back
5. Fill out the documentation on Stoplight in a way that’s useable by others

Once our documentation is sorted out, we can begin actually creating these endpoints. At first, we will only return dummy data or perform superficial operations, but once every endpoint exists, we can go into making each one fully functional. After the design phase it will become apparent that some endpoints should be made before others, either because they are more useful or they are base we can work off of for harder endpoints. The endpoints can be split up between group members, and each one can work on a set of related endpoints. The first few can also be done as a group, so we can establish a style and consistency in our code.
Stoplight lets us run the API in web service mode.

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
| Name | Vicknesh | James | Luke | Kenneth | Liam |
|------|----------|-------|------|---------|------|
| Languages | <ul><li>C#</li><li>Java</li><li>JavaScript</li><li>(Vue/React)</li><li>Python</li></ul> | <ul><li>Java</li><li>Python</li><li>C</li><li>HTML5/JavaScript</li><li>C#</li><li>C++</li><li>SQL</li><li>Bash</li></ul> | <ul><li>C#</li><li>Python</li><li>C</li><li>JavaScript</li><li></ul> | <ul><li>Python</li><li>C</li><li>Perl</li><li>Java</li><li>MIPS</li><li>Shell</li><li>SQL</li></ul> | <ul><li>Python</li><li>Java</li><li>Perl</li><li>JavaScript</li><li>C</li></ul> |

Pros and Cons of Languages for APIs:
| Language | Pros | Cons |
|----------|------|------|
| Python | <ul><li>Easy API calls through web development frameworks such as Flask</li><li>Readability - easy to learn and understand</li><li>Supports both procedural and object-oriented programming</li><li>Can be run on multiple platforms</li><li>Automatic memory management</li><li>Simplified unit testing</li></ul> | <ul><li>Relatively slow performance</li><li>High memory consumption due to flexibility of data types</li><li>Has errors that only show up in runtime as language is dynamically typed</li><li>Needs large degree of unit testing</li></ul> |
| Java/C# | <ul><li>Relatively high performance</li><li>Compiled</li><li>Statically typed so errors can be detected during runtime</li><li>Object oriented - offers maintainability and modularity</li></ul> | <ul><li>Not as readable and beginner friendly as python</li></ul> |
| JavaScript (Full Stack) | <ul><li>Covers full stack of development</li><li>Manages backend and frontend</li><li>Common language allows for better team efficiency with less resources</li><li>Extensive code reusability</li><li>Relatively high performance</li></ul> | <ul><li>Insufficiency with computation-heavy back end</li><li>The drawback of each item in the stack causes framework to have to inherit the flaws of each part</li></ul> |
| C/C++ | <ul><li>High performance and efficient</li><li>Statically typed so errors can be detected during runtime</li></ul> | <ul><li>Need to manually manage memory</li><li>Commonly used to be platform specific</li><li>Can be more complex and therefore harder to use</li></ul> |
| SQL | <ul><li>Fast data lookup once it is stored</li></ul> | <ul><li>Backend database</li><li>Not for frontend use</li><li>Not used to crawl internet directly</li></ul> |

After evaluating the possible languages we could use for developing our API and Web App, we decided to use Python as it was the language that everyone in the team was relatively familiar with and thus would allow all team members to contribute in the development of the program. Furthermore with how Python filing works it is very easy to import packages, allowing us to easily work on separate functions without reliance on others work.

Additionally, Python’s ease of use arising from its simple syntax and dynamic typing make it easier to maintain and collaborate on between five team members who have not worked together on a project of this scale before. With python being interpreted rather than compiled, it is slower compared to languages such as C, C# or Java, however, due to the relatively small scale of this project, we believe the difference in performance would not be significant enough to outweigh the benefits python brings. 
Additionally, python also has a large community of users as well as extensive libraries which will speed up the development process. 
Some of the libraries we will be using in this project include:
* json : a library for reading and production of JSON data. This is a common format for API input and output meaning it will be an essential library during our development.
* flask : one of two major options for server development in python. Due to this server only being a backend server, flask will be a simple option and preferable to django.
* pytest : one of the best options for unit testing in python.
* psycopg2 : if we use an SQL database, this will be how we connect to it and run associated code on it.
* datetime : for dates and/or times.
* requests : for making requests to websites and/or pages and/or other api’s
* selenium : for requesting HTML from dynamic websites

#### Operating System
| Operating System | Pros | Cons |
|----------|------|------|
| Linux | <ul><li>Linux being free and dominance of Unix on the internet lead to there being more Linux hosting, which leads to more web apps being written which may purposely or accidentally favour Linux</li><li>Available documentation, resources for support and problem solving reflect disproportionate use of Linux</li><li>Industry Standard OS</li><li>Linux is FOSS</li></ul> | <ul><li>Open source leads to more opportunity for attack and abuse</li><li>Can’t host any .NET or ASP programs</li></ul> |
| OS-X Server | <ul><li>Benefits for apple users</li><li>Access to some apple specific programs</li></ul> | <ul><li>Can’t host any .NET or ASP programs</li><li>On top of the cost of the macintosh OS, you then have to purchase the server program from the app store</li><li>Mostly used for small scale business organization</li></ul> |
| Windows Server | <ul><li>Proprietary and constantly getting security updates</li><li>Applications written in Windows-only languages like .NET or ASP must be run from a Windows server</li><li>Good all rounder</li></ul> | <ul><li>All rounder, but sometimes can’t do the same specifics that can be done on a linux host</li><li>Much harder to work with for the inexperienced</li><li>Proprietary, so costs money to set up and use, alongside the extra costs of server</li></ul> |

We have decided that we will be using Linux for our hosting system. Alongside being an industry standard, it is free and can be run in a VM or as a machine itself. Furthermore, with all of us having access to the CSE computers via VNC or via downloaded image, we can be certain that we all have the same local setup and ensure there won’t be any compatibility issues.

Furthermore we are using a virtual env so that we are all working in the same area. To use this, first a person must install venv. Follow the instructions below:
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
