
#******************************************************************************
#ImporntLibraries Here
from time import sleep# We imported the sleep funtion from the time libary

import random
#******************************************************************************
                                                                                     
#Developer: Landon Krusniak
#Version: 1.0

"""
Our Welcome Screen will start our program letting drivers know that the InfoTechCenter OS Loading.
"""


print('\033[1;31;0"m Welcome to Operation Fury InfoTech Center')

sleep(2)

print('\n \033[1;28;0"mOperation fury System is Booting Up\033[0m')
for i in range(3):
    print("OS Booting Up")
    sleep(1.5)

#******************************************************************************
#gasoline
#Programe Landon Krusniak
#version1.0


"""Define a fundtion to cheak our gas gauge and determine how far
we have until we have until we need gasoline based on an if,elif,else condition"""


#import libarary here


#gas level function
def gas_levelGauge():
    gasLevelList = ["Empty","Low","Quarter_Tank","Halftank","Threequarter tank","Full tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

def ListOFGasstations():
   gasstationslist = ["Shell","Circle K","marathon","Speedway","Meijer"]
   gasstationNearby= random.choice(gasstationslist)
   return gasstationNearby

#varible calling the gaslevelgauge funtion stored once
gasLevelIndicator = gas_levelGauge()

def gasLevelAlert():
    miles_To_Gas_Station_Low = round(random.uniform(1, 25), 1)
    miles_To_Gas_StationQuater_Tank = round(random.uniform(26, 50), 1)
    if gasLevelIndicator == "Empty":
        print("***WARNING GO GET GAS YOUR WILL RUN OUT***\nCalling Rich Friend")
    elif gasLevelIndicator == "Low":
        print("Run it to Empty\n Checking google maps for gas stations")
        print("The closest gas station is",ListOFGasstations())
        print("The closest gas station is",ListOFGasstations(),"which is",miles_To_Gas_Station_Low,"miles.")
    elif gasLevelIndicator == "Quarter Tank":
        print("***WARNING***")
        print("Your gas tank is a quarter tank full, checking google maps to your nearest gas station")
        print("The closest gas station is", ListOFGasstations(), "which is", miles_To_Gas_StationQuater_Tank,
              "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is at half of a tank and you have plenty of gas.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at a quarter of a tank and you have A good amount of gas to get you a couple of days")
    else:
        print("Your gas tank is full and you have plenty to drive a week without stopping .")


#******************************************************************************
#Wether
#Developer Landon Krusniak
#Version 1.0

"""
We are createong a funtion for out current wether using the
random.choice function to determine wht the wether is
pickingfrom a list-using If, Elif &else statemants to check the condition and print a specifc print line 
"""



#Weather condition list using the randome.choice library
#to randomly chose a codnition and storing it in its brain

def weather():
    weatherForecast = ["Rain","Snow","Sunny","Cloudy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition
weatherAlert = weather()
def vrs():
    if weatherAlert == "Icy":
        print("\nVRS has changed your alarm 30 minutes earlier based on the NWS forcast of "+ weatherAlert)
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\nVRS has changed your alarm 15 minutes earlier based on the NWS forcast of "+ weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of " + weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Cloudy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of "+ weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of " + weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Storming":
        print("\nVRS has changed your alarm 15 minutes earlier based on the NWS forcast of " + weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    else:
        print("\nVRS has changed your alarm to normal minutes based on the NWS forcast of " + weatherAlert)
        print("VRS will only allow your car to go 70MPH")


#******************************************************************************************************
#Call Functions Here..

print()
gasLevelAlert()

vrs()



