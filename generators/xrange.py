#!/usr/bin/env python

"""Foobar.py: Description of what foobar does."""

__author__      = "@Code.on.Tap"
__copyright__   = "Copyright 2019"
__license__     = "MIT"
__source__      = "https://github.com/code-on-tap/examples/generators/xrange.py"


class xrange2( object ):
  def __init__( self, *args ):
    if not args:
      raise ValueError()
  
    self.i = None
    n = len( args )
    if n == 1:
      self.start = 0
      self.stop = args[0]
      self.step = 1
    elif n == 2:
      self.start = args[0]
      self.stop = args[1]
      self.step = 1
    elif n == 3:
      self.start = args[0]
      self.stop = args[1]
      self.step = args[2]
    else:
      raise ValueError()
  
  def __iter__( self ):
    self.i = self.start - self.step
    return self
  
  def next( self ):
    self.i += self.step
    if self.i >= self.stop:
      raise StopIteration()
    else:
      return self.i

for i in xrange2( 1, 17, 2 ):
  print( i )
#> 1
#> 3
#> 5
#> 7
#> 9
#> 11
#> 13
#> 15

for i in xrange( 1, 17, 2 ):
  print( i )
#> 1
#> 3
#> 5
#> 7
#> 9
#> 11
#> 13
#> 15
