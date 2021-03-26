# Testing Documentation
## API Testing
Our team employed a variety of testing methods to validate and verify our API and related functions. In the early stages of the project, unit testing was employed to validate a number of the helper functions which would later be used in the development of our scraper. These tests were useful for verifying that each part of the scraper worked as it was intended to, and split the whole task of gathering information into more manageable chunks.

As we started developing endpoints, we ran into difficulty with using pytest to do unit testing of Flask endpoints. While there are modules that can integrate Flask with pytest, due to time restrictions we decided to focus on testing the endpoints once they had been deployed on Lambda, by using the Python requests library to automatically call the API. In the meantime our focus was on manual testing, by calling the endpoints of a locally run version of the API using tools like Postman and ARC. We were able to manually verify the results of the outputs were correct based on the test data we had placed into the database. To test if the database was being correctly populated by our scripts, we used MySQL’s command line interface to query the database and see what it contained.

Once our API was deployed on Lambda, we were able to test it using several already written Pytest tests, testing the result returned by a query to the API was the same as the output described by our API documentation. Additionally, we were able to use Lambda’s built in testing tools to test various calls to our API directly.

In summary, our team mostly relied on free-play testing of the API, supplemented by a strong core of unit/endpoint tests to verify features of our API worked as they were described in the stoplight documentation. Our team was limited by time from writing more complex and thorough tests, but will continue to test and maintain the API leading up to submission.