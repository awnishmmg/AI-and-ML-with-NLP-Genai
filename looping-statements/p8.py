#wap in python to Iterate using dictionary
d =  {'name':'Ravi','age':20,'salary':5000.50,'id':False}

#values
for v in d.values():
    print(v)
    
#keys
for k in d.keys():
    print(k)
    
#keys and values 
for k,v in d.items(): #tuple inside list
    print('keys:',k,'values:',v)
    
#keys and values 
for [k,v] in d.items(): #tuple inside list
    print('keys:',k,'values:',v)
    