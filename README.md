# Motor Insurance Claim

This simple django project serves as a claim application for motor insurance. Below are the features:

1. User:

- As a user, I would like to submit a Motor Insurance claim form via website. 
- I need to login in order to submit the claim form. I need to fill in the "basic insured and driver details", "vehicle details", "loss details" and "documents required for claims" in the claim form. 
- I can login to do modification on my claims or delete my claims as long as the claim's status is "In Progress". 
- If the claim status becomes "Accepted", I cannot modify or delete the claim. 

2. Claim agent:

- I can login to Django admin to view the claims submitted by the users. 
- I can change the claim's status from "In Progress" to "Accepted".