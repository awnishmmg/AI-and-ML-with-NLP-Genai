#wap in python to with argument and no return type 


def add(x,y): #with Argument 
    print('Result by add :',(x+y))
    #No Return 
    

def main():
    x = eval(input('Enter the x value:'))
    y = eval(input('Enter the y value:'))
    add(x,y)

import sys 
sys.exit(main())

