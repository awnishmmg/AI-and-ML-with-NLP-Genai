#wap in python to show default argument

def sayHello(message='Welcome'): #default argument
    print('Hello,',message)
    
    
def main():
    sayHello() # No value Pass
    sayHello('Good Evening') #value -> Message
    
import sys
sys.exit(main())



    
    
    