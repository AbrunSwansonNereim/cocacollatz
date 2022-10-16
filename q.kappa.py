#!/Users/zabby/anaconda3/bin/python

import numpy as np
import sys
from math import cos, sin, fabs
from fractions import Fraction

### Evalutes kappa( a/b ) ( b should be a power of 2 )
### Usage :
### ./q.kappa.py a b

def check( fr ) :
    
    if fr.denominator != 1 :
        if fr.numerator == 1 :
            check_d=fr.denominator
            while check_d % 2 == 0 :
                check_d = check_d//2
            if check_d == 1 :
                return False
            else :
                return True
        else :
            return True
    else :
        check_n=fr.numerator
        while check_n % 2 == 0 :
            check_n=check_n//2
        if check_n == 1 :
            return False
        else: 
            return True

num=int( sys.argv[ 1 ] )
den=int( sys.argv[ 2 ] )

np=int( num*3+den )
dp=den

trial=Fraction( np, dp )

ii=0
while trial.numerator//trial.denominator > (2**(2*(ii+1))-1)//3 :
    ii=ii+1

num_p=trial.numerator - trial.denominator*( 2**(2*ii)-1 )//3
den_p=trial.denominator*( ( 2**(2*(ii+1))-1)//3-( 2**(2*(ii))-1)//3 )

phi=Fraction( num_p, den_p )


status=check( trial )

ct=0

while status :

    np=trial.numerator
    corr=1
    while np % 2 == 0 :
        np=np//2
        corr=corr*2
    np=trial.numerator*3+corr
    frp=Fraction( np, trial.denominator )
    trial=frp

    status=check( trial )
    corr=0
    np=trial.numerator
    while np % 2 == 0 :
        np=np//2
        corr=corr+1

    ii=0
    while trial.numerator//trial.denominator > (2**(2*(ii+1))-1)//3 :
        ii=ii+1

    num_p=trial.numerator - trial.denominator*( 2**(2*ii)-1 )//3
    den_p=trial.denominator*( ( 2**(2*(ii+1))-1)//3-( 2**(2*(ii))-1)//3 )

    phi=Fraction( num_p, den_p )

    
    ct=ct+1

r=ct

EVEN = ct % 2 == 0

i=0

if EVEN :
    while num/den > (1/3)*( 3**(-r)*2**( i+3*r/2 )-1 ) :
        i=i+1
    i=i-1

    l=r//2

    kn=3**r*(3*num+den)-2**(i+3*l)*den
    kd=den*2**(i+3*l)

    kappa=Fraction( kn, kd )

    print( kappa ) # print( '{} {}'.format( kappa.numerator, kappa.denominator ) )

else :
    while num/den > (1/3)*( 3**(-r)*2**( i+3*r/2-1/2 )-1 ) :
        i=i+1
    i=i-1

    q=( 3*r-1 )//2

    kn=3**r*(3*num+den)-den*2**(i+q)
    kd=den*2**(i+q)
 
    kappa=Fraction( kn, kd )

    print( kappa ) # print( '{} {}'.format( kappa.numerator, kappa.denominator ) )
