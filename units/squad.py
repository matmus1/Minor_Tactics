class Squad:

    def __init__(self, name, faction, position):

        self.name = name
        self.faction = faction

        self.position = position

        self.size = 10

        self.morale = 100

        self.suppression = 0

        self.ammunition = 100

        self.order = "hold"


    def update(self):

        # Future squad logic:
        # - movement
        # - combat behavior
        # - morale changes
        # - orders

        pass


    def take_suppression(self, amount):

        self.suppression += amount

        if self.suppression > 100:
            self.suppression = 100


    def reduce_morale(self, amount):

        self.morale -= amount

        if self.morale < 0:
            self.morale = 0


    def is_alive(self):

        return self.size > 0
