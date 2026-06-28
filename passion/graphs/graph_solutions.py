"""
GRAPH PROBLEMS - FAANG/GOOGLE L6 STAFF INTERVIEW PREP
======================================================
Complete solutions organized by PATTERNS

Based on Striver's Graph Series + LeetCode FAANG favorites

PATTERN INDEX:
--------------
PATTERN 1:  Graph Traversal (BFS/DFS)              [G-5, G-6, G-10, G-16, LC 200]
PATTERN 2:  Cycle Detection                        [G-11, G-12, G-19, G-23]
PATTERN 3:  Bipartite Graph                        [G-17, G-18, LC 785]
PATTERN 4:  Topological Sort                       [G-21, G-22, G-24, G-26, LC 207, 210, 269]
PATTERN 5:  Shortest Path                          [G-27, G-28, G-32, G-41, G-42, LC 743, 787]
PATTERN 6:  Minimum Spanning Tree (MST)            [G-45, G-47, LC 1584]
PATTERN 7:  Disjoint Set Union (Union-Find)        [G-46, LC 323, 547, 684]
PATTERN 8:  Advanced (SCC, Bridges, Articulation)  [G-54, G-55, G-56, LC 1192]

GRAPH REPRESENTATIONS:
----------------------
1. Adjacency List:  graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: []}
2. Adjacency Matrix: graph[i][j] = 1 if edge exists
3. Edge List:       edges = [(0,1), (1,2), (2,0)]

TIME COMPLEXITY REFERENCE:
--------------------------
BFS/DFS:           O(V + E)
Dijkstra:          O((V + E) log V) with heap
Bellman-Ford:      O(V * E)
Floyd-Warshall:    O(V^3)
Prim's:            O(E log V) with heap
Kruskal's:         O(E log E)
Union-Find:        O(alpha(V)) amortized per op
Tarjan's/Kosaraju: O(V + E)
"""

from collections import defaultdict, deque
import heapq


# ============================================================================
# ============================================================================
# PATTERN 1: GRAPH TRAVERSAL (BFS / DFS)
# ============================================================================
# ============================================================================
"""
PATTERN TEMPLATE - BFS:
-----------------------
def bfs(start, graph):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        # process node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

PATTERN TEMPLATE - DFS (recursive):
------------------------------------
def dfs(node, graph, visited):
    visited.add(node)
    # process node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

PATTERN TEMPLATE - DFS (iterative):
------------------------------------
def dfs(start, graph):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        # process node
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

WHEN TO USE:
- BFS: Shortest path in unweighted graph, level-order processing
- DFS: Path existence, cycle detection, topological sort, connected components
"""


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 1.1: G-5 - Breadth First Search (BFS) Traversal
# ============================================================================
"""
Problem:
--------
Given a connected undirected graph with V vertices and adjacency list,
return BFS traversal starting from vertex 0.

Example:
Input: V=5, adj=[[1,2,3],[0],[0,4],[0],[2]]
Output: [0, 1, 2, 3, 4]
"""

def bfs_of_graph(V, adj):
    """
    Approach: Standard BFS using queue
    
    Key Insight:
    - BFS explores level by level (closest neighbors first)
    - Use a queue (FIFO) to maintain order
    - Mark nodes visited when adding to queue (not when popping) to avoid duplicates
    
    Time: O(V + E)
    Space: O(V)
    """
    visited = [False] * V
    result = []
    queue = deque([0])
    visited[0] = True
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 1.2: G-6 - Depth First Search (DFS) Traversal
# ============================================================================
"""
Problem:
--------
Given a connected undirected graph, return DFS traversal starting from vertex 0.

Example:
Input: V=5, adj=[[2,3,1],[0],[0,4],[0],[2]]
Output: [0, 2, 4, 3, 1]
"""

def dfs_of_graph(V, adj):
    """
    Approach: Recursive DFS
    
    Key Insight:
    - DFS goes deep before exploring siblings
    - Uses implicit stack (recursion) or explicit stack
    - Mark visited when entering the node
    
    Time: O(V + E)
    Space: O(V) for recursion stack
    """
    visited = [False] * V
    result = []
    
    def dfs(node):
        visited[node] = True
        result.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(0)
    return result


# HIGHEST FREQUENCY (Must Know for Interviews) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 1.3: LeetCode 200 - Number of Islands
# ============================================================================
"""
Problem:
--------
Given an m x n 2D binary grid which represents a map of '1's (land) and 
'0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically.

Example:
Input: grid = [["1","1","0"],["1","0","0"],["0","0","1"]]
Output: 2

Constraints:
- m == grid.length, n == grid[i].length
- 1 <= m, n <= 300
"""

def numIslands(grid):
    """
    Approach: DFS on 2D grid (each cell is a node)
    
    Key Insight:
    - Treat each land cell as a node connected to 4 adjacent land cells
    - For each unvisited land cell, do DFS and mark entire island as visited
    - Count how many times we initiate a new DFS = number of islands
    - We can modify grid in-place to mark visited (saves space)
    
    Time: O(m * n)
    Space: O(m * n) for recursion stack in worst case
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        # Out of bounds or water - stop
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        # Mark as visited
        grid[r][c] = '#'
        # Explore 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    
    return count


# HIGHEST FREQUENCY (Must Know for Interviews) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 1.4: G-10 / LeetCode 994 - Rotting Oranges
# ============================================================================
"""
Problem:
--------
You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell
- 1 representing a fresh orange
- 2 representing a rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten 
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a 
fresh orange. If this is impossible, return -1.

Example:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""

def orangesRotting(grid):
    """
    Approach: Multi-source BFS (level-by-level)
    
    Key Insight:
    - Multiple sources rot oranges simultaneously - this is multi-source BFS
    - Start BFS from ALL rotten oranges at once (add all to queue initially)
    - Each "level" of BFS = 1 minute passing
    - Count fresh oranges; if any remain after BFS, return -1
    - This is shortest-time problem -> BFS is natural fit
    
    Time: O(m * n)
    Space: O(m * n)
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # Find all rotten oranges and count fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh_count += 1
    
    minutes = 0
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    while queue:
        r, c, time = queue.popleft()
        minutes = max(minutes, time)
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2  # Rot it
                fresh_count -= 1
                queue.append((nr, nc, time + 1))
    
    return minutes if fresh_count == 0 else -1


# ============================================================================
# PROBLEM 1.5: G-16 / LeetCode 694 - Number of Distinct Islands
# ============================================================================
"""
Problem:
--------
Given a 2D grid of 0's and 1's, count the number of DISTINCT islands.
Two islands are considered the same if and only if one island can be 
translated (NOT rotated/reflected) to equal the other.

Example:
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1
"""

def numDistinctIslands(grid):
    """
    Approach: DFS with shape encoding
    
    Key Insight:
    - Two islands are "same" if their SHAPES match (after translation)
    - Encode each island's shape relative to a starting point
    - Use the DFS traversal path as a signature (directions taken)
    - Store unique signatures in a set
    - Must include backtrack markers to disambiguate shapes!
    
    Time: O(m * n)
    Space: O(m * n)
    """
    rows, cols = len(grid), len(grid[0])
    shapes = set()
    
    def dfs(r, c, direction, path):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return
        grid[r][c] = 0  # Mark visited
        path.append(direction)
        dfs(r+1, c, 'D', path)
        dfs(r-1, c, 'U', path)
        dfs(r, c+1, 'R', path)
        dfs(r, c-1, 'L', path)
        path.append('B')  # Backtrack marker - CRITICAL for uniqueness
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                path = []
                dfs(r, c, 'S', path)  # Start
                shapes.add(tuple(path))
    
    return len(shapes)


# Test Pattern 1
print("=" * 70)
print("PATTERN 1: GRAPH TRAVERSAL (BFS / DFS)")
print("=" * 70)

print("\n1.1 BFS Traversal:")
print(bfs_of_graph(5, [[1,2,3],[0],[0,4],[0],[2]]))

print("\n1.2 DFS Traversal:")
print(dfs_of_graph(5, [[2,3,1],[0],[0,4],[0],[2]]))

print("\n1.3 Number of Islands:")
grid1 = [["1","1","0"],["1","0","0"],["0","0","1"]]
print(numIslands(grid1))

print("\n1.4 Rotting Oranges:")
print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

print("\n1.5 Number of Distinct Islands:")
print(numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))


# ============================================================================
# ============================================================================
# PATTERN 2: CYCLE DETECTION
# ============================================================================
# ============================================================================
"""
PATTERN TEMPLATE - Undirected (BFS):
------------------------------------
Track (node, parent). If visited neighbor != parent, cycle exists.

PATTERN TEMPLATE - Undirected (DFS):
------------------------------------
def dfs(node, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, node): return True
        elif neighbor != parent:
            return True  # Cycle!
    return False

PATTERN TEMPLATE - Directed (DFS - 3 colors):
---------------------------------------------
WHITE (0): unvisited
GRAY  (1): in current DFS path (recursion stack)
BLACK (2): fully processed

If we hit a GRAY node -> back edge -> cycle!

PATTERN TEMPLATE - Directed (BFS - Kahn's):
-------------------------------------------
Count in-degrees, repeatedly remove 0 in-degree nodes.
If processed nodes < V -> cycle exists.
"""


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 2.1: G-11 - Detect Cycle in Undirected Graph (BFS)
# ============================================================================
"""
Problem:
--------
Given an undirected graph with V vertices and adjacency list, check if 
there exists a cycle.
"""

def has_cycle_undirected_bfs(V, adj):
    """
    Approach: BFS tracking parent
    
    Key Insight:
    - In undirected graph, cycle exists if BFS visits an already-visited node
      that is NOT its parent
    - Track (node, parent) in queue
    - If we find visited neighbor != parent, it's a cycle
    - Must check all components (graph may be disconnected)
    
    Time: O(V + E)
    Space: O(V)
    """
    visited = [False] * V
    
    def bfs(start):
        queue = deque([(start, -1)])
        visited[start] = True
        while queue:
            node, parent = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True  # Cycle detected
        return False
    
    # Check all components
    for i in range(V):
        if not visited[i]:
            if bfs(i):
                return True
    return False


# ============================================================================
# PROBLEM 2.2: G-12 - Detect Cycle in Undirected Graph (DFS)
# ============================================================================
def has_cycle_undirected_dfs(V, adj):
    """
    Approach: DFS tracking parent
    
    Key Insight:
    - Same logic as BFS version, but recursive
    - For each node, pass parent in recursion
    - If we find visited neighbor != parent, cycle exists
    
    Time: O(V + E)
    Space: O(V)
    """
    visited = [False] * V
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # Back edge = cycle
        return False
    
    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 2.3: G-19 - Detect Cycle in Directed Graph (DFS)
# ============================================================================
"""
Problem:
--------
Given a directed graph, detect if it contains a cycle.

Key difference from undirected: A "back edge" to ancestor in CURRENT path = cycle
Just visiting a previously-visited node is NOT a cycle (could be cross edge)
"""

def has_cycle_directed_dfs(V, adj):
    """
    Approach: DFS with recursion stack tracking (3-color method)
    
    Key Insight:
    - In directed graph, we need to track if a node is in the CURRENT DFS path
    - Use two arrays: visited (ever seen) and in_path (in current recursion stack)
    - If we encounter a node that's in current path -> cycle!
    - When we finish processing a node, remove it from in_path
    
    Alternative: 3-color method
    - WHITE (0): unvisited
    - GRAY (1):  in current path
    - BLACK (2): fully processed
    - GRAY->GRAY edge = cycle
    
    Time: O(V + E)
    Space: O(V)
    """
    visited = [False] * V
    in_path = [False] * V
    
    def dfs(node):
        visited[node] = True
        in_path[node] = True
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif in_path[neighbor]:
                return True  # Back edge to ancestor in current path = cycle
        
        in_path[node] = False  # Remove from current path
        return False
    
    for i in range(V):
        if not visited[i]:
            if dfs(i):
                return True
    return False


# ============================================================================
# PROBLEM 2.4: G-23 - Detect Cycle in Directed Graph (BFS / Kahn's)
# ============================================================================
def has_cycle_directed_bfs(V, adj):
    """
    Approach: Kahn's Algorithm (BFS-based topological sort)
    
    Key Insight:
    - If we can perform topological sort on all V nodes -> no cycle
    - If some nodes remain unprocessed (still have in-degree > 0) -> cycle exists
    - Cycle nodes can never have in-degree drop to 0
    
    Steps:
    1. Compute in-degree of all nodes
    2. Add all 0 in-degree nodes to queue
    3. Process: remove from queue, decrement neighbors' in-degrees
    4. If processed count < V -> cycle
    
    Time: O(V + E)
    Space: O(V)
    """
    in_degree = [0] * V
    for u in range(V):
        for v in adj[u]:
            in_degree[v] += 1
    
    queue = deque([i for i in range(V) if in_degree[i] == 0])
    processed = 0
    
    while queue:
        node = queue.popleft()
        processed += 1
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return processed != V  # Cycle if we couldn't process all nodes


# Test Pattern 2
print("\n" + "=" * 70)
print("PATTERN 2: CYCLE DETECTION")
print("=" * 70)

print("\n2.1 Cycle in Undirected (BFS):")
print(has_cycle_undirected_bfs(4, [[1,2],[0,2],[0,1,3],[2]]))  # True (0-1-2-0)

print("\n2.2 Cycle in Undirected (DFS):")
print(has_cycle_undirected_dfs(4, [[1],[0,2],[1,3],[2]]))  # False (linear)

print("\n2.3 Cycle in Directed (DFS):")
print(has_cycle_directed_dfs(4, [[1],[2],[3],[1]]))  # True (1->2->3->1)

print("\n2.4 Cycle in Directed (BFS/Kahn's):")
print(has_cycle_directed_bfs(4, [[1],[2],[3],[]]))  # False (DAG)


# ============================================================================
# ============================================================================
# PATTERN 3: BIPARTITE GRAPH
# ============================================================================
# ============================================================================
"""
A graph is BIPARTITE if its vertices can be split into two sets where every
edge connects vertices from different sets (2-colorable).

KEY PROPERTY: A graph is bipartite iff it contains NO ODD-LENGTH CYCLE.

PATTERN TEMPLATE - BFS Coloring:
--------------------------------
color = [-1] * V
for each unvisited node:
    BFS, assigning alternate colors (0/1) to neighbors
    If a neighbor already has same color as current -> NOT bipartite

PATTERN TEMPLATE - DFS Coloring:
--------------------------------
def dfs(node, c):
    color[node] = c
    for neighbor in graph[node]:
        if color[neighbor] == -1:
            if not dfs(neighbor, 1 - c): return False
        elif color[neighbor] == c:
            return False  # Same color = not bipartite
    return True
"""


# HIGHEST FREQUENCY (Must Know for Interviews) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 3.1: G-17 / LeetCode 785 - Is Graph Bipartite? (BFS)
# ============================================================================
"""
Problem:
--------
There is an undirected graph with n nodes labeled from 0 to n - 1.
Given the adjacency list, determine if the graph is bipartite.

Example:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
"""

def isBipartite_bfs(graph):
    """
    Approach: BFS with 2-coloring
    
    Key Insight:
    - Try to color graph with 2 colors such that adjacent nodes have different colors
    - Use BFS to assign colors layer by layer (alternating)
    - If we ever try to color a node with a color different from already assigned -> not bipartite
    - Must check all connected components
    
    Time: O(V + E)
    Space: O(V)
    """
    n = len(graph)
    color = [-1] * n
    
    for start in range(n):
        if color[start] != -1:
            continue
        
        # BFS from this component
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False  # Conflict!
    
    return True


# ============================================================================
# PROBLEM 3.2: G-18 - Is Graph Bipartite? (DFS)
# ============================================================================
def isBipartite_dfs(graph):
    """
    Approach: DFS with 2-coloring
    
    Key Insight:
    - Same as BFS version but recursive
    - Assign color, then DFS to neighbors with opposite color
    - If conflict found at any point, return False
    
    Time: O(V + E)
    Space: O(V)
    """
    n = len(graph)
    color = [-1] * n
    
    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False
    return True


# Test Pattern 3
print("\n" + "=" * 70)
print("PATTERN 3: BIPARTITE GRAPH")
print("=" * 70)

print("\n3.1 Is Bipartite (BFS):")
print(isBipartite_bfs([[1,3],[0,2],[1,3],[0,2]]))  # True
print(isBipartite_bfs([[1,2,3],[0,2],[0,1,3],[0,2]]))  # False

print("\n3.2 Is Bipartite (DFS):")
print(isBipartite_dfs([[1,3],[0,2],[1,3],[0,2]]))  # True


# ============================================================================
# ============================================================================
# PATTERN 4: TOPOLOGICAL SORT
# ============================================================================
# ============================================================================
"""
TOPOLOGICAL SORT: Linear ordering of vertices in a DAG (Directed Acyclic Graph)
such that for every directed edge u->v, u comes before v in the ordering.

USE CASES:
- Course prerequisites
- Build dependency resolution
- Task scheduling
- Alien dictionary (character ordering)

PATTERN TEMPLATE - DFS (Post-order):
------------------------------------
def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
    stack.append(node)  # Add to stack AFTER processing children

# Result = reversed stack

PATTERN TEMPLATE - Kahn's Algorithm (BFS):
------------------------------------------
1. Compute in-degrees
2. Add all 0 in-degree nodes to queue
3. Process queue: add to result, decrement neighbors' in-degrees
4. If neighbor's in-degree becomes 0, add to queue

NOTE: Topological sort only exists for DAG (no cycles)
"""


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 4.1: G-21 - Topological Sort (DFS)
# ============================================================================
def topological_sort_dfs(V, adj):
    """
    Approach: DFS with post-order stack
    
    Key Insight:
    - DFS goes deep first, finishing dependents before dependencies
    - Push node to stack AFTER all its neighbors are processed
    - Reversing stack gives topological order
    - Intuition: deepest dependencies finish first, get pushed first,
      end up at BOTTOM of stack (i.e., LAST in topological order)
    
    Time: O(V + E)
    Space: O(V)
    """
    visited = [False] * V
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)  # Post-order: add after processing children
    
    for i in range(V):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]  # Reverse for correct order


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 4.2: G-22 - Kahn's Algorithm (Topological Sort BFS)
# ============================================================================
def topological_sort_kahns(V, adj):
    """
    Approach: BFS using in-degrees
    
    Key Insight:
    - Nodes with 0 in-degree have no dependencies -> can come first
    - Process them, "remove" their outgoing edges (decrement neighbors' in-degrees)
    - This may create new 0 in-degree nodes -> add to queue
    - Continue until queue empty
    
    Why BFS works:
    - We process nodes only when ALL their prerequisites are done
    - This is exactly what topological sort requires
    
    Time: O(V + E)
    Space: O(V)
    """
    in_degree = [0] * V
    for u in range(V):
        for v in adj[u]:
            in_degree[v] += 1
    
    queue = deque([i for i in range(V) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == V else []  # Empty if cycle exists


# HIGHEST FREQUENCY (Must Know for Interviews) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 4.3: G-24 / LeetCode 207 - Course Schedule I
# ============================================================================
"""
Problem:
--------
There are numCourses courses you have to take, labeled from 0 to numCourses-1.
You are given an array prerequisites where prerequisites[i] = [a_i, b_i] 
indicates you must take course b_i before a_i.

Return true if you can finish all courses, otherwise return false.

Example:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
"""

def canFinish(numCourses, prerequisites):
    """
    Approach: Detect cycle in directed graph (Kahn's algorithm)
    
    Key Insight:
    - Can finish all courses iff prerequisite graph has NO cycle
    - Build graph: edge from b -> a means "take b before a"
    - Use Kahn's: if we can topologically sort all courses, no cycle
    - If processed count < numCourses, cycle exists
    
    Time: O(V + E)
    Space: O(V + E)
    """
    adj = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    finished = 0
    
    while queue:
        node = queue.popleft()
        finished += 1
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return finished == numCourses


# HIGHEST FREQUENCY (Must Know for Interviews) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 4.4: LeetCode 210 - Course Schedule II
# ============================================================================
"""
Problem:
--------
Same as Course Schedule I, but return the order in which to take courses.
If impossible, return empty array.

Example:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3] or [0,1,2,3]
"""

def findOrder(numCourses, prerequisites):
    """
    Approach: Topological sort (Kahn's)
    
    Time: O(V + E)
    Space: O(V + E)
    """
    adj = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return order if len(order) == numCourses else []


# HIGHEST FREQUENCY (HARD - Must Know for L6) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 4.5: G-26 / LeetCode 269 - Alien Dictionary
# ============================================================================
"""
Problem:
--------
You are given a list of words from an alien language sorted lexicographically.
Derive the order of characters in the alien alphabet.

Example:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Constraints:
- Return "" if no valid ordering (cycle or invalid input)
"""

def alienOrder(words):
    """
    Approach: Build graph from adjacent word pairs + topological sort
    
    Key Insight:
    - Compare adjacent words to derive character ordering
    - For words[i] and words[i+1], find first differing character
      -> first[diff_idx] comes BEFORE second[diff_idx]
    - Edge case: if words[i] is a prefix of words[i+1] longer than it -> invalid
      Example: ["abc", "ab"] is invalid
    - Then perform topological sort on character graph
    - If cycle exists -> return ""
    
    Time: O(C) where C = total characters in all words
    Space: O(1) for graph (max 26 nodes), O(26) for tracking
    """
    # Initialize graph and in-degree for all unique chars
    adj = {c: set() for word in words for c in word}
    in_degree = {c: 0 for c in adj}
    
    # Build edges from adjacent word pairs
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        
        # Edge case: w1 is prefix of w2 and longer -> invalid
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        
        # Find first differing character
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break
    
    # Kahn's algorithm for topological sort
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []
    
    while queue:
        c = queue.popleft()
        result.append(c)
        for neighbor in adj[c]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If cycle exists, not all chars processed
    return "".join(result) if len(result) == len(in_degree) else ""


# Test Pattern 4
print("\n" + "=" * 70)
print("PATTERN 4: TOPOLOGICAL SORT")
print("=" * 70)

print("\n4.1 Topological Sort (DFS):")
print(topological_sort_dfs(6, [[],[],[3],[1],[0,1],[0,2]]))

print("\n4.2 Topological Sort (Kahn's BFS):")
print(topological_sort_kahns(6, [[],[],[3],[1],[0,1],[0,2]]))

print("\n4.3 Course Schedule I:")
print(canFinish(2, [[1,0]]))  # True
print(canFinish(2, [[1,0],[0,1]]))  # False

print("\n4.4 Course Schedule II:")
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

print("\n4.5 Alien Dictionary:")
print(alienOrder(["wrt","wrf","er","ett","rftt"]))  # "wertf"


# ============================================================================
# ============================================================================
# PATTERN 5: SHORTEST PATH ALGORITHMS
# ============================================================================
# ============================================================================
"""
SHORTEST PATH ALGORITHM SELECTION GUIDE:
----------------------------------------
| Algorithm        | Use When                              | Time          |
|------------------|---------------------------------------|---------------|
| BFS              | Unweighted graph                      | O(V + E)      |
| Topo Sort + Relax| DAG with weights                      | O(V + E)      |
| Dijkstra         | Non-negative weights                  | O((V+E)logV)  |
| Bellman-Ford     | Negative weights, detect neg cycles   | O(V * E)      |
| Floyd-Warshall   | All-pairs shortest path               | O(V^3)        |

KEY INSIGHT:
- BFS works for unweighted because all edges have weight 1 (level = distance)
- Dijkstra fails with negative weights (greedy assumption breaks)
- Bellman-Ford handles negative weights via V-1 iterations of relaxation
- Floyd-Warshall: 3 nested loops, considering each node as intermediate
"""


# ============================================================================
# PROBLEM 5.1: G-28 / LeetCode - Shortest Path in Unweighted Undirected Graph
# ============================================================================
def shortest_path_unweighted(V, edges, source):
    """
    Approach: BFS (works because all edges have weight 1)
    
    Key Insight:
    - In unweighted graph, BFS gives shortest path (level = distance)
    - Distance to a node = number of edges traversed
    - Each BFS level represents one more edge
    
    Time: O(V + E)
    Space: O(V)
    """
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    dist = [-1] * V
    dist[source] = 0
    queue = deque([source])
    
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    return dist


# ============================================================================
# PROBLEM 5.2: G-27 - Shortest Path in DAG (Topological Sort)
# ============================================================================
def shortest_path_dag(V, edges, source):
    """
    Approach: Topological sort + edge relaxation
    
    Key Insight:
    - In DAG, process nodes in topological order
    - When we process a node, ALL paths leading to it are already finalized
    - So we can simply relax outgoing edges
    - This is FASTER than Dijkstra for DAGs (O(V+E) vs O((V+E)logV))
    
    Time: O(V + E)
    Space: O(V + E)
    """
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
    
    # Topological sort using DFS
    visited = [False] * V
    stack = []
    
    def dfs(node):
        visited[node] = True
        for v, _ in adj[node]:
            if not visited[v]:
                dfs(v)
        stack.append(node)
    
    for i in range(V):
        if not visited[i]:
            dfs(i)
    
    # Relax edges in topological order
    dist = [float('inf')] * V
    dist[source] = 0
    
    while stack:
        node = stack.pop()
        if dist[node] != float('inf'):
            for v, w in adj[node]:
                if dist[node] + w < dist[v]:
                    dist[v] = dist[node] + w
    
    return [d if d != float('inf') else -1 for d in dist]


# HIGHEST FREQUENCY (Must Know for L6) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 5.3: G-32 - Dijkstra's Algorithm
# ============================================================================
"""
Problem:
--------
Given a weighted graph with non-negative edges, find shortest path from
source to all other nodes.
"""

def dijkstra(V, adj, source):
    """
    Approach: Greedy with min-heap (priority queue)
    
    Key Insight:
    - At each step, pick the UNVISITED node with smallest distance
    - Update (relax) distances of its neighbors
    - Use min-heap to efficiently get next closest node
    - Works only with NON-NEGATIVE weights (greedy assumption)
    
    Why min-heap?
    - We need to repeatedly extract minimum
    - Standard PriorityQueue gives O(log V) per operation
    
    Time: O((V + E) log V)
    Space: O(V)
    """
    dist = [float('inf')] * V
    dist[source] = 0
    heap = [(0, source)]  # (distance, node)
    
    while heap:
        d, node = heapq.heappop(heap)
        
        # Skip if we already found shorter path
        if d > dist[node]:
            continue
        
        for neighbor, weight in adj[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return dist


# HIGHEST FREQUENCY (Must Know) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 5.4: LeetCode 743 - Network Delay Time (Dijkstra application)
# ============================================================================
"""
Problem:
--------
You are given a network of n nodes labeled 1 to n. times[i] = (u, v, w)
represents an edge from u to v with travel time w.

Find the minimum time for all nodes to receive a signal from node k.
Return -1 if impossible.

Example:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""

def networkDelayTime(times, n, k):
    """
    Approach: Dijkstra to find max of shortest paths from k
    
    Key Insight:
    - "Time for all nodes to receive signal" = MAX of shortest paths from k
    - Use Dijkstra to find shortest path from k to every node
    - Answer = max(dist) if all reachable, else -1
    
    Time: O((V + E) log V)
    Space: O(V + E)
    """
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
    
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]
    
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    max_time = max(dist.values())
    return max_time if max_time != float('inf') else -1


# ============================================================================
# PROBLEM 5.5: G-41 - Bellman-Ford Algorithm
# ============================================================================
"""
Problem:
--------
Find shortest path from source to all nodes. Handle NEGATIVE weights.
Also detect negative cycles.
"""

def bellman_ford(V, edges, source):
    """
    Approach: Relax all edges V-1 times
    
    Key Insight:
    - Shortest path in graph with V nodes has at most V-1 edges
    - So relaxing all edges V-1 times guarantees finding shortest paths
    - V-th relaxation reveals negative cycle: if any distance still decreases
    - Slower than Dijkstra BUT handles negative weights
    
    Algorithm:
    1. Initialize dist[source] = 0, others = infinity
    2. For V-1 iterations: relax every edge
    3. V-th iteration: if any edge can be relaxed -> negative cycle
    
    Time: O(V * E)
    Space: O(V)
    """
    dist = [float('inf')] * V
    dist[source] = 0
    
    # Relax all edges V-1 times
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Check for negative cycle (V-th iteration)
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return [-1]  # Negative cycle detected
    
    return dist


# HIGHEST FREQUENCY (Must Know for L6) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 5.6: LeetCode 787 - Cheapest Flights Within K Stops
# ============================================================================
"""
Problem:
--------
There are n cities connected by flights[i] = [from, to, price].
Find cheapest price from src to dst with AT MOST k stops.
Return -1 if no such route.

Example:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
       src = 0, dst = 3, k = 1
Output: 700 (0->1->3)
"""

def findCheapestPrice(n, flights, src, dst, k):
    """
    Approach: Modified Bellman-Ford (k+1 iterations) OR BFS with state
    
    Key Insight:
    - "At most k stops" = at most k+1 edges
    - Run Bellman-Ford for k+1 iterations
    - IMPORTANT: Use SNAPSHOT of distances to avoid using updates from same iteration
    - Otherwise, single iteration might propagate through multiple edges
    
    Time: O(k * E)
    Space: O(V)
    """
    dist = [float('inf')] * n
    dist[src] = 0
    
    for _ in range(k + 1):
        # CRITICAL: use snapshot to limit to one edge per iteration
        temp = dist.copy()
        for u, v, price in flights:
            if dist[u] != float('inf') and dist[u] + price < temp[v]:
                temp[v] = dist[u] + price
        dist = temp
    
    return dist[dst] if dist[dst] != float('inf') else -1


# ============================================================================
# PROBLEM 5.7: G-42 - Floyd-Warshall (All-Pairs Shortest Path)
# ============================================================================
def floyd_warshall(matrix):
    """
    Approach: Dynamic Programming over intermediate nodes
    
    Key Insight:
    - For each pair (i, j), check if going through node k gives shorter path
    - dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    - The k loop MUST be outermost (consider intermediates in order)
    - Handles negative edges (but not negative cycles, which it can detect)
    
    Time: O(V^3)
    Space: O(V^2)
    
    Input: matrix where matrix[i][j] = weight (or -1 for no edge)
    """
    n = len(matrix)
    INF = float('inf')
    
    # Initialize: -1 means no edge, set to INF
    dist = [[INF if matrix[i][j] == -1 and i != j else (0 if i == j else matrix[i][j]) 
             for j in range(n)] for i in range(n)]
    
    # Try each node as intermediate
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Negative cycle detection: dist[i][i] < 0
    for i in range(n):
        if dist[i][i] < 0:
            return "Negative cycle detected"
    
    return dist


# Test Pattern 5
print("\n" + "=" * 70)
print("PATTERN 5: SHORTEST PATH ALGORITHMS")
print("=" * 70)

print("\n5.1 Shortest Path Unweighted (BFS):")
print(shortest_path_unweighted(6, [(0,1),(0,2),(1,3),(2,3),(3,4),(4,5)], 0))

print("\n5.2 Shortest Path in DAG:")
print(shortest_path_dag(6, [(0,1,2),(0,4,1),(4,5,4),(4,2,2),(1,2,3),(2,3,6),(5,3,1)], 0))

print("\n5.3 Dijkstra:")
adj_dijk = {0: [(1,4),(2,1)], 1: [(3,1)], 2: [(1,2),(3,5)], 3: []}
print(dijkstra(4, adj_dijk, 0))

print("\n5.4 Network Delay Time:")
print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))

print("\n5.5 Bellman-Ford:")
print(bellman_ford(5, [(0,1,4),(0,2,1),(2,1,2),(1,3,1),(2,3,5),(3,4,3)], 0))

print("\n5.6 Cheapest Flights K Stops:")
print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))

print("\n5.7 Floyd-Warshall:")
print(floyd_warshall([[0,1,43],[1,0,6],[-1,-1,0]]))


# ============================================================================
# ============================================================================
# PATTERN 6: MINIMUM SPANNING TREE (MST)
# ============================================================================
# ============================================================================
"""
MINIMUM SPANNING TREE: A subset of edges connecting all V vertices with:
- Exactly V-1 edges (tree property)
- Minimum total edge weight
- No cycles

TWO MAIN ALGORITHMS:
1. Prim's:    Grow MST from single vertex, pick min-weight edge to unvisited node
2. Kruskal's: Sort all edges, add if doesn't form cycle (use Union-Find)

WHEN TO USE:
- Network design (minimum cable cost)
- Cluster analysis
- Approximation for TSP
"""


# ============================================================================
# PROBLEM 6.1: G-45 - Prim's Algorithm
# ============================================================================
def prims(V, adj):
    """
    Approach: Greedy growth with min-heap
    
    Key Insight:
    - Start with any vertex, grow MST one edge at a time
    - At each step, pick MINIMUM weight edge from MST to outside vertex
    - Use min-heap to efficiently get next minimum edge
    - Similar structure to Dijkstra
    
    Time: O((V + E) log V)
    Space: O(V + E)
    
    Input: adj = {node: [(neighbor, weight), ...]}
    Returns: total weight of MST
    """
    in_mst = [False] * V
    heap = [(0, 0)]  # (weight, node) - start from node 0
    mst_weight = 0
    
    while heap:
        weight, node = heapq.heappop(heap)
        
        if in_mst[node]:
            continue
        
        in_mst[node] = True
        mst_weight += weight
        
        for neighbor, w in adj[node]:
            if not in_mst[neighbor]:
                heapq.heappush(heap, (w, neighbor))
    
    return mst_weight


# ============================================================================
# PROBLEM 6.2: G-47 - Kruskal's Algorithm
# ============================================================================
def kruskals(V, edges):
    """
    Approach: Sort edges + Union-Find
    
    Key Insight:
    - Sort all edges by weight (ascending)
    - For each edge: if it doesn't form a cycle (endpoints in different sets), include it
    - Use Union-Find to efficiently check/merge components
    - Stop when V-1 edges added
    
    Time: O(E log E) - dominated by sorting
    Space: O(V)
    
    Input: edges = [(u, v, weight), ...]
    """
    parent = list(range(V))
    rank = [0] * V
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False  # Already in same set (would create cycle)
        # Union by rank
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    edges.sort(key=lambda e: e[2])
    mst_weight = 0
    edges_added = 0
    
    for u, v, w in edges:
        if union(u, v):
            mst_weight += w
            edges_added += 1
            if edges_added == V - 1:
                break
    
    return mst_weight


# HIGHEST FREQUENCY (Must Know) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 6.3: LeetCode 1584 - Min Cost to Connect All Points
# ============================================================================
"""
Problem:
--------
Given points on a 2D plane, return the minimum cost to connect all points.
Cost between two points = Manhattan distance.

Example:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
"""

def minCostConnectPoints(points):
    """
    Approach: Prim's MST on complete graph
    
    Key Insight:
    - This is MST problem on complete graph (every pair connected)
    - Use Prim's with min-heap
    - Lazy version: push all edges, pop min, skip if already in MST
    
    Time: O(N^2 log N)
    Space: O(N^2)
    """
    n = len(points)
    if n <= 1:
        return 0
    
    in_mst = [False] * n
    min_dist = [float('inf')] * n
    min_dist[0] = 0
    total = 0
    
    for _ in range(n):
        # Find unvisited node with minimum distance
        u = -1
        for i in range(n):
            if not in_mst[i] and (u == -1 or min_dist[i] < min_dist[u]):
                u = i
        
        in_mst[u] = True
        total += min_dist[u]
        
        # Update distances to remaining nodes
        for v in range(n):
            if not in_mst[v]:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                if dist < min_dist[v]:
                    min_dist[v] = dist
    
    return total


# Test Pattern 6
print("\n" + "=" * 70)
print("PATTERN 6: MINIMUM SPANNING TREE (MST)")
print("=" * 70)

print("\n6.1 Prim's Algorithm:")
adj_mst = {0:[(1,2),(2,1),(3,4)], 1:[(0,2),(2,3),(3,2)], 2:[(0,1),(1,3),(3,5)], 3:[(0,4),(1,2),(2,5)]}
print(prims(4, adj_mst))

print("\n6.2 Kruskal's Algorithm:")
print(kruskals(4, [(0,1,2),(0,2,1),(0,3,4),(1,2,3),(1,3,2),(2,3,5)]))

print("\n6.3 Min Cost Connect Points:")
print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))


# ============================================================================
# ============================================================================
# PATTERN 7: DISJOINT SET UNION (UNION-FIND)
# ============================================================================
# ============================================================================
"""
DISJOINT SET UNION (DSU) / UNION-FIND: Data structure to track elements 
partitioned into disjoint subsets. Supports two operations efficiently:
- find(x): Which set does x belong to?
- union(x, y): Merge sets containing x and y

USE CASES:
- Detect cycles in undirected graphs
- Find connected components
- Kruskal's MST
- Dynamic connectivity problems

OPTIMIZATIONS (CRITICAL FOR INTERVIEW):
1. Path Compression: During find, point each node directly to root
2. Union by Rank/Size: Attach smaller tree under larger tree

With both optimizations: O(alpha(N)) per operation ~ O(1) practically
"""


# ============================================================================
# PROBLEM 7.1: G-46 - Disjoint Set Union (Implementation)
# ============================================================================
class DSU:
    """
    Disjoint Set Union with Path Compression + Union by Rank
    
    Key Insight:
    - parent[i] points to parent in tree representation of set
    - Root represents the set (root's parent is itself)
    - find(): traverse to root, compress path along the way
    - union(): attach shorter tree under taller (by rank)
    
    Time per operation: O(alpha(N)) amortized ~ O(1)
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n  # Optional: track set sizes
    
    def find(self, x):
        """Path compression: make all nodes point directly to root"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union by rank: attach smaller tree under larger"""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in same set
        
        # Attach smaller rank tree under root of higher rank tree
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        
        # If ranks were equal, the new root's rank increases
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def component_size(self, x):
        return self.size[self.find(x)]


# HIGHEST FREQUENCY (Must Know) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 7.2: LeetCode 323 - Number of Connected Components
# ============================================================================
"""
Problem:
--------
You have a graph of n nodes. Given edges, return the number of connected
components.

Example:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
"""

def countComponents(n, edges):
    """
    Approach: Union-Find
    
    Key Insight:
    - Start with n components (each node alone)
    - Each successful union reduces component count by 1
    - Final count = initial - successful_unions
    
    Time: O(E * alpha(N))
    Space: O(N)
    """
    dsu = DSU(n)
    components = n
    
    for u, v in edges:
        if dsu.union(u, v):
            components -= 1
    
    return components


# HIGHEST FREQUENCY (Must Know) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 7.3: LeetCode 547 - Number of Provinces
# ============================================================================
"""
Problem:
--------
There are n cities. isConnected[i][j] = 1 if i and j are directly connected.
A province is a group of directly or indirectly connected cities.
Return the total number of provinces.

Example:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""

def findCircleNum(isConnected):
    """
    Approach: Union-Find on adjacency matrix
    
    Time: O(N^2 * alpha(N))
    Space: O(N)
    """
    n = len(isConnected)
    dsu = DSU(n)
    
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                dsu.union(i, j)
    
    # Count unique roots
    return len(set(dsu.find(i) for i in range(n)))


# HIGHEST FREQUENCY (Must Know) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 7.4: LeetCode 684 - Redundant Connection
# ============================================================================
"""
Problem:
--------
A tree has n nodes labeled 1 to n with n-1 edges. One extra edge was added.
Find the edge that can be removed so the resulting graph is a tree.
If multiple, return the last one in input.

Example:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
"""

def findRedundantConnection(edges):
    """
    Approach: Union-Find - first edge that creates cycle
    
    Key Insight:
    - Process edges in order
    - If union(u, v) fails (they're already connected), this edge creates cycle
    - That's the redundant edge
    
    Time: O(N * alpha(N))
    Space: O(N)
    """
    n = len(edges)
    dsu = DSU(n + 1)  # Nodes are 1-indexed
    
    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]
    
    return []


# Test Pattern 7
print("\n" + "=" * 70)
print("PATTERN 7: DISJOINT SET UNION (UNION-FIND)")
print("=" * 70)

print("\n7.2 Number of Connected Components:")
print(countComponents(5, [[0,1],[1,2],[3,4]]))  # 2

print("\n7.3 Number of Provinces:")
print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # 2

print("\n7.4 Redundant Connection:")
print(findRedundantConnection([[1,2],[1,3],[2,3]]))  # [2,3]


# ============================================================================
# ============================================================================
# PATTERN 8: ADVANCED (SCC, BRIDGES, ARTICULATION POINTS)
# ============================================================================
# ============================================================================
"""
ADVANCED GRAPH ALGORITHMS - L6 STAFF INTERVIEW LEVEL

1. STRONGLY CONNECTED COMPONENTS (SCC) - Kosaraju's Algorithm
   - SCC: Every pair of vertices reaches each other (directed graph)
   - Uses 2 DFS passes + transposed graph
   
2. BRIDGES - Tarjan's Algorithm
   - Bridge: edge whose removal disconnects the graph
   - Uses low-link values and discovery times
   
3. ARTICULATION POINTS - Tarjan's Algorithm
   - Articulation point: vertex whose removal disconnects the graph
   - Critical for network reliability problems
"""


# ============================================================================
# PROBLEM 8.1: G-54 - Strongly Connected Components (Kosaraju's)
# ============================================================================
def kosaraju_scc(V, adj):
    """
    Approach: Kosaraju's Algorithm (2 DFS passes)
    
    Key Insight:
    Step 1: Do DFS on ORIGINAL graph, push nodes to stack in finish order
    Step 2: TRANSPOSE the graph (reverse all edges)
    Step 3: Pop from stack, do DFS on transposed graph - each DFS tree = 1 SCC
    
    Why this works:
    - Finish order ensures we start from "source" SCC
    - In transposed graph, we can only reach nodes within same SCC
    
    Time: O(V + E)
    Space: O(V + E)
    """
    # Step 1: DFS to fill stack by finish order
    visited = [False] * V
    stack = []
    
    def dfs1(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(node)
    
    for i in range(V):
        if not visited[i]:
            dfs1(i)
    
    # Step 2: Transpose graph (reverse edges)
    adj_rev = defaultdict(list)
    for u in range(V):
        for v in adj[u]:
            adj_rev[v].append(u)
    
    # Step 3: DFS on transposed in finish order
    visited = [False] * V
    sccs = []
    
    def dfs2(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in adj_rev[node]:
            if not visited[neighbor]:
                dfs2(neighbor, component)
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs2(node, component)
            sccs.append(component)
    
    return sccs


# HIGHEST FREQUENCY (Must Know for L6) - GOOGLE FAVORITE
# ============================================================================
# PROBLEM 8.2: G-55 / LeetCode 1192 - Critical Connections (Bridges)
# ============================================================================
"""
Problem:
--------
There are n servers numbered 0 to n-1 connected by undirected server-to-server
connections. A critical connection is one that, if removed, will make some 
server unable to reach some other.

Return all critical connections.

Example:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
"""

def criticalConnections(n, connections):
    """
    Approach: Tarjan's Bridge-Finding Algorithm
    
    Key Insight:
    - Bridge: edge (u, v) where v cannot reach u (or earlier ancestor) without using this edge
    - Track two values for each node:
      * disc[u]: discovery time (when DFS first visits)
      * low[u]: lowest disc reachable from u's subtree (via at most one back edge)
    - Edge (u, v) is a bridge iff low[v] > disc[u]
      (v's subtree cannot reach back to u or its ancestors)
    
    Algorithm:
    - DFS, assign disc and low
    - low[u] = min(low[u], low[v]) for tree edges
    - low[u] = min(low[u], disc[v]) for back edges
    - After processing child v: if low[v] > disc[u], (u,v) is a bridge
    
    Time: O(V + E)
    Space: O(V)
    """
    adj = defaultdict(list)
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)
    
    disc = [-1] * n
    low = [-1] * n
    bridges = []
    timer = [0]
    
    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        
        for v in adj[u]:
            if v == parent:
                continue  # Skip edge back to parent
            
            if disc[v] == -1:
                # Tree edge
                dfs(v, u)
                low[u] = min(low[u], low[v])
                
                # Bridge condition
                if low[v] > disc[u]:
                    bridges.append([u, v])
            else:
                # Back edge
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    
    return bridges


# ============================================================================
# PROBLEM 8.3: G-56 - Articulation Points
# ============================================================================
def articulation_points(V, adj):
    """
    Approach: Tarjan's Algorithm for Articulation Points
    
    Key Insight:
    - Articulation point: removing it disconnects graph
    - Similar to bridges, but conditions differ:
      * ROOT of DFS tree: articulation point iff it has >= 2 children
      * NON-ROOT u: articulation point iff has child v with low[v] >= disc[u]
        (v's subtree cannot reach an ancestor of u without going through u)
    
    Difference from bridges: >= instead of >
    - For bridges: low[v] > disc[u]
    - For articulation: low[v] >= disc[u]
    
    Time: O(V + E)
    Space: O(V)
    """
    disc = [-1] * V
    low = [-1] * V
    is_ap = [False] * V
    timer = [0]
    
    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        children = 0
        
        for v in adj[u]:
            if v == parent:
                continue
            
            if disc[v] == -1:
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])
                
                # Non-root articulation condition
                if parent != -1 and low[v] >= disc[u]:
                    is_ap[u] = True
            else:
                low[u] = min(low[u], disc[v])
        
        # Root articulation condition: 2+ children
        if parent == -1 and children > 1:
            is_ap[u] = True
    
    for i in range(V):
        if disc[i] == -1:
            dfs(i, -1)
    
    return [i for i in range(V) if is_ap[i]]


# Test Pattern 8
print("\n" + "=" * 70)
print("PATTERN 8: ADVANCED (SCC, BRIDGES, ARTICULATION POINTS)")
print("=" * 70)

print("\n8.1 Strongly Connected Components (Kosaraju):")
adj_scc = {0:[1], 1:[2], 2:[0,3], 3:[4], 4:[]}
print(kosaraju_scc(5, adj_scc))

print("\n8.2 Critical Connections (Bridges):")
print(criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))

print("\n8.3 Articulation Points:")
adj_ap = {0:[1,2], 1:[0,2], 2:[0,1,3], 3:[2,4], 4:[3]}
print(articulation_points(5, adj_ap))


# ============================================================================
# ============================================================================
# INTERVIEW STRATEGY & PATTERN RECOGNITION CHEAT SHEET
# ============================================================================
# ============================================================================
"""
HOW TO IDENTIFY GRAPH PROBLEMS IN INTERVIEWS:
----------------------------------------------

KEYWORDS -> PATTERN MAPPING:

1. "Connected", "Reachable", "Components", "Islands"
   -> PATTERN 1: BFS/DFS Traversal

2. "Cycle", "Loop", "Circular dependency"
   -> PATTERN 2: Cycle Detection
   -> Use DFS for directed, BFS or DFS for undirected

3. "Two groups", "Color", "Partition into two sets"
   -> PATTERN 3: Bipartite

4. "Order", "Schedule", "Prerequisites", "Dependencies"
   -> PATTERN 4: Topological Sort
   -> Kahn's (BFS) is easier to code, DFS is more elegant

5. "Shortest path", "Minimum cost path", "Fewest steps"
   -> PATTERN 5: Shortest Path
   -> Unweighted: BFS
   -> Non-negative weights: Dijkstra
   -> Negative weights: Bellman-Ford
   -> All pairs: Floyd-Warshall

6. "Minimum cost to connect", "MST", "Network design"
   -> PATTERN 6: MST (Prim's or Kruskal's)

7. "Group", "Friend circles", "Disjoint", "Dynamic connectivity"
   -> PATTERN 7: Union-Find

8. "Critical connection", "Bridge", "Cut vertex"
   -> PATTERN 8: Tarjan's algorithms

INTERVIEW DECISION FRAMEWORK:
-----------------------------
1. Is it a graph? (nodes with relationships)
2. Directed or undirected?
3. Weighted or unweighted?
4. What am I being asked?
   - Existence/reachability -> DFS/BFS
   - Shortest path -> BFS/Dijkstra/Bellman-Ford
   - Ordering -> Topological sort
   - Cycle -> DFS with state tracking
   - Components -> DFS/BFS or Union-Find
   - Min total cost -> MST

L6 INTERVIEW TIPS:
------------------
1. CLARIFY first: directed? weighted? size constraints?
2. DRAW small example before coding
3. STATE complexity upfront (time + space)
4. DISCUSS trade-offs: why Dijkstra vs Bellman-Ford?
5. CONSIDER edge cases: empty graph, disconnected, self-loops
6. SCALE discussion: what if graph is too large for memory?
   - Distributed algorithms (Pregel, GraphX)
   - Streaming algorithms
   - Approximation algorithms

GOOGLE-SPECIFIC FAVORITES:
--------------------------
- Number of Islands (LC 200)
- Course Schedule I/II (LC 207, 210)
- Alien Dictionary (LC 269)
- Network Delay Time (LC 743)
- Cheapest Flights K Stops (LC 787)
- Min Cost Connect Points (LC 1584)
- Critical Connections (LC 1192)
- Word Ladder (LC 127) - BFS
- Clone Graph (LC 133) - DFS/BFS
- Pacific Atlantic Water Flow (LC 417) - Multi-source BFS
"""

print("\n" + "=" * 70)
print("ALL TESTS COMPLETED - Graph Solutions File Ready for FAANG L6 Prep!")
print("=" * 70)

