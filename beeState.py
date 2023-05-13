import random

# COLORS
SITE_COLOR = '\033[96m'
NEST_COLOR = '\033[95m'
NORMAL_COLOR = '\033[0m'
RESTING_COLOR = '\033[94m'
EXPLORING_COLOR = '\033[92m'
VERIFYING_COLOR = '\033[93m'
DANCING_COLOR = '\033[91m'

danced_for_location = [1, 3]


class BeeAgent(object):
    def __init__(self, total_simulation_time=20, max_exploring_time=5, site_options=[[1, 3]]):
        self.state = "Resting"
        self.total_dance_time = 0
        self.dance_time_left = 0
        self.exploring_time_left = 0
        self.site_found = False
        self.location = [0, 0]
        self.max_exploring_time = max_exploring_time
        self.total_simulation_time = total_simulation_time
        self.site_options = site_options

    def bee_agent_info(self):
        return [self.state, self.total_dance_time, self.dance_time_left, self.exploring_time_left, self.site_found, self.location, self.max_exploring_time, self.total_simulation_time, self.site_options]

    # def state_function(self):
    #     for i in range(0, self.total_simulation_time):
    #         print(f"{self.total_simulation_time-i}")
    #         print(f"Current location: {self.location}")
    #         bee_location = [[self.location]]
    #         state = self.state
    #         if state == "Resting":
    #             self.resting()
    #         elif state == "Exploring":
    #             self.exploring()
    #         elif state == "Dancing":
    #             self.dancing()
    #         elif state == "Verifying":
    #             self.Verifying()
    #         else:
    #             print("Error: state not found")
    #             "Error"

    def resting(self):
        if self.convinced_by_dance():
            self.state = "Verifying"
            print(
                f"{VERIFYING_COLOR}I am convinced by the dance. I'm verifying their information")
            self.exploring_time_left = self.max_exploring_time
        elif self.decides_to_explore():  # (there is a 20% chance of going out exploring)
            self.state = "Exploring"
            self.exploring_time_left = self.max_exploring_time
            print(f"{EXPLORING_COLOR}I have decided to explore")
        else:
            self.state = "Resting"
            print(f"{RESTING_COLOR}I am still resting")

    def exploring(self):
        print(self.location[0])
        self.location = self.Exploring_tiles(
            self.location[0], self.location[1])
        self.location_site_checker()
        if self.site_found:
            self.exploring_time_left = 0
            print(f"{DANCING_COLOR}I found a site, I'm going to dance")
            self.location = [0, 0]
            self.state = "Dancing"
            self.start_dance(3)
        elif self.exploring_time_left-1 == 0:
            self.exploring_time_left = 0
            self.location = [0, 0]
            self.state = "Resting"
            print(
                f"{RESTING_COLOR}I didn't find anything but I'm tired so I'm done exploring")
        else:
            self.exploring_time_left -= 1
            self.state = "Exploring"
            print(
                f"{EXPLORING_COLOR}I am still exploring because I have {self.exploring_time_left} units of time left")

    def dancing(self):
        if self.total_dance_time == 0:
            self.state = "Resting"
            print(f"{RESTING_COLOR}I'm done dancing, I'm going to rest now")
        else:
            print(
                f"{DANCING_COLOR}I'm dancing. My dance still has {self.total_dance_time} time left")
            self.total_dance_time -= 1

    def Verifying(self):
        self.location_site_checker()
        self.location = self.Verifying_Path(
            self.location[0], self.location[1], danced_for_location)
        if self.site_found:
            print(f"{DANCING_COLOR}I found a site, I'm going to dance")
            self.location = [0, 0]
            self.start_dance(3)
            self.state = "Dancing"
        else:
            self.state = "Verifying"
            print(
                f"I am still going out to verify because I haven't reached the site yet")

        #####################
        # Helper Functions ##
        #####################

    def location_site_checker(self):
        if self.location in self.site_options:
            self.site_found = True

        else:
            self.site_found = False
        return self.location

    def Exploring_tiles(self, curr_x, curr_y):
        X_change = random.choice([-1, 0, 1])
        Y_change = random.choice([-1, 0, 1])
        if X_change == 0 and Y_change == 0:
            return self.Exploring_tiles(curr_x, curr_y)
        else:
            return [curr_x + X_change, curr_y + Y_change]

    def Verifying_Path(self, curr_x, curr_y, goal_site_coordinates):
        if curr_x < goal_site_coordinates[0]:
            X_change = 1
            Y_change = 0
        elif curr_y < goal_site_coordinates[1]:
            Y_change = 1
            X_change = 0
        elif curr_x > goal_site_coordinates[0]:
            X_change = -1
            Y_change = 0
        elif curr_y > goal_site_coordinates[1]:
            Y_change = 1
            X_change = 0
        else:
            Y_change = 0
            X_change = 0
        return [curr_x + X_change, curr_y + Y_change]

    def convinced_by_dance(self):
        if self.probability_convinced_by_dance() > 0.6:
            return True
        else:
            return False

    def decides_to_explore(self):
        if self.probability_resting_to_Exploring() > 0.4:
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


# BeeAgent().state_function()

# __    __    __
# /  \__/  \__/  \
# \__/  \__/  \__/
# /  \__/  \__/  \
# \__/  \__/  \__/
# /  \__/  \__/  \
# \__/  \__/  \__/
