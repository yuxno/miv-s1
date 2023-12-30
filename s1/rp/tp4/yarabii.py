import random
from util import MOVEMENTS_DICT, movements
import pygame
import sys
MUTATION_RATE = 0.01

class Chromosome:
    def __init__(self, genes=None):
        self.genes = [random.randint(1, 8) for _ in range(63)] if genes is None else genes

    def crossover(self, partner):
        crossover_point = random.randint(0, len(self.genes) - 1)
        child_genes1 = self.genes[:crossover_point] + partner.genes[crossover_point:]
        child_genes2 = partner.genes[:crossover_point] + self.genes[crossover_point:]
        
        return Chromosome(child_genes1), Chromosome(child_genes2)

    def mutation(self):
        for i in range(len(self.genes)):
            if random.random() < MUTATION_RATE:
                self.genes[i] = random.randint(1, 8)



class Knight:
    def __init__(self, chromosome=None):
        self.position = (0, 0)
        self.chromosome = Chromosome() if chromosome is None else chromosome
        self.path = [self.position]
        self.fitness = 0

    def move_forward(self, direction):
        current_move = movements[direction - 1]
        move_x, move_y = MOVEMENTS_DICT[current_move]
        x, y = self.position
        new_position = (x + move_x, y + move_y)
        self.position = new_position

    def move_backward(self, direction):
        current_move = movements[direction - 1]
        move_x, move_y = MOVEMENTS_DICT[current_move]
        x, y = self.position
        new_position = (x - move_x, y - move_y)
        self.position = new_position

    def check_moves(self):
        step = random.choice([-1, 1])
        
        for direction in self.chromosome.genes:
            self.move_forward(direction)
            if self.is_valid_move(self.position, self.path):
                self.path.append(self.position)
            else:
                self.move_backward(direction)
                new_direction = direction % 8 + 1 if step == 1 else (direction - 2) % 8 + 1
                self.move_forward(new_direction)

                while not self.is_valid_move(self.position, self.path) and (new_direction != direction):
                    self.move_backward(new_direction)
                    new_direction = new_direction % 8 + 1 if step == 1 else (new_direction - 2) % 8 + 1
                    self.move_forward(new_direction)

                self.path.append(self.position)

    def is_valid_move(self, position, path):
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8 and position not in path

    def evaluate_fitness(self):
        path = []
        for position in self.path:
            if not self.is_valid_move(position, path):
                break
            path.append(position)
        self.fitness = len(path)





class Population:
	def __init__(self, population_size):
		self.population_size = population_size
		self.generation = 1
		self.knights = [Knight() for _ in range(self.population_size)]


	def check_population(self):
		for knight in self.knights:
			knight.check_moves()

	def evaluate(self):
		for knight in self.knights:
			knight.evaluate_fitness()
			
		best_knight = max(self.knights, key=lambda knight: knight.fitness)
		return best_knight.fitness, best_knight

	def tournament_selection(self, size=3):
		tournament_sample = random.sample(self.knights, size)
		winner1 = max(tournament_sample, key=lambda knight: knight.fitness)
		tournament_sample.remove(winner1)
		winner2 = max(tournament_sample, key=lambda knight: knight.fitness)
		return winner1, winner2

	def create_new_generation(self):
		new_generation = []
		for _ in range(self.population_size // 2):
			parent1, parent2 = self.tournament_selection()
			offspring1, offspring2  = parent1.chromosome.crossover(parent2.chromosome)

			offspring1.mutation()
			offspring2.mutation()

			knight1 = Knight(chromosome=offspring1)
			knight2 = Knight(chromosome=offspring2)

			new_generation.extend([knight1, knight2])
			
		self.knights = new_generation
		self.generation += 1



def draw_solution(screen, path, knight_image):
    square_size = screen.get_width() // 8
    move_index = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if move_index < len(path):
            x, y = path[move_index][1] * square_size, path[move_index][0] * square_size
            screen.blit(knight_image, (x, y))
            pygame.display.update()
            move_index += 1
            pygame.time.delay(1000)  # Delay between moves in milliseconds
        else:
            break

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
    

    knight_image = pygame.image.load("knight tour/img.jpg")  
    knight_image = pygame.transform.scale(knight_image, (window_size[0] // 8, window_size[0] // 8))
    

    while True:
        population.check_population()
        maxFit, best_solution = population.evaluate()
        print(f"Gen : {population.generation}, Fitness : {maxFit}")
		
        if maxFit == 64:
            break
        population.create_new_generation()


    running = True
    while running:

        screen.fill((255, 255, 255))
        draw_chessboard(screen, window_size)
        solution_path = best_solution.path
        draw_solution(screen,solution_path, knight_image)
        pygame.display.flip()

        # Control frame rate
        clock.tick(10)  # Adjust the frame rate as needed (e.g., 10 FPS)


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()