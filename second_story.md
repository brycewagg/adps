User Story #2: As an employee of the Animals R Us veterinarian center, I use the Pet Clinic app to create or update the pet profiles of our existing pet owner customers. Such pet profile information include the type of pet (dog, cat, etc.), name, and age. This pet profile information is used to facilitate scheduling appointments with a veterinarian who's specialty matches the tpe of pet.


Datatable
For a sinlge owner 
Name {randomString}
Birthdate {randomDate}
Type oneof.(cat, bird, hamster, dog, lizard, snake)

Assumptions

Questions- 
The Scenario says that we're making these pet parameters for vet matching, but the vet matching doesn't occur in the system that I can see. How do we intend to do this matching? 

Tests- 
Ensure I can add a pet with long name 
select birthdate (relevant dates only)
Select Type
Type is required 
Name is required- bug 

Bug Report- 
I can add a pet with only a single space. We should be escaping spaces at the beginning and end of the entry before submitting for validation. 
