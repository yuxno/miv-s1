from math import inf
import pygame
import time

MAX = +1 
MIN = -1

class Play:
    
    @staticmethod
    def minimax(node, depth, player=MAX):
        pass
        
    @staticmethod
    def minimaxAlphaBetaPruning(screen, node, depth, alpha=-inf, beta=+inf, player=MAX):
        pass        

class Node:
    def __init__(self, parent=None, side=None, depth=0, value=None):
        self.parent = parent
        self.value = value
        self.path = None        
        self.leftChild = None
        self.rightChild = None

        if self.parent == None:
            self.position = (600,100)
        else:
            if side == "L":
                self.position =(self.parent.position)        
            else:
                self.position = # The position of the node if it's a right child

    def display(self, color, player):
        pass

class Tree:
    def __init__(self):
        self.root_node = Node(parent=None)
                      
    def createEmptyTree(self, node, depth, values):     
        
        self.value=None
        self.leftchild=None
        self.rightchild=None

        pass

    def drawTree(self, node, depth, player):
        pass

def main():
    # Initialize pygame
    pygame.init()

    # Create the screen
    global screen
    w = # The width of the window
    h = # The height of the window 
    screen = pygame.display.set_mode(((w, h)))

    # Title
    pygame.display.set_caption("MINIMAX")

    tree = Tree()
    values = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
    depth = 4

    # Game loop
    running = True   
    draw = True    
    
    while running:

        # RGB coloring of the screen
        screen.fill((192, 192, 192))
        
        # Add the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False   

        if draw == True:   
            tree.createEmptyTree(tree.root_node, depth, values)
            tree.drawTree(tree.root_node, depth, player=MAX)
            pygame.display.update()
            time.sleep(1.5)            
            draw = False         

if __name__ == "__main__":
    main()
   

    
    
