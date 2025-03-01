from .grid import Grid
from .player import Player
from . import pickups

score = 0
number_of_turns = 0
inventory = []

g = Grid()
player = Player(g.width // 2, g.height // 2)
g.set_player(player)
g.make_outer_walls()
g.make_vertical_wall1()
g.make_horizontal_wall1()
pickups.place_initial_pickups(g)

command = "a"


def apply_floor_is_lava(score):
    return score - 1


# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    g.print_status(score)

    command = input(f"Use WASD to move, I for inventory, Q/X to quit. Turn number:{number_of_turns}")
    command = command.casefold()[:1]

    player_moved = False
    maybe_item = None

    if command == "w" and player.can_move(0, -1, g):  # move up
        maybe_item = g.get(player.pos_x, player.pos_y - 1)
        player.move(0, -1)
        player_moved = True
        score = apply_floor_is_lava(score)
        number_of_turns += 1

    if command == "s" and player.can_move(0, +1, g):  # move down
        maybe_item = g.get(player.pos_x, player.pos_y + 1)
        player.move(0, +1)
        player_moved = True
        score = apply_floor_is_lava(score)
        number_of_turns += 1

    if command == "a" and player.can_move(-1, 0, g):  # move left
        maybe_item = g.get(player.pos_x - 1, player.pos_y)
        player.move(-1, 0)
        player_moved = True
        score = apply_floor_is_lava(score)
        number_of_turns += 1

    if command == "d" and player.can_move(1, 0, g):  # move right
        maybe_item = g.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0)
        player_moved = True
        score = apply_floor_is_lava(score)
        number_of_turns += 1

    if command == "i":
        if player.inventory_is_empty():
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in player.get_inventory_items():
                print(f"- {item}")

    if isinstance(maybe_item, pickups.Item):
        # we found something

        if maybe_item.name == "trap":
            print(f"You stepped on a trap! You lost {maybe_item.value} points.")
        elif maybe_item.name == "showel":
            print(f"You found a showel! You can use it go through a wall..")
            g.clear(player.pos_x, player.pos_y)
            player.add_item(maybe_item.name)
        elif maybe_item.name == "key":
            print(f"You found a key! Now if there are any chests around...")
            g.clear(player.pos_x, player.pos_y)
            player.add_item(maybe_item.name)
        elif maybe_item.name == "treasure" and player.has_key():
            print("You found a treasure! You use your key and unlock it... and find a lot of goodies!")
            g.clear(player.pos_x, player.pos_y)
            player.add_item(maybe_item.name)
            player.remove_item("key")
            score += maybe_item.value
        elif maybe_item.name == "treasure" and player.has_key()==False:
            print("You found a treasure! But you also need a key... get back here when you find it.")
        else:
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            g.clear(player.pos_x, player.pos_y)
            # Add item to inventory
            player.add_item(maybe_item.name)
    if number_of_turns > 0 and number_of_turns % 25 == 0 and command != "i":
        print(f"You have played for {number_of_turns} turns... and a new item emerges!")
        pickups.add_random_item(g,"fruit_or_vegetable")
        #pickups.add_random_fruit_or_vegetable(g)
# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
