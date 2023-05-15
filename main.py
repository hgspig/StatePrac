import SiteChoicesFile
import Map
import beeState


total_simulation_time = 6
max_exploring_time = 5
# site_options = SiteChoicesFile.site_choices
bee_locations = []
num_bee_agents = 5
list_of_bees = []  # this is of type pointers to the bee object instances

# COLORS
SITE_COLOR = '\033[96m'
NEST_COLOR = '\033[95m'
NORMAL_COLOR = '\033[0m'
RESTING_COLOR = '\033[94m'
EXPLORING_COLOR = '\033[92m'
VERIFYING_COLOR = '\033[93m'
DANCING_COLOR = '\033[91m'


def main():
    bee_locations = []
    site_choices = SiteChoicesFile.SiteChoices()
    SiteChoicesFile.print_site_chart(site_choices)
    Map.create_world(10, 10, [], site_choices.list_of_coordinates)
    for bee_creator in range(0, num_bee_agents):
        bee = beeState.BeeAgent()
        bee_locations.append(bee.bee_agent_info()[5])
        list_of_bees.append(bee)
    for time_iterator in range(0, total_simulation_time):
        print(f"{NORMAL_COLOR}Next turn")
        bee_locations = []
        for bee in list_of_bees:
            if bee.state == "Resting":
                bee.resting()
            elif bee.state == "Exploring":
                bee.exploring()
            elif bee.state == "Dancing":
                bee.dancing()
            elif bee.state == "Verifying":
                bee.Verifying()
            else:
                print("Error: state not found")
                exit()
            bee_locations.append(bee.bee_agent_info()[5])
            # print(bee.location)
        print(bee_locations)

        Map.create_world(10, 10, bee_locations,
                         site_choices.list_of_coordinates)


main()
