#wap in python to show the demo of the logical operator's

papa = False
mama = False 

print('<=============| cases of the And |=============>')
print(f' papa and mumma : {0 and 0}')
print(f' papa and mumma : {0 and 1}')
print(f' papa and mumma : {1 and 0}')
print(f' papa and mumma : {1 and 1}')

print(' papa and mumma : ',(papa and mama))         #false 
print(' papa and mumma : ',(papa and not mama))     #false 
print(' papa and mumma : ',(not papa and mama)) #false 
print(' papa and mumma : ',(not papa and not mama)) #True 

print('<=============| cases of the or |=============>')
print(f' papa and mumma : {0 or 0}') #0 
print(f' papa and mumma : {0 or 1}') #1
print(f' papa and mumma : {1 or 0}') #1
print(f' papa and mumma : {1 or 1}') #1

print(' papa and mumma : ',(papa or mama)) #False 
print(' papa and mumma : ',(papa or not mama)) #True 
print(' papa and mumma : ',(not papa or mama)) #True 
print(' papa and mumma : ',(not papa or not mama)) #True

# mumkin Na mumkin and na mumkin ko mumkin
print(False)
print(not False) #true
print(True)#
print(not True)#


