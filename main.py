import SiteChoicesFile
import Map
import beeState
import location


total_simulation_time = 9
max_exploring_time = 5
# site_options = SiteChoicesFile.site_choices
bee_locations = []
num_bee_agents = 1
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
    # Map.create_world(10, 10, [], site_choices.list_of_coordinates)

    for bee_creator in range(0, num_bee_agents):
        bee = beeState.BeeAgent()
        bee_locations.append(bee.bee_agent_info()[5])
        list_of_bees.append(bee)
    for time_iterator in range(0, total_simulation_time):
        print(f"{NORMAL_COLOR}Next turn")
        bee_locations = []
        bee_printing_locations = []
        for bee in list_of_bees:
            if bee.state == "Resting":
                bee.resting()
            elif bee.state == "Exploring":
                bee.exploring()
            elif bee.state == "Dancing":
                bee.dancing()
            elif bee.state == "Verifying":
                bee.Verifying()
            elif bee.state == "Returning_From_Exploring":
                bee.Returning_From_Exploring()
            elif bee.state == "Returning_From_Verifying":
                bee.Returning_From_Verifying()
            elif bee.state == "Going_To_Verify":
                bee.Going_To_Verify()
            else:
                print("Error: state not found")
                exit()
            bee_locations.append(bee.bee_agent_info()[5])
            bee_printing_locations.append((bee.bee_agent_info()[5]).append("bee.state"))
            print(bee_printing_locations)
            # print(bee.bee_agent_info()[5])
            # print(bee.location)
        print(bee_locations)

        # Map.create_world(10, 10, bee_locations, site_choices.list_of_coordinates)


main()

#for bee.location 
#if map(bee.location) !contains bee then add bee to the location
#for  location in locations_being_verified
#if len > quorm amount then location has been reached and all bee locations switch to there and simulation over. 
