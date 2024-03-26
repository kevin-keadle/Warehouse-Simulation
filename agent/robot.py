# -*- coding: utf-8 -*-
"""
Spyder Editor

This file defines the robot class which handles movement of an individual robot
in an arbitrary environment.
"""
import numpy as np

class robot:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dest_x = 0
        self.dest_y = 0
        self.IsAtPickupLocation = False
        self.step = 0
        self.vertices = []
        
    def UpdateRobotPosition(self, x, y):
        self.x = x
        self.y = y
        
    def UpdateDestinationPosition(self, x, y):
        self.dest_x = x
        self.dest_y = y
    
    def GetNextDestination(self, PickLocations, DropLocations):
        '''
        This function will determine if the robot is at a drop location or a
        pick location. Based on the current location, it will load a new
        destination into the robots properties and compute the move path.

        Parameters
        ----------
        PickLocations : dict(int, float)
            Dictionary of the pick locations.
        DropLocations : dict(str, float)
            Dictionary of the drop locations.

        Returns
        -------
        None.

        '''
        x = 0.0
        y = 0.0
        
        # Determines if we are at a pick or drop location
        self.WhereIsAgent(PickLocations)
        
        # If at pick location, go to drop location and vice versa
        if self.IsAtPickupLocation == True:
            x, y = DropLocations[str(np.random.randint(0, len(DropLocations)))]
        else:
            x, y = PickLocations[np.random.randint(0,len(PickLocations))]

        self.UpdateDestinationPosition(int(x), int(y))
        self.ComputeMovePath()
        
    
    def WhereIsAgent(self, PickLocations):
        '''
        This function determines if the entity is currently at a pickup 
        location. The IsAtPickupLocation variable on the entity is set based
        on this determination.

        Parameters
        ----------
        PickLocations : dict(int, float)
            Dictionary of the pickup locations in the factory.

        Returns
        -------
        None.

        '''
        
        for x in PickLocations:
            if abs(self.x - PickLocations[x][0]) < 1 and abs(self.y - PickLocations[x][1]) < 1:
                self.IsAtPickupLocation = True
                return
        
    
    def ManhattanDistance(self):
        '''
        This function computes the Manhattan distance between the robot current
        position and the destination position.

        Returns
        -------
        int
            Manhattan distance between points

        '''
    
        return (abs(self.dest_x - self.x) +
                abs(self.dest_y - self.y))
    
    def ComputeStraightLine(self):
        '''
        This function computes the straight line distance between the robot
        current position and the destination position.

        Returns
        -------
        m : float
            Slope of the line between the current and distination positions
        b : float
            Intercept of the line between the current and distination positions

        '''
        
        xsteps = np.abs(self.dest_x - self.x)
        ysteps = np.abs(self.dest_y - self.y)

        # Straight line between initial and destination
        # y = mx + b
        m = 0
        if abs(xsteps * np.sign(self.dest_x - self.x)) > 0:
            m = (ysteps * np.sign(self.dest_y - self.y)) / \
                (xsteps * np.sign(self.dest_x - self.x))
        b = self.y - m*self.x
        
        return m, b

    def ComputeMovePath(self):
        '''
        This function determines the actual travel path between the current
        and destination locations. This function is specifically used for a
        single element simulation. The robot will travel unfettered between
        the start and destination locations moving as close as possible to the
        straight line between the two locations.
        
        It is assumed that each step of the simulation
        
        *** TODO ***
         1. Determine path function (this, but modified). Needs to include
            any permanent paths
         2. Update one time step function
         3. Forward look that searches for interactions (2, then many)
         4. Method to pause the current robot (waitsteps = 3, waitsteps -= 1)
         5. Update path to be closer to a straight line than partially flat
            Maybe move 25% distance in x, then remaining 25% in y, etc.
         6. Expand destinations to be 4 spots at a location
         7. Add pickup randomization and return to new location

        Returns
        -------
        vertices : list
            Vertices of travel between the initial and destination locations
        xreal : array
            Discrete x-values between initial and destination locations
        yreal : array
            Discrete y-values between initial and destination locations

        '''
        
        # This is the initial point
        self.vertices.append([self.x, self.y])
        
        m, b = self.ComputeStraightLine()
        
        # The real straight line between the points
        xsteps = np.abs(self.dest_x - self.x)
        xreal  = np.linspace(self.x,  self.dest_x, xsteps + 1)
        yreal  = m * xreal + b
        
        # This solution continually moves along the closest line to straight
        #  while still transiting toward the destination
        mdist = self.ManhattanDistance()
        while mdist > 0:
            # Compute the y location we should be at
            y = m * self.x + b
            
            # If we are already there, transit in x
            if np.abs(self.y - y) < 0.9999:
                self.x += np.sign(self.dest_x - self.x)
            else:
                self.y += np.sign(self.dest_y - self.y)
            
            # Save the vertex where we just moved & how many steps we've hit
            self.vertices.append([self.x, self.y])
            
            # Compute our new distance to destination
            mdist = self.ManhattanDistance()
            
        # Need to reset the x,y of the robot once the position has updated
        self.x, self.y = self.vertices[0][:]
        return self.vertices, xreal, yreal
    
    def Step(self):
        '''
        This function iterates the current entity forward one unit step.

        Returns
        -------
        None.

        '''
        
        self.x = self.vertices[self.step][0]
        self.y = self.vertices[self.step][1]
        self.step += 1 - int(self.IsAtDestination())

    
    def IsAtDestination(self):
        '''
        This function determines if the current entity is at its destination
        location. Both the x and y coordinates of the entity and the 
        destination must be coincident.

        Returns
        -------
        bool
            TRUE if the entity and destination are coincident.

        '''
        if abs(self.x - self.dest_x) == 0 and abs(self.y - self.dest_y) == 0:
            return True
        return False


##############################################################################
