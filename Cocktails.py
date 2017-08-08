# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 12:34:21 2016

@author: Thomas
"""

import csv
from copy import copy
import sys

cocktails = {}
cocktails_all = set()
ingredients_all = set()
bottles = 2
budget = 100
#glpsol.exe -m --model cocktailsILP.model --data cocktailsILP.data > output.txt

#Read Data
with open('cocktails_list.csv','r') as f:
    data = list(csv.reader(f, delimiter=','))
    

for line in data:
    if (line[0] == "Cocktail"):
        continue
    else:
        cocktails_all.add(line[0])
        ingredients_all.add(line[1])
        if line[0] in cocktails:
            cocktails[line[0]].append(line[1])
        else:
            cocktails[line[0]] = [line[1]]

cocktails_all = list(cocktails_all)
ingredients_all = list(ingredients_all)
noof_cocktails = len(cocktails_all)
noof_ingredients = len(ingredients_all)

ing_prices = dict.fromkeys(ingredients_all, 999)
print ("Input file has {0} cocktails\n{1} unique ingredients found\n".format(noof_cocktails,noof_ingredients))

ing_prices = dict.fromkeys(ingredients_all, 999)
with open('price_list.csv') as f:
    prices = list(csv.reader(f, delimiter=','))
    
error_raised = False

for price_row in prices:
    if price_row[0] in ing_prices:
        if (price_row[1] == "-") or (price_row[1] == "NIL"):
            continue
        else:
            ing_prices[price_row[0]] = float(price_row[1])
    elif (price_row[0] == "Ingredient"):
        continue
    else:
        print ("Ingredient {0} not found. Please check the spelling.".format(price_row[0]))
        error_raised = True


if error_raised: 
    input("This program will now close. Please try again.")
    sys.exit()


ingredients_all = list(ing_prices.keys())

#Write to file
with open('cocktailsILP.data','w') as cocktail_data:

    cocktail_data.write("param m := {0};\nparam n:= {1};\nparam bottles:= {2};\nparam budget:={3};\n".format(noof_cocktails, noof_ingredients, bottles, budget))
    
    #Price List
    cocktail_data.write("param p:= \n")
    price_list = list(ing_prices.values())
    for i in range(noof_ingredients):
        cocktail_data.write(str(i+1) + " ")
        cocktail_data.write(str(price_list[i])+"\n")
    cocktail_data.write(";\n")
    
    #Meal-Ingredient Dependency Matrix
    cocktail_data.write("param A: ")
    for i in range(noof_ingredients):
        cocktail_data.write(str(i+1) + " ")
    cocktail_data.write(":= \n")
    
    for cocktail_no,m in enumerate(cocktails_all):
        cocktail_data.write(str(cocktail_no+1) +" ")
        for n in ingredients_all:
            if n in cocktails[m]: 
                cocktail_data.write("1 ")
            else: 
                cocktail_data.write("0 ")
        if cocktail_no == noof_cocktails-1:
            cocktail_data.write(";\n")
        else: cocktail_data.write("\n")
    
    cocktail_data.write("end;\n")


    
#Finished! Decoding starts here
print ("Written cocktails and ingredients matrix to cocktailsILP.data\nPlease run GLPsol.exe and paste the solution from 'display statement at line 26' to 'Total drinks.val = '. \nPress enter one more time after you're done.")
#glpsol.exe -m --model cocktailsILP.model --data cocktailsILP.data > output.txt

line = ""
solution_temp = []

while (True):
    line = input("Enter here: ")
    if line != "":
        solution_temp.append(line)
    else: 
        break

if len(solution_temp) ==1: #Handles difference in string input between command-line and iPython
    solution = solution_temp[0].split("\n")
else: 
    solution = copy(solution_temp)
    
#print (solution)

#Input finished. Now to process the input
counter = 1

optimal_ingredients = set()
available_cocktails = set()

for ingredient_counter in range(noof_ingredients):
    string = solution[ingredient_counter+counter].split("= ")
    if int(string[1]) == 1:
        optimal_ingredients.add(ingredients_all[ingredient_counter])

counter = counter + noof_ingredients +1

for cocktail_counter in range(noof_cocktails):
    string = solution[cocktail_counter+counter].split("= ")
    if int(string[1]) == 1:
        available_cocktails.add(cocktails_all[cocktail_counter])
        
total_price = 0


print ("="*22)
print ("FINAL PROGRAM OUTPUT")
print ("="*22)
print ("\n{0} Bottle(s) to buy:".format(len(optimal_ingredients)))
for i,v in enumerate(sorted(optimal_ingredients)):
    print ("    {0}. {1}".format(i+1,v))
print ("\n{0} Cocktails that can be made:".format(len(available_cocktails)))
for i,v in enumerate(sorted(available_cocktails)):
    print ("    {0}. {1}".format(i+1,v))
    
print ("\n Price Breakdown:")

for ing in optimal_ingredients:
    if (ing_prices[ing] > 0):
        print ("{0}: ${1}".format(ing, ing_prices[ing]))
    total_price = total_price + ing_prices[ing]
print ("\nTotal Price: ${0}".format(total_price))





    