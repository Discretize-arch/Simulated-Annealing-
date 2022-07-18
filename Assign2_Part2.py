import random
import math
# suppose you are part of an airline company. Plan the shortest trip from a list of given cities
# solve a traveling salesman problem using simulated annealing

# added cities
def cities():
    Kyiv = (50.45, 30.52)
    San_Francisco = (37.77, 122.41)
    New_York = (40.71, 74.00)
    Tokyo = (35.67, 139.65)
    Los_Angeles = (34.05, 118.24)
    Sydney = (33.85, 151.20)
    cities = [Kyiv, San_Francisco, New_York, Tokyo, Los_Angeles, Sydney]
    return cities

# distance between two points
def distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

# total distance of a path
def path_distance(path):
    dist = 0
    for i in range(len(path)):
        dist += distance(path[i], path[(i + 1) % len(path)])
    return dist

# Translate coordinates back into cities
def translate(path):
    readablePath = []
    i = 0
    while i <= 5:
        if path[i] == (50.45, 30.52):
            readablePath.append("Kyiv")
        elif path[i] == (37.77, 122.41):
            readablePath.append("San Francisco")
        elif path[i] == (40.71, 74.00):
            readablePath.append("New York")
        elif path[i] == (35.67, 139.65):
            readablePath.append("Tokyo")
        elif path[i] == (34.05, 118.24):
            readablePath.append("Los Angeles")
        elif path[i] == (33.85, 151.20):
            readablePath.append("Sydney")
        i += 1
    return readablePath

# annealing algorithm for TSP
def anneal(path):
    # set the initial temperature
    T = 1000
    # decrease the temperature as the iterations go on
    dT = 0.9
    dist = path_distance(path)
    best_dist = dist
    # set the best path
    best_path = path
    # set the number of iterations
    i = 0
    accepted = 0
    rejected = 0
    # set the number of iterations to stop at
    max_iter = 100000
    # set the number of iterations to run at each temperature
    max_temp = 100
    while T > 0.01 and i < max_iter:
        # set the new path
        new_path = path[:]
        # randomly swap two cities
        i1 = random.randint(0, len(path) - 1)
        i2 = random.randint(0, len(path) - 1)
        new_path[i1], new_path[i2] = new_path[i2], new_path[i1]
        # set the new path distance
        new_dist = path_distance(new_path)
        # if the new path is better, accept it
        if new_dist < dist:
            path = new_path[:]
            dist = new_dist
            accepted += 1
        # if the new path is worse, accept it with a probability
        elif random.random() < math.exp((dist - new_dist) / T):
            path = new_path[:]
            dist = new_dist
            accepted += 1
        # if the new path is worse, reject it
        else:
            rejected += 1
        # if the number of accepted iterations is greater than the number of iterations to run at each temperature
        if accepted > max_temp:
            accepted = 0
            T *= dT
        # if the number of rejected iterations is greater than the number of iterations to run at each temperature
        if rejected > max_temp:
            rejected = 0
            T *= dT
        # increase the number of iterations
        i += 1
        print("\n Temperature:", T, "Distance:", dist, "Iteration:", i)
        print(path)
        print(translate(path))

    # return the best path
    print("Best Path")
    return best_path

# main
if __name__ == "__main__":
    # set the initial path
    path = cities()
    bestPath = anneal(path)
    print("\nCourse: CS 3642"
          "\n Student name: Leiko Niwano"
          "\n Student ID: -------------"
          "\n Assignment #: 2"
          "\n Due Date: 3/27/2022"
          "\n Signature: __Leiko Niwano__")