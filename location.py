locations_worth = {} # a list of the locations with all the bees in the location
locations_being_danced_for = {} # a list of the locations with all the bees in the location #tuple([0,0]):['bee']

def add_location(location, worth):
    locations_being_danced_for[tuple(location)] = [] 
    locations_worth[tuple(location)] = worth 

# def add_worth_to_location(location, worth):
#     if location in locations_worth:
#         locations_worth[location].append(worth) 
#     else:
#         print("Error: location not in locations_being_verified dictionary")

def add_bee_dancing_for_location(location, bee):
    location_tuple = tuple(location)
    if location_tuple in locations_being_danced_for:
        locations_being_danced_for[location_tuple].append(bee) 
    else:
        #instead I should add a new location
        locations_being_danced_for
        print("Error: location not in locations_being_danced_for dictionary (adding function)")

def remove_bee_dancing_for_location(location, bee):
    location_tuple = tuple(location)
    if location_tuple in locations_being_danced_for:
        if bee in locations_being_danced_for[location_tuple]:
            locations_being_danced_for[location_tuple].remove(bee) 
        else:
            print(bee)
            print(locations_being_danced_for[location_tuple])
            print("Error: bee not in locations_being_danced_for dictionary (removing function)")
    else:
        print("Error: location not in locations_being_danced_for dictionary (removing function)")

def quorum_verification(quorum_reached, quorum_amount):
    for location in locations_being_danced_for:
        if len(locations_being_danced_for[location]) > quorum_amount:
            quorum_reached = True
            return list(location) #for each value in keys find the length. if length is greater then quorum amount end
