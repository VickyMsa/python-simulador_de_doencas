#!/usr/bin/env python
# coding: UTF-8
#
# @package World
#
import sys
from Actor import Actor


##
#
# Class for holding Actor objects in cells of a grid in the world.
# The world is represented by a 2 dimensional array of cells,
# with the specified width and height. One cell
# can keep at most 5 Actor objects.
#
# @author Viviane Magalhães Siqueira (based on Professor Paulo Roma's work)
# @date 10/08/2020
#

class World:

    ##
    # Constructor.
    # Creates a world with the given width and height.
    #
    # - The maximum width and height are 1000.
    # - The maximum number of Actor objects in a cell is 5.
    # <PRE>
    # If worldWidth <= 0 or worldWidth > maximum width
    #     use the maximum width instead.
    # If worldHeight <=0 or worldHeight > maximum height
    #     use the maximum height instead.
    # </PRE>
    #
    # @param worldWidth Width in number of cells
    # @param worldHeight Height in number of cells
    #
    def __init__(self, worldWidth, worldHeight):

        ## A 3D array of Actors.
        self.__grid = []

        ## Counter for the number of added objects.
        self.__objCounter = 0

        ## Width of the world.
        self.__width = 0

        ## Height of the world.
        self.__height = 0

        ## Depth of the world.
        self.__depth = 5

        # self.__MAXDIM = 1000  # ??

        if worldWidth <= 0 or worldWidth > 1000:
            worldWidth = 1000

        if worldHeight <= 0 or worldHeight > 1000:
            worldHeight = 1000

        self.__width = worldWidth
        self.__height = worldHeight

        self.__grid = self.createGrid(worldHeight, worldWidth, self.__depth)

    ## Initializes each object of the array as None.
    #
    # @param h grid height.
    # @param w grid width.
    # @param d grid depth.
    # @return grid.
    #
    def createGrid(self, h, w, d):
        return [[[None] * self.__depth for y in range(self.__width)] for x in range(self.__height)]

    ## Return a string representation of the grid.
    # List by width. Each slice is height x depth. (List by height. Each slice is width x depth)
    #
    # @return string with the grid.
    def __str__(self):
        gstr = f'Grid is {self.getHeight()} x {self.getWidth()} x {self.getDepth()}\n\n'
        for i, x in enumerate(self.__grid):
            gstr += f'width {i}\n'
            gstr += '\n'.join(
                [' '.join([' '.join(str('*' if z is None else z.getID())) for z in y]) for y in x]) + '\n\n'
        return gstr

    ## Return a string representation of the grid.
    # List by depth. Each slice is height x width.
    #
    # @return string with the grid.
    # @see https://www.ict.social/python/basics/multidimensional-lists-in-python

    def __repr__(self):
        g = self.__grid
        h = self.getHeight()
        w = self.getWidth()
        d = self.getDepth()

        gstr = f'Grid is {h} x {w} x {d}\n\n'
        for z in range(d):
            gstr += f'depth {z}\n'
            for y in range(h):
                for x in range(w):
                    o = g[y][x][z]
                    gstr += str('*' if o is None else o.getID()) + ' '
                gstr += '\n'
            gstr += '\n'
        return gstr

    ##
    # Blank method body.
    # Overriden in subclasses as appropriate
    #
    def act(self):
        pass

    ##
    # Adds a new actor to this world at a given position.
    #
    # - The new object will be added at the cell (x,y) if there are less than 5 objects in this cell.
    # - Be sure to make the added object know that it is in this world and it is at this cell.
    # - Check which methods of the Actor class to call.
    #
    # @param object the object to be added at this cell (x, y)
    # @param x the column
    # @param y the row
    # @return number of objects in cell (x,y).
    #
    # @throws SyntaxError when already max number of objects are in that cell
    # @throws ValueError if x or y is not in the valid range
    # @throws NameError if the object is null
    #
    def addObject(self, objct, x, y):
        if objct is None:
            raise NameError
        if x < 0 or x >= self.getWidth():
            raise ValueError
        if y < 0 or y >= self.getHeight():
            raise ValueError
        try:
            quant = self.__grid[y][x].index(None)
            self.__grid[y][x][quant] = objct
            objct.addedToWorld(self)
            objct.setLocation(x, y)
            return quant + 1
        except ValueError:
            raise SyntaxError

    ##
    # Returns the world height.
    #
    # @return the world height.
    #
    def getHeight(self):
        return len(self.__grid)

    ##
    # Returns the world width.
    #
    # @return the world width.
    #
    def getWidth(self):
        return len(self.__grid[0])

    ##
    # Returns the world depth.
    #
    # @return the world depth.
    #
    def getDepth(self):
        return len(self.__grid[0][0])

    ##
    # Returns the total number of objects in this world.
    #
    # @return Total number of objects in this world.
    #
    def numberOfObjects(self):
        return self.__objCounter

    ##
    # Returns an array with all Actor objects in this world.
    #
    # @return Array of Actor objects that are in this world.
    #
    # Comments:
    # - Each class in Java is a subclass of the Object class.
    # - Observe that you use the implicit upcast where you assign an Actor
    #   object (sub-class) in an element of the Object array.
    #
    def getObjects(self):
        obj = list()
        for l in range(len(self.__grid)):
            for c in range(len(self.__grid[l])):
                for d in range(len(self.__grid[l][c])):
                    if self.__grid[l][c][d] is not None:
                        obj.append(self.__grid[l][c][d])
        return obj

    ## 
    #
    #  It checks if aGrid is a 3D array with the same positive length in each dimension.
    #  If so, it sets the grid to aGrid and the other private fields of class World to
    #  the dimension lengths of aGrid and numObjs.
    #
    #  Note that some checks are omitted. For example, no check is performed to make sure
    #  that numObjs is consistent with the number of Actor objects in aGrid.
    #
    #  Each Actor object in aGrid has to be set to this World object.
    #
    #  @param aGrid reference to a 3D array of Actor objects.
    #
    #  @param numObjs the number of Actor objects in aGrid.
    #
    #  @throws ValueError if the length of each dimension is out of range
    #         or 2nd/3rd dimension has different lengths.
    #
    def setGrid(self, aGrid, numObjs):
        pass


def main():
    world = World(8, 10)
    print(f"Number of objects in cell(4,4) = {world.addObject(Actor(), 4, 4)}")
    print(f"Number of objects in cell(2,3) = {world.addObject(Actor(), 2, 3)}")
    print(f"Number of objects in cell(4,4) = {world.addObject(Actor(), 4, 4)}")
    print(f"Number of objects in cell(4,4) = {world.addObject(Actor(), 7, 7)}")
    print(f"Number of objects in cell(4,4) = {world.addObject(Actor(), 4, 4)}")
    print(f"Number of objects in cell(4,4) = {world.addObject(Actor(), 4, 4)}")
    print(f"Number of objects in cell(4,4) = {world.addObject(Actor(), 4, 4)}")
    print(f"Number of objects in cell(4,4) = {world.addObject(Actor(), 7, 9)}")

    print(world)
    print(f"{world}")


if __name__ == "__main__":
    sys.exit(main())
