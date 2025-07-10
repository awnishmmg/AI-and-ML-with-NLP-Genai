#wap in python to variable length or dyanic Argument.

def add(*arg): #Argument Length: 3
    total = 0 
    for i in arg:
        total = total + int(i)
    return total
       
def main():
    print('result :',add(10)) #10
    print('result :',add(10,20)) #30
    print('result :',add(10,20,30)) #60
    print('result :',add(10,20,30,40,50)) #150
import sys
sys.exit(main())

    
