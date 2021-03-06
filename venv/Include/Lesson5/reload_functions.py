from multipledispatch import dispatch
from collections import namedtuple
from types import *  # we can test for lambda type, e.g.:



Sprite = namedtuple('Sprite', ['name'])
Point = namedtuple('Point', ['x', 'y'])
Curve = namedtuple('Curve', ['x', 'y', 'z'])
Vector = namedtuple('Vector', ['x','y','z'])

@dispatch(Sprite, Point, Vector, int)
def add_bullet(sprite, start, direction, speed):
    print("Called Version 1")

@dispatch(Sprite, Point, Point, int, float)
def add_bullet(sprite, start, headto, speed, acceleration):
    print("Called version 2")

@dispatch(Sprite, LambdaType)
def add_bullet(sprite, script):
    print("Called version 3")

@dispatch(Sprite, Curve, int)
def add_bullet(sprite, curve, speed):
    print("Called version 4")

sprite = Sprite('Turtle')
start = Point(1,2)
direction = Vector(1,1,1)
speed = 100 #km/h
acceleration = 5.0 #m/s