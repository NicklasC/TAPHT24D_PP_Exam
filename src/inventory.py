class Inventory:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def get_all_items(self):
        return self.__items

    def get_items_count(self):
        return len(self.__items)

    def is_empty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
