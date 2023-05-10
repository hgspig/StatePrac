import random


def random_site_goodness():
    return random.randint(0, 100)/100


class Site(object):
    def __init__(self, site_goodness, prob_of_finding, X_distance_from_center, Y_distance_from_center):
        self.site_goodness = site_goodness
        self.prob_of_finding = prob_of_finding
        self.X_distance_from_center = X_distance_from_center
        self.Y_distance_from_center = Y_distance_from_center


class SiteChoices(object):
    # makes six possible sites
    def __init__(self):

        self.site_one = Site(random_site_goodness(),
        self.site_two=random_site_goodness()
        self.site_three=random_site_goodness()
        self.site_four=random_site_goodness()
        self.site_five=random_site_goodness()
        self.site_six=random_site_goodness()
        self.list_of_sites=[self.site_one, self.site_two,
                              self.site_three, self.site_four, self.site_five, self.site_six]


class Location(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y




print(SiteChoices().list_of_sites)
