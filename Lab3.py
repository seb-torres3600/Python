#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sebastian Torres
#Homework 1-LING, Part 2

unitsInput = input("Enter input units(km/m/cm/mi/yd/in):")

    
unitsOutput = input("Enter outputs units(km/m/cm/mi/yd/in):")
quantity = int(input("Enter quantity to convert:"))

if unitsInput == "km":
     meter = quantity * 1000
if unitsInput == "m":
     meter = quantity
if unitsInput == "cm":
     meter = quantity * .01
if unitsInput == "mi":
     meter = quantity * 1609.34
if unitsInput == "yd":
     meter = quantity * .9144
if unitsInput == "in":
     meter = quantity * .0254
if unitsOutput == "km":
     conversion = meter / 1000
if unitsOutput == "m":
     conversion = meter
if unitsOutput == "cm":
     conversion = meter*100
if unitsOutput == "mi":
     conversion = meter/1609.34
if unitsOutput == "yd":
     conversion = meter/.9144
if unitsOutput == "in":
     conversion = meter /.0254

conversionRound = round(conversion, 3)
print(quantity, unitsInput, "is",conversionRound, unitsOutput)


# In[2]:


#Sebastian Torres
#Homework 1, Part A

print("Only answer with yes or no")
water = input("Does it live in water?")
if (water == "yes"):
    mammal = input("Is it a mammal?")
    if (mammal == "yes"):
        size = input("Is it large in size?")
        if size == "yes":
            print("It's a whale!")


# In[ ]:




