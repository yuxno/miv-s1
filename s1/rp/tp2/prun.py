from math import inf
import pygame
import time

MAX = +1
MIN = -1

class Play:
    @staticmethod
    def minimaxAlphaBetaPruning(node, depth, alpha=-inf, beta=+inf, player=MAX):
        if depth == 0:
            # Display the current node's value and mark it as explored
            print("Exploring node at depth", depth, "with value", node.value)
            node.display(screen, explored=True, depth=depth, color=(65, 105, 225))
            pygame.display.update()
            time.sleep(1)
            return node.value  # Return the node's value
        else:
            node.display(screen, explored=True, depth=depth,color=(65,105,225))  # Change color to blue for explored nodes
            pygame.display.update()
            time.sleep(1)
            if player == MAX:
                node.value = -inf
                node.path = None
                child = node.leftChild
                left=child
                child.display(screen, explored=True, depth=depth-1,color=(65,105,225))  # Change color to red for explored nodes
                pygame.display.update()
                time.sleep(1)
                node.display(screen, explored=True, depth=depth,color=(65,105,225),child=child,childColor=(65,105,225),alpha=alpha,beta=beta) #to draw the link 
                pygame.display.update()
                time.sleep(1)
                child_value = Play.minimaxAlphaBetaPruning(child, depth - 1, alpha, beta, -player)
                if child_value > node.value:
                    node.value = child_value
                    node.path = child
                    child.display(screen, explored=True, depth=depth-1,color=(144, 12, 63))  
                    pygame.display.update()
                    time.sleep(1)
                    node.display(screen, explored=True, depth=depth,color=(65,105,225),child=child,childColor=(144, 12, 63),alpha=alpha,beta=beta)
                    pygame.display.update()
                    time.sleep(1)
                if node.value >= beta:
                    return node.value
                alpha=max(alpha,node.value)
                node.display(screen, explored=True, depth=depth,color=(65,105,225),alpha=alpha,beta=beta)
                pygame.display.update()
                time.sleep(1)

                child = node.rightChild
                child.display(screen, explored=True, depth=depth-1,color=(65,105,225))  # Change color to red for explored nodes
                pygame.display.update()
                time.sleep(1)
                child_value = Play.minimaxAlphaBetaPruning(child, depth - 1, alpha, beta, -player)
                if child_value > node.value:
                    node.value = child_value
                    node.path = child
                    child.display(screen, explored=True, depth=depth-1,color=(144, 12, 63))  # Change color to red for explored nodes
                    pygame.display.update()
                    time.sleep(1)
                    node.display(screen, explored=True, depth=depth,color=(65,105,225),child=child, childColor=(144, 12, 63),alpha=alpha,beta=beta)
                    pygame.display.update()
                    time.sleep(1)
                    left.display(screen, explored=True, depth=depth-1,color=(65,105,225))
                    pygame.display.update()
                    time.sleep(1)
                    node.display(screen, explored=True, depth=depth,color=(65,105,225),child=left,childColor=(65,105,225),alpha=alpha,beta=beta)
                    pygame.display.update()
                    time.sleep(1)
                if node.value >= beta:
                    return node.value
                alpha=max(alpha,node.value)
                node.display(screen, explored=True, depth=depth,color=(65,105,225),alpha=alpha,beta=beta)
                pygame.display.update()
                time.sleep(1)
                #alpha = max(alpha, node.value)
                #graphical updates
            else:
                # node.display(screen, explored=True, depth=depth,color=(65,105,225),alpha=alpha,beta=beta)  # Change color to red for explored nodes
                # pygame.display.update()
                # time.sleep(1)
                node.value = +inf
                node.path = None
                child = node.leftChild
                left=child
                child.display(screen, explored=True, depth=depth-1,color=(65,105,225))  # Change color to red for explored nodes
                pygame.display.update()
                time.sleep(1)
                child_value = Play.minimaxAlphaBetaPruning(child, depth - 1, alpha, beta, -player)
                if child_value < node.value:
                    node.value = child_value
                    node.path = child
                    child.display(screen, explored=True, depth=depth-1,color=(144, 12, 63))  # Change color to red for explored nodes
                    pygame.display.update()
                    time.sleep(1)
                    node.display(screen, explored=True, depth=depth,color=(65,105,225),child=child,childColor=(144, 12, 63),alpha=alpha,beta=beta)
                    pygame.display.update()
                    time.sleep(1)
                if node.value <= alpha:
                    return node.value
                beta=min(beta,node.value)
                node.display(screen, explored=True, depth=depth,color=(65,105,225),alpha=alpha,beta=beta)
                pygame.display.update()
                time.sleep(1)
                # beta = min(beta, node.value)
                child = node.rightChild
                child.display(screen, explored=True, depth=depth-1,color=(65,105,225))  # Change color to red for explored nodes
                pygame.display.update()
                time.sleep(1)
                child_value = Play.minimaxAlphaBetaPruning(child, depth - 1, alpha, beta, -player)
                if child_value < node.value:
                    node.value = child_value
                    node.path = child
                    child.display(screen, explored=True, depth=depth-1,color=(144, 12, 63))  # Change color to red for explored nodes
                    pygame.display.update()
                    time.sleep(1)
                    node.display(screen, explored=True, depth=depth,color=(65,105,225),child=child,childColor=(144, 12, 63),alpha=alpha,beta=beta)
                    pygame.display.update()
                    time.sleep(1)
                    left.display(screen, explored=True, depth=depth-1,color=(65,105,225))
                    pygame.display.update()
                    time.sleep(1)
                    node.display(screen, explored=True, depth=depth,color=(65,105,225),child=left,childColor=(65,105,225),alpha=alpha,beta=beta)
                    pygame.display.update()
                    time.sleep(1)
                if node.value <= alpha:
                    return node.value
                beta=min(beta,node.value)
                
                node.display(screen, explored=True, depth=depth,color=(65,105,225),alpha=alpha,beta=beta)
                pygame.display.update()
                time.sleep(1)
                #beta = min(beta, node.value)
            return node.value

class Node:
    def __init__(self, parent=None, side=None, depth=0, value=None):
        self.parent = parent
        self.value = value
        self.path = None
        self.leftChild = None
        self.rightChild = None
        self.color = (99, 97, 97)  # Initial color: Gray

        if self.parent is None:
            self.position = (600, 150)  # The position of the root node
            self.horizontal_spacing = 500  # Adjust the horizontal spacing
        else:
            self.horizontal_spacing = parent.horizontal_spacing / 2  # Decrease spacing for child nodes
            if side == "L":
                self.position = (parent.position[0] - self.horizontal_spacing, parent.position[1] + 100)
            else:
                self.position = (parent.position[0] + self.horizontal_spacing, parent.position[1] + 100)

    
    def display(self, screen, explored=False, depth=4, color=(255, 0, 0), child=None,childColor=(0,0,0), alpha=None, beta=None):
        if self.position:
            color = color if explored else self.color
            Tree.draw_triangle(screen, self.position[0], self.position[1], depth, color=color)

            if self.value is not None:
                font = pygame.font.Font(None, 24)
                text = font.render(str(self.value), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (self.position[0], self.position[1])
                screen.blit(text, text_rect)

                if depth!=0:
                    if alpha is not None:
                        alpha_text = font.render(f"α={alpha}", True, (0, 0, 0))
                        alpha_rect = alpha_text.get_rect()
                        alpha_rect.topleft = (text_rect.topleft[0] - 30, text_rect.topleft[1] - 90)
                        
                    
                        screen.fill((192, 192, 192), (text_rect.topleft[0] - 30, text_rect.topleft[1] - 90, alpha_rect.width + 30, alpha_rect.height))
                        
                        screen.blit(alpha_text, alpha_rect)

                    
                    if beta is not None:
                        beta_text = font.render(f"β={beta}", True, (0, 0, 0))
                        beta_rect = beta_text.get_rect()
                        beta_rect.topleft = (text_rect.topleft[0] - 30, text_rect.topleft[1] - 70)

                        screen.fill((192, 192, 192), (text_rect.topleft[0] - 30, text_rect.topleft[1] - 70, beta_rect.width + 30, beta_rect.height))
                        
                        screen.blit(beta_text, beta_rect)



                if child:
                    pygame.draw.line(screen, childColor, self.position, child.position, 2)
class Tree:
    def __init__(self):
        self.root_node = Node(parent=None)
        self.depth_labels = {}  # Dictionary to store depth labels
        self.label_x = 20  

    def createEmptyTree(self, node, depth, values, player=MAX):
        if depth==4:
            node.value=-inf
        if depth == 1:
            if values:
                node.leftChild = Node(parent=node, side="L", depth=depth, value=values.pop(0))
                if values:
                    node.rightChild = Node(parent=node, side="R", depth=depth, value=values.pop(0))
            else:
                # If no more values, it's a leaf node, don't change value
                return
        else:
            if player == MAX:
                node.leftChild = Node(parent=node, side="L", depth=depth, value=+inf)
                node.rightChild = Node(parent=node, side="R", depth=depth, value=+inf)
            else:
                node.leftChild = Node(parent=node, side="L", depth=depth, value=-inf)
                node.rightChild = Node(parent=node, side="R", depth=depth, value=-inf)

            self.createEmptyTree(node.leftChild, depth - 1, values, -player)
            self.createEmptyTree(node.rightChild, depth - 1, values, -player)

    @staticmethod
    def draw_triangle(surface, x, y, depth, color=(255, 255, 255)):
        if depth % 2 != 0:
            points = [(x, y + 20), (x + 20, y - 20), (x - 20, y - 20)]
        else:
            points = [(x, y - 20), (x + 20, y + 20), (x - 20, y + 20)]
        pygame.draw.polygon(surface, color, points)

    def draw_lines_between_nodes(self, node, depth):
        if node.leftChild:
            pygame.draw.line(screen, (99, 97, 97), node.position, node.leftChild.position, 2)
            self.draw_lines_between_nodes(node.leftChild, depth - 1)
        if node.rightChild:
            pygame.draw.line(screen, (99, 97, 97), node.position, node.rightChild.position, 2)
            self.draw_lines_between_nodes(node.rightChild, depth - 1)

    def drawTree(self, node, depth):
        if node:
            if node.position:
                # Draw the node first
                node.display(screen, depth=depth)
                self.draw_triangle(screen, node.position[0], node.position[1], depth, color=node.color)

                if node.value is not None:
                    font = pygame.font.Font(None, 24)
                    text = font.render(str(node.value), True, (255, 255, 255))
                    text_rect = text.get_rect()
                    text_rect.center = (node.position[0], node.position[1])
                    screen.blit(text, text_rect)
                else:
                    # Display "None" for empty nodes
                    font = pygame.font.Font(None, 24)
                    text = font.render("None", True, (255, 255, 255))
                    text_rect = text.get_rect()
                    text_rect.center = (node.position[0], node.position[1])
                    screen.blit(text, text_rect)

                # Draw lines between nodes after drawing the current node
                self.draw_lines_between_nodes(node, depth)

                # Depth labels and recursion
                if depth not in self.depth_labels:
                    max_min_text = "MAX" if depth % 2 == 0 else "MIN"
                    font = pygame.font.Font(None, 24)
                    max_min_label = font.render(max_min_text, True, (0, 0, 255))
                    label_rect = max_min_label.get_rect()
                    label_rect.topleft = (self.label_x, node.position[1])
                    screen.blit(max_min_label, label_rect)
                    self.depth_labels[depth] = max_min_text

                # Recur for child nodes
                self.drawTree(node.leftChild, depth - 1)
                self.drawTree(node.rightChild, depth - 1)



def main():
    # Initialize pygame
    pygame.init()

    # Create the screen
    global screen
    w = 1200  # The width of the window
    h = 800  # The height of the window
    screen = pygame.display.set_mode((w, h))

    # Title
    pygame.display.set_caption("MINIMAX with Alpha-Beta Pruning")

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
            tree.drawTree(tree.root_node, depth)
            Play.minimaxAlphaBetaPruning(tree.root_node, depth)
            pygame.display.update()
            time.sleep(1.5)
            draw = False

if __name__ == "__main__":
    main()
