#!/usr/bin/env python
# coding: UTF-8
#
## @package Disease

from Actor import Actor
from IDisease import IDisease


##
# This Disease class is a sub-class of the Actor class.
#
# @author Viviane Magalhães Siqueira (based on Professor Paulo Roma's work)
# @date 10/08/2020
#
#
class Disease(Actor, IDisease):

    ##
    # Constructor.
    # - Call its superclass’s default constructor.
    # - Initialize the lower bound and the upper bound temperatures for the
    #   growth rate to 0.
    # - Set the growth rate to 0.
    # - Set the disease strength to 1.
    #
    def __init__(self):
        super(Disease, self).__init__()
        ### Rate at which the disease grows when subjected to the appropriate temperature range.    
        self.__growthRate = 0.0
        ### Minimum temperature for the disease development.
        self.__lowerTemp = 0.0
        ### Maximum temperature for the disease development.
        self.__higherTemp = 0.0
        ### Disease strength.
        self.__dStrength = 1.0

    ##
    # Sets the disease growth rate, lower temperature and higher temperature.
    #
    # @param lTemp Lower bound temperature for the disease to grow at this gRate.
    # @param hTemp Upper bound temperature for the disease to grow at this gRate.
    # @param gRate The growth rate.
    #
    def setGrowthCondition(self, lTemp, hTemp, gRate):
        self.__growthRate = gRate
        self.__lowerTemp = lTemp
        self.__higherTemp = hTemp

    ##
    # Returns the disease growth rate, lower temperature and higher temperature.
    #
    # @return growth rate, lower temp and higher temp
    #
    def getGrowthCondition(self):
        return self.__growthRate, self.__lowerTemp, self.__higherTemp

    ## Returns the quadrant of this disease.
    #
    # @return 0, 1, 2 or 3.
    #
    def getQuadrant(self):
        worldQuad = self.getWorld()
        width = worldQuad.getWidth()
        height = worldQuad.getHeight()
        if self.getX() < (width // 2) and self.getY() < (height // 2):
            return 0
        if self.getX() >= (width // 2) and self.getY() < (height // 2):
            return 1
        if self.getX() < (width // 2) and self.getY() >= (height // 2):
            return 2
        if self.getX() >= (width // 2) and self.getY() >= (height // 2):
            return 3


    ##
    # Return the disease strength of this object.
    #
    # @return disease strength of the object.
    #

    def getStrength(self):
        return self.__dStrength

    ##
    # This method overrides the act () method in the Actor class .
    # Check whether the object is in the region where the region
    # temperature is within the lower bound and the upper bound
    # temperatures for the object ’s growth rate . If it is
    # the case , multiply its strength with the growth rate .
    #
    def act(self):
        #print(f'Iteration {self.Iteration()}: Disease {self.getID()}')
        temp = self.getWorld().getTemp(self.getQuadrant())
        if self.__lowerTemp <= temp <= self.__higherTemp:
            self.__dStrength *= self.__growthRate
            #print(self.__dStrength)
    ##
    # Return a string with the strength, growth and quadrant of this disease.
    #
    def __str__(self):
        st = super(Disease, self).__str__()
        st += f'strength = {self.getStrength()}\n'
        st += 'growth = %.2f, %.2f, %.2f\n' % self.getGrowthCondition()
        st += 'quadrant = %d, temp = %d\n' % (self.getQuadrant(), self.getWorld().getTemp(self.getQuadrant()))
        return st


