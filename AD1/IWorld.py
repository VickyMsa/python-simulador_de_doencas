#!/usr/bin/env python
# coding: UTF-8
#
## package IWorld
#
#  World Interface.

try:  # python >= 3.4
    from abc import ABC, ABCMeta, abstractmethod
except ImportError:  # python 2
    from abc import ABCMeta, abstractmethod

    ABC = object


##
# Interface IWorld allows initializing and setting diseases for a world.
#
# @author Viviane Magalhães Siqueira (based on Professor Paulo Roma's work)
# @date 10/08/2020
#
class IWorld(ABC):
    __metaclass__ = ABCMeta

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
    @abstractmethod
    def prepare(self): pass

    ##
    # Set the temperature of the region of the world
    # to the value of temp .
    # The quadID indicates the region .
    # The valid value is between [0, 3].
    # Any value of float is accepted for temp .
    #
    @abstractmethod
    def setTemp(self, quad, temp): pass

    ##
    # Return the temperature of the world region with
    # the ID of quadID .
    # The valid value is between zero and three inclusive .
    #
    @abstractmethod
    def getTemp(self, quad): pass

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
    @abstractmethod
    def initDiseases(self, numDisStr): pass

    ## Return the list of objects in
    # the class implementing this interface .
    @abstractmethod
    def getObjects(self): pass

    ##
    # Set the temperature for each quadrant of the MyWorld
    # according to the value of the tempStr .
    # An example of tempStr is below .
    # The region temperatures for regions 0, 1, 2, and 3
    # are 12, 20, 50, and 100 , respectively .
    #
    # Return 0 for a successful initialization of
    # the quadrant temperatures . No exceptions are thrown .
    # the quadrant temperatures . No exceptions are thrown .
    #
    # Ex: "12;20;50;100"
    #
    # If tempStr is empty or not in the correct format
    # or does not have all the temperatures of all
    # the regions , print on screen
    # " Check the Temperature line in simulation . config ."
    # and return -1.
    #
    @abstractmethod
    def initTemps(self, tempStr): pass

    ## Return the total disease strength of all the diseases
    # in the class implementing this interface .
    @abstractmethod
    def getSumStrength(self): pass

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

    @abstractmethod
    def initLocations(self, locationsStr, diseaseArr): pass

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
    # " Check the DiseasesGrowth line in simulation . config ."
    # and return -1.
    #
    # Return 0 for a successful
    # initialization of the Disease growth conditions .
    # No exceptions are thrown .
    #
    @abstractmethod
    def initGrowthConditions(self, growthStr, diseaseArr): pass
