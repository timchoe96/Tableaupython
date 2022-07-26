#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 18:37:16 2022

@author: timothychoe
"""

import pandas as pd 
import json 
import numpy as np
import matplotlib.pyplot as plt 

#method 1 to read json data

json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data 

with open("loan_data_json.json") as json_file:
    data = json.load(json_file)
        
#transform list to dataframe 

loandata = pd.DataFrame(data)

loandata.info()


#finding unique values for purpose column 

loandata["purpose"].unique()


#describe data for specific column

loandata["fico"].describe()
loandata["int.rate"].describe()
loandata["dti"].describe()

#using exp to get annual income 

income = np.exp(loandata['log.annual.inc'])
loandata["annualincome"] = income


    
#create new column for fico score categories 

ficocat = []

for row in loandata['fico']:
    if row >= 300 and row < 400:
        ficocat.append("Very Poor")
    elif row >= 400 and row < 600:
        ficocat.append("Poor")
    elif row >= 601 and row < 660:
        ficocat.append("Fair")
    elif row >= 660 and row < 700:
        ficocat.append("Good")
    elif row >=700:
        ficocat.append("Excellent")
    else:
        ficocat.append("Unkown")


loandata["ficocat"] = pd.Series(ficocat)


#number of rows/loans per fico catergory 

# catplot = loandata.groupby(['ficocat']).size()
    

# #plotting loan group data

# catplot.plot.bar(color = 'green' ,width = 0.1)
# plt.show()

# #plotting purpose group data
# purposeplot = loandata.groupby(['purpose']).size()
# purposeplot.plot.bar(color = 'green' ,width = 0.2)
# plt.show()

loandata.to_csv('loan_cleaned.csv',index = True)







    