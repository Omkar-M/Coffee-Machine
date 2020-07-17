class Lightbulb:
    def __init__(self):
        self.state = "off"

    # create method change_state here
    def change_state(self):
        if self.state == "off":
            self.state = 'on'
        else:
            self.state = 'off'
        print(f'Turning the light {self.state}')
