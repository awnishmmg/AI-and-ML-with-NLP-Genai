#wap in python to concept of call by Reference: mu-mutability

def change(l):
    l.append(10)
    print('The value of list inside :',l)
    print('The length of the list inside :',len(l))
    print('the id of l inside :',id(l))
    
l=[10,20,30]
print('the id of l outiside :',id(l))
print('The value of list outside:',l)
change(l)
print('The value of list outside:',l)
print('the id of l outiside :',id(l))
print('The length of the list outside:',len(l))