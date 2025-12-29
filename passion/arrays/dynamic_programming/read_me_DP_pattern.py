"""
Dynamic Programming Design Patterns Guide
=========================================

This guide organizes DP problems by their underlying design patterns rather than by data structure.
For each pattern, you'll find:

1. Key characteristics and when to use the pattern
2. Template code that can be adapted to similar problems
3. Step-by-step approach for solving problems with this pattern
4. Problems organized by difficulty (easy -> medium -> hard)

Master these patterns and you'll be equipped to solve nearly any DP problem!
"""

# ============================================================================
# TABLE OF CONTENTS
# ============================================================================
"""
1. Linear DP (Sequence)
   - 1-D Array Traversal
   - Kadane's Algorithm (Maximum Subarray)
   - House Robber Pattern

2. Two-Dimensional DP
   - Grid Traversal
   - Path Problems
   - Area/Region Optimization

3. String-Based DP
   - Substring/Subsequence Problems
   - String Matching and Edit Distance
   - Palindromic Problems

4. Partition DP
   - 0/1 Knapsack
   - Subset Sum
   - Partition Problems

5. Interval DP
   - Range-based Problems
   - Merging Intervals

6. Decision Making DP
   - Buy/Sell Stock Problems
   - State Machine Transitions

7. Counting DP
   - Combinatorial Counting
   - Arrangement Problems

8. Advanced Patterns
   - Tree DP
   - Graph DP 
   - Bitmask DP
   - DP with Binary Search
   - DP with Data Structures (Monotonic Queue, etc.)
"""

# ============================================================================
# PATTERN 1: LINEAR DP (SEQUENCE DP)
# ============================================================================
"""
Pattern Characteristics:
-----------------------
- Problems involving sequences where the solution depends on previous computations
- Typically uses a 1D array to store states
- Current state depends only on a few previous states
- Often follows the form dp[i] = some_function(dp[i-1], dp[i-2], ...)

When to Use:
-----------
- Problems asking for optimization (max/min) over a sequence
- Problems involving choices at each position that affect future decisions
- When current decisions depend only on a limited number of previous states
"""

# ============================================================================
# 1-A: Basic Linear Sequence Template
# ============================================================================

def linear_dp_template(arr):
    """
    Template for basic linear DP problems
    
    Pattern:
    1. Define state: dp[i] = answer for subproblem ending at position i
    2. Define base cases
    3. Define recurrence relation (transition)
    4. Fill DP array in a bottom-up manner
    5. Return final answer
    """
    if not arr:
        return 0
    
    n = len(arr)
    
    # Initialize DP array
    dp = [0] * n
    
    # Base case(s)
    dp[0] = arr[0]  # Example base case
    
    # Fill DP array
    for i in range(1, n):
        # Recurrence relation
        dp[i] = some_function(dp[i-1], arr[i])
    
    # Return final answer
    return dp[n-1]


# ============================================================================
# 1-B: Kadane's Algorithm Template (Maximum Subarray)
# ============================================================================

def kadane_template(arr):
    """
    Template for maximum subarray and related problems
    
    Pattern:
    1. Track current_sum and max_sum
    2. At each position, decide whether to extend previous subarray or start a new one
    3. Update max_sum if current_sum is larger
    """
    if not arr:
        return 0
    
    current_sum = max_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Decision: extend previous subarray or start a new one
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update maximum sum found so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# ============================================================================
# 1-C: House Robber Pattern (Non-adjacent Selection)
# ============================================================================

def house_robber_template(arr):
    """
    Template for problems where you can't select adjacent elements
    
    Pattern:
    1. At each position, you have two choices:
       - Take the current element (and skip the next one)
       - Skip the current element (and potentially take the next one)
    2. Choose the option that maximizes the result
    """
    if not arr:
        return 0
    
    n = len(arr)
    
    if n == 1:
        return arr[0]
    
    # Initialize DP array
    # dp[i] = maximum value obtainable up to position i
    dp = [0] * n
    
    # Base cases
    dp[0] = arr[0]  # Only one house
    dp[1] = max(arr[0], arr[1])  # Take the max of first two houses
    
    # Fill DP array
    for i in range(2, n):
        # Either skip current house or take it (and skip the previous one)
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    
    return dp[n-1]


# ============================================================================
# 1-D: Problems by Difficulty
# ============================================================================
"""
Easy Problems:
-------------
1. LC 70 - Climbing Stairs
   - Find ways to climb n steps when you can climb 1 or 2 steps at a time
   - dp[i] = dp[i-1] + dp[i-2]

2. LC 746 - Min Cost Climbing Stairs
   - Minimum cost to reach the top of the stairs
   - dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

3. LC 53 - Maximum Subarray
   - Find contiguous subarray with largest sum
   - Kadane's algorithm

4. LC 121 - Best Time to Buy and Sell Stock
   - Max profit by buying once and selling once
   - Track minimum price seen so far

Medium Problems:
--------------
1. LC 198 - House Robber
   - Maximum money that can be robbed without alerting adjacent houses
   - dp[i] = max(dp[i-1], dp[i-2] + nums[i])

2. LC 213 - House Robber II
   - Same as House Robber but houses arranged in a circle
   - Run House Robber twice (once excluding the first house, once excluding the last)

3. LC 300 - Longest Increasing Subsequence
   - Length of longest strictly increasing subsequence
   - dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]

4. LC 152 - Maximum Product Subarray
   - Find contiguous subarray with largest product
   - Track both max and min product ending at each position

5. LC 413 - Arithmetic Slices
   - Count number of arithmetic subarrays
   - dp[i] = dp[i-1] + 1 if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]

6. LC 740 - Delete and Earn
   - Maximum points earned by deleting numbers
   - Transform into House Robber problem

Hard Problems:
------------
1. LC 1425 - Constrained Subsequence Sum
   - Maximum sum of subsequence with distance constraint
   - Use DP with monotonic deque

2. LC 123/188 - Best Time to Buy and Sell Stock III/IV
   - Max profit with at most k transactions
   - dp[i][j][0/1] = profit after i transactions on day j holding/not holding stock
"""


# ============================================================================
# PATTERN 2: TWO-DIMENSIONAL DP
# ============================================================================
"""
Pattern Characteristics:
-----------------------
- Problems involving grids, matrices, or two parameters
- Uses a 2D array to store states
- State depends on previously computed values in the grid
- Often follows form dp[i][j] = some_function(dp[i-1][j], dp[i][j-1], dp[i-1][j-1], etc.)

When to Use:
-----------
- Grid traversal problems
- Problems with two changing parameters
- Path finding in matrices
- Area calculation problems
"""

# ============================================================================
# 2-A: Grid Traversal Template
# ============================================================================

def grid_traversal_template(grid):
    """
    Template for grid traversal problems
    
    Pattern:
    1. Define state: dp[i][j] = answer for subgrid ending at position (i,j)
    2. Define base cases (first row and column)
    3. Define transitions based on allowed moves
    4. Fill grid row by row, column by column
    5. Return final state
    """
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    # Initialize DP array
    dp = [[0] * n for _ in range(m)]
    
    # Base cases
    dp[0][0] = grid[0][0]  # Starting position
    
    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill DP array
    for i in range(1, m):
        for j in range(1, n):
            # Recurrence relation based on allowed moves
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # Return final answer
    return dp[m-1][n-1]


# ============================================================================
# 2-B: Area/Region Optimization Template
# ============================================================================

def area_optimization_template(matrix):
    """
    Template for area/region optimization problems in a grid
    
    Pattern:
    1. Define state: dp[i][j] = optimal size/value ending at position (i,j)
    2. Update based on surrounding cells and the current cell's value
    3. Track the global optimum
    """
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    
    # Initialize DP array
    dp = [[0] * n for _ in range(m)]
    
    # Global optimum
    max_result = 0
    
    # Fill DP array
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:  # Example condition, adapt as needed
                # Base case for first row and column
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    # Update based on neighbors (example for maximal square)
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                # Update global optimum
                max_result = max(max_result, dp[i][j])
    
    return max_result


# ============================================================================
# 2-C: Problems by Difficulty
# ============================================================================
"""
Easy Problems:
-------------
1. LC 303 - Range Sum Query - Immutable
   - Calculate the sum of elements between indices
   - Use prefix sum: dp[i] = dp[i-1] + nums[i-1]

Medium Problems:
--------------
1. LC 62 - Unique Paths
   - Number of unique paths from top-left to bottom-right
   - dp[i][j] = dp[i-1][j] + dp[i][j-1]

2. LC 64 - Minimum Path Sum
   - Find path with minimum sum in a grid
   - dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

3. LC 120 - Triangle
   - Minimum path sum from top to bottom in a triangle
   - dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

4. LC 221 - Maximal Square
   - Find largest square containing only 1's
   - dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

5. LC 1105 - Filling Bookcase Shelves
   - Minimum height of bookshelf with width constraint
   - dp[i] = min(dp[j-1] + max_height) for valid j

Hard Problems:
------------
1. LC 85 - Maximal Rectangle
   - Find largest rectangle containing only 1's
   - Use histogram technique row by row

2. LC 174 - Dungeon Game
   - Minimum initial health to rescue princess
   - Work backwards from bottom-right
   - dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

3. LC 329 - Longest Increasing Path in a Matrix
   - Length of longest increasing path
   - DP with memoization (DFS)
"""


# ============================================================================
# PATTERN 3: STRING-BASED DP
# ============================================================================
"""
Pattern Characteristics:
-----------------------
- Problems involving string manipulation, matching, or transformation
- Often uses a 1D or 2D array where indices correspond to string positions
- Recurrence relations depend on character comparisons
- Common in substring, subsequence, and edit distance problems

When to Use:
-----------
- Problems asking about substrings or subsequences
- String matching or alignment problems
- Edit distance or transformation problems
- Palindrome-related problems
"""

# ============================================================================
# 3-A: Subsequence Template
# ============================================================================

def string_subsequence_template(s, t):
    """
    Template for string subsequence problems involving two strings
    
    Pattern:
    1. Define state: dp[i][j] = answer for s[0:i] and t[0:j]
    2. Handle base cases (empty strings)
    3. Define transitions based on character comparisons
    4. Fill DP table and return final state
    """
    m, n = len(s), len(t)
    
    # Initialize DP array with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: empty strings
    for i in range(m + 1):
        dp[i][0] = 0  # Match with empty t
    
    for j in range(n + 1):
        dp[0][j] = 0  # Match with empty s
    
    # Fill DP array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                # Characters match
                dp[i][j] = dp[i-1][j-1] + 1  # Example: count matches
            else:
                # Characters don't match
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # Example: LCS
    
    return dp[m][n]


# ============================================================================
# 3-B: Palindrome Template
# ============================================================================

def palindrome_dp_template(s):
    """
    Template for palindrome-related DP problems
    
    Pattern:
    1. Define state: dp[i][j] = whether s[i:j+1] is a palindrome
    2. Base cases: single characters and adjacent pairs
    3. Fill DP table using expanding window approach
    4. Process results based on problem requirements
    """
    n = len(s)
    
    # Initialize DP array: dp[i][j] = is s[i:j+1] a palindrome?
    dp = [[False] * n for _ in range(n)]
    
    # Base case 1: single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Base case 2: check adjacent characters
    for i in range(n - 1):
        dp[i][i + 1] = (s[i] == s[i + 1])
    
    # Fill DP array for substrings of length 3 to n
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # A substring is palindrome if first and last chars match
            # AND the substring between them is also a palindrome
            dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
    
    # For problems like "longest palindromic substring"
    # find the longest palindrome from the DP table
    max_length = 0
    start = 0
    
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] and j - i + 1 > max_length:
                max_length = j - i + 1
                start = i
    
    return s[start:start + max_length]  # Example return


# ============================================================================
# 3-C: Edit Distance Template
# ============================================================================

def edit_distance_template(word1, word2):
    """
    Template for edit distance problems between strings
    
    Pattern:
    1. Define state: dp[i][j] = min operations to transform word1[0:i] to word2[0:j]
    2. Base cases: transforming to/from empty string
    3. Define transitions based on character comparisons and edit operations
    4. Return the final state
    """
    m, n = len(word1), len(word2)
    
    # Initialize DP array
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: transforming to/from empty string
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    # Fill DP array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i-1][j-1]
            else:
                # Three operations: insert, delete, replace
                dp[i][j] = 1 + min(
                    dp[i][j-1],    # Insert
                    dp[i-1][j],    # Delete
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]


# ============================================================================
# 3-D: Problems by Difficulty
# ============================================================================
"""
Easy Problems:
-------------
None

Medium Problems:
--------------
1. LC 5 - Longest Palindromic Substring
   - Find the longest palindromic substring
   - dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]

2. LC 516 - Longest Palindromic Subsequence
   - Length of longest palindromic subsequence
   - dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j] else max(dp[i+1][j], dp[i][j-1])

3. LC 647 - Palindromic Substrings
   - Count all palindromic substrings
   - Use palindrome dp table and count all true values

4. LC 91 - Decode Ways
   - Count ways to decode a string of digits
   - dp[i] = dp[i-1] if valid + dp[i-2] if valid pair

5. LC 139 - Word Break
   - Determine if string can be segmented into dictionary words
   - dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))

6. LC 1143 - Longest Common Subsequence
   - Length of LCS between two strings
   - dp[i][j] = dp[i-1][j-1] + 1 if match else max(dp[i-1][j], dp[i][j-1])

7. LC 97 - Interleaving String
   - Whether s3 is formed by interleaving s1 and s2
   - dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

8. LC 583 - Delete Operation for Two Strings
   - Min deletions to make two strings equal
   - Find LCS, then delete (len(word1) - LCS) + (len(word2) - LCS)

9. LC 1048 - Longest String Chain
   - Longest chain where each word adds one letter
   - Sort by length, dp[word] = max(dp[word], dp[predecessor] + 1)

Hard Problems:
------------
1. LC 10 - Regular Expression Matching
   - Match string to pattern with '.' and '*'
   - Complex state transitions with wildcards

2. LC 44 - Wildcard Matching
   - Match string to pattern with '?' and '*'
   - Similar to regex but with different wildcards

3. LC 72 - Edit Distance
   - Minimum operations to convert one string to another
   - dp[i][j] = min(insert, delete, replace) if chars don't match

4. LC 115 - Distinct Subsequences
   - Count distinct subsequences of t in s
   - dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1] == t[j-1] else 0)

5. LC 32 - Longest Valid Parentheses
   - Length of longest valid parentheses substring
   - dp[i] = dp[i-2] + 2 or dp[i-1] + dp[i-dp[i-1]-2] + 2 depending on pattern
"""

# ============================================================================
# PATTERN 4: PARTITION DP (KNAPSACK VARIATIONS)
# ============================================================================
"""
Pattern Characteristics:
-----------------------
- Problems involving selecting items from a set with constraints
- Often use a 2D array where one dimension is the item index, another is capacity/target
- Decisions involve taking or not taking items
- Involves optimization over a subset of elements

When to Use:
-----------
- Problems asking to find optimal subsets
- When constraints limit what can be selected
- When there's a weight/capacity and value/profit trade-off
- When you need to partition a set into subsets with specific properties
"""

# ============================================================================
# 4-A: 0/1 Knapsack Template
# ============================================================================

def knapsack_template(weights, values, capacity):
    """
    Template for 0/1 Knapsack problems
    
    Pattern:
    1. Define state: dp[i][w] = maximum value using items 0...i with capacity w
    2. Base cases: no items or zero capacity
    3. For each item, decide whether to include it or not
    4. Return the maximum value possible
    """
    n = len(weights)
    
    # Initialize DP array
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill DP array
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # Can include this item
                # Choose max of (include current item) vs (exclude current item)
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # Can't include this item (too heavy)
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]


# Space-optimized version
def knapsack_optimized(weights, values, capacity):
    """
    Space-optimized version of 0/1 Knapsack
    
    Pattern:
    1. Use a 1D array instead of 2D
    2. Process weights in reverse order to avoid overwriting needed values
    """
    n = len(weights)
    
    # Initialize 1D DP array
    dp = [0] * (capacity + 1)
    
    # Fill DP array
    for i in range(n):
        # Process from right to left to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]


# ============================================================================
# 4-B: Subset Sum Template
# ============================================================================

def subset_sum_template(nums, target):
    """
    Template for Subset Sum problems
    
    Pattern:
    1. Define state: dp[i][j] = whether subset of nums[0...i-1] can sum to j
    2. Base cases: empty subset sums to 0
    3. For each number, decide whether to include it or not
    4. Return whether the target can be achieved
    """
    n = len(nums)
    
    # Initialize DP array
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Base case: empty subset sums to 0
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill DP array
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i-1] <= j:
                # Current element can be part of the sum
                # Either include it or exclude it
                dp[i][j] = dp[i-1][j - nums[i-1]] or dp[i-1][j]
            else:
                # Current element cannot be part of the sum (too large)
                dp[i][j] = dp[i-1][j]
    
    return dp[n][target]


# Space-optimized version
def subset_sum_optimized(nums, target):
    """
    Space-optimized version of Subset Sum
    
    Pattern:
    1. Use a 1D array instead of 2D
    2. Process in reverse order to avoid overwriting needed values
    """
    # Initialize 1D DP array
    dp = [False] * (target + 1)
    dp[0] = True  # Base case
    
    # Fill DP array
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]


# ============================================================================
# 4-C: Problems by Difficulty
# ============================================================================
"""
Easy Problems:
-------------
None

Medium Problems:
--------------
1. LC 416 - Partition Equal Subset Sum
   - Whether array can be partitioned into two equal sum subsets
   - Subset sum with target = sum(nums)/2

2. LC 494 - Target Sum
   - Ways to assign + and - to reach a target sum
   - Transform into subset sum: find subset that sums to (target + sum(nums))/2

3. LC 1049 - Last Stone Weight II
   - Minimum possible weight after smashing stones
   - Partition to minimize difference: subset sum closest to sum(stones)/2

Hard Problems:
------------
1. LC 1434 - Number of Ways to Wear Different Hats to Each Other
   - Complex assignment problem with constraints
   - DP with bitmask representation

2. LC 1125 - Smallest Sufficient Team
   - Find smallest team with all required skills
   - DP with bitmask representation of skills
"""

# Continue to the next file for the remaining patterns...
