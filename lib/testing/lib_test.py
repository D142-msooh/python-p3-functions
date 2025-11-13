#!/usr/bin/env python3

from functions import greet_programmer, greet, greet_with_default, \
                        add, halve

import io
import sys


class TestGreetProgrammer:
    '''function greet_programmer()'''

    def test_greet_programmer(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_programmer()
        sys.stdout = sys.__stdout__

class TestGreet:
    '''function greet()'''

    def test_greet_programmer(self):
        print ("Hello, {name}!")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet("Guido")
        sys.stdout = sys.__stdout__

class TestGreetWithDefault:
    '''function greet_with_default()'''

    def test_greet_with_default(self):
        print ("Hello, programmer!")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_with_default()
        sys.stdout = sys.__stdout__

    def test_greet_with_default_with_param(self):
        print ("Hello, {name}!")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_with_default("Guido")
        sys.stdout = sys.__stdout__

class TestAdd:
    '''function add()'''

    def test_add(self):
        '''calculates 45 + 55 = 100'''

class TestHalve:
    '''function halve()'''

    def test_halve_int(self):
        '''halves integer input'''

    def test_halve_float(self):
        '''halves float input'''
