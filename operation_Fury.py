#Wether
#Developer Landon Krusniak
#Version 1.0

"""
We are createong a funtion for out current wether using the
random.choice function to determine wht the wether is
pickingfrom a list-using If, Elif &else statemants to check the condition and print a specifc print line 
"""

#Import Libraries here
import random
#Weather condition list using the randome.choice library
#to randomly chose a codnition and storing it in its brain
def weather():
    weatherForecast = ["Rain","Snow","Sunny","Cloudy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition
