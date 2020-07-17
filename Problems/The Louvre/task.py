class Painting:
    def __init__(self, title1, artist1, year1):
        self.title = title1
        self.artist = artist1
        self.year = year1

    def print_value(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.')


title, artist, year = [input() for x in range(3)]
painting = Painting(title, artist, year)
painting.print_value()
