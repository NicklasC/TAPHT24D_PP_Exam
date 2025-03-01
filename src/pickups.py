from random import Random
from venv import create


class Item:
    """Representerar saker man kan plocka upp."""

    def __init__(self, name, value=10, symbol="?", from_start=False):
        self.name = name
        self.value = value
        self.symbol = symbol
        self.from_start = from_start

        if self.name in {'apple', 'strawberry', 'watermelon'}:
            self.value = 20
        if self.name == 'trap':
            self.value = -10
        if self.name == 'treasure':
            self.value = 100

    def __str__(self):
        return self.symbol


def set_initial_pickups():
    item_names = [
        "carrot", "apple", "strawberry", "cherry", "watermelon",
        "radish", "cucumber", "meatball", "trap", "showel", "key", "treasure"
    ]
    return [Item(name, from_start=True) for name in item_names]


pickups = set_initial_pickups()


def create_random_fruit_or_vegetable():
    item_names = "carrot", "apple", "strawberry", "cherry", "watermelon", "radish", "cucumber"
    return Item(Random().choice(item_names))


def number_of_initial_pickups():
    # Variable below is needed in order to enable Exits
    return len(pickups) - 1  # -1 for trap


def create_exit():
    return Item("exit", symbol="E")


def is_original_item(item):
    return item.from_start


def add_random_item(grid, item_type):
    x, y = get_empty_random_coordinates(grid)
    if item_type == "fruit_or_vegetable":
        item = create_random_fruit_or_vegetable()
    elif item_type == "exit":
        item = create_exit()
    else:
        raise ValueError(f"function add_random_item: Item '{item_type}' not implemented.. exiting program")
    grid.set(x, y, item)


def get_empty_random_coordinates(grid):
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            return x, y


# Refactored initial randomize. Created get_empty_random_coordinates instead as that functionality was needed in add_random_item.
def place_initial_pickups(grid):
    for item in pickups:
        x, y = get_empty_random_coordinates(grid)
        grid.set(x, y, item)
