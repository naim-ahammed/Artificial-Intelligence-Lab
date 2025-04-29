import random

class Individual:
    def __init__(self, k, T, genes=None):
        self.k = k
        self.T = T
        if genes:
            self.genes = genes
        else:
            self.genes = [random.randint(0, 9) for _ in range(min(2, k))] + [0] * (k - 2)
        self.fitness = self.cf()

    def cf(self):
        return 18 - abs(sum(self.genes[:2]) - self.T)

class GeneticAlgorithm:
    def __init__(self, T, k, ps=30, cr=0.8, mr=0.2):
        self.T = T
        self.k = k
        self.ps = ps
        self.cr = cr
        self.mr = mr
        self.population = [Individual(k, T) for _ in range(ps)]
        self.generation = 0

    def select_parents(self):
        return sorted(random.sample(self.population, 2), key=lambda ind: ind.fitness, reverse=True)

    def crossover(self, parent1, parent2):
        if random.random() < self.cr and self.k > 1:
            child1_g = parent1.genes[:]
            child2_g = parent2.genes[:]
            child1_g[0], child2_g[0] = child2_g[0], child1_g[0]
            return Individual(self.k, self.T, child1_g), Individual(self.k, self.T, child2_g)
        return parent1, parent2

    def mutate(self, individual):
        new_genes = individual.genes[:]
        for i in range(min(2, self.k)):
            if random.random() < self.mr:
                new_genes[i] = random.randint(0, 9)
        return Individual(self.k, self.T, new_genes)

    def evolve(self, max_g=500):
        while self.generation < max_g:
            self.population.sort(key=lambda ind: ind.fitness, reverse=True)
            if self.population[0].fitness == 18:
                break
            np = self.population[:2] 

            while len(np) < self.ps:
                p1, p2 = self.select_parents()
                c1, c2 = self.crossover(p1, p2)
                np.extend([self.mutate(c1), self.mutate(c2)])
            self.population = np[:self.ps]
            self.generation += 1

        return max(self.population, key=lambda ind: ind.fitness)

def main():
    T = int(input("T = "))
    k = int(input("k = "))
    ga = GeneticAlgorithm(T, k)
    result = ga.evolve()
    print("Output:")
    print(" ".join(map(str, result.genes)))

if __name__ == "__main__":
    main()
