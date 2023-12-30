from math import inf
import pygame
import time

MAX = +1
MIN = -1

class Play:
    @staticmethod
    def minimax(node, depth, player=MAX):
        if depth == 0:
            # Display the current node's value and mark it as explored
            print("Exploring node at depth", depth, "with value", node.value)
            node.display(screen, explored=True)  # Change color to red for explored nodes
            pygame.display.update()
            time.sleep(1)
            return node.value  # Return the node's value
        else:
            if player == MAX:
                node.value = -inf
                node.path = None
                child = node.leftChild
                child_value = Play.minimax(child, depth - 1, -player)
                if child_value > node.value:
                    node.value = child_value
                    node.path = child
                    node.display(screen, explored=True, depth=depth)  # Change color to red for explored nodes
                    pygame.display.update()
                    time.sleep(1)
                child = node.rightChild
                child_value = Play.minimax(child, depth - 1, -player)
                if child_value > node.value:
                    node.value = child_value
                    node.path = child
                    node.display(screen, explored=True, depth=depth)  # Change color to red for explored nodes
                    pygame.display.update()
                    time.sleep(1)
                return node.value
            else:
                node.value = +inf
                node.path = None
                child = node.leftChild
                child_value = Play.minimax(child, depth - 1, -player)
                if child_value < node.value:
                    node.value = child_value
                    node.path = child
                    node.display(screen, explored=True, depth=depth)  # Change color to red for explored nodes
                    pygame.display.update()
                    time.sleep(1)
                child = node.rightChild
                child_value = Play.minimax(child, depth - 1, -player)
                if child_value < node.value:
                    node.value = child_value
                    node.path = child
                    node.display(screen, explored=True, depth=depth)  # Change color to red for explored nodes
                    pygame.display.update()
                    time.sleep(1)
                return node.value

class Node:
    def __init__(self, parent=None, side=None, depth=0, value=None):
        self.parent = parent
        self.value = value
        self.path = None
        self.leftChild = None
        self.rightChild = None
        self.color = (169, 169, 169)  # Initial color: Gray

        if self.parent is None:
            self.position = (600, 40)  # The position of the root node
            self.horizontal_spacing = 500  # Adjust the horizontal spacing
        else:
            self.horizontal_spacing = parent.horizontal_spacing / 2  # Decrease spacing for child nodes

            if side == "L":
                self.position = (parent.position[0] - self.horizontal_spacing, parent.position[1] + 100)
            else:
                self.position = (parent.position[0] + self.horizontal_spacing, parent.position[1] + 100)

    def display(self, screen, explored=False, depth=0):
        if self.position:
            color = (255, 0, 0) if explored else self.color
            # Draw the triangle with the specified color
            Tree.draw_triangle(screen, self.position[0], self.position[1], depth, color=color)
            
            if self.value is not None:
                font = pygame.font.Font(None, 24)
                text = font.render(str(self.value), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (self.position[0], self.position[1])
                screen.blit(text, text_rect)

                if self.leftChild:
                    pygame.draw.line(screen, (0, 0, 0), self.position, self.leftChild.position, 2)
                if self.rightChild:
                    pygame.draw.line(screen, (0, 0, 0), self.position, self.rightChild.position, 2)

class Tree:
    def __init__(self):
        self.root_node = Node(parent=None)
        self.depth_labels = {}  # Dictionary to store depth labels
        self.label_x = 20  

    def createEmptyTree(self, node, depth, values):
        if depth == 1:
            if values:
                node.leftChild = Node(parent=node, side="L", depth=depth, value=values.pop(0))
                if values:
                    node.rightChild = Node(parent=node, side="R", depth=depth, value=values.pop(0))
        else:
            node.leftChild = Node(parent=node, side="L", depth=depth, value=None)
            node.rightChild = Node(parent=node, side="R", depth=depth, value=None)
            self.createEmptyTree(node.leftChild, depth - 1, values)
            self.createEmptyTree(node.rightChild, depth - 1, values)

    @staticmethod
    def draw_triangle(surface, x, y, depth, color=(255, 255, 255)):
        if depth % 2 != 0:
            points = [(x, y + 20), (x + 20, y - 20), (x - 20, y - 20)]
        else:
            points = [(x, y - 20), (x + 20, y + 20), (x - 20, y + 20)]
        pygame.draw.polygon(surface, color, points)

    def draw_lines_between_nodes(self, node, depth):
        if node.leftChild:
            pygame.draw.line(screen, (144, 12, 63), node.position, node.leftChild.position, 2)
            self.draw_lines_between_nodes(node.leftChild, depth - 1)
        if node.rightChild:
            pygame.draw.line(screen, (144, 12, 63), node.position, node.rightChild.position, 2)
            self.draw_lines_between_nodes(node.rightChild, depth - 1)

    def drawTree(self, node, depth):
        if node:
            if node.position:
                node.display(screen, depth=depth)
                self.draw_triangle(screen, node.position[0], node.position[1], depth, color=node.color)
                if node.value is not None:
                    font = pygame.font.Font(None, 24)
                    text = font.render(str(node.value), True, (255, 255, 255))
                    text_rect = text.get_rect()
                    text_rect.center = (node.position[0], node.position[1])
                    screen.blit(text, text_rect)

                # Display "MIN" or "MAX" label for each new depth level on the left side
                if depth not in self.depth_labels:
                    max_min_text = "MAX" if depth % 2 == 0 else "MIN"
                    font = pygame.font.Font(None, 24)
                    max_min_label = font.render(max_min_text, True, (0, 0, 255))  # Blue for MAX, Red for MIN
                    label_rect = max_min_label.get_rect()
                    label_rect.topleft = (self.label_x, node.position[1])
                    screen.blit(max_min_label, label_rect)
                    self.depth_labels[depth] = max_min_text  # Store the label for this depth

                self.draw_lines_between_nodes(node, depth)
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
            tree.drawTree(tree.root_node, depth)
            Play.minimax(tree.root_node, depth)
            pygame.display.update()
            time.sleep(1.5)
            draw = False

if __name__ == "__main__":
    main()
