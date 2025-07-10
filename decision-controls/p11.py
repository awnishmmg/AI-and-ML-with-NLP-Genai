#wap in python to find odd and even
#using dictionary

no = eval(input('Enter the No:'))
dictionary = {0:'Even',1:'Odd'}

#remainder 1 -> Odd 
#remainder 0 -> Even

index = rem = no%2
print(f'using [] {no} is {dictionary.get(index)}')
print(f'using get,{no} is {dictionary[index]}')

        
       