class Person:
    # Singletone
    __instance = None
    def __new__(cls, *args, **kwgs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    # Конструктор
    def __init__(self, name):
        self.name = name
    
    # Метод выводящий имя объекта класса Person
    def Print(self):
        print(self.name)