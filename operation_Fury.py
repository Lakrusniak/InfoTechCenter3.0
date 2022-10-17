#gasoline
#Programe Landon Krusniak
#version1.0


"""Define a fundtion to cheak our gas gauge and determine how far
we have until we have until we need gasoline based on an if,elif,else condition"""

#import libarary here
import random

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
        print("Run it to Empty\n Check google maps for gas stations")
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

gasLevelAlert()