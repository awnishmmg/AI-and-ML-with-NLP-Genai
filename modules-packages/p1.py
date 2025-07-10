#wap in python to show the demo of the module 

#class 
class Test:
    def sayHello(self):
        print('This is sayHello method from Test Class')
        
        
#functions 
def welcome(message):
    print(message)
    
name = 'Awnish'
age = 27
hobbies = ['reading','riding','playing']

if __name__ == "__main__":  
    print('from p1.py This code will be when directly executed')
    print('from p1.py :',name)
    print('from p1.py :',age)
    print('from p1.py',hobbies)
    test = Test()
    test.sayHello()

