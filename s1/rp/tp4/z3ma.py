import random
import sys
import pygame
from pygame.locals import QUIT


class Chromosome:
    def __init__(self, genes=None):
        self.num_moves = 8
        if genes is None:
            self.genes = self.generate_random_genes()
        else:
            self.genes = genes

    def generate_random_genes(self):
        # Generate a random set of genes representing knight's moves
        return [random.randint(0, self.num_moves - 1) for _ in range(63)]

    def crossover(self, partner):
        # Single-point crossover
        crossover_point = random.randint(1, len(self.genes) - 1)
        child_genes = self.genes[:crossover_point] + partner.genes[crossover_point:]
        return Chromosome(child_genes)

    def mutation(self, mutation_rate):
        # Mutate genes based on a given mutation rate
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = random.randint(0, self.num_moves - 1)

    def __iter__(self):
        return iter(self.genes)




class Knight:
    def __init__(self, chromosome=None, position=(0, 0)):
        self.board_size = 8  # Assuming an 8x8 chessboard
        self.moves = [
            (1, 2), (2, 1), (2, -1), (1, -2),
            (-1, -2), (-2, -1), (-2, 1), (-1, 2)
        ]
        self.position = position
        self.path = [self.position]
        self.fitness = 0
        
        if chromosome is None:
            self.chromosome = self.generate_chromosome()
        else:
            self.chromosome = chromosome


    def generate_chromosome(self):
        return [random.randint(1, 8) for _ in range(self.board_size * self.board_size)]

    def move_forward(self, direction):
        move_y, move_x = self.moves[direction - 1]  # Corrected order
        new_x = self.position[0] + move_x
        new_y = self.position[1] + move_y
        self.position = (new_x, new_y)
        self.path.append(self.position)

    def move_backward(self, direction):
        move_y, move_x = self.moves[direction - 1]  # Corrected order
        new_x = self.position[0] - move_x
        new_y = self.position[1] - move_y
        self.position = (new_x, new_y)
        self.path.pop()

    def check_moves(self):
        for direction in self.chromosome:
            self.move_forward(direction)
            if not self.is_valid_move():
                self.move_backward(direction)
                # Handle invalid move - adjust chromosome or recombine/crossover if needed
            else:
                # Move was valid, continue
                self.evaluate_fitness()  # Update fitness based on the new position
                self.path.append(self.position)  # Update the path with the new position

    def is_valid_move(self):
        x, y = self.position
        return 0 <= x < self.board_size and 0 <= y < self.board_size and self.position not in self.path

    def evaluate_fitness(self):
        unique_positions = set(self.path)
        self.fitness = len(unique_positions)

    def solve(self, generations):
        for _ in range(generations):
            self.check_moves()
            self.evaluate_fitness()
            if self.fitness == self.board_size * self.board_size:
                break
            
        return self.path


class Population:
    def __init__(self, population_size=10):
        """
        Initialize a Population instance.

        Parameters:
        - population_size: The size of the population (default is 50).
        """
        self.population_size = population_size
        self.generation = 1
        self.knights = self.init()

    def init(self):
        return [Knight(position=(random.randint(0, 7), random.randint(0, 7)), chromosome=Chromosome()) for _ in range(self.population_size)]


    def check_population(self):
        for knight in self.knights:
            knight.check_moves()

    def evaluate(self):
        for knight in self.knights:
            knight.evaluate_fitness()

        best_knight = max(self.knights, key=lambda x: x.fitness)
        return best_knight, best_knight.fitness



    def tournament_selection(self, size=3):
        """
        Perform tournament selection to select parental combinations for crossover.

        Parameters:
        - size: The sample size for the tournament (default is 3).

        Returns:
        - parents: List of selected parent knights.
        """
        parents = []

        for _ in range(2):  # Select two parents
            tournament_samples = random.sample(self.knights, size)
            best_knight = max(tournament_samples, key=lambda x: x.fitness)
            parents.append(best_knight)

        return parents
    
    #ghalta
    def create_new_generation(self, mutation_rate=0.1):
        new_generation = []
        
        print("new generation")
        while len(new_generation) < self.population_size:
            parents = self.tournament_selection(size=3)

            # Perform crossover
            offspring = parents[0].chromosome.crossover(parents[1].chromosome)

            # Perform mutation
            offspring.mutation(mutation_rate)

            # Add offspring to the new generation
            new_generation.append(Knight(chromosome=offspring))

        # Update the population with the new generation
        self.knights = new_generation
        self.generation += 1




def main():
    pygame.init()
    clock = pygame.time.Clock()

    window_size = (600, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Knight's Tour")

    population_size = 10
    population = Population(population_size)

    # Visualization
    horse_image = pygame.image.load("knight tour/download (1).png")
    horse_image = pygame.transform.scale(horse_image, (window_size[0] // 8, window_size[0] // 8))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        print("Checking population...")
        population.check_population()
        print("Evaluating population fitness...")
        best_solution, max_fit = population.evaluate()
        print(max_fit)
        if max_fit == 64:
            print("Maximum fitness achieved. Exiting loop.")
            running = False
        else:
            print("Creating new generation...")
            population.create_new_generation()

            # Visualization
            screen.fill((255, 255, 255))
            graphicTour(best_solution.path, screen, horse_image)
            pygame.display.flip()

            # Control frame rate
            clock.tick(10)  # Adjust the frame rate as needed (e.g., 10 FPS)

    pygame.quit()
    sys.exit()


def graphicTour(L_coor, window, horse_image):
    window.blit(horse_image, (L_coor[0][0] * 75, L_coor[0][1] * 75))
    pygame.display.update()

    for index in range(1, len(L_coor)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(100)
        window.blit(horse_image, (L_coor[index][0] * 75, L_coor[index][1] * 75))
        pygame.display.update()
