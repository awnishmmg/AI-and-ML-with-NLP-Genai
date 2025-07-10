#wap in python to find odd and even
#using return statement

no = eval(input('Enter the No:'))


def main():
    if(no%2==0): 
        print(f'{no} is Even')
        return 0
    print(f'{no} is Odd')
    
    
main()
    