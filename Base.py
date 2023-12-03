import sqlite3

class PlanetsDB:
    def __init__(self, connect: sqlite3.Connection) -> None:
        self.__connect = connect
        self.__cursor = connect.cursor()
    def getAllPlanets(self):
        sql = "SELECT name, destination, price, image, id FROM planets"
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except:
            print("ошибка чтения из базы данных")
            return []
        
    def getPlanet(self, id):
        sql = "SELECT * FROM planets WHERE id = ?"
        self.__cursor.execute(sql, tuple([id]))
        return self.__cursor.fetchone()
        
    def getCountPlanets(self):
        sql = "SELECT COUNT(id) FROM planets"
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except:
            print("ошибка чтения из базы данных")
            return []
        
    # def addPlanets(self, name:str, price:int, dest:str, image:str):
    #     sql = "INSERT INTO products(name, price, destination, image) VALUES (?, ?, ?, ?)"
    #     try:
    #         self.__cursor.execute(sql, tuple([name, price, dest, image]))
    #         self.__connect.commit()
    #         return True
    #     except:
    #         print("ошибка добавления данных")
    #         return False