Test Charter: pet clinic

Objective: To ensure that the pet clinic app allows users to be added, managed, and found 

Scope: This testing will cover the functionality of the application in three user goals
1 super admin
2 clinic admin
3 pet owner 

Questions
Since there are three different users, how can we simply and track the application functionality, quality, and defects within a backlog that makes each separate flow easily identified and tied to the other parts of the application?

What’s on the roadmap?
What features are users assign for?
What bugs/defects do we know about?
What is the highest ROI surface area?



Acceptance Criteria:

All fields should accept valid inputs and reject invalid inputs 
Searching should return reasonably valid results
Unique users and pets should be easily managed and logged 

Things not covered
Limits to roles that prevent actions
Backend testing 
System lag or total black out 

Testing Approach:

Verify that the all screens have the necessary elements 
Verify that the elements work as intended 
Verify rejections on invalid data 
Confirm that errors are logged
Analytics data is being captured 
Highest value or most frequent flows are automated 

Test Data:

A list of valid and invalid input for the email address and password fields
Correct and incorrect users
Correct and incorrect pets 
Correct and incorrect visit dates 

Exit Criteria:

All tests have been executed
All tests have passed
All defects have been documented and addresse


Opportunities 
- screenplay pattern to focus on steps a use can do 
- put tests in a place where they can be executed by non-technical stakeholder