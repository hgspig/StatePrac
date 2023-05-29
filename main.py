import SiteChoicesFile
import Map
import beeState
import location


total_simulation_time = 5
max_exploring_time = 5
# site_options = SiteChoicesFile.site_choices
bee_locations = []
num_bee_agents = 10
list_of_bees = []  # this is of type pointers to the bee object instances
quorum_reached = False


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
    for site in site_choices.list_of_sites:
        location.add_location([site.X_distance_from_center,site.Y_distance_from_center],site.site_goodness)
    print(location.locations_worth)
    SiteChoicesFile.print_site_chart(site_choices)
    Map.create_world(10, 10, [], site_choices.list_of_coordinates)

    for bee_creator in range(0, num_bee_agents):
        bee = beeState.BeeAgent()
        bee_locations.append(bee.bee_agent_info()[5])
        list_of_bees.append(bee)
    for time_iterator in range(0, total_simulation_time):
        print(f"{NORMAL_COLOR}Next turn")
        bee_locations = []
        num_bees_dancing = 0
        # bee_printing_locations = []
        for bee in list_of_bees:
            if bee.state == "Resting":
                bee.resting()
            elif bee.state == "Exploring":
                bee.exploring()
            elif bee.state == "Dancing":
                bee.dancing()
                if bee.state == "Dancing":
                    num_bees_dancing += 1
            elif bee.state == "Verifying":
                bee.Verifying()
            elif bee.state == "Returning_From_Exploring":
                bee.Returning_From_Exploring()
            elif bee.state == "Returning_From_Verifying":
                bee.Returning_From_Verifying()
                if bee.state == "Dancing":
                    num_bees_dancing += 1
            elif bee.state == "Going_To_Verify":
                bee.Going_To_Verify()
            else:
                print("Error: state not found")
                exit()
            bee_locations.append(bee.location[:])
            # bee_printing_locations.append((bee.location[:]).append(bee.state))
            # print(bee_printing_locations)
            # print(bee.bee_agent_info()[5])
            # print(bee.location)
        for loc in location.locations_being_danced_for:
            if len(location.locations_being_danced_for[loc]) /num_bee_agents > 1:
                print(f".5 of the bees are dancing for the site! Quorum reached on round {time_iterator}")
                exit()
        print(bee_locations)
        print()
        print()
        print()

        Map.create_world(10, 10, bee_locations, site_choices.list_of_coordinates)


main()

## send bees out to verify based on dancing instead of randomness
## have the positive feedback loop for the bees that really like their site
## set up the map drawing stuff
