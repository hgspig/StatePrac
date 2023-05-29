import random
from tabulate import tabulate


def random_site_goodness():
    return random.randint(0, 10)/10


def random_prob_of_finding():
    return random.randint(0, 10)/10


class Site(object):
    def __init__(self, coordinates, site_goodness, prob_of_finding):
        self.site_goodness = site_goodness
        self.prob_of_finding = prob_of_finding
        self.X_distance_from_center = coordinates[0]
        self.Y_distance_from_center = coordinates[1]


class SiteChoices(object):
    # makes six possible sites
    def __init__(self):
        # below is how I could make a site in the future
        # self.site_one = Site(random_site_goodness(),
        #                      random_prob_of_finding(), [-2, 3])
        self.site_one = Site([-2, 3],.6,.7)
        self.site_two = Site([-4, 0],.3,.6)
        self.site_three = Site([1,0],.7,.4)
        self.site_four = Site([0, -2],.9, .7)
        self.site_five = Site([3, -1],.2, .1)
        self.site_six = Site([0, 4],.5,.3)
        # self.list_of_sites = [self.site_one, self.site_two, self.site_three]
        self.list_of_sites = [self.site_one, self.site_two,
                              self.site_three, self.site_four, self.site_five, self.site_six]
        self.list_of_coordinates = [
            [site.X_distance_from_center, site.Y_distance_from_center] for site in self.list_of_sites]


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def print_site_chart(sitechoices):
    Sites = []
    for site in sitechoices.list_of_sites:
        Sites.append([site.X_distance_from_center, site.Y_distance_from_center,
                     site.site_goodness, site.prob_of_finding])
    print(tabulate(Sites, headers=[
          "X cord", "Y cord", "Desirability", "Findability"]))
