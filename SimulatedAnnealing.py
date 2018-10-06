from GlobalFunctions import read_distances, read_coordinates, create_initial_state, State, calculate_fitness
import random
import math
from datetime import datetime
import time
import matplotlib.pyplot as plt


def schedule(t): return a - t / b


def successor_function(chromosome):
    chromosome = list(chromosome)
    index1 = random.randint(0, problem_length - 1)
    index2 = random.randint(0, problem_length - 1)
    while index1 == index2: index2 = random.randint(0, problem_length - 1)

    if index2 < index1: index1, index2 = index2, index1

    while index1 < index2:
        chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]
        index1 += 1
        index2 -= 1

    return chromosome


def simulated_annealing(initial):
    t = 0
    current = initial
    current.fitness = calculate_fitness(distances, current.chromosome)
    while True:
        t = t + 1

        T = schedule(t)
        if T == 0: return t, current

        successor = State()
        successor.chromosome = successor_function(current.chromosome)
        successor.fitness = calculate_fitness(distances, successor.chromosome)

        E = successor.fitness - current.fitness
        if E > 0 or random.randint(1, 101) <= math.exp(E / T): current = successor


file = input('Input Files Prefix: ')
a = abs(int(input('Tuning parameter1(a) required for schedule(t): ')))
b = abs(int(input('Tuning parameter2(b) required for schedule(t): ')))
distances = read_distances(file)
coordinates = read_coordinates(file)
problem_length = len(coordinates)
initial = create_initial_state(problem_length)

time.ctime()
fmt = '%H:%M:%S'
start = time.strftime(fmt)

iterations, result = simulated_annealing(initial)

time.ctime()
end = time.strftime(fmt)
print("Time taken(sec):", datetime.strptime(end, fmt) - datetime.strptime(start, fmt))
print('Iterations:', iterations)
print('Fitness of final configuration:', result.fitness)
print('Chromosome:', result.chromosome)
print(len(result.chromosome) == len(set(result.chromosome)))

x, y = [], []
for i in range(problem_length):
    x.append(coordinates[result.chromosome[i]][0])
    y.append(coordinates[result.chromosome[i]][1])
plt.plot(x, y, marker='o')
plt.show()