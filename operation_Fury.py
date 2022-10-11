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
    if gasLevelIndicator == "Empty":
        print("***WARNING GO GET CAS YOUR WILL RUN OUT***\nCalling Rich Friend")
    elif gasLevelIndicator == "Low":
        print("Run it to Empty\n Check google maps for gas stations")
        print("The closest gas station is",ListOFGasstations())
    
gasLevelAlert()