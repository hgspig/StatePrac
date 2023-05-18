import random
import beeInfo
import math
from matplotlib import pyplot as plt
import matplotlib
import math

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
    def __init__(self, total_simulation_time=20, max_exploring_time=5, site_options=[[1, 3]], current_angle=random.randrange(0, 360, 1)):
        self.state = "Resting"
        self.total_dance_time = 0
        self.dance_time_left = 0
        self.exploring_time_left = 0
        self.site_found = False
        self.location = [0, 0]
        self.max_exploring_time = max_exploring_time
        self.total_simulation_time = total_simulation_time
        self.site_options = site_options
        self.move_radius = 1
        self.optimal_x = math.sqrt((self.move_radius**2)/2)
        self.optimal_y = math.sqrt((self.move_radius**2)/2)
        self.current_angle = 0
        self.time_left_verifying = 0

    def bee_agent_info(self):
        return [self.state, self.total_dance_time, self.dance_time_left, self.exploring_time_left, self.site_found, self.location, self.max_exploring_time, self.total_simulation_time, self.site_options]

    def resting(self):
        print(f"{RESTING_COLOR}I am resting")
        if self.convinced_by_dance():
            self.state = "Going_To_Verify"
            print(
                f"{VERIFYING_COLOR}    I am convinced by the dance. I'm verifying their information")
            self.exploring_time_left = self.max_exploring_time
        elif self.decides_to_explore():  # (there is a 20% chance of going out exploring)
            self.state = "Exploring"
            self.exploring_time_left = self.max_exploring_time
            print(f"{EXPLORING_COLOR}    I have decided to explore")
        else:
            self.state = "Resting"
            print(f"{RESTING_COLOR}    I am still resting")

    def exploring(self):
        print(f"{EXPLORING_COLOR}I am still exploring because I have {self.exploring_time_left} units of time left")
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
            self.state = "Returning_From_Exploring"
            print(
                f"{RESTING_COLOR}I didn't find anything but I'm tired so I'm done exploring")
        else:
            self.exploring_time_left -= 1
            self.state = "Exploring"

    def dancing(self):
        print(
            f"{DANCING_COLOR}I'm dancing. My dance still has {self.total_dance_time} time left")
        if self.total_dance_time == 0:
            self.state = "Resting"
        else:
            self.total_dance_time -= 1

    def Verifying(self):
        if self.time_left_verifying == 0:
            self.state = "Returning_From_Verifying"
        else:
            self.time_left_verifying -= 1
            self.state = "Verifying"
            print(
                f"I am still verifying the site because I have {self.time_left_verifying} units of time left")

    def Returning_From_Exploring(self):
        print("I'm returning from exploring")
        self.state = "Resting"

    def Returning_From_Verifying(self):
        print("I'm returning from verifying")
        if abs(self.location[0]) > self.optimal_x and abs(self.location[1]) > self.optimal_y:
            self.location = [self.location[0]-self.optimal_x,
                             self.location[1]-self.optimal_y]
            print(
                f"I am moving to the optimal location of {self.optimal_x}, {self.optimal_y}")
        self.state = "Dancing"

    def Going_To_Verify(self):
        print("I'm going to verify")
        self.state = "Verifying"
        self.location_site_checker()
        self.location = self.Verifying_Path(
            self.location[0], self.location[1], danced_for_location)
        if self.site_found:
            print(f"{VERIFYING_COLOR}I found a site, I'm going to verify it")
            self.start_dance(3)
            self.state = "Returning_From_Verifying"
        else:
            self.state = "Verifying"
            self.time_left_verifying = 3
            print(
                f"I am still going out to verify because I haven't reached the site yet")

        #####################
        # Helper Functions ##
        #####################

    def plot_location(self, list_of_xy):
        plt.rcParams["figure.figsize"] = [7.00, 7.0]
        plt.rcParams["figure.autolayout"] = True
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.grid()
        point_num = 1
        for i in list_of_xy:
            x = [i[0]]
            y = [i[1]]
            plt.plot(x, y, marker="o", markersize=point_num,
                     markeredgecolor="blue", markerfacecolor="white")
            point_num += 1
        plt.show()

    def location_site_checker(self):
        if self.location in self.site_options:
            self.site_found = True

        else:
            self.site_found = False
        return self.location

    def moving_to_a_specific_location(self, curr_x, curr_y, goal_site_coordinates):
        if curr_x == goal_site_coordinates[0] and curr_y == goal_site_coordinates[1]:
            return self.location
        # one of the directions is close to the goal
        elif abs(curr_x - goal_site_coordinates[0]) < self.optimal_x and abs(curr_y - goal_site_coordinates[1]) < self.optimal_y:
            self.location = goal_site_coordinates
        # cases above this one WORK!
        elif abs(curr_x - goal_site_coordinates[0]) < self.optimal_x and curr_y > goal_site_coordinates[1]:
            x_distance_still_needed = abs(curr_x - goal_site_coordinates[0])
            y_distance = math.sqrt(
                (self.move_radius**2) - (x_distance_still_needed**2))
            self.location = [abs(curr_x)+x_distance_still_needed,
                             curr_y - y_distance]
        elif abs(curr_x - goal_site_coordinates[0]) < self.optimal_x and curr_y < goal_site_coordinates[1]:
            x_distance_still_needed = goal_site_coordinates[0]-curr_x
            y_distance = math.sqrt(
                (self.move_radius**2) - (x_distance_still_needed**2))
            self.location = [round(curr_x+x_distance_still_needed),
                             curr_y + y_distance]
        elif abs(curr_y - goal_site_coordinates[1]) < self.optimal_y and curr_x > goal_site_coordinates[0]:
            y_distance_still_needed = abs(curr_y - goal_site_coordinates[1])
            x_distance = math.sqrt(
                (self.move_radius**2) - (y_distance_still_needed**2))
            self.location = [curr_x - x_distance,
                             abs(curr_y)-y_distance_still_needed]
        elif abs(curr_y - goal_site_coordinates[1]) < self.optimal_y and curr_x < goal_site_coordinates[0]:
            y_distance_still_needed = abs(curr_y - goal_site_coordinates[1])
            x_distance = math.sqrt(
                (self.move_radius**2) - (y_distance_still_needed**2))
            self.location = [curr_x + x_distance,
                             abs(curr_y) - y_distance_still_needed]
        # neither location is close to the goal
        elif curr_x < goal_site_coordinates[0] and curr_y < goal_site_coordinates[1]:
            self.location = [round(curr_x + self.optimal_x, 3),
                             round(curr_y + self.optimal_y, 3)]
        elif curr_x > goal_site_coordinates[0] and curr_y < goal_site_coordinates[1]:
            self.location = [round(curr_x - self.optimal_x, 3),
                             round(curr_y + self.optimal_y, 3)]
        elif curr_x < goal_site_coordinates[0] and curr_y > goal_site_coordinates[1]:
            self.location = [round(curr_x + self.optimal_x, 3),
                             round(curr_y - self.optimal_y, 3)]
        elif curr_x > goal_site_coordinates[0] and curr_y > goal_site_coordinates[1]:
            self.location = [round(curr_x - self.optimal_x, 3),
                             round(curr_y - self.optimal_y, 3)]
        else:
            print("Error calculating the move to a specific location")
        return self.location

    def Exploring_tiles(self, curr_x, curr_y):
        X_change = random.choice([-1, 0, 1])
        Y_change = random.choice([-1, 0, 1])
        if X_change == 0 and Y_change == 0:
            return self.Exploring_tiles(curr_x, curr_y)
        else:
            return [curr_x + X_change, curr_y + Y_change]

    def move(self, curr_x, curr_y):
        """returns a set of new coordinates that are a random angle of 30 degrees away from the current angle and in the radius length"""
        angle_change = (random.randrange(self.current_angle -
                        20, self.current_angle+20, 1)) % 360
        X_change = self.move_radius * math.cos(math.radians(angle_change))
        Y_change = self.move_radius * math.sin(math.radians(angle_change))
        if X_change == 0 and Y_change == 0:
            return self.move(curr_x, curr_y)
        else:
            self.current_angle = angle_change
            return [round(curr_x + X_change, 3), round(curr_y + Y_change, 3)]

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


# bee = BeeAgent()
# print(bee.bee_agent_info())
# bee_location_list = []
# for i in range(0, 10):
#     bee.location = bee.move(bee.location[0], bee.location[1])
#     print(bee.location)
#     print(bee.current_angle)
#     bee_location_list.append(bee.location)
# bee.plot_location(bee_location_list)

# BeeAgent().state_function()
bee = BeeAgent()
print(bee.location)
while bee.location != [3, 7]:
    print(bee.moving_to_a_specific_location(
        bee.location[0], bee.location[1], [3, 7]))
bee.location = [0, 0]
print("new point test")
while bee.location != [-2, 5]:
    print(bee.moving_to_a_specific_location(
        bee.location[0], bee.location[1], [-2, 5]))
bee.location = [0, 0]
print("new point test")
while bee.location != [-3, -1]:
    print(bee.moving_to_a_specific_location(
        bee.location[0], bee.location[1], [-3, -1]))
bee.location = [0, 0]
print("new point test")
while bee.location != [4, -1]:
    print(bee.moving_to_a_specific_location(
        bee.location[0], bee.location[1], [4, -1]))
