"""
Programming Assignment 1 Created on Sat 19 Sep, 2020
@author: Mingi Jeong
@ ID: F00422M
"""

from collections import deque
from SearchSolution import SearchSolution

# SearchNode class given by the problem
# to wrap state objects, keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent_node = parent  # each search node except the root has a parent node
        self.depth = 0  # to keep track of node depth
        self.branch_path = set()  # for path checking in dfs_search

def back_chaining(goal_node):
    reverse_path = []
    reverse_path.append(goal_node.state)

    # add parent continuously until root_node
    while goal_node.parent_node is not None:
        reverse_path.append(goal_node.parent_node.state)
        goal_node = goal_node.parent_node

    # reverse direction of added node sate
    original_path = reverse_path[::-1]
    return original_path

def bfs_search(search_problem):
    search_problem.goal_found = False
    ## initialization of node and solution
    root_node = SearchNode(search_problem.start_state)
    solution = SearchSolution(search_problem, "BFS")
    queue = deque([root_node])
    visited = set()

    # BFS implementation by FIFO
    while queue:
        fringe_node = queue.popleft()  # pop from the left
        # goal test
        if search_problem.goal_test(fringe_node.state):
            # solution exists and finish bfs_search
            solution.path = back_chaining(fringe_node)
            solution.nodes_visited = len(visited)  # visited_node number final update
            search_problem.goal_found = True
            return solution

        # visited test by set for efficiency
        if fringe_node.state not in visited:
            successors = search_problem.get_successors(fringe_node.state)
            for successor in successors:
                successor_node = SearchNode(successor, fringe_node)
                queue.append(successor_node)  # add to the right
            visited.add(fringe_node.state)  # visited set update after expanding fringe

    # when not finding a solution
    solution.nodes_visited = len(visited)  # visited_node number final update
    return solution


def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    search_problem.goal_found = False
    ## initialization of node and solution
    if node is None:
        node = SearchNode(search_problem.start_state)
    if solution is None:
        solution = SearchSolution(search_problem, "DFS")

    # first depth 0 node (root_node)
    node.branch_path.add(node.state)
    ## depth_limit = 0 test (Base case 1)
    if search_problem.goal_test(node.state):
        solution.path = back_chaining(node)
    solution.nodes_visited += 1

    ## when depth_limit is not 0 (recursive case)
    if depth_limit != 0:
        dfs_search_helper_path_check(search_problem, depth_limit, node, solution)

    return solution


def dfs_search_helper_path_check(search_problem, depth_limit, node, solution):
    # successors from input node
    successors = search_problem.get_successors(node.state)

    ## Base case 2
    if len(successors) == 0:
        print("no more successor")
        pass

    ## Recursive case (when there are successors from the given node)
    else:
        for successor in successors:
            successor_node = SearchNode(successor, node)  # node instantiation
            successor_node.depth = node.depth + 1  # update of depth increment

            ## Base case 3
            # in case depth limit is specified and the successor depth will be over the limit
            if depth_limit is not None and successor_node.depth > depth_limit:
                return

            # in case depth limit is not specified or the successor depth will not be over the limit
            ## Main recursive case
            else:
                # path checking and successor not existing in the branch path + goal not found yet
                if successor_node.state not in node.branch_path and search_problem.goal_found is False:
                    successor_node.branch_path = node.branch_path
                    successor_node.branch_path.add(successor_node.state)
                    solution.nodes_visited += 1

                    # goal check
                    if search_problem.goal_test(successor_node.state):
                        solution.path = back_chaining(successor_node)
                        search_problem.goal_found = True  # search problem goal found (bool) update
                        return

                    # recursive function
                    dfs_search_helper_path_check(search_problem, depth_limit, successor_node, solution)

                    # removal for memory efficiency
                    if search_problem.goal_found is False:
                        successor_node.branch_path.remove(successor_node.state)

                # path checking and successor already existing in the branch path
                else:
                    pass

def ids_search(search_problem, depth_limit=100):
    search_problem.goal_found = False
    solution = SearchSolution(search_problem, "IDS")
    for depth in range(depth_limit+1):
        ## initialization of node and solution
        root_node = SearchNode(search_problem.start_state)
        # IDS as per iteration depth
        dfs_search(search_problem,depth,root_node,solution)
        if len(solution.path) != 0:  # solution exist and finish ids_search
            break
        else:  # finding solution failed at a certain depth_limit
            print("This iteration %d failed" % depth)

    # finding solution failed after entire depth_limit and return
    return solution
