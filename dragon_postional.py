class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if (self.pos_x >= x_1 and self.pos_x <= x_2 and
            self.pos_y >= y_1 and self.pos_y <= y_2):
            return True
        else:
            return False

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_units = []
        x_min = x - self.__fire_range
        x_max = x + self.__fire_range
        y_min = y - self.__fire_range
        y_max = y + self.__fire_range

        for unit in units:
            if unit.in_area(x_min, y_min, x_max, y_max):
                hit_units.append(unit)

        return hit_units
