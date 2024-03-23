# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:15:14 2024

@author: Kevin
"""
import unittest
import factory

class TestFactoryClass(unittest.TestCase):
    
    def test_GenerateRandomZipCode(self):
        f = factory.factory()
        
        # Five digit number
        expect = '12345'
        actual = f.GenerateZipCode(12345)
        self.assertEqual(expect, actual)
        
        # Leading zero number
        expect = '01234'
        actual = f.GenerateZipCode(1234)
        self.assertEqual(expect, actual)
        
        # Invalid type
        expect = '00000'
        actual = f.GenerateZipCode('1234')
        self.assertEqual(expect, actual)
        
        # Out of range low
        expect = '00000'
        actual = f.GenerateZipCode(-1)
        self.assertEqual(expect, actual)
        
        # Out of range high
        expect = '00000'
        actual = f.GenerateZipCode(100000)
        self.assertEqual(expect, actual)
        

if __name__ == '__main__':
    unittest.main()