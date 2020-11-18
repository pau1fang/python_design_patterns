class Knight(object):
    def __init__(self, level):
        self.unit_type = "Knight"
        if level == 1:
            self.life = 400
            self.speed = 5
            self.attack_power = 3
            self.attack_range = 1
            self.weapon = "short sword"

        elif level == 2:
            self.life = 450
            self.speed = 6
            self.attack_power = 5
            self.attack_range = 3
            self.weapon = "long sword"

    def __str__(self):
        return "Life: {0}\n" \
               "Speed: {1}\n" \
               "Attack Power: {2}\n" \
               "Attack Range: {3}\n" \
               "Weapon: {4}" \
               "Type: {5}".format(
                self.life,
                self.speed,
                self.attack_power,
                self.attack_range,
                self.weapon,
                self.unit_type
                )


class Archer(object):
    def __init__(self, level):
        self.unit_type = "Archer"
        if level == 1:
            self.life = 200
            self.speed = 7
            self.attack_power = 1
            self.attack_range = 5
            self.weapon = "short bow"

        elif level == 2:
            self.life = 200
            self.speed = 7
            self.attack_power = 3
            self.attack_range = 10
            self.weapon = "long bow"

    def __str__(self):
        return "Life: {0}\n" \
               "Speed: {1}\n" \
               "Attack Power: {2}\n" \
               "Attack Range: {3}\n" \
               "Weapon: {4}" \
               "Type: {5}".format(self.life,
                                  self.speed,
                                  self.attack_power,
                                  self.attack_range,
                                  self.weapon,
                                  self.unit_type)


class Barracks(object):
    def build_unit(self, unit_type, level):
        if unit_type == "knight":
            return Knight(level)
        elif unit_type == "archer":
            return Archer(level)


if __name__ == '__main__':
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    archer1 = barracks.build_unit("archer", 2)
    print("[knight1] {}".format(knight1))
    print("[archer1] {}".format(archer1))
