#!/Users/zabby/anaconda3/bin/python 

import sys

### Provides path for odd integer x
### Usage :
### ./collatz.py x

sys.setrecursionlimit(100000)

def lothar(arg,count) :
    counter=int(count)
    if arg%2 is 0 :
        arg=arg//2
        return lothar(int(arg),int(counter))
    else :
        if arg is not 1 :
            print('{}'.format(arg))
            arg=arg*3+1
            return lothar(int(arg),int(counter+1))
        else :
            return counter-1

print('{} r:{}'.format( sys.argv[1], int(lothar(int(sys.argv[1]),0)) ))
