#wap in python to no argument and with return type 

def pi(): #No Argument 
    return 3.14 #return 
    

def main():

    radius = eval(input('Enter the Radius'))
    area = pi()*radius**2
    print('The Area of circle:',area)
    
    
import sys 
sys.exit(main())




