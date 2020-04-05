class Person():
    def __init__(self, ID: int, name: str, phoneNumber: int):
        self.__ID = ID
        self.__name = name
        self.__phoneNumber = phoneNumber

    def setID(self, ID: int):
        self.__ID = ID

    def getID(self) -> int:
        return self.__ID

    def setName(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setPhoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

    def getPhoneNumber(self) -> int:
        return self.__phoneNumber

