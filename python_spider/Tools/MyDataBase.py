import pymysql

class MyDataBase:
    def __init__(self):
        print("connect to data base......")
        self.db = pymysql.connect("localhost","root","053062","python_spider" )
        self.cursor = self.db.cursor()
        print("connect success!")

    def getConn(self):
        return self.db

    def getExcuter(self):
        return self.cursor

    def close(self):
        self.cursor.close()
        self.db.close()


if __name__=='__main__':
    print("a module used to connect db")