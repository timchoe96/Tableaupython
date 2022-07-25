#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:52:47 2022

@author: timothychoe
"""

import pandas as pd 

#read the csv file using pandas function pd.read_csv()

data = pd.read_csv('transaction.csv',sep=';')

#summary of data 

data.info()


#profit per transaction

data["ProfitPerTransaction"] = (data["SellingPricePerItem"] - data["CostPerItem"])*data["NumberOfItemsPurchased"]

#Sales per transaction

data["SalesPerTransaction"] = data["SellingPricePerItem"] * data["NumberOfItemsPurchased"]

#cost per transacton

data["CostPerTransaction"] = data["CostPerItem"] * data["NumberOfItemsPurchased"]


#markup of each item 

data["Markup"] = (data["SellingPricePerItem"] - data["CostPerItem"]) / data["CostPerItem"]

#rounding markup

data["Markup"] = round(data["Markup"],2)

#combining data fields for full date 

data["date"] = data["Day"].astype(str) + '-' + data["Month"] + '-' +data["Year"].astype(str)

#splitting the client keywords column string into and array of 3 strings

split_column = data["ClientKeywords"].str.split(",",expand=True)


#adding new column with client age from split column 

data["ClientAge"] = split_column[0]
data["ClientType"] = split_column[1]
data["LengthOfContract"] = split_column[2]

#replacing bracket in split columns string 

data["ClientAge"] = data["ClientAge"].str.replace('[',"")
data["LengthOfContract"] = data["LengthOfContract"].str.replace(']',"")

#change item description to lowercase

data["ItemDescription"] = data["ItemDescription"].str.lower()

#merging sales data with another data set 

second_data = pd.read_csv("value_inc_seasons.csv",sep=";")

data = data.merge(second_data, how="inner", on="Month")


#dropping unecessary columns 

data = data.drop(["ClientKeywords","Year","Month","Day"],axis=1)

#export to csv file 

data.to_csv('ValueInce_cleaned.csv',index=False)


