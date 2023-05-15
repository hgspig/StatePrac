import SiteChoicesFile

# COLORS
SITE_COLOR = '\033[96m'
NEST_COLOR = '\033[95m'
NORMAL_COLOR = '\033[0m'
RESTING_COLOR = '\033[94m'
EXPLORING_COLOR = '\033[92m'
VERIFYING_COLOR = '\033[93m'
DANCING_COLOR = '\033[91m'


class initialTerrain(object):
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.hexes = []
        for x in range(x_max, -x_max, -1):
            for y in range(-y_max, y_max):
                self.hexes.append(hex(x, y))

    def get_hex_list(self):
        return self.hexes


def create_world(x_dimension, y_dimension, bee_location_list=[], site_options_coordinates=[]):
    row_gap = "   "
    # hex_list = initialTerrain(x_dimension, y_dimension).get_hex_list()
    y_stager = False
    for y in range(y_dimension//2, -(y_dimension//2), -1):
        for x in range(-x_dimension//2, (x_dimension//2)):
            if [x, y] in bee_location_list:
                print(f"{DANCING_COLOR}{x},{y}", end=row_gap)
            elif [x, y] in site_options_coordinates:
                print(f"{SITE_COLOR}S", end=row_gap)
            elif [x, y] == [0, 0]:
                print(f"{NEST_COLOR}C", end=row_gap)
            elif [x, y] == [-5, 5]:
                print(f"{NEST_COLOR}E", end=row_gap)
            elif [x, y] == [4, -4]:
                print(f"{NEST_COLOR}E", end=row_gap)
            else:
                print(f"{NORMAL_COLOR}:", end=row_gap)
        print()
        print()
        if y_stager == False:
            print("  ", end="")
            y_stager = True
        else:
            y_stager = False
