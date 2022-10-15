#!/Users/zabby/anaconda3/bin/python

import numpy as np
import sys
from math import cos, sin, fabs
from fractions import Fraction

### Provides path for a/b
### where a is odd positive integer
###   and b is power of 2
### Usage :
### ./frac.path.py a b

def check( fr ) :
    
    if fr.denominator != 1 :
        if fr.numerator == 1 :
            check_d=fr.denominator
            while check_d % 2 == 0 :
                check_d = int( check_d/2 )
            if check_d == 1 :
                return False
            else :
                return True
        else :
            return True
    else :
        check_n=fr.numerator
        while check_n % 2 == 0 :
            check_n=int( check_n/2 )
        if check_n == 1 :
            return False
        else: 
            return True

num=int( sys.argv[ 1 ] )
den=int( sys.argv[ 2 ] )
print( 'Checking path for {}/{}'.format( num, den ) )
print( '{}/{}'.format( num, den ) )

np=int( num*3+den )
dp=den

trial=Fraction( np, dp )

ii=0
while trial.numerator/trial.denominator > (2**(2*(ii+1))-1)/3 :
    ii=ii+1

num_p=int( trial.numerator - trial.denominator*( 2**(2*ii)-1 )/3 )
den_p=int( trial.denominator*( ( 2**(2*(ii+1))-1)/3-( 2**(2*(ii))-1)/3 ) )

phi=Fraction( num_p, den_p )

print( '{}'.format( trial ) )

status=check( trial )

while status :

    np=trial.numerator
    corr=1
    while np % 2 == 0 :
        np=int( np/2 )
        corr=corr*2
    np=trial.numerator*3+corr
    frp=Fraction( np, trial.denominator )
    trial=frp

    status=check( trial )
    corr=0
    np=trial.numerator
    while np % 2 == 0 :
        np=int( np/2 )
        corr=corr+1

    ii=0
    while trial.numerator/trial.denominator > (2**(2*(ii+1))-1)/3 :
        ii=ii+1

    num_p=int( trial.numerator - trial.denominator*( 2**(2*ii)-1 )/3 )
    den_p=int( trial.denominator*( ( 2**(2*(ii+1))-1)/3-( 2**(2*(ii))-1)/3 ) )

    phi=Fraction( num_p, den_p )

    if corr == 0 :    
        print( '{}'.format( trial ) )
    else :
        print( '2^{} * {}'.format( corr, np ) )
    

