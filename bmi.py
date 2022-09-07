# -*- coding: utf-8 -*-
import json

# function to calculate BMI
def formula1(weight,height):
    bmi=weight/(height**2)
    return bmi

# function to assign BMI category and Health Risk based on BMI value
def bmi_details(bmi):
    result_dict={}
   # Opening JSON input file after placing in working directory
    table1_input = open('table1.json')

   # load data to a variable
    data = json.load(table1_input)
   # Iterating through the json
    for i in data:
       if (bmi==i["BMI_min"] or bmi==i["BMI_max"]) or (bmi>i["BMI_min"] and bmi<i["BMI_max"]):
           result_dict["BMI Category"] = i["BMI Category"]
           result_dict["Health risk"] = i["Health risk"]
           break
       # Closing file
       table1_input.close()
    return result_dict
      
    

# Opening JSON input file after placing in working directory
bmi_input = open('input.json')
  
# load data to a variable
data = json.load(bmi_input)
  
# Iterating through the json
for i in data:
    # checking data validity of weight and height before calculating BMI
    if type(i["WeightKg"]) is int and  type(i["HeightCm"]) is int:
        # converting centimetres to metres
        height_in_metres = float(i["HeightCm"]/100)
        #calculating and assigning BMI after rounding off to 1 demical place
        i["BMI"] = round(formula1(i["WeightKg"],height_in_metres),1)
        #Merging result_dict with i    
        i.update(bmi_details(i["BMI"]))
    else:
        i["BMI"] = "Invalid inputs. Please check input.json"

 # Saving output in file  
with open("output.json","w") as outfile:
    json.dump(data,outfile)
  
# Closing file
bmi_input.close()
