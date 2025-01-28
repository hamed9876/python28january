


class Database : 

    instance = None

    def __init__(self):
        if Database.instance is not None :
            raise ValueError("The instanse already exsit !.")
        else :
            Database.instance = self

    @classmethod
    def getInstance(cls):
        if cls.instance is None :
            cls.instance = cls()
        return cls.instance

db1 = Database.getInstance()
db2 = Database.getInstance()
print(db1 is db2, db1,db2)