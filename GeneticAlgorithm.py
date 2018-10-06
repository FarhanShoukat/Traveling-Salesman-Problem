from GlobalFunctions import read_distances, read_coordinates, State, calculate_fitness, create_initial_state
import random
import operator
import math
import matplotlib.pyplot as plt
from datetime import datetime
import time





def rank_select_parents(brackets):
    try:
        rand = random.randint(1, brackets[len(brackets) - 1][1])
    except:
        x = 0
    i = 0
    while True:
        if brackets[i][0] <= rand <= brackets[i][1]:
            break
        i = i + 1

    while True:
        try:
            rand = random.randint(1, brackets[len(brackets) - 1][1])
        except:
            x = 0
        j = 0
        while True:
            if brackets[j][0] <= rand <= brackets[j][1]:
                if i != j:
                    return i, j
                else:
                    break
            j = j + 1


def calculate_rank_brackets(population):
    length = len(population)
    brackets = [0] * length
    brackets = [length - i for i in range(length)]
    for i in range(1, length):
        if population[i].fitness == population[i - 1].fitness:
            brackets[i] = brackets[i - 1]

    mul = 100 * k / sum(brackets)
    for i in range(length):
        brackets[i] = math.floor(brackets[i] * mul)

    brackets[0] = 1, brackets[0]
    for i in range(1, length):
        brackets[i] = brackets[i - 1][1] + 1, brackets[i - 1][1] + brackets[i]
        # x = brackets[i - 1][1] + 1
        # y = brackets[i - 1][1] + brackets[i]
        # if x < y: brackets[i] = x, y
        # else: brackets[i] = x, x

    return brackets


def select_new_generation(old_population, new_generation):
    new_generation.sort(key=operator.attrgetter('fitness'), reverse=True)
    i1 = 0
    i2 = 0
    result = []

    while len(result) != k:
        if old_population[i1].fitness < new_generation[i2].fitness:
            if new_generation[i2] not in result:
                result.append(new_generation[i2])
            i2 = i2 + 1
        else:
            if old_population[i1] not in result:
                result.append(old_population[i1])
            i1 = i1 + 1

    return result


def create_initial_population():
    population = []
    while len(population) != k:
        s = create_initial_state(problem_length)
        if s not in population:
            population.append(s)

    return population


def partially_mapped_crossover(p1, p2):
    rand1 = random.randint(2, problem_length - 2)
    rand2 = rand1
    while rand1 == rand2: rand2 = random.randint(1, problem_length - 2)

    o1 = [None] * problem_length
    o2 = [None] * problem_length
    for i in range(rand1, rand2 + 1):
        o1[i] = p2[i]
        o2[i] = p1[i]

    for i in range(rand1):
        if p1[i] not in o1: o1[i] = p1[i]
        if p2[i] not in o2: o2[i] = p2[i]

    for i in range(rand2 + 1, problem_length):
        if p1[i] not in o1: o1[i] = p1[i]
        if p2[i] not in o2: o2[i] = p2[i]

    for i in range(problem_length):
        if o1[i] is None:
            new = p1[i]
            while new in o1: new = p1[p2.index(new)]
            o1[i] = new
        if o2[i] is None:
            new = p2[i]
            while new in o2: new = p2[p1.index(new)]
            o2[i] = new

    return o1, o2


# random.randint(1, 101) <= mutation_rate


def apply_mutation(chromosome):
    index = random.randint(0, problem_length - 1)
    value = random.randint(0, problem_length - 1)
    while value == chromosome[index]: value = random.randint(0, problem_length - 1)
    index2 = chromosome.index(value)
    chromosome[index], chromosome[index2] = value, chromosome[index]
    return chromosome


def genetic_algorithm():
    population = create_initial_population()
    for i in population:
        if i.fitness is None:
            i.fitness = calculate_fitness(distances, i.chromosome)

    i = iterations
    while i != 0:
        population.sort(key=operator.attrgetter('fitness'), reverse=True)
        if fitness <= population[0].fitness: break

        i -= 1

        new_generation = []
        brackets = calculate_brackets(population)
        while len(new_generation) != problem_length:
            x, y = rank_select_parents(brackets)
            o1, o2 = crossover(population[x].chromosome, population[y].chromosome)

            if random.randint(1, 101) <= mutation_rate: o1 = apply_mutation(o1)
            if random.randint(1, 101) <= mutation_rate: o2 = apply_mutation(o2)

            s1 = State()
            s1.chromosome = o1
            s1.fitness = calculate_fitness(distances, s1.chromosome)
            s2 = State()
            s2.chromosome = o2
            s2.fitness = calculate_fitness(distances, s2.chromosome)
            if len(new_generation) + 1 < problem_length:
                if s1 not in new_generation: new_generation.append(s1)
                if s2 not in new_generation: new_generation.append(s2)
            else:
                if s1.fitness < s2.fitness and s2 not in new_generation: new_generation.append(s2)
                elif s1 not in new_generation: new_generation.append(s1)

        population = select_new_generation(population, new_generation)

    return population[0], iterations - i


# p1 = [0, 1, 2, 3, 4, 5, 6, 7]
# p2 = [7, 4, 1, 0, 2, 5, 3, 6]
# r = cycle_crossover(p1, p2)
# for i in range(len(r[0])):
#     r[0][i] = r[0][i] + 1
#     r[1][i] = r[1][i] + 1
k = int(input('k: '))
mutation_rate = float(input('Mutation Rate: '))
iterations = int(input('Maximum number of iterations: '))
fitness = float(input('Minimum value of fitness: '))
file = input('Input Files Prefix: ')

distances = read_distances(file)
coordinates = read_coordinates(file)
problem_length = len(coordinates)
calculate_brackets = calculate_rank_brackets
crossover = partially_mapped_crossover

time.ctime()
fmt = '%H:%M:%S'
start = time.strftime(fmt)

result, i = genetic_algorithm()

time.ctime()
end = time.strftime(fmt)
print("Time taken(sec):", datetime.strptime(end, fmt) - datetime.strptime(start, fmt))

print('Iterations Taken: ', i)
print('Fitness of final configuration:', result.fitness)
print(len(result.chromosome) == len(set(result.chromosome)))

x, y = [], []
for i in range(problem_length):
    x.append(coordinates[result.chromosome[i]][0])
    y.append(coordinates[result.chromosome[i]][1])
plt.plot(x, y, marker='o')
plt.show()


def cycle_crossover1(p1, p2):
    o = [-1] * problem_length

    o[0] = p1[0]
    index = 0
    while -1 in o:
        index = p2[index]
        found = p1[index]
        if found not in o:
            o[index] = found
        else: break

    for i in range(problem_length):
        if o[i] == -1:
            o[i] = p2[i]

    return o


def cycle_crossover(p1, p2):
    return cycle_crossover1(p1, p2), cycle_crossover1(p2, p1)