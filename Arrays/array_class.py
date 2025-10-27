from typing import Any


class Array:

    def __init__(self):
        self.__array = []
        self.__items_num = 0

    def __len__(self):
        return self.__items_num

    def get(self, n: int) -> Any | None:
        if 0 <= n <= self.__items_num:
            return self.__array[n]
        return None

    def set(self, n: int, item: Any) -> None:
        if 0 <= n <= self.__items_num:
            self.__array[n] = item

    def insert(self, item: Any) -> None:
        self.__array[self.__items_num] = item
        self.__items_num += 1

    def find(self, item: Any) -> Any|None:
        for i in range(self.__items_num):
            if self.__array[i] == item:
                return i
        return None

    def search(self, item: Any) -> Any | None:
        return self.get(self.find(item=item))

    def delete(self, item: Any) -> bool:
        for i in range(self.__items_num):
            if self.__array[i] == item:
                self.__items_num -= 1
                for k in range(i, self.__items_num):
                    self.__array[k] = self.__array[k + 1]
                return True
        return False

    def traverse(self, function=print) -> Any:
        for i in range(self.__items_num):
            function(self.__array[i])