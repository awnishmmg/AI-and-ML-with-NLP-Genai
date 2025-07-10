#wap in python to show dynamic type casting

x=input('Enter any value:')
print('--------without typecasting---------')
print('type of x:',type(x)) #<class 'str'>
dynamic_x = eval(x)
print('type of dynamic_x:',type(dynamic_x))
