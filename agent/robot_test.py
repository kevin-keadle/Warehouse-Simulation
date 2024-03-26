# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:36:27 2024

@author: Kevin
"""
import unittest
import robot
import numpy as np

class TestRobotMethods(unittest.TestCase):
    
    def test_UpdateRobotPosition(self):
        # this method should have no processing of the position
        r = robot.robot()
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        
        r.UpdateRobotPosition(7, 12)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 12)
        
        r.UpdateRobotPosition(-2, -1)
        self.assertEqual(r.x, -2)
        self.assertEqual(r.y, -1)
        
    def test_UpdateDestinationPosition(self):
        # this method should have no processing of the position
        r = robot.robot()
        self.assertEqual(r.dest_x, 0)
        self.assertEqual(r.dest_y, 0)
        
        r.UpdateDestinationPosition(8, 3)
        self.assertEqual(r.dest_x, 8)
        self.assertEqual(r.dest_y, 3)
        
        r.UpdateDestinationPosition(-4, -6)
        self.assertEqual(r.dest_x, -4)
        self.assertEqual(r.dest_y, -6)
        
    def test_WhereIsAgent(self):
        r = robot.robot()
        PickLocations = {}
        PickLocations[0] = [100,50]
        PickLocations[1] = [150,75]
        
        # neither x nor y are coincident
        r.x = 0
        r.y = 0
        r.WhereIsAgent(PickLocations)
        self.assertFalse(r.IsAtPickupLocation)
        
        # only x is coincident
        r.x = 150
        r.WhereIsAgent(PickLocations)
        self.assertFalse(r.IsAtPickupLocation)
        
        # only y is coincident
        r.x = 0
        r.y = 50
        r.WhereIsAgent(PickLocations)
        self.assertFalse(r.IsAtPickupLocation)
        
        # x and y are coincident, but with different locations
        r.x = 100
        r.y = 75
        r.WhereIsAgent(PickLocations)
        self.assertFalse(r.IsAtPickupLocation)
        
        # both x and y are coincident
        r.x = 100
        r.y = 50
        r.WhereIsAgent(PickLocations)
        self.assertTrue(r.IsAtPickupLocation)
    
    def test_ManhattanDistance(self):
        # should have zero distance when no start/end are initialized
        r = robot.robot()
        dist = r.ManhattanDistance()
        self.assertEqual(dist, 0)
        
        r.UpdateDestinationPosition(1, 1)
        dist = r.ManhattanDistance()
        self.assertEqual(dist, 2)
        
        r.UpdateDestinationPosition(-1, -1)
        dist = r.ManhattanDistance()
        self.assertEqual(dist, 2)
        
        r.UpdateDestinationPosition(1, np.Inf)
        dist = r.ManhattanDistance()
        self.assertEqual(dist, np.Inf)
    
    def test_IsAtDestination(self):
        # should only be true when both x and y are at the dest location
        r = robot.robot()
        r.x, r.y = 50, 100
        r.dest_x, r.dest_y = 50, 100
        atDestination = r.IsAtDestination()
        self.assertTrue(atDestination)
        
        r.x, r.y = 50, 100
        r.dest_x, r.dest_y = 51, 100
        atDestination = r.IsAtDestination()
        self.assertFalse(atDestination)
        
        r.x, r.y = 50, 100
        r.dest_x, r.dest_y = 50, 101
        atDestination = r.IsAtDestination()
        self.assertFalse(atDestination)
        
        r.x, r.y = 50, 100
        r.dest_x, r.dest_y = 51, 101
        atDestination = r.IsAtDestination()
        self.assertFalse(atDestination)
        
        r.x, r.y = 50, 100
        r.dest_x, r.dest_y = 49, 100
        atDestination = r.IsAtDestination()
        self.assertFalse(atDestination)
        
        r.x, r.y = 50, 100
        r.dest_x, r.dest_y = 50, 99
        atDestination = r.IsAtDestination()
        self.assertFalse(atDestination)
        
        r.x, r.y = 50, 100
        r.dest_x, r.dest_y = 49, 99
        atDestination = r.IsAtDestination()
        self.assertFalse(atDestination)
        


if __name__ == '__main__':
    unittest.main()
    