import math

from PIL.ImageOps import expand

from BFS.trees import failure
from trees import Node
from trees import expand
from collections import deque


def breadth_first_search(problem):
  node = Node(problem.initial)
  if problem.is_goal(problem.initial):
    return  node
  fringe = deque([node])
  visited ={problem.initial}
  while fringe:
   node =  fringe.pop()
   for child in expand(problem,node):
       s=child.state
       if problem.is_goal(s):
           return child
       if s not in visited:
           visited.add(s)
           fringe.append(child)
  return failure



# from collections import deque
# from trees import Node  # Đảm bảo bạn có class Node được định nghĩa đúng
#
# def breadth_first_search(problem):
#     node = Node(problem.initial)
#     if problem.is_goal(node.state):
#         return node
#
#     fringe = deque([node])
#     visited = {node.state}
#
#     while fringe:
#         node = fringe.popleft()  # BFS dùng popleft()
#         for child in node.expand(problem):
#             s = child.state
#             if s not in visited:
#                 if problem.is_goal(s):
#                     return child
#                 visited.add(s)
#                 fringe.append(child)
#
#     return None