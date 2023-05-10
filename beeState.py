import random


class bcolors:
    RESTING_COLOR = '\033[94m'
    # PURPLE = '\033[95m'
    EXPLORING_COLOR = '\033[92m'
    # TEAL = '\033[96m'
    VERIFYING_COLOR = '\033[93m'
    DANCING_COLOR = '\033[91m'


max_exploring_time = 5
total_simulation_time = 20
site_options = [(-3, 0), (-2, 6), (-1, -2), (0, -2), (2, 3), (4, 0)]


class initialTerrain(object):
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.hexes = []
        for x in range(-x_max, x_max):
            for y in range(-y_max, y_max):
                self.hexes.append(hex(x, y))

    def get_hex_list(self):
        return self.hexes


class BeeAgent(object):
    def __init__(self):
        self.state = "Resting"
        self.total_dance_time = 0
        self.dance_time_left = 0
        self.exploring_time_left = 0
        self.site_found = False
        self.location = [0, 0]

    def state_function(self):
        for i in range(0, total_simulation_time):
            print(f"{total_simulation_time-i}")
            state = self.state
            if state == "Resting":
                self.resting()
            elif state == "Exploring":
                self.exploring()
            elif state == "Dancing":
                self.dancing()
            elif state == "Verifying":
                self.Verifying()
            else:
                print("Error: state not found")
                "Error"

    def resting(self):
        if self.convinced_by_dance():
            self.state = "Verifying"
            print(
                f"{bcolors.VERIFYING_COLOR}I am convinced by the dance. I'm verifying their information")
            self.exploring_time_left = max_exploring_time
        elif self.decides_to_explore():  # (there is a 20% chance of going out exploring)
            self.state = "Exploring"
            self.exploring_time_left = max_exploring_time
            print(f"{bcolors.EXPLORING_COLOR}I have decided to explore")
        else:
            self.state = "Resting"
            print(f"{bcolors.RESTING_COLOR}I am still resting")

    def exploring(self):
        self.search_for_site()
        if self.site_found:
            self.exploring_time_left = 0
            print(f"{bcolors.DANCING_COLOR}I found a site, I'm going to dance")
            self.location = [0, 0]
            self.state = "Dancing"
            self.start_dance(3)
        elif self.exploring_time_left-1 == 0:
            self.exploring_time_left = 0
            self.state = "Resting"
            print(
                f"{bcolors.RESTING_COLOR}I didn't find anything but I'm tired so I'm done exploring")
        else:
            self.exploring_time_left -= 1
            self.state = "Exploring"
            print(
                f"{bcolors.EXPLORING_COLOR}I am still exploring because I have {self.exploring_time_left} units of time left")

    def dancing(self):
        if self.total_dance_time == 0:
            self.state = "Resting"
            print(f"{bcolors.RESTING_COLOR}I'm done dancing, I'm going to rest now")
        else:
            print(
                f"{bcolors.DANCING_COLOR}I'm dancing. My dance still has {self.total_dance_time} time left")
            self.total_dance_time -= 1

    def Verifying(self):
        if self.site_found:
            self.exploring_time_left = 0
            print(f"{bcolors.DANCING_COLOR}I found a site, I'm going to dance")
            self.start_dance(3)
            self.state = "Dancing"
        elif self.exploring_time_left == 0:
            self.state = "Resting"
            print(
                f"{bcolors.RESTING_COLOR}I didn't find the site but I'm tired so I'm done verifying")
        else:
            self.exploring_time_left -= 1
            self.state = "Verifying"
            print(
                f"I am still going out to verify because I have {self.exploring_time_left} units of time left")

        #####################
        # Helper Functions ##
        #####################

    def search_for_site(self):
        new_position = Exploring_tiles(self.location[0], self.location[1])
        if tuple(new_position) in site_options:
            self.site_found = True
        else:
            self.site_found = False

    def convinced_by_dance(self):
        if self.probability_convinced_by_dance() > 0.6:
            return True
        else:
            return False

    def decides_to_explore(self):
        if self.probability_resting_to_Exploring() > 0.8:
            return True
        else:
            return False

    def probability_convinced_by_dance(self):
        return random.randrange(1, 11, 1)/10

    def probability_resting_to_Exploring(self):
        return random.randrange(1, 11, 1)/10

    def start_dance(self, site_goodness):
        self.dance_time_left = site_goodness
        self.total_dance_time = site_goodness


# BeeAgent().state_function()


class hex(object):
    def __init__(self, X_distance_from_center, Y_distance_from_center):
        self.X_distance_from_center = X_distance_from_center
        self.Y_distance_from_center = Y_distance_from_center
        self.contians_potential_site = False

    def make_site(self, site_goodness, prob_of_finding):
        return Site(site_goodness, prob_of_finding, self.X_distance_from_center, self.Y_distance_from_center)


class Site(object):
    def __init__(self, site_goodness, prob_of_finding, X_distance_from_center, Y_distance_from_center):
        self.site_goodness = site_goodness
        self.prob_of_finding = prob_of_finding
        self.X_distance_from_center = X_distance_from_center
        self.Y_distance_from_center = Y_distance_from_center


def Exploring_tiles(curr_x, curr_y):
    X_change = random.choice([-1, 0, 1])
    Y_change = random.choice([-1, 0, 1])
    if X_change == 0 and Y_change == 0:
        return Exploring_tiles(curr_x, curr_y)
    else:
        return (curr_x + X_change, curr_y + Y_change)

    # __    __    __
    # /  \__/  \__/  \
    # \__/  \__/  \__/
    # /  \__/  \__/  \
    # \__/  \__/  \__/
    # /  \__/  \__/  \
    # \__/  \__/  \__/
