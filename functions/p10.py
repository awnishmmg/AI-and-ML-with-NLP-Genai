#wap in python to show return tuple

def getMultiple():
    return 10,20 
    

def main():
   t = getMultiple()
   print('value of tuples :',t)
   print(type(getMultiple())) #<class 'tuple'>

import sys 
sys.exit(main())
