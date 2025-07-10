#wap in python make power function using default argument.

def power(base,exp=2):
    return base**exp
    
    
def main():
    print('Result :',power(3)) #9
    print('Result :',power(3,1)) #3
    print('Result :',power(3,3)) #27
    print('Result :',power(3,4)) #81

import sys
sys.exit(main())



    
    
    