from .grid import Grid
from .player import Player
from . import pickups

score = 0
inventory = []

g = Grid()
player = Player(g.width // 2, g.height // 2)
g.set_player(player)
g.make_walls()
pickups.randomize(g)

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    g.print_status(score)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    player_moved = False
    maybe_item = None

    if command == "w" and player.can_move(0, -1, g):  # move up
        maybe_item = g.get(player.pos_x, player.pos_y - 1)
        player.move(0, -1)
        player_moved = True

    if command == "s" and player.can_move(0, +1, g):  # move down
        maybe_item = g.get(player.pos_x, player.pos_y + 1)
        player.move(0, +1)
        player_moved = True

    if command == "a" and player.can_move(-1, 0, g):  # move left
        maybe_item = g.get(player.pos_x - 1, player.pos_y)
        player.move(-1, 0)
        player_moved = True

    if command == "d" and player.can_move(1, 0, g):  # move right
        maybe_item = g.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0)
        player_moved = True

    if isinstance(maybe_item, pickups.Item):
        # we found something
        score += maybe_item.value
        print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
        # g.set(player.pos_x, player.pos_y, g.empty)
        g.clear(player.pos_x, player.pos_y)

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
