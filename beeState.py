import random
import beeInfo
import math
from matplotlib import pyplot as plt
import matplotlib
import math
import location

# COLORS
SITE_COLOR = "\033[96m"
NEST_COLOR = "\033[95m"
NORMAL_COLOR = "\033[0m"
RESTING_COLOR = "\033[94m"
EXPLORING_COLOR = "\033[92m"
VERIFYING_COLOR = "\033[93m"
DANCING_COLOR = "\033[91m"

danced_for_location = [1, 3]
tab_text_formatting = "     "
verifying_time = 3


class BeeAgent(object):
    def __init__(self,total_simulation_time=20,max_exploring_time=5, site_options=[[-2,3],[-4,0],[1,0],[0,-2],[3,-1],[0,4]], current_angle=random.randrange(0, 360, 1)):
        self.state = "Resting"
        self.total_dance_time = 0
        self.dance_time_left = 0
        self.exploring_time_left = 0
        self.site_found = False
        self.location = [0, 0]
        self.location_verifying = [0,0]
        self.max_exploring_time = max_exploring_time
        self.total_simulation_time = total_simulation_time
        self.site_options = site_options
        self.move_radius = 1
        self.current_angle = 0
        self.time_left_verifying = 0
        self.trajectory_angle_radians = 0
        self.info_about_site = []

    def bee_agent_info(self):
        return [self.state, self.total_dance_time, self.dance_time_left, self.exploring_time_left, self.site_found, self.location, self.max_exploring_time, self.total_simulation_time, self.site_options]

    def resting(self):
        print(f"{RESTING_COLOR}I am resting")
        if self.convinced_by_dance(): #currently just randomized
            self.state = "Going_To_Verify" 
            print(tab_text_formatting+f"{VERIFYING_COLOR}I am convinced by the dance. I'm verifying their information")
            # self.exploring_time_left = self.max_exploring_time
        elif self.decides_to_explore():  #currently just randomized
            self.state = "Exploring"
            self.exploring_time_left = self.max_exploring_time
            print(tab_text_formatting+f"{EXPLORING_COLOR}I have decided to explore")
        else:
            self.state = "Resting"
            print(tab_text_formatting+f"{RESTING_COLOR}I am still resting")

    def exploring(self):
        print(f"{EXPLORING_COLOR}I am still exploring because I have {self.exploring_time_left} units of time left")
        self.location = self.Exploring_tiles(self.location[0], self.location[1])
        self.location_site_checker()
        if self.site_found:
            self.exploring_time_left = 0
            print(tab_text_formatting+f"{NORMAL_COLOR}I found a site, I'm now going to verify it")
            self.state = "Verifying"
            self.time_left_verifying = verifying_time
        elif self.exploring_time_left == 0:
            self.state = "Returning_From_Exploring"
            print(tab_text_formatting+f"{RESTING_COLOR}I didn't find anything but I'm tired so I'm going to return from exploring")
        else:
            self.state = "Exploring"
            print(tab_text_formatting+f"{EXPLORING_COLOR}I am still exploring")
            self.exploring_time_left -= 1 #exploring goes from the time given to 0 not including the number given


    def dancing(self):
        print(f"{DANCING_COLOR}I'm dancing. My dance still has {self.total_dance_time} time left")
        if self.total_dance_time == 0:
            location.remove_bee_dancing_for_location(self.location, self)
            self.state = "Resting"
            print(tab_text_formatting+f"{RESTING_COLOR}I'm done dancing so now I'm resting")
        else:
            self.total_dance_time -= 1
            print(tab_text_formatting+f"{DANCING_COLOR}I'm still dancing")

    def Verifying(self):
        print(f"{VERIFYING_COLOR}I'm verifying the site because I have {self.time_left_verifying} units of time left")
        if self.time_left_verifying == 0:
            self.state = "Returning_From_Verifying"
            print(tab_text_formatting+f"I'm have finished verifying so now I'm returning from verifying")
            self.info_about_site = location.locations_worth[tuple(self.location_verifying)]
            print(self.info_about_site)
        else:
            self.time_left_verifying -= 1
            self.state = "Verifying"
            print(tab_text_formatting+f"I am still verifying the site because I have {self.time_left_verifying} units of time left")

    def Returning_From_Exploring(self):
        print("I'm returning from exploring. My current location is: ", self.location)
        self.moving_to_a_specific_location(self.location[0], self.location[1], [0, 0])
        if self.location != [0,0]:
            print(tab_text_formatting+"I'm not there yet so I'm still returning from exploring.")
        else:
            print(tab_text_formatting+"I have arrived at the nest so now I'm resting.")
            self.state = "Resting"

    def Returning_From_Verifying(self):
        print("I'm returning from Verifying. My current location is: ", self.location)
        self.moving_to_a_specific_location(self.location[0], self.location[1], [0, 0])
        if self.location != [0,0]:
            print(tab_text_formatting+"I'm still returning from Verifying.")
        else:
            print(tab_text_formatting+"I've arrived at the nest. I'm going to dance now.")
            self.dance_time_left = 3
            self.state = "Dancing"
            location.add_bee_dancing_for_location(self.location, self)

# hasn't been checked off yet
    def Going_To_Verify(self):
        print("I'm traveling to verify: ", self.location_verifying)
        self.moving_to_a_specific_location(self.location[0], self.location[1], self.location_verifying)
        if self.location==self.location_verifying:
            print(tab_text_formatting+f"{VERIFYING_COLOR}I found a site, I'm going to verify it")
            self.time_left_verifying = verifying_time
            self.state = "Verifying"
        else:
            print(tab_text_formatting+f"I am still going out to verify because I haven't reached the site yet")
            self.state = "Going_To_Verify"

        #####################
        # Helper Functions ##
        #####################
# hasn't been checked off yet

    def location_site_checker(self):
        for site in self.site_options:
            if abs(self.location[0]-site[0]) < self.move_radius:
                if abs(self.location[1]-site[1]) < self.move_radius:
                    self.site_found = True
                    return site
        # self.site_found = False
        return self.location
# hasn't been checked off yet

    def moving_to_a_specific_location(self, curr_x, curr_y, goal_site_coordinates):
        x_needed = goal_site_coordinates[0] - curr_x
        y_needed = goal_site_coordinates[1] - curr_y
        self.trajectory_angle_radians = math.atan2(y_needed, x_needed)
        x_distance = self.move_radius * math.cos(self.trajectory_angle_radians)
        y_distance = self.move_radius * math.sin(self.trajectory_angle_radians)
        if abs(x_distance) > abs(x_needed) and abs(y_distance) > abs(y_needed):
            x_distance = x_needed
            y_distance = y_needed
        self.location = [round(curr_x + x_distance, 3), round(curr_y + y_distance, 3)]

    def Exploring_tiles(self, curr_x, curr_y):
        """returns a set of new coordinates that are a random angle of 30 degrees away from the current angle and in the radius length"""
        angle_change = (random.randrange(self.current_angle - 20, self.current_angle + 20, 1)) % 360
        X_change = self.move_radius * math.cos(math.radians(angle_change))
        Y_change = self.move_radius * math.sin(math.radians(angle_change))
        self.current_angle = angle_change
        return [round(curr_x + X_change, 3), round(curr_y + Y_change, 3)]
# hasn't been checked off yet

    def convinced_by_dance(self):
        if self.probability_convinced_by_dance() > 0.6:
            return True
        else:
            return False
# hasn't been checked off yet

    def decides_to_explore(self):
        if self.probability_resting_to_Exploring() > 0.4:
            return True
        else:
            return False
# hasn't been checked off yet

    def probability_convinced_by_dance(self):
        return random.randrange(1, 11, 1) / 10
# hasn't been checked off yet

    def probability_resting_to_Exploring(self):
        return random.randrange(1, 11, 1) / 10
# hasn't been checked off yet

    def start_dance(self, site_goodness):
        self.dance_time_left = site_goodness
        self.total_dance_time = site_goodness

# hasn't been checked off yet

class hex(object):
    def __init__(self, X_distance_from_center, Y_distance_from_center):
        self.X_distance_from_center = X_distance_from_center
        self.Y_distance_from_center = Y_distance_from_center
        self.contians_potential_site = False

    def make_site(self, site_goodness, prob_of_finding):
        return Site(site_goodness,prob_of_finding,self.X_distance_from_center,self.Y_distance_from_center)

# hasn't been checked off yet

class Site(object):
    def __init__( self, site_goodness,prob_of_finding, X_distance_from_center, Y_distance_from_center):
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
# bee = BeeAgent()
# # print(bee.location)
# # while bee.location != [-3, 7]:
# #     bee.moving_to_a_specific_location(bee.location[0], bee.location[1], [-3, 7])
# #     print(bee.location)
# bee.exploring_time_left =6
# bee.state = "Exploring"
# while bee.state == "Exploring":
#     bee.exploring()