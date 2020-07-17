class Sphere:
    # finish class Sphere here
    pi = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = 4 / 3 * Sphere.pi * self.radius ** 3
