class Inventory:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def remove(self, item):
        self.__items.remove(item)

    def get_all_items(self):
        return self.__items

    def get_items_count(self):
        return len(self.__items)

    def item_exists(self, item):
        if item in self.__items:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
