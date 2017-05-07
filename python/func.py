#!/usr/bin/env python2

from random import choice

def func1(data):
    return "func1 %s" %(data)

def func2(data):
    return "func2 %s" %(data)

data = "testing"

print(choice([
    func1,
    func2
    ])(data[::]))
