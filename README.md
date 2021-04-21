# Exploring Reasons for Employee Resignations using Survey Data

Clean and Analyze Employee Exit Surveys

In this project, we'll clean and analyze exit surveys from employees of the Department of Education, Training and Employment (DETE) and the Technical and Further Education (TAFE) body of the Queensland government in Australia. The TAFE exit survey can be found here "https://data.gov.au/dataset/ds-qld-89970a3b-182b-41ea-aea2-6f9f17b5907e/details?q=exit%20survey" and the survey for the DETE can be found here "https://data.gov.au/dataset/ds-qld-fe96ff30-d157-4a81-851d-215f2a0fe26d/details?q=exit%20survey".
We'll pretend our stakeholders want us to combine the results for both surveys to answer the following question:
Are employees who only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been there longer?

Introduction:
First, we'll read in the datasets and do some initial exporation.
Next we will Identify Missing Values and Drop Unneccessary Columns, Rename columns and filter unnecessary data.

End goal: Are employees who have only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been at the job longer? Next, we'll identify any employees who resigned because they were dissatisfied. Below are the columns we'll use to categorize employees as "dissatisfied" from each dataframe.

This analysis is based on this article: "https://www.businesswire.com/news/home/20171108006002/en/Age-Number-Engage-Employees-Career-Stage", which makes the argument that understanding employee's needs according to career stage instead of age is more effective.

We'll calculate the percentage of employees who resigned due to dissatisfaction in each service_cat group and plot the results.

