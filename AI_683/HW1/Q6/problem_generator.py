import random
import math
import numpy


def generate_TSP_instance(k, epsilon):

    def check_conflict(temp_instance, node, epsilon):
        # print (node[0],node[1])
        # print (temp_instance)
        distance = list(map(lambda y: math.sqrt(
            (node[0] - y[0])**2 + (node[1] - y[1])**2), temp_instance))
        # print(distance)
        if(min(distance) > epsilon):
            return True
        return False

    # Add k cities of the form (x, y) to instance where each city is at least a distance of epsilon from each other
    instance = []
    while (len(instance) < k):
        x_cord = random.uniform(0, 1)
        y_cord = random.uniform(0, 1)
        if(len(instance) == 0):
            instance.append((x_cord, y_cord))
        elif check_conflict(instance, (x_cord, y_cord), epsilon):
            instance.append((x_cord, y_cord))

    return instance

# k - number of cities
# instance - list with city coordinates as tuples


def calculate_grid_distances(k, instance):
    grid_distances = numpy.zeros((k, k))
    for i in range(k):
        for j in range(i):
            tuple1 = instance[i]
            tuple2 = instance[j]

            grid_distances[i][j] = math.sqrt(
                (tuple1[0] - tuple2[0])**2 + (tuple1[1] - tuple2[1])**2)
            grid_distances[j][i] = grid_distances[i][j]

    return grid_distances


def run_main(k, epsilon):
    instance = generate_TSP_instance(k, epsilon)
    grid_distances = calculate_grid_distances(k, instance)
    return grid_distances, k

# print(instance,"\n\n",grid_distances)
