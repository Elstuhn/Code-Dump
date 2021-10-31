from math import radians, cos, sin, sqrt, atan
from collections import namedtuple
import typing

CPoint = namedtuple("Cartesian Point", ["x", "y"])
PPoint = namedtuple("Polar Point", ["r", "theta"])
def p2c(theta : float, r : float, theta_unit = "r", nearest = 1): #theta will default to radians, "d" for degrees 
  """
  Conversion of polar coordinates to cartesian coordinates
  Theta defaults to radians, theta_unit = "d" for theta to be in degrees
  Returns a namedtuple of cartesian coordinates
  """
  if theta_unit == "d":
    theta = radians(theta)
    
  x = round(cos(theta)*r, nearest)
  y = round(sin(theta)*r, nearest)
  return CPoint(x=x, y=y)

def c2p(x, y, nearest = 1):
  """
  Conversion of cartesian coordinates to polar coordinates
  Theta returned will be in radians
  Returns a namedtuple of polar coordinates
  """
  r = round(sqrt(x**2+y**2), nearest)
  theta = round(atan(y/x), nearest)
  return PPoint(r, theta)
  
  
