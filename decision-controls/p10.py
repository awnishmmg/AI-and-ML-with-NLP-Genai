#wap in python to find odd and even
#using List 

no = eval(input('Enter the No:'))
output = ['Even','Odd']

#remainder 1 -> Odd 
#remainder 0 -> Even

index = rem = no%2
print(f' {no} is {output[index]}')

        
       