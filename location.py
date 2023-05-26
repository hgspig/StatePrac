locations_worth = {} # a list of the locations with all the bees in the location
locations_being_danced_for = {tuple([0,0]):['bee']} # a list of the locations with all the bees in the location

#[0,0]:[bee,bee,bee]
def add_location(location, worth):
    locations_being_danced_for[tuple(location)] = [] 
    locations_worth[tuple(location)] = worth 

# def add_worth_to_location(location, worth):
#     if location in locations_worth:
#         locations_worth[location].append(worth) 
#     else:
#         print("Error: location not in locations_being_verified dictionary")

def add_bee_dancing_for_location(location, bee):
    if location in locations_being_danced_for:
        locations_being_danced_for[location].append(bee) 
    else:
        print("Error: location not in locations_being_danced_for dictionary")

def remove_bee_dancing_for_location(location, bee):
    if location in locations_being_danced_for:
        if bee in locations_being_danced_for[location]:
            locations_being_danced_for[location].remove(bee) 
        else:
            print("Error: bee not in locations_being_danced_for dictionary")
    else:
        print("Error: location not in locations_being_danced_for dictionary")

def quorum_verification(quorum_reached, quorum_amount):
    for location in locations_being_danced_for:
        if len(locations_being_danced_for[location]) > quorum_amount:
            quorum_reached = True
            return list(location) #for each value in keys find the length. if length is greater then quorum amount end
