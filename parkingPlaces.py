#!/usr/bin/env Python3


from os import system
from random import randint

PARKING_PLACES = 7
FREE_PLACE = 3



system( "clear" )


print( "#" * PARKING_PLACES * 5 )
 

for place_index in range( 1, PARKING_PLACES + 1 ):
 
 if( place_index == FREE_PLACE ):
  print( "|   |", end = "" )
 else:
  print( "| X |", end = "" )

print( "\n","#" * PARKING_PLACES * 5, sep = "" )
