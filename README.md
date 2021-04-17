# Exploring Reasons for Employee Resignations using Survey Data

Clean and Analyze Employee Exit Surveys

In this project, we'll clean and analyze exit surveys from employees of the Department of Education, Training and Employment (DETE) and the Technical and Further Education (TAFE) body of the Queensland government in Australia. The TAFE exit survey can be found here "https://data.gov.au/dataset/ds-qld-89970a3b-182b-41ea-aea2-6f9f17b5907e/details?q=exit%20survey" and the survey for the DETE can be found here "https://data.gov.au/dataset/ds-qld-fe96ff30-d157-4a81-851d-215f2a0fe26d/details?q=exit%20survey".
We'll pretend our stakeholders want us to combine the results for both surveys to answer the following question:
Are employees who only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been there longer?

Introduction:
First, we'll read in the datasets and do some initial exporation.
Next we will Identify Missing Values and Drop Unneccessary Columns, Rename columns and filter unnecessary data.

Create a New Column:
Since our end goal is to answer the question below, we need a column containing the length of time an employee spent in their workplace, or years of service, in both dataframes.

End goal: Are employees who have only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been at the job longer?
  
Identify Dissatisfied Employees:
Next, we'll identify any employees who resigned because they were dissatisfied. Below are the columns we'll use to categorize employees as "dissatisfied" from each dataframe.


Combining the Data:
Below, we'll add an institute column so that we can differentiate the data from each survey after we combine them. Then, we'll combine the dataframes and drop any remaining columns we don't need.


Clean the Service Column:
Next, we'll clean the institute_service column and categorize employees according to the following definitions:
  
  
  New: Less than 3 years in the workplace
  
  Experienced: 3-6 years in the workplace
  
  Established: 7-10 years in the workplace
  
  Veteran: 11 or more years in the workplace

Our analysis is based on this article: "https://www.businesswire.com/news/home/20171108006002/en/Age-Number-Engage-Employees-Career-Stage", which makes the argument that understanding employee's needs according to career stage instead of age is more effective.

Perform Analysis:
Finally, we'll replace the missing values in the dissatisfied column with the most frequent value, False. Then, we'll calculate the percentage of employees who resigned due to dissatisfaction in each service_cat group and plot the results.

