#!/usr/bin/env python
#encoding: UTF-8

# --- IMPORT MODULES --------------------------------------
import math

# --- INIT ------------------------------------------------
gravity = (math.pi, 0.1) # The vector for gravity
drag = .999
elasticity = 0.5

# --- UTILITY FUNCTIONS ----------------------------------
def addVectors((angle1, length1), (angle2, length2)):
    # This is done using Pythagoras... or magic!
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    length = math.hypot(x,y)
    # All angles are calculated in radians - just remember this
    angle = 0.5 * math.pi - math.atan2(y,x)
    return (angle, length)

def collideTest(A, B):
    dx = A.x - B.x
    dy = A.y - B.y
    # Look, the hypotenuse!
    distance = math.hypot(dx, dy)
    # And we return a boolean
    if distance <= A.size + B.size:
        return True
    else:
        return False

# --- FUNCTIONS -------------------------------------------
def exteriorCircleBounce(A, B):
    # This is used when the exterior of two circles are colliding.
    # This happens in two cases:
    #   1. Two Balls collide
    #   2. A Ball collides with a circle it can't pass through.
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
