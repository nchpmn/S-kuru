#!/usr/bin/env python
#encoding: UTF-8

# --- MODULE IMPORTING ------------------------------------
import random
import math

# --- INIT ------------------------------------------------
gravity = (math.pi, 0.1) # The vector for gravity
drag = .999
elasticity = 0.5

# --- FUCNTIONS -------------------------------------------

def addVectors((angle1, length1), (angle2, length2)):
    """Take two vectors and find the resultant"""
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    length = math.hypot(x,y)
    angle = 0.5 * math.pi - math.atan2(y,x)
    return (angle, length)

def collideTest(A, B):
    """Test for collision between two class objects, reutrn boolean"""
    dx = A.x - B.x
    dy = A.y - B.y
    
    distance = math.hypot(dx, dy)
    
    if distance <= A.size + B.size:
        return True
    else:
        return False

def ballBounce(A, B):
    """Calculate the correct changes to each ball after a collision"""
    dx = A.x - B.x
    dy = A.y - B.y
    tangent = math.atan2(dy, dx) # Find the tangent of the point
    angle = 0.5 * math.pi + tangent # We use this later on
    A.angle = 2*tangent - A.angle # Alter angles
    B.angle = 2*tangent - B.angle
    if A.speed != 0 and B.speed != 0:
        (A.speed, B.speed) = (B.speed, A.speed) # Swap speeds
    A.speed *= elasticity # Reduce speed due to elasticity
    B.speed *= elasticity

    A.x += math.sin(angle) # Move particles away from each other
    A.y -= math.cos(angle)
    B.x -= math.sin(angle)
    B.y += math.cos(angle)

def circleBounce(C, B):
    """Calculate a ball's bounce off of a circle"""
    dx = C.x - B.x
    dy = C.y - B.y
    
    tangent = math.atan2(dy, dx)
    B.angle = 2 * tangent - B.angle
    B.speed *= elasticity + 0.251
    
    distance = math.hypot(dx, dy)
    reboundFactor = (C.size - B.size) - distance
    # reboundFactor must be more than 1
    
    angle = 0.5 * math.pi + tangent
    B.x += math.sin(angle) * -reboundFactor
    B.y -= math.cos(angle) * -reboundFactor