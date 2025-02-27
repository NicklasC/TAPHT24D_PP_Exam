from random import Random





class Item:
    """Representerar saker man kan plocka upp."""

    def __init__(self, name, value=10, symbol="?",from_start=False):
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


def add_random_item(grid):
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            new_item = Random().choice(pickups)
            new_item.from_start = False
            grid.set(x, y, new_item)
            break

def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledigw
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
