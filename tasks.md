Claims Application for Motor Insurance

Requirements:

1. As a user, I would like to submit a Motor Insurance claim form via website. I need to login in order to submit the claim form. I need to fill in the "basic insured and driver details", "vehicle details", "loss details" and "documents required for claims" in the claim form. I can login to do modification on my claims or delete my claims as long as the claim's status is "In Progress". If the claim status becomes "Accepted", I cannot modify or delete the claim. The claim form details are as follow:

   Basic insured and driver details:
   - Name
   - Email
   - Mobile No.

   Vehicle details:
   - Vehicle Year Make
   - Vehicle Model
   - Vehicle No.

   Loss details:
   - Date and time of accident
   - Location
   - Type of Loss. Choices of: Own Damage, Knock for Knock, Windscreen Damage, Theft.
   - Description of Loss
   - Police Report Lodged? Choices of: Yes or No
   - Anybody Injured? Choices of: Yes or No

   Documents required for claims
   - Photo
   - PDF document of Insurance Cover Not

2. As a claim agent. I can login to Django admin to view the claims submitted by the users. I can change the claim's status from "In Progress" to "Accepted".

Steps:
1. Create an app called `claims`.
2. Design and create models for `Claim`.
3. Create Django admin with link `http://localhost:8000/claims-admin/` for claim agent to login and view the claims data.
4. Create Django admin action on Claim model admin for claim agent to select on claims and do "update status to Accepted".
5. Create claims form page for authenticated user to submit and save into database.
