# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 01:00:37 2024

@author: Kevin
"""
import unittest
import simulator

class TestSimulatorClass(unittest.TestCase):
    
    def test_SetNumberOfEntities(self):
        s = simulator.Simulation()
        
        # Expect the default to be 1 entity
        self.assertEqual(1, len(s.Entities))


if __name__ == '__main__':
    unittest.main()