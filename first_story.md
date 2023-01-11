User Story 1

As an employee of the Animals R Us veterinarian center, one of my responsibilities is to use our Pet Clinic web application to enter new customers and their pets into our system, and to schedule appointments for these pets. I just got a phone call from a new pet owner who just moved into the neighborhood. While his pets are currently doing fine, he did want me to add his name and contact information so that he can more easily schedule appointments in the future.


Assumptions- 
This scenario only convers a single need- Add a new user to the system. This test should be automated in add_owners.spec.cy.js 

A few things I would want to clarify that are potentially ambiguous- 
1. What information needs to be put into the owner information fields? I can add ! to the name, address and city fields and have the system accept that I've added the fields, so what I really need are different types of information to be added to the fields. Such as... name cannot take more than 10000 characters 

BUG REPORT:
oihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhr as Name causes app to throw 500 error. 

Steps to reproduce: 
1. Open a new user form  
2. Add in above for name field 
3. add ! to every other field, except for phone number 
4. add 10 1s to the phone field and click "Add Owner" 

This bug report should be covered by test 
long_name_accepted.spec.cy.js

2. Should there be any limits on country code? Since only 10- digit numbers are accepted, then what should happen is we try to accept other country codes, or other 10 digit phone numbers? Do we check things like area code?

Test Parameters- 

General 
- User already exists (name, address, phone)

Name 
Long Name - bug 
Special Characters - passed

Address
Long Address- bug? 
Special Characters - passed
Line Breaks - not possible 

City 
Long City- bug? 
Special Characters - passed
Line Breaks - not possible 

Errors to assert- should be covered in errors tests in p1 
Must be 10 chars for phone 
Can't be blank 


