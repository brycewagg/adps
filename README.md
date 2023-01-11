Hello! 
This is a submission for testing a Pet Clinic Site, and I've spent about 3 hours getting this ready. HEre's what you need to know about the tests, and the rest. 

## Stories
Each user Story is listed in it's own markdown file and has test parameters, butgs found, and test cases that should cover the needed flows. 

## Test directories 
There are multiple test directories to allow these tests to be run without requiring parallelization 
which also allows the folders themselves to get reports. I've used Selenium as the framework, 
but the same approach should roughly work with any other automation framework. 

### Subdirectories 
While there are multiple ways of organizing tests, I've chosen to organize based on priority of functionality using a priority scale or "p" scale. This sets up the future where I'll be able to know if a release is a go/no-go based on where flakyness or failures are being found. 

## How to read each test
Each test has steps that help guide you along to read the test, but there is also a gherkin scenario at the 
top of each test file to help you understand how to parse the tests. 

## A few notes about the tests 
- Every test file is as isolated as possible to reduce awaits which might introduce flaky tests. 
- A todo will be to wrap these limited test steps into functions that can be used to extend other tests 
- The tests themselves can be run individually, but a todo will be to link them togehter which cannot be done due to Time restrictions for this exercise. 

To run a test individually

The requried packages to run these tests are 
node
nvm?
chromedriver
python
selenium 
selenium-side-runner
