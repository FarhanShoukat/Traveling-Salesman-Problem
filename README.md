# Traveling-Salesman-Problem

## Abstract:
In this study, two methods were used for solving Traveling Salesman Problem. The problem is solved using Genetic Algorithm and Simulated Annealing. Simulated Annealing gave better results in short amount of time as compared to Genetic Algorithm.


## Methadology:

### 1) Data Set Selection:
For this study, **USCAP dataset** was used. This dataset contain 312 cities. Names of cities are given in uscap_name.txt file and NxN matrix giving distance between each pair of cities is given in usca312_dist.txt file. (Each city is directed connected with every other city). The x-y coordinated mapping of cities are given in usc312_xy.txt file, and 2D plot is given in usc312.png file. Some description of data is given in usca312_main.txt file. For more details see [link](http://people.sc.fsu.edu/~jburkardt/datasets/cities/cities.html).

### 2) Chromosome Design
Chromosome is represented as a list/array. Value in index(i) and index(i+1) represents path from i to i+1.

### 3) Fitness Function
In this problem, fitness is the negative of sum of distance of path.


### 4.1) Setting of Simulated Annealing

#### a) Actions and Successor Function
Randomly selecting two indices and reversing path between them.

#### b) Schedule Function
Schedule function = **a - t/b** where a and b are variables.
* a: initial value of temperature.
* b: rate at which temperature decrease.


### 4.2) Setting of Genetic Algorithm

#### a) Crossover Method
Partially Mapped Crossover(PMX) was used.

#### b) Mutation Method
Replacing one value with another random value and replacing value of index having this new value with old value of first index.


## Results:
Simulated Annealing gave best results overall. Detailed results of study is given in [Report](../master/Report.docx).


## Conclusion:
To conclude, both methods work for Traveling Salesman Problem. However, Simulated Annealing gives better results in short amount of time.


## Contact
You can get in touch with me on my LinkedIn Profile: [Farhan Shoukat](https://www.linkedin.com/in/farhan-shoukat-782542167/)


## License
[MIT](../master/LICENSE)
Copyright (c) 2018 Farhan Shoukat

