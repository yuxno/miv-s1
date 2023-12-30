from node import Node
from queue import Queue, PriorityQueue
from rushHourPuzzle import RushHourPuzzle

class Search:
    @staticmethod
    def astar_search(initial_state, heuristic=1):
        open = PriorityQueue()
        closed = list()

        init_node=Node(initial_state)
        #init.node.g
        open.put(init_node)
        step = 0
        while not open.empty():
            current=open.get()
            if current.state.isGoal():
                return current, step
            closed.append(current)
            step +=1 
            for action, successor in current.state.successorFunction():
                child=Node(successor,current,action, heuristic=heuristic)

                if (child.state.board not in [node.state.board for node in closed] and \
                    child.state.board not in [node.state.board for node in list(open.queue)]):
                    open.put(child)
                    print(action)  #just checking not working

                elif (child.state.board in [node.state.board for node in list(open.queue)]):
                    existing_node=None
                    for node in open.queue:
                        if node.state==child.state:
                            existing_node=node
                            break
                    if existing_node is not None and child.f >= existing_node.f:
                        open.queue.remove(existing_node)
                        open.put(child)
                elif (child.state.board not in [node.state.board for node in closed]):
                    existing_node=None
                    for node in closed:
                        if node.state==child.state:
                            existing_node=node
                            break
                    
                    if existing_node is not None and child.f>=existing_node.f:
                        continue
                    closed.remove(existing_node)
                    open.put(child)
        return None
    
def main():
    initial_state = RushHourPuzzle('tp1/rushHourPuzzle/2-a.csv')
    RushHourPuzzle.printRushHourBoard(initial_state.board)   
    goal_node, step = Search.astar_search(initial_state)
    print(f"Path cost: {goal_node.g}")
    print(f"Number of steps: {step}")
    print("Moves: {}".format(" ".join(map(str, goal_node.getSolution()))))

if __name__ == "__main__":
    main()
