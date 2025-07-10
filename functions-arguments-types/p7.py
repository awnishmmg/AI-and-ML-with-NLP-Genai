#wap in python to show *args and **args 


def f(*t,**d):
    print(t)
    print('type of the *t:',type(t))
    print(d)
    print('type of the **d:',type(d))
    
    print(d.keys())
    print(d.values())
    
     
def main():
    f()
    f(10)
    f(10,20,30)
    f(name='Ravi',age=30)
    f(10,20,30,name='Ravi',age=30)
    
import sys 
sys.exit(main())