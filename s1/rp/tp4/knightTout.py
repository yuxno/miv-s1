import random
import sys
import pygame

class Chromosome:
    def __init__(self, genes=None):
        if genes is None:
            self.genes = self.generate_random_genes()
        else:
            self.genes = genes

    def generate_random_genes(self):
        return [(random.randint(1, 8), random.randint(1, 8)) for _ in range(63)]
    
    def crossover(self, partner):

        crossover_point = random.randint(1, len(self.genes) - 1)

        # Take genes from the first part of self and the second part of the partner
        new_genes1 = self.genes[:crossover_point] + partner.genes[crossover_point:]
        new_genes2 = partner.genes[:crossover_point] + self.genes[crossover_point:]

        # Create new Chromosome instances with the combined genes
        offspring1 = Chromosome(genes=new_genes1)
        offspring2 = Chromosome(genes=new_genes2)

        return offspring1, offspring2
    
    def mutate(self, mutation_rate=0.01):
        """
        Mutate the genes with a certain probability.

        Parameters:
        - mutation_rate: The probability of mutation for each gene.

        Returns:
        - None
        """
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                # Mutate the gene by replacing it with a new random move
                self.genes[i] = (random.randint(1, 8))


class Knight:
    def __init__(self,position,chromosome):
        self.position = position
        self.chromosome = chromosome
        self.path = [position]
        self.fitness = 0

    def init(self,chromosome):
        if chromosome is None:
            self.chromosome = Chromosome()
        else:
            self.chromosome = chromosome
        
        self.position= (0,0)
        self.fitness=0
        self.path = [self.position]

    def move_forward(self,direction):

        move_dict = {
            1: (1, 2),  
            2: (2, 1),  
            3: (2,-1),
            4: (1, -2),
            5: (-1,-2),
            6: (-2,-1),
            7: (-2,1),
            8: (-1,2)
        }

        if direction in move_dict:
            x, y = self.position
            dx, dy = move_dict[direction]
            new_position = (x + dx, y + dy)

            # Update the position, path, and fitness
            self.position = new_position
            self.path.append(new_position)
            self.fitness= self.evaluate_fitness()

        
    def move_backward(self,direction):
        # Move the knight backward to trace back if the applied move is illegal.
        reverse_move_dict = {
            1: (-1, -2),  
            2: (-2, -1),  
            3: (-2, 1),
            4: (-1, 2),
            5: (1,2),
            6: (2,1),
            7: (2,-1),
            8: (1,-2)
        }

        if direction in reverse_move_dict:
            x, y = self.position
            dx, dy = reverse_move_dict[direction]
            new_position = (x + dx, y + dy)

            # Update the position and fitness
            self.position = new_position
            if self.path:
                self.path.pop()  # Remove the last position from the path if the list is not empty
            
            self.fitness= self.evaluate_fitness()
    
    def check_moves(self):
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
                    if self.get_valid_direction(move, new_direction):
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
        unique_positions = set()

        for position in self.path:
            if position not in unique_positions:
                unique_positions.add(position)
                self.fitness += 1
            else:
                break

        return self.fitness
            


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
        return [Knight(position=(0, 0), chromosome=Chromosome()) for _ in range(self.population_size)]


    def check_population(self):
        for knight in self.knights:
            knight.check_moves()
            knight.evaluate_fitness()


    def evaluate(self):
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
    
    #ghalta
    def create_new_generation(self, mutation_rate=0.1):
        new_generation = []

        while len(new_generation) < self.population_size:
            parents = self.tournament_selection(size=3)

            # Perform crossover
            offspring1, offspring2 = parents[0].chromosome.crossover(parents[1].chromosome)

            # Perform mutation
            offspring1.mutate(mutation_rate)
            offspring2.mutate(mutation_rate)

            # Add offspring to the new generation
            new_generation.extend([offspring1, offspring2])

        # Update the population with the new generation
        self.knights = new_generation
        self.generation += 1




def draw_solution(screen, path, knight_image):
    square_size = screen.get_width() // 8
    for i, position in enumerate(path):
        x, y = position[1] * square_size, position[0] * square_size
        screen.blit(knight_image, (x, y))
        pygame.display.update()
        pygame.time.delay(200)

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

    knight_image = pygame.image.load("knight tour/download (1).png")  # Replace with the path to your knight image
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
        draw_solution(screen, best_solution.path, knight_image)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

