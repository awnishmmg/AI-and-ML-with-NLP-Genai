#wap in python to show the Indentation Blocks 

def main():
    print('Line 1')
    print('Line 2')
    print('Line 3')
    if True:
        print('\tLine 4')
        if True:
            print('\t\tLine 5') #2 Tabbed Space
            print('\t\tLine 6') #2 Tabbed Space
        print('\tLine 7')
print('Line 8')



main()
