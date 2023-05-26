import SiteChoicesFile
import math
from matplotlib import pyplot as plt
from matplotlib import lines
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

def plot_location(x_dimension, y_dimension,list_of_xy):
    plt.rcParams["figure.figsize"] = [x_dimension, y_dimension]
    plt.rcParams["figure.autolayout"] = True
    plt.xlim(-(x_dimension//2), (x_dimension//2))
    plt.ylim(-(y_dimension//2), (y_dimension//2))
    plt.grid()
    point_num = 7
    plt.plot(0,0,marker=f"D",markersize=point_num,markeredgecolor="purple",markerfacecolor="purple",)
    for i in list_of_xy:
        x = [i[0]]
        y = [i[1]]
        if i[2] == "B":
            plt.plot(x,y,marker=f"${i[2]}$",markersize=point_num,markeredgecolor="red",markerfacecolor="white",)
            # lines.Line2D([0,i[0],10],[0,i[1],10],color="red",linestyle="dashed",linewidth=2)
        elif i[2] == "S":
            plt.plot(x,y,marker=f"${i[2]}$",markersize=point_num,markeredgecolor="green",markerfacecolor="white",)
        point_num += 0
    plt.show()


def create_world(x_dimension, y_dimension, bee_location_list=[], site_options_coordinates=[]):
    copy_of_bee_location_list = bee_location_list.copy()
    copy_of_site_options_coordinates = site_options_coordinates.copy()
    for bee in copy_of_bee_location_list:
        bee.insert(2, "B")
    for site in copy_of_site_options_coordinates:
        site.insert(2, "S")
    noteworthy_locations = copy_of_bee_location_list + copy_of_site_options_coordinates
    plot_location(x_dimension, y_dimension, noteworthy_locations)

