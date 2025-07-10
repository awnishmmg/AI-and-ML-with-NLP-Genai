#wap in python to with argument and with return type 


def add(x,y): #with Argument 
    return x+y #return 
    

def main():
    x = eval(input('Enter the x value:'))
    y = eval(input('Enter the y value:'))
    result = add(x,y)
    print('The Addition :',result)

import sys 
sys.exit(main())

