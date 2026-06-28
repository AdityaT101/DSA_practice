#--=======================

# adjacency matrix
# arr = [[ 0 for j in range(0,6)] for i in range(0,6)]
# print(arr)
# arr=[]
# for i in range(0,6):
#     row = []
#     for j in range(0,6):
#         row.append(0)
#     arr.append(row)
# print(arr)

#--=======================

#  adjacency list
# edges = [
#             [0, 1],
#             [0, 2],
#             [1, 2],
#             [1, 3],
#             [2, 3]      ]
#
# # undirected graphs
# adj_dict = {}
# for a,b in edges:
#     if a not in adj_dict:
#         adj_dict[a] = []
#     if b not in adj_dict:
#         adj_dict[b] = []
#     adj_dict[a].append(b)
#     adj_dict[b].append(a)
#
# print(adj_dict)
#
# # directed graphs
# adj_dict = {}
# for a,b in edges:
#     if a not in adj_dict:
#         adj_dict[a] = []
#     adj_dict[a].append(b)
#
# print(adj_dict)

#--=======================

# from collections import deque
#
# queue = deque()
#
# queue.append(1)
# queue.append(2)
# queue.append(3)
#
# print(queue)

#--=======================
#--======================= BFS =======================
#--=======================

# from collections import deque
#
# adj_dict = {
#      0: [],
#      1: [2,6],
#      2: [1,3,4],
#      3: [2],
#      4: [2,5],
#      5: [4,8],
#      6: [1,7,9],
#      7: [6,8],
#      8: [7,5],
#      9: [6]
# }
#
# # create a visited list
# visited = [0]*10
# # mark the first element as visited
# visited[1] = 1
#
# # BFS works in FIFO manner
# queue = deque()
# queue.append(1)
#
# return_list = []
#
# while queue:
#     # grab element/key from the queue( pipe )
#     element = queue.popleft()
#
#     #return list just shows order of traversal...pretty much redundant for this logic
#     return_list.append(element)
#
#     # grab the neighbors of the element from adj_dict
#     for a in adj_dict[element]:
#         # # beofre adding to the queue , check in the visited list/array
#         if visited[a] != 1:
#             visited[a] = 1
#             queue.append(a)
#
# print(return_list)


#--=======================
#--======================= DFS =======================
#--=======================


# adj_dict = {
#      0: [],
#      1: [2,3],
#      2: [1,5,6],
#      3: [1,4,7],
#      4: [3,8],
#      5: [2],
#      6: [2],
#      7: [3,8],
#      8: [4,7]
# }
#
# # create a visited list
# visited = [0]*10
#
# dfs_return_list = []
#
# def dfs(element):
#     visited[element] = 1
#
#     dfs_return_list.append(element)
#
#     # iterates through all the neighbors
#     for a in adj_dict[element]:
#         if visited[a] != 1:
#             dfs(a)
#
# dfs(1)
# print(dfs_return_list)

#--=======================
#--======================= Number Of Islands =======================
#--=======================

# arr = [ [0,1,1,0],
#         [0,1,1,0],
#         [0,0,1,0],
#         [0,0,1,1],
#         [1,1,0,1] ]
#
# visited = [ [0]*len(arr[0]) for _ in range( 0, len(arr)) ]
# count = 0
#
# def DFS(row,col):
#     visited[row][col] = 1
#
#     if row+1 < len(arr) and arr[row+1][col] == 1 and visited[row+1][col] != 1:
#         DFS(row+1,col)
#
#     if row-1 >=0  and arr[row-1][col] == 1 and visited[row-1][col] != 1:
#         DFS(row-1,col)
#
#     if col+1 < len(arr[0]) and arr[row][col+1] == 1 and visited[row][col+1] != 1:
#         DFS(row,col+1)
#
#     if col-1 >=0 and arr[row][col-1] == 1 and visited[row][col-1] != 1:
#         DFS(row,col-1)
#
#
# # traverse through the arr matrix
# for row in range(0,len(arr)):
#     for col in range(0, len(arr[0])):
#         # only if Not visited, run the DFS traversal through it
#         # count represents the number of islands
#         if arr[row][col] == 1 and visited[row][col] != 1:
#             DFS(row,col)
#             count += 1
#
# print(count)

#--=======================
#--======================= Connected Components(graphs) =======================
#--=======================

# 1 -> 2 -> 3           4 -> 5 -> 6              7 -> 8

# adj_dict = {
#     0 : [],
#     1 : [2],
#     2 : [1,3],
#     3 : [2],
#     4 : [5],
#     5 : [4,6],
#     6 : [5],
#     7 : [8],
#     8 : [7]
# }
#
# visited = [0]*9
# count = 0
#
#
# def DFS(element):
#     # mark the starting point as visited in the visited array/list
#     visited[element] = 1
#
#     # find the corresponding value for the key in the dict
#     # and iterate through all the values
#     # update the visited array as you go ahead and call DFS on related values
#     for a in adj_dict[element]:
#         if visited[a] != 1:
#             DFS(a)
#
# # Iterate through all the elements and find the count of distinct sub-graphs
# for element in range( 1, len(adj_dict) ):
#     if visited[element] != 1:
#         DFS(element)
#         count += 1
#
# print(count)

#--=======================
#--======================= Flood Fill Algorithm(graphs) =======================
#--=======================

# arr = [ [1,1,1,0],
#         [2,2,0,0],
#         [2,2,2,0],
#         [2,2,0,2] ]
#
# row = 1
# col = 0
# new_color = 3
#
#
# def DFS(row,col):
#
#     arr[row][col] =3
#
#     if row+1 < len(arr) and arr[row+1][col] == 2:
#         DFS(row+1,col)
#     if row-1 >=0  and arr[row-1][col] == 2:
#         DFS(row-1,col)
#     if col+1 < len(arr[0]) and arr[row][col+1] == 2:
#         DFS(row,col+1)
#     if col-1 >=0 and arr[row][col-1] == 2:
#         DFS(row,col-1)
#
# DFS(row,col)
# print(arr)


#--=======================
#--======================= rotten Oranges(graphs) =======================
#--=======================


# from collections import deque
# queue = deque()
#
#
# arr = [ [2,1,1],
#         [1,1,0],
#         [0,1,1],
#         [0,1,1] ]
#
# visited = [ [0]*len(arr[0]) for i in range(0,len(arr)) ]
# print(visited)
# time = 0
#
# # find the occurences of rotten oragnes / 2's
# # append the occurences to the queue
# for row in range(0, len(arr)):
#     for col in range(0, len(arr[0])):
#         if arr[row][col] == 2:
#           if visited[row][col] != 1:
#              queue.append([row,col,time])
#
# max_time = 0
#
# while (queue):
#     # grab the first element from the queue
#     row, col, time = queue.popleft()
#     max_time  = max(max_time , time)
#
#     # mark that element as visited
#     visited[row][col] = 1
#
#     # now, for that element look up,down,left,right for 1 (fresh oranges)
#     # and then rot them
#     # right
#     if col+1 < len(arr[0]) and arr[row][col+1] == 1 and visited[row][col+1] != 1   :
#         queue.append([row, col+1, time+1])
#     # left
#     if col-1 >= 0 and arr[row][col-1] == 1 and visited[row][col-1] != 1 :
#         queue.append([row, col-1, time+1])
#     # up
#     if row-1 >= 0 and arr[row-1][col] == 1 and visited[row-1][col] != 1 :
#         queue.append([row-1, col, time+1])
#     # down
#     if row+1 < len(arr) and arr[row+1][col] == 1 and visited[row+1][col] != 1 :
#         queue.append([row+1, col, time+1])
#
# print(max_time)

#--=======================
#--======================= detet cycle in undirected graph ( BFS ) =======================
#--=======================


# UNDIRECTED GRAPH (from the image)
#
#                  (2) ----------- (5)
#                 /                   \
#               /                      \
#             (1)                      (7)
#               \                      /
#                \                   /
#                 (3) ----------- (6)
#                  |
#                  |
#                 (4)
#
# Cycle present:  1 -> 2 -> 5 -> 7 -> 6 -> 3 -> 1
# Leaf node:      4 (attached to 3)
#
# Adjacency list representation:
# adj_dict = {
#       1: [2, 3],
#       2: [1, 5],
#       3: [1, 4, 6],
#       4: [3],
#       5: [2, 7],
#       6: [3, 7],
#       7: [5, 6]
# }
#
# visited = [0]*8
# visited[0] = 0
# visited[1] = 1
#
# from collections import deque
# queue = deque()
# queue.append([1,0])
# # each element appended to the queue will be -> ( current element , origin)
# # so for 2, the combo will be -> (2,1)
# # so for 3, the combo will be -> (3,1)
# # so for 1, the combo will be -> (1,0), here 0 origin is arbitrary, can be -1 as well.
# cyclic = [False]
#
# while(queue):
#     # pop the leftmost element in the queue
#     current_element, parent = queue.popleft()
#     print( [current_element, parent] )
#
#     # in the ad_list, find the corresponding neighbors and add them into the queue as
#     for a in adj_dict[current_element]:
#         if visited[a] != 1:
#             visited[a] = 1
#             # add the element from the list and the corresponding parent
#             queue.append([ a, current_element])
#
#         elif( visited[a] == 1 and a != parent ):
#             cyclic[0] = True
#
# print( cyclic )


#--=======================
#--======================= detect cycle in undirected graph ( DFS ) =======================
#--=======================



# UNDIRECTED GRAPH (from the image)
#
#                  (2) ------- (5)
#                 /                \
#               /                   \
#             (1)                   (7)
#               \                   /
#                \                /
#                 (3) ------- (6)
#                  |
#                 |
#                (4)
#
# Cycle present:  1 -> 2 -> 5 -> 7 -> 6 -> 3 -> 1



# # Adjacency list representation:
# adj_dict = {
#       1: [2, 3],
#       2: [1, 5],
#       3: [1, 4, 6],
#       4: [3],
#       5: [2, 7],
#       6: [3, 7],
#       7: [5, 6]
#   }
#
# visited = [0]*8
# visited[0] = 1
# DFS_list = [1]
# cycle_found = [False]  # Use list to allow modification in nested function
#
# def DFS(current_element, parent):
#
#     visited[current_element] = 1
#
#     for a in adj_dict[current_element] :
#         # a(neighbour) not visited → recurse with current as NEW parent
#         if visited[a] != 1 :
#             DFS_list.append(a)
#             DFS( a, current_element)
#         # a is Visited but NOT parent → CYCLE FOUND!
#         elif visited[a] == 1 and a != parent:
#             cycle_found[0] = True
#
#
# DFS(1,0)
# print( cycle_found)

#--=======================
#--======================= surrounded Regions ( Replace Os with Xs ) =======================
#--=======================


# arr = [
#         ['X','X','X','X','X'],
#         ['X','O','O','X','O'],
#         ['X','X','O','X','O'],
#         ['X','O','X','O','X'],
#         ['O','O','X','X','X']
# ]
# visited = [ [0]*len(arr[0]) for i in range( 0,len(arr) ) ]
#
#
# def DFS_border( row, col):
#     visited[row][col] = 1
#
#     if row+1 < len(arr) and arr[row+1][col] == 'O' and visited[row+1][col] != 1:
#         DFS_border(row+1,col)
#
#     if row-1 >=0  and arr[row-1][col] == 'O' and visited[row-1][col] != 1:
#         DFS_border(row-1,col)
#
#     if col+1 < len(arr[0]) and arr[row][col+1] == 'O' and visited[row][col+1] != 1:
#         DFS_border(row,col+1)
#
#     if col-1 >=0 and arr[row][col-1] == 'O' and visited[row][col-1] != 1:
#         DFS_border(row,col-1)
#
#
# def DFS( row, col):
#     if visited[row][col] != 1:
#         arr[row][col] = 'X'
#
#     if row+1 < len(arr) and arr[row+1][col] == 'O' and visited[row+1][col] != 1:
#         DFS(row+1,col)
#
#     if row-1 >=0  and arr[row-1][col] == 'O' and visited[row-1][col] != 1:
#         DFS(row-1,col)
#
#     if col+1 < len(arr[0]) and arr[row][col+1] == 'O' and visited[row][col+1] != 1:
#         DFS(row,col+1)
#
#     if col-1 >=0 and arr[row][col-1] == 'O' and visited[row][col-1] != 1:
#         DFS(row,col-1)
#
#
# # traverse bordering rows/cols and apply DFS to the border elements( rows anf cols )
# for col in range( 0, len(arr[0]) ):
#     if arr[0][col] == 'O':
#         DFS_border(0, col)
#
#     if arr[ len(arr)-1 ][col] == 'O':
#         DFS_border(len(arr)-1, col)
#
# # traverse bordering rows/cols and apply DFS to the border elements( rows anf cols )
# for row in range( 0, len(arr) ):
#     if arr[row][0] == 'O':
#         DFS_border(row, 0)
#
#     if arr[row][ len(arr[0])-1 ] == 'O':
#         DFS_border(row, len(arr[0])-1 )
#
#
# for row in range(0,len(arr)):
#     for col in range(0, len(arr[0])):
#         if arr[row][col] == 'O':
#             DFS(row, col)
#
#
# for row in arr:
#     print(row)


#--=======================
#--======================= surrounded Regions ( Replace Os with Xs ) =======================
#--=======================


# arr = [
#     [0,0,0,1,1],
#     [0,0,1,1,0],
#     [0,1,0,0,0],
#     [0,1,1,0,0],
#     [0,0,0,1,1]
# ]
#
# visited = [ [0]*len(arr[0]) for i in range( 0,len(arr) ) ]
#
#
# from collections import deque
# queue = deque()
#
# # traverse bordering rows/cols and add the border elements( rows anf cols ) to the queue
# for col in range( 0, len(arr[0]) ):
#     if arr[0][col] == 1:
#         queue.append([0, col])
#     if arr[ len(arr)-1 ][col] == 1:
#         queue.append([len(arr)-1, col])
#
#
# # traverse bordering rows/cols and add the border elements( rows anf cols ) to the queue
# for row in range( 0, len(arr) ):
#     if arr[row][0] == 1:
#         queue.append([row, 0])
#     if arr[row][ len(arr[0])-1 ] == 1:
#         queue.append([row, len(arr[0])-1] )
#
#
# # from the elements added into the queue, perform BFS traversala and mark the elements as 1.
# while(queue):
#     row, col = queue.popleft()
#
#     visited[row][col] = 1
#
#     if row+1 < len(arr) and arr[row+1][col] == 1 and visited[row+1][col] != 1:
#         queue.append([row+1,col])
#
#     if row-1 >=0  and arr[row-1][col] == 1 and visited[row-1][col] != 1:
#         queue.append([row-1,col])
#
#     if col+1 < len(arr[0]) and arr[row][col+1] == 1 and visited[row][col+1] != 1:
#         queue.append([row,col+1])
#
#     if col-1 >=0 and arr[row][col-1] == 1 and visited[row][col-1] != 1:
#         queue.append([row,col-1])
#
# count = 0
#
# for row in range(0,len(arr)):
#     for col in range(0, len(arr[0])):
#         if arr[row][col] == 1 and visited[row][col] != 1:
#             count+=1
#
# print(count)
#
# for row in arr:
#     print(row)


#--=======================
#--======================= Bipartite Graph - (BFS) =======================
#--=======================


# Colors shown next to each node ( 0 / 1 ) represent bipartite coloring.
#
#                           0
#                         ( 3 )
#                      /        \
#                    /           \
#                  /              \
#       0      1 /               1 \
#      (1)----(2)                 (4)----(7)----(8)
#               \                /
#                \             /
#                 \          /
#                  (6)----(5)
#                   0      1

from collections import deque
# # Adjacency list representation:
# adj_dict = {
#       1: [2],
#       2: [1, 3, 6],
#       3: [2, 4],
#       4: [3, 5, 7],
#       5: [4, 6],
#       6: [2, 5],
#       7: [4, 8],
#       8: [7]
#   }


#
#                            (3) 0
#                         /     \
#                      /         \
#         0       1 /             \ 1      0
#        (1)----(2)               (4)----(6)
#                  \              /
#                   \           /
#                    \        /
#                     \    /
#                      (5) 0
#
# Adjacency list representation:
# adj_dict = {
#       1: [2],
#       2: [1, 3, 5],
#       3: [2, 4],
#       4: [3, 5, 6],
#       5: [2, 4],
#       6: [4]
#   }
# visited = [-1]*( len(adj_dict)+1 )
# queue = deque()
#
# # The colors are 0 or 1
# # So, for the first element, we are assigning the color as 0
# queue.append([1,0])
# visited[1]=0
# is_bipartite = True
#
#
# while(queue):
#
#     element, color = queue.popleft()
#
#     for a in adj_dict[element]:
#         if visited[a] == -1:
#             if color == 0 :
#                 visited[a] = 1
#                 queue.append([a,1])
#             else:
#                 visited[a] = 0
#                 queue.append([a,0])
#
#         # if the neighbour is already visited and the
#         # color of the current element == color of neighbour,
#         # then the graph is not bipartite
#         elif( visited[a] != -1 and visited[a]  == color ):
#             is_bipartite = False
#             break  # exits for loop, while condition stops outer
#
#
# print(is_bipartite)
# print( visited )


#--=======================
#--======================= Bipartite Graph - (DFS) =======================
#--=======================


# Colors shown next to each node ( 0 / 1 ) represent bipartite coloring.
#
#                           0
#                         ( 3 )
#                      /        \
#                    /           \
#                  /              \
#       0      1 /               1 \
#      (1)----(2)                 (4)----(7)----(8)
#               \                /
#                \             /
#                 \          /
#                  (6)----(5)
#                   0      1

from collections import deque
# # Adjacency list representation:
# adj_dict = {
#       1: [2],
#       2: [1, 3, 6],
#       3: [2, 4],
#       4: [3, 5, 7],
#       5: [4, 6],
#       6: [2, 5],
#       7: [4, 8],
#       8: [7]
#   }

#--==========================

#
#                            (3) 0
#                         /     \
#                      /         \
#         0       1 /             \ 1      0
#        (1)----(2)               (4)----(6)
#                  \              /
#                   \           /
#                    \        /
#                     \    /
#                      (5) 0
#
# Adjacency list representation:
# adj_dict = {
#       1: [2],
#       2: [1, 3, 5],
#       3: [2, 4],
#       4: [3, 5, 6],
#       5: [2, 4],
#       6: [4]
#   }
#
# is_bipartite = [True]
# visited = [-1]*( len(adj_dict)+1 )
#
# def DFS(element, color):
#     # mark the element with corresponding color, the first one being 0
#     visited[element] = color
#
#     # traverse through the dict and mark the neighbors with opposite colors
#     for a in adj_dict[element]:
#         # mark the adj neighbors with opposite colors
#         if visited[a] == -1:
#             if color == 0:
#                DFS(a,1)
#             if color == 1:
#                DFS(a,0)
#
#         # if the neighbour is already visited and the
#         # color of the current element == color of neighbor, then the graph is not bipartite
#         elif( visited[a] != -1 and visited[a]  == color ):
#             is_bipartite[0] = False
#             break  # exits for loop, while condition stops outer
#
# DFS(1,0)
# print( is_bipartite[0] )

#--=======================
#--======================= Topological Sort - DFS =======================
#--=======================
#
#
#       (5) ──→ (0) ←── (4)
#        │               │
#        ↓               ↓
#       (2) ──→ (3) ──→ (1)

# adj_dict = {
#     0: [],
#     1: [],
#     2: [3],
#     3: [1],
#     4: [0,1],
#     5: [0,2]
# }
#
# visited=[0]*len(adj_dict)
# stack = []
#
# def DFS(element):
#     # mark the element as visited
#     visited[element] = 1
#
#     # iterates through all the neighbors
#     for a in adj_dict[element]:
#         if visited[a] != 1:
#            DFS(a)
#     stack.append(element)
#
#
# for i in range(0,len(adj_dict)):
#     if visited[i] != 1:
#         DFS(i)
#
#
# print( visited )
# while(stack):
#     print( stack.pop() )

#--=======================
#--======================= Detect a cycle in a directed Graph - DFS =======================
#--=======================

#  Detect a cycle in a Directed Graph (DFS)
#
#       (1) ──→ (2) ──→ (3) ──→ (4)
#                ↑       ↓       ↓
#                │       ↓       ↓
#                │      (7) ──→ (5) ──→ (6)
#                │
#               (8) ←──────┐
#                ↓         │
#                ↓         │
#               (9) ────→ (10)
#

# adj_dict = {
#       1  : [2],
#       2  : [3],
#       3  : [4, 7],
#       4  : [5],
#       5  : [6],
#       6  : [],
#       7  : [5],
#       8  : [2, 9],
#       9  : [10],
#       10 : [8]
# }

#  Detect a cycle in a Directed Graph (DFS) — NON-CYCLIC version (DAG)
#
#       (1) ──→ (2) ──→ (3) ──→ (4)
#                ↑       ↓       ↓
#                │       ↓       ↓
#                │      (7) ──→ (5) ──→ (6)
#                │
#               (8)
#                ↓
#                ↓
#               (9) ────→ (10)
#


f'''
  recurse through each node keeping visited and path_visited array updated.
  a cycle is found only when  visited and path_visited flag is true for an element
  if the DFS recusrion reaches end of the traversal, keep on removing path_visited flag for the same
  return True only if a cycle is found
'''

# adj_dict = {
#       1  : [2],
#       2  : [3],
#       3  : [4, 7],
#       4  : [5],
#       5  : [6],
#       6  : [],
#       7  : [5],
#       8  : [2, 9],
#       9  : [10],
#       10 : []
# }
#
# # # create a visited list
# visited = [0]*(len(adj_dict) + 1)
# path_visited = [0]*(len(adj_dict) + 1)
# is_cyclic = False
#
#
# def DFS(element):
#
#     visited[element] = 1
#     path_visited[element] = 1
#
#     for a in adj_dict[element]:
#         if visited[a] == 1 and path_visited[a] == 1:
#             return True
#
#         if visited[a] != 1:
#             if DFS(a) == True:
#                 return True
#
#     path_visited[element] = 0
#     return False
#
# for element in range( 1 , len(adj_dict) + 1 ):
#     if visited[element] != 1:
#         if DFS(element) == True:
#             is_cyclic = True
#
# print(is_cyclic)

#--=======================
#--======================= Detect a cycle in a directed Graph - BFS - Kahn's Algorithm =======================
#--=======================

#       (5) ──→ (0) ←── (4)
#        │               │
#        ↓               ↓
#       (2) ──→ (3) ──→ (1)


adj_dict = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0,1],
    5: [0,2]
}






