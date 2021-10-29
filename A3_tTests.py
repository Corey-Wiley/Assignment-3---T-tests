#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:06:05 2021

@author: coreywiley
"""

import pandas as pd
from scipy.stats import ttest_ind

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

# Question 1
# Is there a difference between sex (M:F) and the number of days in hospital?

list(diabetes)

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']

ttest1 = ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

list(ttest1)

## The dependent variable is time in hospital and the independent variable or 2 
## level group factor is sex (male or female). P-value: -1.42, T-test value: 9.54.
## There is no statistically significant difference in average time in hospital
## between males and females.


# Question 2
# Is there a difference between RACE (Caucasian and African American) and the 
# number of days in hospital?

Caucasian = diabetes[diabetes['race']=='Caucasian']
AfrAmer = diabetes[diabetes['race']=='AfricanAmerican']

ttest2 = ttest_ind(Caucasian['time_in_hospital'], AfrAmer['time_in_hospital'])

list(ttest2)

## The dependent variable is time in hospital and the independent variable or 2 
## level group factor is race (Caucasian or African American). P-value: -4.18, 
## T-test value: -5.06.
## There is no statistically significant difference in average time in hospital
## between Caucasians and African Americans.



# Question 3
# Is there a difference between RACE (Asian and African American) and the number 
# of lab procedures performed?

Asian = diabetes[diabetes['race']=='Asian']
AfrAmer = diabetes[diabetes['race']=='AfricanAmerican']

ttest3 = ttest_ind(Asian['num_lab_procedures'], AfrAmer['num_lab_procedures'])

list(ttest3)

## The dependent variable is number of lab procedures and the independent variable or 2 
## level group factor is race (Asian or African American). P-value: -6.95, 
## T-test value: -3.98.
## There is no statistically significant difference in number of lab procedures
## between Asians and African Americans.

