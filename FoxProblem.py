"""
Programming Assignment 1 Created on Sat 19 Sep, 2020
@author: Mingi Jeong
@ ID: F00422M
"""
# for tuple operation
import operator

class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)

        self.goal_found = False

        self.total_number_of_chicken = self.start_state[0]
        self.total_number_of_fox = self.start_state[1]

    # get successor states for the given state
    def get_successors(self, state):
        blank_successor_list = []
        result_successor = self.succesor_helper(state, blank_successor_list)
        return result_successor

    # goal test method
    def goal_test(self, state):
        if state == self.goal_state and self.subtract_operator(self.start_state, state) == self.start_state:
            return True
        return False

    # for subtracting tuples (it is useful to derive a certain state from the start state)
    def subtract_operator(self, before_tuple, subtract_tuple):
        return (tuple(map(operator.sub, before_tuple, subtract_tuple)))

    # successor_helper for get_successor function
    def succesor_helper(self, state, successor_list):
        # we already reached the goal state
        if self.goal_test(state):
            print("Already reached the goal")
            return successor_list

        # we did not reached the goal state, there should be a successor(s)
        else:
            if state[2] == 1: # boat is located at this side
                # chicken moving 1
                if state[0] >= 1:
                    expected_state_here = self.subtract_operator(state, (1,0,1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here0")
                        successor_list.append(expected_state_here)

                # fox moving 1
                if state[1] >= 1:
                    expected_state_here = self.subtract_operator(state, (0,1,1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here1")
                        successor_list.append(expected_state_here)

                # fox, chicken moving each 1
                if state[0] >= 1 and state[1] >= 1:
                    expected_state_here = self.subtract_operator(state, (1,1,1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    #print("expected here", expected_state_here)
                    #print("expected there", expected_state_there)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here2")
                        successor_list.append(expected_state_here)

                # fox moving 2
                if state[1] >= 2:
                    expected_state_here = self.subtract_operator(state, (0,2,1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here3")
                        successor_list.append(expected_state_here)

                # chicken moving 2
                if state[0] >= 2:
                    expected_state_here = self.subtract_operator(state, (2,0,1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here4")
                        successor_list.append(expected_state_here)

            else: # boat is located at the other side
                # chicken moving 1
                if self.total_number_of_chicken - state[0] >= 1:
                    expected_state_here = self.subtract_operator(state, (-1,0,-1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here5")
                        successor_list.append(expected_state_here)

                # fox moving 1
                if self.total_number_of_fox - state[1] >= 1:
                    expected_state_here = self.subtract_operator(state, (0,-1,-1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here6")
                        successor_list.append(expected_state_here)

                # fox, chicken moving each 1
                if self.total_number_of_chicken - state[0] >= 1 and self.total_number_of_fox - state[1] >= 1:
                    expected_state_here = self.subtract_operator(state, (-1,-1,-1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here7")
                        successor_list.append(expected_state_here)

                # fox moving 2
                if self.total_number_of_fox - state[1] >= 2:
                    expected_state_here = self.subtract_operator(state, (0,-2,-1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here8")
                        successor_list.append(expected_state_here)

                # chicken moving 2
                if self.total_number_of_chicken - state[0] >= 2:
                    expected_state_here = self.subtract_operator(state, (-2,0,-1))
                    expected_state_there = self.subtract_operator(self.start_state, expected_state_here)
                    # legality check
                    if self.legality_check(expected_state_here) is True and self.legality_check(expected_state_there) is True:
                        #print("here9")
                        successor_list.append(expected_state_here)

        return successor_list

    # After getting successors(expected), it checks legality
    def legality_check(self, expected_state):
        # expected state input
        if expected_state is not None:
            # Number of fox is more than number of chicken
            if expected_state[1] > expected_state[0]:
                # Number of chicken is 0 so that number of foxes can be more
                if expected_state[0] == 0:
                    number_of_index = len(self.start_state)
                    # subtracted or added new state is valid or not
                    for i in range(number_of_index):
                        if expected_state[i] > self.start_state[i] or expected_state[i] < 0:
                            return False
                    # pass of validity test
                    return True
                return False

            # Number of fox is less than or equal to number of chicken
            else:
                number_of_index = len(self.start_state)
                # subtracted or added new state is valid or not
                for i in range(number_of_index):
                    if expected_state[i] > self.start_state[i] or expected_state[i] < 0:
                        return False
                # pass of validity test
                return True

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((3, 3, 1))
    print(test_cp.get_successors((3, 1, 0)))
    print(test_cp)
