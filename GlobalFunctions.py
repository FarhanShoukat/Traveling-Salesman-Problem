import math
import random


class State:
    chromosome = None
    fitness = None

    def __eq__(self, other):
        return self.chromosome == other.chromosome and self.fitness == other.fitness


def calculate_fitness(distances, chromosome):
    f = 0
    problem_length = len(chromosome)
    for i in range(problem_length - 1):
        f += distances[chromosome[i]][chromosome[i + 1]]

    return -f


def create_initial_state(problem_length):
    chromosome = []
    while len(chromosome) != problem_length:
        rand = random.randint(0, problem_length - 1)
        if rand not in chromosome:
            chromosome.append(rand)

    s = State()
    s.chromosome = chromosome
    return s


def read_distances(file):
    distances = []
    file = open(file + '_dist.txt')
    for i in range(7):
        next(file)
    for line in file:
        line = line.rstrip().lstrip().split(" ")
        for num in line:
            try:
                distances.append(int(num))
            except:
                x = 0

    n = int(math.sqrt(len(distances)))
    l = distances
    return [l[i:i + n] for i in range(0, len(l), n)]


def read_coordinates(file):
    coordinates = []
    file = open(file + '_xy.txt')
    for i in range(7):
        next(file)

    for line in file:
        line = ' '.join(line.lstrip().rstrip().split(' ')).split()
        coordinates.append((float(line[0]), float(line[1])))

    return coordinates
