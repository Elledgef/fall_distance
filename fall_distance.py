# Author: Faith Elledge
# Github username: elledgef
# Date: 4/20/22
# Description: This code will calculate the fall distance of an object

#Function
def fall_distance(t):
 """Returns the fall distance of an object"""
# The constant for gravity that is given
gravity = 9.8
#Finds the distance
d=(1/2)*g*t**2
#will return value that is rounded to 3 spaces like in example
return round(d,3)
#t=float(input())
#dist=fall_distance(t)
#print(dist)