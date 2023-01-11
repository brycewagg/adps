User Story #3 [Bonus]: As an employee of the Animals R Us veterinarian center, I take appointment requests over the phone as well as through emails and form submissions from our ecommerce website. I use Pet Clinic to schedule appointments for owners and to provide them with the history of their previous visits. When scheduling the appointment, I should be able to provide the desired date of the appointment as well as a description of what the visit is for.


Add visit 
http://3.238.20.218:8080/owners/1 causes error when I try to add a visit for a new pet 
http://3.238.20.218:8080/owners/1/pets/32/visits/new

Description is required- bug, need escaped space 
Long description allowed- bug, long desription throws 500 
Cann

Questions- 
Should I be able to set a visit for the future that appear under previous visits? That UI might be confsing for someone becuase those visits have not happened yet. 