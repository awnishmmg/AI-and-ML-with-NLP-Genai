#wap in python to show Anonymous functions :-

def square(n):
    return n*n
    

def main():
    n = eval(input('Enter the no:'))
    result = square(n)
    print('Square of ',n,'is',result)
    

import sys
sys.exit(main())