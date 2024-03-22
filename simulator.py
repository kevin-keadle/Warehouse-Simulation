# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:02:39 2024

@author: Kevin
"""
import robot
import factory
import numpy as np
import matplotlib.pyplot as plt

class Simulation:
    def __init__(self):
        self.NumberOfEntities = 1
        self.Duration = 3600

    
    def SetNumberOfEntities(self, entities):
        self.NumberOfEntities = entities
        
    
    def InitializeFactory(self):
        
        # Create the factory layout / factory class object
        f = factory.factory()
        self.Factory = f
    
    def InitializeEntities(self):
        
        # Create all of the entities
        self.Entities = []
        for i in range(self.NumberOfEntities):
            r = robot.robot()

            # Random start (package pickup) location
            x, y = self.Factory.PickLocations[np.random.randint(0,4)]
            r.UpdateRobotPosition(int(x), int(y))

            # Determine the drop location based on the package
            x, y = self.Factory.DropLocations[str(np.random.randint(0,9))]
            r.UpdateDestinationPosition(int(x), int(y))

            r.ComputeMovePath()
            self.Entities.append(r)
            
        
    def SetSimulationRuntime(self, duration, units):
        '''
        This sets the total duration for the simulation

        Parameters
        ----------
        duration : int
            Total simulation time.
        units : string
            Describes the simulation units (options = 's', 'm', 'h').

        Returns
        -------
        None.

        '''
        if units == 'm':
            self.Duration = duration * 60
        elif units == 'h':
            self.Duration = duration * 3600
        else:
            self.Duration = duration

    
    def Run(self):
        if len(self.Entities) == 0:
            return

        fig, ax = plt.subplots()
        scatter = ax.scatter(0, 0)
        plt.show(block=False)
        plt.get_current_fig_manager().window.showMaximized()
        
        
        # Display the package pickup and dropoff locations within the factory
        self.Factory.PlotPickLocations(ax)
        self.Factory.PlotDropLocations(ax)
        
        # Set the plot size to the factory size
        ax.set_xlim(0, self.Factory.factory_x)
        ax.set_ylim(0, self.Factory.factory_y)
        ax.set_aspect('equal')
        
        # Run indefinitely
        count = 0
        packagesPicked = 0
        endSimulation = False
        while not endSimulation:
            if count%100 == 0:
                print('Elapsed cycles = ', count)
            count += 1
                
            # At each time step, loop through every entity
            for entity in self.Entities:
                # If we are at the destination, drop the package and return
                if entity.IsAtDestination():
                    packagesPicked += 1
                    
                    x, y = self.Factory.PickLocations[np.random.randint(0,4)]
                    entity.UpdateDestinationPosition(int(x), int(y))
                    entity.ComputeMovePath()
                    
                    print('Robot', entity.x, entity.y)
                    print('desty', entity.dest_x, entity.dest_y)
                    
                    if packagesPicked > 2:
                        endSimulation = True
                        print('Simulation ended')
                        return
                    continue
                
                # Increment the robot in space
                entity.Step()
                
                # This needs to be outside of the for-loop
                # We need to update all entity positions, then zip, then plot
                scatter.set_offsets(np.c_[entity.x, entity.y])
                
            
            # Redraw the figure once per loop
            fig.canvas.draw()
            fig.canvas.flush_events()


##############################################################################

s = Simulation()
s.SetSimulationRuntime(3600, 's')
s.SetNumberOfEntities(1)
s.InitializeFactory()
s.InitializeEntities()

s.Run()