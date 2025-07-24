from BFS.problems import RouteProblem
from BFS.trees import path_states
from maps import Map
from bfs import breadth_first_search
if __name__ == "__main__":
    romania = Map(
        {('O', 'Z'): 71, ('O', 'S'): 151, ('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118},
        {'A': (76, 497),  'O': (117, 580),  'S': (187, 463), 'T': (83, 414), 'Z': (92, 539)}
    )
    my_route = RouteProblem('O', 'T', map=romania)
    # print(my_route.is_goal('S'))
    # print(my_route.actions('A'))
    bfs= breadth_first_search(my_route)
    print(path_states(bfs))