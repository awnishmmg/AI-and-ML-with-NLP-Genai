#wap in python return multiple values as collection (tuple,list,dict,set,frozen set,range)

def getAdmin():
    return {
        'id':10001,
        'active':True,
        'is_admin':True,
        'role':'super_user',
        'email_id':'admin@gmail.com'
    }
    
def main():
   for k,v in getAdmin().items():
        print(f'{k} => {v}')

import sys 
sys.exit(main())

