# our class Ship
class Ship:
    def __init__(self, name, capacity, place1):
        self.name = name
        self.capacity = capacity
        self.place = place1
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self):
        return f"The {self.name} has sailed for {self.place}!"


place = input()
black_pearl = Ship("Black Pearl", 800, place)
print(black_pearl.sail())
