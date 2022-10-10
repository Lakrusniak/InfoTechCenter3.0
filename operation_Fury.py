
#Developer: Landon Krusniak
#Version: 1.0

"""
Our Welcome Screen will start our program letting drivers know that the InfoTechCenter OS Loading.
"""

#ImporntLibraries Here
from time import sleep# We imported the sleep funtion from the time libary

print('\n\033[1;31;0"m Welcome to Operation Fury InfoTech Center')

sleep(2)

print('\n \033[1;28;0"mOperation fury System is Booting Up\033[0m')
for i in range(3):
    print("OS Booting Up")
    sleep(1.5)



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

vrs()

