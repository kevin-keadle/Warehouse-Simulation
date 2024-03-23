# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 00:57:40 2024

@author: Kevin
"""
from simulator import simulator

s = simulator.Simulation()
s.SetSimulationRuntime(3600, 's')
s.SetNumberOfEntities(1)
s.InitializeFactory()
s.InitializeEntities()

s.Run()
