# Data Dictionary

## financials 
- id - The loan id (PK)
- funded_amount - The amount of the loan
- currency - The currency in which the loan was disbursed
- term_in_months - The duration for which the loan was disbursed in months

## use 
- id - The loan id (PK)
- activity - More granular category
- sector- High level category
- use - Exact usage of loan amount

## demographics 
- id - The loan id (PK)
- country - Full country name of country in which loan was disbursed
- region - Full region name within the country
- borrower_genders - Comma separated M,F letters, where each instance represents a single male/female in the group

## crowdsource
- id - The loan id (PK)
- posted_time - The time at which the loan is posted on Kiva by the field agent
- funded_time - The time at which the loan posted to Kiva gets funded by lenders completely
- lender_count - The total number of lenders that contributed to this loan





