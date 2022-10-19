from SortedList import SortedList

class SymbolTable:
    def __init__(self):
        self.__sortedList = SortedList()

    def add(self, value):
        return self.__sortedList.add(value)

    def get(self, value):
        return self.__sortedList.getId(value)
