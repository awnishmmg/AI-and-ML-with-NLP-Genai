#wap in python to show collection datatypes 

name = 'Awnish' #string datatype : collection
print(name)
print(type(name)) #<class 'str'>
print(len(name)) #string is collection of character.


arr = [10,20,30,40]  #homogenous : same type 
print(arr)
print(type(arr))  #<class 'list'>
print(len(arr))

elements = [10,20.5,True,["Apple","Orange"],(10,20,30),"ravi"]  #hetrogenous list : different type 
print(elements)
print(type(elements))  #<class 'list'>
print(len(elements))

t = (10,20,30,'awnish') #hetrogenous 
print(t)
print(type(t))  #<class 'tuple'>
print(len(t))


s = {10,20,20,30,30} #sets : duplicates not allowed
print(s)
print(type(s))  #<class 'set'>
print(len(s))

s = {10,20,20,30,30} #sets : duplicates not allowed
fs = frozenset(s)
print(fs)
print(type(fs))  #<class 'frozenset'>
print(len(fs))

#range dataType 
rng = range(5)
print(rng)
print(type(rng))  #<class 'range'>
print(len(rng))

lst = list(range(5)) #[0,1,2,3,4] #frozenset (readonly)
print(lst)
print(type(lst))  #<class 'list'>
print(len(lst))

users  = {'name':'ravi','class':'Btech','age':20}  #key value pairs 
print(users)
print(type(users))  #<class 'dict'>
print(len(users))

users  = {0:'ravi',1:'Btech',2:20}  #key value pairs 
print(users)
print(type(users))  #<class 'dict'>
print(len(users))

users  = {None:'ravi',1:'Btech',2:20}  #key value pairs 
print(users)
print(type(users))  #<class 'dict'>
print(len(users))

dataType  = {None:'ravi',1:'Btech',20.5:20,list:'list',True:'boolean'}  #key value pairs 
print(dataType)
print(type(dataType))  #<class 'dict'>
print(len(dataType))




