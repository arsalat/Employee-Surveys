#!/usr/bin/env python
# coding: utf-8

# The project aims to explore the unemployment reasons for two organizations DETE and TAFE using Employee Exit Surveys.

# In[31]:


import pandas as pd
import numpy as np

#reading the data into pandas
dete_survey = pd.read_csv('dete_survey.csv')
tafe_survey = pd.read_csv('tafe_survey.csv')

#examining the data for dete
dete_survey.info()

dete_survey.head(10)

dete_survey['SeparationType'].value_counts()






# In[32]:


#examining data for tafe survey
tafe_survey.info()

tafe_survey.head(15)

tafe_survey['Reason for ceasing employment'].value_counts()


# The dete_survey dataframe contains 'Not Stated' values that indicate values are missing, but they aren't represented as NaN.
# 
# Both the dete_survey and tafe_survey contain many columns that we don't need to complete our analysis.
# 
# Each dataframe contains many of the same columns, but the column names are different.
# 
# There are multiple columns/answers that indicate an employee resigned because they were dissatisfied.

# In[33]:


#setting not stated values as NaN in dete survey
dete_survey = pd.read_csv('dete_survey.csv', na_values = 'Not Stated')


# In[34]:


#dropping unwanted columns from dete

dete_survey_updated = dete_survey.drop(dete_survey.columns[28:49], axis=1)
tafe_survey_updated = tafe_survey.drop(tafe_survey.columns[17:66], axis=1)


# columns that do not contribute to our analysis of reasons for employee exit were removed.

# In[35]:


#renaming columns in dete
dete_survey_updated.columns = dete_survey_updated.columns.str.lower().str.replace(' ', '_').str.strip()
print(dete_survey_updated.head(5))

#updating column names in tafe
tafe_survey_updated = tafe_survey.rename(columns = {'CESSATION YEAR':'cease_date', 'Record ID':'id', 'Reason for ceasing employment':'separationtype', 'Gender. What is your Gender?':'gender','Employment Type. Employment Type':'employment_status', 'Classification. Classification': 'position','LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service', 'LengthofServiceCurrent. Length of Service at current workplace (in years)': 'role_service'})


# In[36]:


tafe_survey_updated.head()


# In[37]:


dete_survey_updated['separationtype'].value_counts()


# In[38]:


tafe_survey_updated['separationtype'].value_counts()


# In[39]:


#selecting only rows with separation type resignation for dete 

pattern = r"Resignation"
resignation_in = dete_survey_updated['separationtype'].str.contains(pattern, na = False)
dete_resignations = dete_survey_updated[resignation_in].copy()

#removing characters after Resignation
dete_resignations['separationtype'] = dete_resignations['separationtype'].str.split('-').str.get(0)
dete_resignations


# In[40]:


#selecting only rows with separation type resignation for tafe 
pattern_t = r"Resignation"
resignation_t = tafe_survey_updated['separationtype'].str.contains(pattern, na = False)
tafe_resignations = tafe_survey_updated[resignation_t].copy()
tafe_resignations


# In[41]:


dete_resignations['cease_date'].value_counts()


# In[42]:


dete_resignations['cease_date'] = dete_resignations['cease_date'].str.split('/').str[-1]
dete_resignations['cease_date'] = dete_resignations['cease_date'].astype("float")


# In[43]:


dete_resignations['cease_date'].value_counts().sort_values()


# In[44]:


dete_resignations['dete_start_date'].value_counts().sort_values()


# In[45]:


tafe_resignations['cease_date'].value_counts()


# The span of years for each dataframe is very different and cannto be aligned. Overall the data looks fine.

# In[46]:


dete_resignations['institute_service'] = dete_resignations['cease_date'] - dete_resignations['dete_start_date']


# In[47]:


dete_resignations['institute_service'].head()


# subtracting start date from the cease date gives us the length of service or duration of service for the employee

# In[48]:


tafe_resignations['Contributing Factors. Dissatisfaction'].value_counts()
tafe_resignations['Contributing Factors. Job Dissatisfaction'].value_counts()


# In[49]:


def update_vals(val):
    if pd.isnull(val):
        return np.nan
    elif val == '-':
        return False
    else:
        return True
    
tafe_resignations['dissatisfied'] = tafe_resignations[['Contributing Factors. Dissatisfaction', 'Contributing Factors. Job Dissatisfaction']].applymap(update_vals).any(1, skipna=False)
tafe_resignations_up = tafe_resignations.copy()

dete_resignations['dissatisfied'] = dete_resignations[['job_dissatisfaction','dissatisfaction_with_the_department','physical_work_environment','lack_of_recognition','lack_of_job_security','work_location','employment_conditions','work_life_balance','workload']].any(1, skipna=False)
dete_resignations_up = dete_resignations.copy()
dete_resignations_up['dissatisfied'].value_counts(dropna=False)

    


# In[50]:


dete_resignations_up['institute'] = 'DETE'
tafe_resignations_up['institute'] = 'TAFE'


# In[51]:


combined = pd.concat([dete_resignations_up, tafe_resignations_up],ignore_index=True)


# In[52]:


combined.notnull().sum().sort_values()


# In[53]:


combined_updated = combined.dropna(thresh = 500, axis =1).copy()


# In[54]:


combined_updated['institute_service'].value_counts(dropna = False)


# In[55]:



# Extract the years of service and convert the type to float
combined_updated['institute_service_up'] = combined_updated['institute_service'].astype('str').str.extract(r'(\d+)')
combined_updated['institute_service_up'] = combined_updated['institute_service_up'].astype('float')

# Check the years extracted are correct
combined_updated['institute_service_up'].value_counts()


# In[56]:


# COnvert years of service to category

def career_stage(val):
    if pd.isnull(val):
        return np.nan
    elif val < 3:
        return "New"
    elif 3 <= val <7:
        return "Experienced"
    elif 7 <= val <11:
        return "Established"
    else:
        return "Veteran"

combined_updated['service_cat'] = combined_updated['institute_service_up'].apply(career_stage)
combined_updated['service_cat'].value_counts()
        


# In[57]:


# Verify the unique values
combined_updated['dissatisfied'].value_counts(dropna=False)


# Finally, we'll replace the missing values in the dissatisfied column with the most frequent value, False. Then, we'll calculate the percentage of employees who resigned due to dissatisfaction in each service_cat group and plot the results.

# In[58]:


# Replace missing values with the most frequent value, False

combined_updated['dissatisfied'] = combined_updated['dissatisfied'].fillna(False)


# In[59]:



# Calculate the percentage of employees who resigned due to dissatisfaction in each category
dis_pct = combined_updated.pivot_table(index='service_cat', values='dissatisfied')

# Plot the results
get_ipython().run_line_magic('matplotlib', 'inline')
dis_pct.plot(kind='bar', rot=30)


# In[ ]:





# In[ ]:




