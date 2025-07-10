#wap in python to show keywords list 

import keyword as k 
keywords = k.kwlist
n = input('Enter the column:')

print(f' No of keyword :{len(keywords)}')
print(f'============== Keywords List ===================')

counter = 0

for kw in keywords:
    if counter == n:
        print()
        counter=0
    else:
        print(kw,'\t',end='')
        counter=counter+1
        