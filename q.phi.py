#!/Users/zabby/anaconda3/bin/python

import numpy as np
import sys
from math import cos, sin
from fractions import Fraction

### Evaluates phi(x) or provides list { x_i } where phi( x_0 )=phi( x_1 )= ... =phi( x_i )=a/b
### Usage :
### ./q.phi.py x
### or
### ./q.phi.py a b

if len( sys.argv ) == 3 :

    for i in range( 20 ) :

        n_x=3*int( sys.argv[ 1 ] )*(2**(2*i))+(2**(2*i))*int( sys.argv[ 2 ] )-int( sys.argv[ 2 ] )
        d_x=3*int( sys.argv[ 2 ] )

        value=Fraction( n_x, d_x )

        print( '{}'.format( value ) )

elif len( sys.argv ) == 2 :

    i=0

    while int( sys.argv[ 1 ] ) > (2**(2*(i+1))-1)//3 :
        i=i+1

    num=int( sys.argv[ 1 ] )-( 2**(2*i)-1 )//3 
    den=( 2**(2*(i+1))-1)//3-( 2**(2*(i))-1)//3 

    print( Fraction( int( num ), int( den ) ) )
