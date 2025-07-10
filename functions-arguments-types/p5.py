#wap in python to variable length or dyanic Argument.

def add(*arg): #Argument Length: 3
    print('Argument value :',arg)
    print('length of argument :',len(arg))
       
def main():
    add(10) #1
    add(10,20) #2
    add(10,20,30) #3
    add(10,20,30,40,50) #5
import sys
sys.exit(main())

    
