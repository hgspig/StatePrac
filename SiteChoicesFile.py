import random
from tabulate import tabulate


def random_site_goodness():
    return random.randint(0, 10)/10


def random_prob_of_finding():
    return random.randint(0, 10)/10


class Site(object):
    def __init__(self, site_goodness, prob_of_finding, coordinates):
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
        self.site_one = Site(.6,
                             random_prob_of_finding(), [-2, 3])
        self.site_two = Site(.3,
                             random_prob_of_finding(), [-4, 0])
        self.site_three = Site(.7,
                               random_prob_of_finding(), [1, 0])
        self.site_four = Site(.9,
                              random_prob_of_finding(), [0, -2])
        self.site_five = Site(.2,
                              random_prob_of_finding(), [3, -1])
        self.site_six = Site(.5,
                             random_prob_of_finding(), [0, 4])
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
