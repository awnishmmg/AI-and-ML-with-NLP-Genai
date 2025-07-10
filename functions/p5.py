#wap in python to no argument and with return type 


def getConnection(): #No Argument 
    class Db:
        def __init__(self,db_host,db_user,db_pass,db_name):
            self.db_host = db_host
            self.db_user = db_user
            self.db_pass = db_pass
            self.db_name = db_name
         
        def connect(self):
            print('connection success')
     
    return Db('localhost','root','1234','mydb')
    

def main():
    db = getConnection()
    print(db)
    db.connect() #connection success
import sys 
sys.exit(main())




