#wap in python to show Anonymous functions :-

square = lambda n:n*n #Anonymous or lambda or inline function.

add = lambda a,b:a+b

def main():
    n = eval(input('Enter the no:'))
    result = square(n)
    print('Square of ',n,'is',result)
    a = eval(input('Enter the a value:'))
    b = eval(input('Enter the b value:'))
    result = add(a,b)
    print('Addition of a+b :',result)
    

import sys
sys.exit(main())