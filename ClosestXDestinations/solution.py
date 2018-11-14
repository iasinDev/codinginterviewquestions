# Python 2.7
import sys
import math

def ClosestXdestinations(numDestinations, allLocations, numDeliveries):
    # This solution is too complex because I did not understand the question correctly
    current_location = [0,0]
    rest_locations = allLocations[:]
    result = []
    for i in range(numDeliveries):
        next_destination = find_closest_location(current_location, rest_locations)
        result.append(next_destination)
        del rest_locations[rest_locations.index(next_destination)]
    return result

def find_closest_location(start, list_of_possible_stations):
    shortest_distance = sys.maxint
    shortest_x_y = None
    for i in range(len(list_of_possible_stations)):
        distance = math.sqrt(pow(list_of_possible_stations[i][0] - start[0],2)+pow(list_of_possible_stations[i][1] - start[1],2))
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_x_y = list_of_possible_stations[i]
    return shortest_x_y



print(ClosestXdestinations(3, [[1,2], [3,4], [1,-1]],2))
print(ClosestXdestinations(6, [[3,6], [2,4], [5,3], [2,7], [1,8], [7,9]],3)) # 2,4 3,6 5,3
