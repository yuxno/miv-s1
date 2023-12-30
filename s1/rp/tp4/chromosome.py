import random
import pygame
import sys


class Chromosome:
    def __init__(self,genes=None):

        self.genes = self.generate_random_genes()

    def generate_random_genes(self):
        possible_moves = [(i, j) for i in range(8) for j in range(8)]
        random.shuffle(possible_moves)
        return possible_moves[:self.size]
    
    
    def crossover(self, partner):
        """
        Perform single-point crossover with another chromosome.

        Parameters:
        - partner: Another Chromosome instance to crossover with.

        Returns:
        - offspring: A new Chromosome instance representing the offspring.
        """
        crossover_point = random.randint(1, self.size - 1)

        # Take genes from the first part of self and the second part of the partner
        new_genes = self.genes[:crossover_point] + partner.genes[crossover_point:]

        # Create a new Chromosome with the combined genes
        offspring = Chromosome()
        offspring.genes = new_genes

        return offspring
    

    def mutate(self, mutation_rate=0.1):
        """
        Mutate the genes with a certain probability.

        Parameters:
        - mutation_rate: The probability of mutation for each gene.

        Returns:
        - None
        """
        for i in range(self.size):
            if random.random() < mutation_rate:
                # Mutate the gene by replacing it with a random move
                self.genes[i] = (random.randint(0, 7), random.randint(0, 7))



class Knight:
    def __init__(self, position=(0, 0), chromosome=None):
        """
        Initialize a Knight instance.

        Parameters:
        - position: Initial position of the knight (default is (0, 0)).
        - chromosome: Chromosome representing the knight's moves.
        """
        self.position = position
        self.chromosome = chromosome if chromosome else Chromosome()
        self.path = [position]
        self.fitness = 0

    def init(self, chromosome=None):
        """
        Create a new knight. If no chromosome is given, generate a new chromosome.
        Set the current position to (0, 0), fitness to 0, and save the initial position to the path.

        Parameters:
        - chromosome: Optional chromosome to be used (default is None, which generates a new chromosome).
        """
        self.position = (0, 0)
        self.chromosome = chromosome if chromosome else Chromosome()
        self.path = [self.position]  # Save the initial position to the path
        self.fitness = 0  # Reset fitness to 0


    def draw_solution(self, screen, knight_image):
        square_size = screen.get_width() // 8
        for i, position in enumerate(self.path):
            x, y = position[1] * square_size, position[0] * square_size
            screen.blit(knight_image, (x, y))
            pygame.display.update()
            pygame.time.delay(200)

    def calculate_path(self):
        """
        Calculate the list of knight's positions after applying the moves defined in the chromosome.

        Returns:
        - path: List of positions.
        """
        x, y = self.position
        path = [self.position]

        for move in self.chromosome.genes:
            x += move[0]
            y += move[1]
            path.append((x, y))

        return path

    def calculate_fitness(self):
        """
        Calculate the fitness value based on the number of unique positions visited.

        Returns:
        - fitness: Fitness value.
        """
        unique_positions = set(self.path)
        return len(unique_positions)
    
    def move_forward(self, direction):
        """
        Move the knight in one of the 8 directions.

        Parameters:
        - direction: An integer from 1 to 8 representing the direction.
        """
        move_dict = {
            1: (2, 1),
            2: (1, 2),
            3: (-1, 2),
            4: (-2, 1),
            5: (-2, -1),
            6: (-1, -2),
            7: (1, -2),
            8: (2, -1)
        }

        if direction in move_dict:
            x, y = self.position
            dx, dy = move_dict[direction]
            new_position = (x + dx, y + dy)

            # Update the position, path, and fitness
            self.position = new_position
            self.path.append(new_position)
            self.fitness = self.calculate_fitness()
        

    def move_backward(self, direction):
        """
        Move the knight backward to trace back if the applied move is illegal.

        Parameters:
        - direction: An integer from 1 to 8 representing the direction of the previous move.
        """
        reverse_move_dict = {
            1: (-2, -1),
            2: (-1, -2),
            3: (1, -2),
            4: (2, -1),
            5: (2, 1),
            6: (1, 2),
            7: (-1, 2),
            8: (-2, 1)
        }

        if direction in reverse_move_dict:
            x, y = self.position
            dx, dy = reverse_move_dict[direction]
            new_position = (x + dx, y + dy)

            # Update the position and fitness
            self.position = new_position
            if self.path:
                self.path.pop()  # Remove the last position from the path if the list is not empty
            self.fitness = self.calculate_fitness()
        else:
            print("Invalid direction. Please choose a direction from 1 to 8.")

    def check_moves(self):
        """
        Check the validity of each move in the chromosome array.
        Correct illegal moves by canceling the move using move_backward (direction).
        Test other moves by cycling forward or backward if needed.
        """
        # Determine the direction of the cycle (randomly chosen and remains the same for the entire set of moves)
        cycle_direction = random.choice([-1, 1])  # -1 for backward, 1 for forward

        for move in self.chromosome.genes:
            direction = self.get_valid_direction(move)
            if direction is not None:
                # If the move is valid, move forward
                self.move_forward(direction)
            else:
                # If the move is invalid, cycle forward or backward
                cycle_moves = list(range(1, 9)) if cycle_direction == 1 else list(range(8, 0, -1))
                for new_direction in cycle_moves:
                    if self.get_valid_direction((0, 0), new_direction):
                        # If a valid move is found, move forward and break the loop
                        self.move_forward(new_direction)
                        break
                else:
                    # If no valid move is found, move backward (retain the last move)
                    last_direction = move[0] if move else None
                    self.move_backward(last_direction)

    def get_valid_direction(self, move, direction=None):
        """
        Check the validity of a move using move_forward (direction).
        Return the valid direction if the move is valid, otherwise, return None.

        Parameters:
        - move: The move to be checked.
        - direction: The direction to be checked if provided.

        Returns:
        - direction: The valid direction if the move is valid, otherwise, None.
        """
        temp_knight = Knight(position=self.position, chromosome=self.chromosome)
        temp_knight.move_forward(direction if direction else move[0])

        if temp_knight.position not in temp_knight.path:
            return direction

        return None
    
    def evaluate_fitness(self):
        """
        Loop through the knight’s path and increment the fitness value by one until an invalid move is encountered.
        If the knight has visited all squares on the chessboard, the fitness value is equal to 64.
        """
        unique_positions = set(self.path)
        visited_squares = len(unique_positions)

        if visited_squares == 64:
            self.fitness = 64  # The knight has visited all squares on the chessboard
        else:
            self.fitness = visited_squares

class Population:
    def __init__(self, population_size=50):
        """
        Initialize a Population instance.

        Parameters:
        - population_size: The size of the population (default is 50).
        """
        self.population_size = population_size
        self.generation = 1
        self.knights = self.init()

    def init(self):
        """
        Generate the list of knights for the initial population.
        Initialize the number of generations to 1.

        Returns:
        - knights: List of Knight instances.
        """
        return [Knight() for _ in range(self.population_size)]

    def check_population(self):
        """
        Loop through the knights of the population and check the validity of their moves using check_moves().
        """
        for knight in self.knights:
            knight.check_moves()

    def evaluate(self):
        """
        Evaluate the fitness of every individual/knight in the population using evaluate_fitness().
        Returns the best knight with its fitness.

        Returns:
        - max_fit: The maximum fitness value in the population.
        - best_knight: The best knight with its fitness.
        """
        for knight in self.knights:
            knight.evaluate_fitness()

        best_knight = max(self.knights, key=lambda x: x.fitness)
        return best_knight.fitness, best_knight
    
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
    
    def create_new_generation(self, mutation_rate=0.1):
        new_generation = []

        while len(new_generation) < self.population_size:
            parents = self.tournament_selection(size=2)

            # Perform crossover on parents
            offspring1 = parents[0].chromosome.crossover(parents[1].chromosome)
            offspring2 = parents[1].chromosome.crossover(parents[0].chromosome)

            # Create new knights with the crossover results
            knight1 = Knight(chromosome=offspring1)
            knight2 = Knight(chromosome=offspring2)

            # Mutate offspring
            knight1.chromosome.mutate(mutation_rate)
            knight2.chromosome.mutate(mutation_rate)

            # Add offspring to the new generation
            new_generation.extend([knight1, knight2])

        # Replace the old generation with the new one
        self.knights = new_generation
        self.generation += 1


def draw_chessboard(screen, window_size):
    square_size = window_size[0] // 8
    colors = [(255, 255, 255), (0, 0, 0)]

    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))



def main():
    pygame.init()
    clock = pygame.time.Clock()

    window_size = (600, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Knight's Tour")

    population_size = 50
    population = Population(population_size)

    knight_image = pygame.image.load("knight tour/download (1).png")
    
    knight_image = pygame.transform.scale(knight_image, (window_size[0] // 8, window_size[0] // 8))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        population.check_population()
        max_fit, best_solution = population.evaluate()

        if max_fit == 64:
            break

        population.create_new_generation()

        screen.fill((255, 255, 255))
        draw_chessboard(screen, window_size)
        best_solution.draw_solution(screen, knight_image)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()