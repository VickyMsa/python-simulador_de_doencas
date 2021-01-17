#!/usr/bin/env python
# coding: UTF-8
#
# @package MyWorld
#
# @author Viviane Magalhães Siqueira (based on Professor Paulo Roma's work)
# @date 10/08/2020
#
from IWorld import IWorld
from World import World
from Disease import Disease
import sys


##
# Call the constructor of the World class with the
# width and height of 720 and 640 cells , respectively .
#
# Initialize a list to keep the average temperature
# of each world region ( quadrant ).
#
# Call the prepare () method .
#


class MyWorld(World, IWorld):
    __quadId = (0, 1, 2, 3)

    def __init__(self, width=720, height=640):
        super().__init__(width, height)
        self.__itCounter = 0
        self.__temperature = None
        self.__arrayDis = []
        self.prepare()

    ##
    # Prepare the world . Open a text file named
    # " simulation . config " in the current path
    # ( directly under the project directory ).
    # Parse the configuration file for the number
    # of Disease objects , the cell locations of these objects ,
    # the growth rates , and the temperature ranges associated
    # with individual growth rates .
    # Read Section 4 on the content of the configuration file
    # before reading the rest .
    #

    def prepare(self):
        try:
            with open('simulation.config', 'r') as document:
                doc = document.readlines()
                for i in range(len(doc)):
                    doc[i] = doc[i].strip('\n').split('=')
        except FileNotFoundError:
            print('Terminating the program.')
            sys.exit(-1)
        self.__arrayDis = self.initDiseases(doc[0][1])
        aux = self.initGrowthConditions(doc[2][1], self.__arrayDis)
        if aux == -1:
            print('Terminating the program.')
            sys.exit(-1)
        aux = self.initTemps(doc[3][1])
        if aux == -1:
            print('Terminating the program.')
            sys.exit(-1)
        aux = self.initLocations(doc[1][1], self.__arrayDis)
        if aux == -1:
            print('Terminating the program.')
            sys.exit(-1)
        self.setTemp(self.__quadId, self.__temperature)


    ##
    # Return the list of objects in
    # the class implementing this interface .
    #

    def getObjects(self):
        return self.__arrayDis

    ##
    # Create Disease objects ; the number of the objects equals
    # to the value passed in numDisStr .
    # Return a list of object references to the created
    # Disease objects .
    #
    # An example of a valid numDisStr is below.
    #
    # Ex: "2"
    #
    # If numDisStr is None or it cannot be converted to
    # a positive integer , print a message on screen
    # " Check the NumDiseases line in simulation . config ."
    # and return None .
    #
    # No exceptions are thrown.
    #

    def initDiseases(self, numDisStr):
        array = []
        for _ in range(int(numDisStr)):
            array.append(Disease())
            self.__arrayDis.append(Disease())
        return array

    ##
    # Add each Disease object into the MyWorld object
    # implementing this method according to the information
    # in locationStr .
    #
    # An example of a locationStr is "200 ,200;400 ,480".
    # This means that the first Disease is planted at cell
    # (200 ,200) and the second Disease is at cell (400 , 480).
    #
    # If the locationStr is empty or not in the correct format
    # or does not have all the cell coordinates of all the
    # Disease objects , print on screen
    # " Check the Locations line in simulation . config "
    # and return -1.
    #
    # Return 0 for a successful initialization
    # of the Disease locations . No exceptions are thrown .
    #

    def initLocations(self, locationsStr, diseaseArr):
        locationsStr = locationsStr.split(';')
        if len(locationsStr) != len(diseaseArr):
            print("Check the DiseasesGrowth line in simulation.config.")
            return -1
        for i in range(len(locationsStr)):
            locationsStr[i] = locationsStr[i].split(',')
            if len(locationsStr[i]) != 2:
                print("Check the DiseasesGrowth line in simulation.config.")
                return -1
        for i in range(len(diseaseArr)):
            self.addObject(diseaseArr[i], int(locationsStr[i][0]), int(locationsStr[i][1]))
        return 0

    ##
    # Set the lower bound and upper bound temperature
    # and the growth rate for each disease according
    # to the input growthStr .
    # An example of a valid string for two Disease objects is:
    #
    # Ex: "10.0 ,15.0 ,2.0;10.0 ,13.0 ,3.0"
    #
    # If growthStr is empty or not in the correct format
    # or does not have all the growth for all the Disease objects
    # in the Disease array , print on screen
    # "Check the DiseasesGrowth line in simulation.config."
    # and return -1.
    #
    # Return 0 for a successful
    # # initialization of the Disease growth conditions .
    # # No exceptions are thrown .
    #

    def initGrowthConditions(self, growthStr, diseaseArr):
        if growthStr == '':
            print("Check the DiseasesGrowth line in simulation.config.")
            return -1
        growthStr = growthStr.split(';')
        if len(growthStr) != len(diseaseArr):
            print("Check the DiseasesGrowth line in simulation.config.")
            return -1
        for i in range(len(growthStr)):
            growthStr[i] = growthStr[i].split(',')
            if len(growthStr[i]) != 3:
                print("Check the DiseasesGrowth line in simulation.config.")
                return -1
        for i in range(len(diseaseArr)):
            diseaseArr[i].setGrowthCondition(float(growthStr[i][0]), float(growthStr[i][1]), float(growthStr[i][2]))
        return 0

    ##
    # Set the temperature for each quadrant of the MyWorld
    # according to the value of the tempStr .
    # An example of tempStr is below .
    # The region temperatures for regions 0, 1, 2, and 3
    # are 12, 20, 50, and 100 , respectively .

    # Return 0 for a successful initialization of
    # the quadrant temperatures . No exceptions are thrown .

    # Ex: "12;20;50;100"

    # If tempStr is empty or not in the correct format
    # # or does not have all the temperatures of all
    # # the regions , print on screen
    # # " Check the Temperature line in simulation . config ."
    # # and return -1.

    def initTemps(self, tempStr):
        tempStr = tempStr.split(';')
        if len(tempStr) != 4:
            print("Check the DiseasesGrowth line in simulation.config.")
            return -1
        self.__temperature = [int(tempStr[0]), int(tempStr[1]), int(tempStr[2]), int(tempStr[3])]


    ##
    # Return the total disease strength of all the diseases
    # in the class implementing this interface .
    #

    def getSumStrength(self):
        total = 0
        for obj in self.__arrayDis:
            total += obj.getStrength()
        return total

    ##
    # Return the temperature of the world region with
    # the ID of quadID .
    # The valid value is between zero and three inclusive .
    #

    def getTemp(self, quad):
        return self.__temperature[quad]


    ##
    # Set the temperature of the region of the world
    # to the value of temp .
    # The quadID indicates the region .
    # The valid value is between [0, 3].
    # Any value of float is accepted for temp .
    #

    def setTemp(self, quad, temp):
        for i in range(len(quad)):
            self.__temperature[i] = temp[i]


    ##
    # This method overrides the act () method in the World class .
    # This method prints :
    #
    # " Iteration <ITRID >: World disease strength is <WorldDisease >"
    # where <ITRID > is replaced by the current iteration number and
    # <WorldDisease > is replaced by the returned value of
    # getSumStrength () in 2 decimal places .
    # An example is below .
    #
    # Iteration 0: World disease strength is 2.00
    # Iteration 1: World disease strength is 3.00
    #
    def act(self):
        print(f'Iteration {self.__itCounter}: World disease strength is {self.getSumStrength()}')
        self.__itCounter += 1


