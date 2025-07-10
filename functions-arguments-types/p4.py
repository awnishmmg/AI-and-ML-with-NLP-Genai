#wap in python to keyword argument in python 

def add(x,y,z): #Argument Length: 3
    print('x=',x)
    print('y=',y)
    print('z=',z)
    return x+y+z
    
def main():
    result = add(10,20,30,40) #10->x, 20->y,30->z
    print('Result = ',result)
    
    result = add(x=10,y=20,z=30) #10->x, 20->y,30->z
    print('Result = ',result)
    
    result = add(20,10,30) #20->x, 10->y,30->z
    print('Result = ',result)
    
    result = add(z=30,y=20,x=10) #10->x, 20->y,30->z
    print('Result = ',result)
    
import sys
sys.exit(main())

    
