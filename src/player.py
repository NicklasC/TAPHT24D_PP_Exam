from src.inventory import Inventory


class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.__inventory = Inventory()

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        potential_x = self.pos_x + x
        potential_y = self.pos_y + y
        if grid.get(potential_x, potential_y) == grid.wall and self.has_item("showel") == False:
            print("I cannot go there, there is a wall in the way!")
            return False
        elif grid.get(potential_x, potential_y) == grid.wall and self.has_item("showel") == True:
            #TODO: Ask PO about how this should be handled. Currently, passing outer walls can cause the program to
            # raise error. Should only the inner walls be passable? Should we raise a text saying "You cannot leave the grid" or similar?
            print("You ran into a wall, but use your showel to get through! It only works once though...")
            grid.clear(potential_x, potential_y)
            self.__inventory.remove("showel")
            return True
        else:
            return True

    def has_item(self, item):
        if self.__inventory.item_exists(item) == True:
            return True
        else:
            return False

    def remove_item(self, item):
        self.__inventory.remove(item)

    def add_item(self, item):
        self.__inventory.add(item)

    def inventory_is_empty(self):
        return self.__inventory.is_empty()

    def get_inventory_items(self):
        return self.__inventory.get_all_items()
