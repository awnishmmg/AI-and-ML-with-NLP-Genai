#wap in python to show string to string operation

x=input('Enter the x value:')
y=input('Enter the y value:')

print('type of x:',type(x)) #<class 'str'>
print('value of x:',x)
print('type of y:',type(y)) #<class 'str'>
print('value of y:',y)

result = x+y 
print('type of result:',type(result))
print('value of result:',result)

#type conversion str -> int
a=int(x)
b=int(y)
print('value of a:',a) #10
print('value of b:',b) #20
print('type of a:',type(a)) #<class 'int'>
print('type of b:',type(b))  #<class 'int'>

result2 = a+b 
print('value of result2:',result2) #30
print('type of result2:',type(result2)) #<class 'int'>



