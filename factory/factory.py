# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:00:11 2024

@author: Kevin
"""
import numpy as np

class factory:
    
    def __init__(self):
        self.factory_x = 1200   # Total x size of the factory
        self.factory_y = 400    # Total y size of the factory
        self.PickLocations = {} # Where packages get picked up for sorting
        self.DropLocations = {} # Where packages get deposited
        self.PlotPickLocs = []  # Pick locations which can be used for plotting
        self.PlotDropLocs = []  # Drop locations which can be used for plotting
        self.PkgsDropped = {}   # Dict that tracks how many packages are at drop location
        self.PkgsPicked = {}    # Dict that tracks how many packages are taken from each pick location
    
        self.SetPickLocations()
        self.SetDropLocations()

    
    def SetPickLocations(self):
        '''
        This methods sets an equally spaced grid of pick locations based on the
        size of the factory. There are five equally spaced pickup locations.
        These are located 50 feet from the front of the factory

        Returns
        -------
        None.

        '''
        
        lsp = np.linspace(50, self.factory_x - 50, 5)
        
        for i in range(5):
            self.PickLocations[i] = [lsp[i], 50]
            self.PlotPickLocs.append(self.PickLocations[i])
    
    
    def PlotPickLocations(self, ax):
        '''
        This method will accept the handle to a figure and plot the package
        pickup locations on that figure.

        Parameters
        ----------
        ax : matplotlib.axes
            Axes for an active figure.

        Returns
        -------
        None.

        '''
        
        if len(self.PlotPickLocs) == 0:
            return
        
        x, y = zip(*self.PlotPickLocs)
        ax.scatter(x, y, color='k', marker='o', facecolors='none')
        
    
    def SetDropLocations(self):
        '''
        This method sets an equally spaced grid of drop locations based on the
        first digit of the zip code. The grid is equally spaced along the x
        length of the factory including a 50 foot buffer to the factory edge.
        The drop locations are spaced along two lines where the even zip codes
        are dropped 250 feet from the front of the factory and odd zip codes
        are dropped 350 feet from the front of the factory.

        Returns
        -------
        None.

        '''
        
        lsp = np.linspace(50, self.factory_x - 50, 5)
        
        # Even zip codes are along the (x, 250) line
        # Odd zip codes are along the (x, 350) line of the factory
        for i in range(10):
            self.DropLocations[str(i)] = [lsp[int(np.floor(i/2))], 250 + 100*(i % 2)]
            self.PlotDropLocs.append(self.DropLocations[str(i)])
    
    
    def PlotDropLocations(self, ax):
        '''
        This method will accept the handle to a figure and plot the package
        drop locations on that figure.

        Parameters
        ----------
        ax : matplotlib.axes
            Axes for an active figure.

        Returns
        -------
        None.

        '''
        
        if len(self.PlotDropLocs) == 0:
            return
        
        x, y = zip(*self.PlotDropLocs)
        ax.scatter(x, y, color='k', marker='x')
        
    
    def PickUpPackage(self):
        zip = np.random.randint(1, 99999)

        return True
    
    
    def GenerateZipCode(self, zip):
        '''
        This method accepts an integer on the range of 0 - 99999 (inclusive)
        and returns a formatted string of the zip code.

        Parameters
        ----------
        zip : int
            Integer representation of a zip code.

        Returns
        -------
        string
            Formatted zip code.

        '''
                
        # Invalid input type
        if type(zip) is not int:
            return '00000'
        
        # Invalid input range
        if zip < 0 or zip > 99999:
            return '00000'
        
        return '{:0>5}'.format(zip)

