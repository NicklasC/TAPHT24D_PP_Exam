class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

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
        if grid.get(potential_x, potential_y) == grid.wall:
            print("I cannot go there, there is a wall in the way!")
            return False
        else:
            return True
