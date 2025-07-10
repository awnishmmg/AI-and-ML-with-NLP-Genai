#wap in python to concept of call by value : im-mutability


def change(x):
    x=x+1
    print('x value inside:',x)
    print('id of x inside: ',id(x))
    
    
x=10
print('id of 10 outside:',id(10))
print('id of x outside:',id(x))
change(x)
print('value of x outside:',x)
print('id of 10 outside:',id(10))
print('id of x outside:',id(x))