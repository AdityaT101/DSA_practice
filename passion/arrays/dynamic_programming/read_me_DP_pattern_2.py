"""
Dynamic Programming Design Patterns Guide - Part 2
=================================================

This is the continuation of the DP patterns guide, covering patterns 5-8:
- Interval DP
- Decision Making DP
- Counting DP
- Advanced Patterns (Tree/Graph/Bitmask)
"""

# ============================================================================
# PATTERN 5: INTERVAL DP
# ============================================================================
"""
Pattern Characteristics:
-----------------------
- Problems dealing with intervals or ranges
- Often requires considering all possible ways to split an interval
- Typically uses a 2D array where dp[i][j] represents optimal result for interval [i...j]
- Solved by considering all possible splitting points within the interval

When to Use:
-----------
- Problems involving merging elements
- Problems asking for optimal partition of a sequence
- When solutions depend on combining results from smaller intervals
- Problems about operations on subarrays
"""

# ============================================================================
# 5-A: Interval DP Template
# ============================================================================

def interval_dp_template(arr):
    """
    Template for interval DP problems
    
    Pattern:
    1. Define state: dp[i][j] = optimal result for subarray arr[i...j]
    2. Base cases: typically single elements
    3. Fill the DP array diagonally (considering lengths 1, 2, 3, etc.)
    4. For each interval [i,j], consider all possible ways to split it
    5. Return the result for the entire interval
    """
    n = len(arr)
    
    # Initialize DP array
    dp = [[0] * n for _ in range(n)]
    
    # Base case: single elements
    for i in range(n):
        dp[i][i] = base_case_value(arr[i])  # Adapt based on problem
    
    # Fill the DP array diagonally (by length)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1  # End of current interval
            
            # Initialize with a default value
            dp[i][j] = initial_value  # Adapt based on problem
            
            # Consider all splitting points
            for k in range(i, j):
                # Combine results from the two subintervals
                current = combine(dp[i][k], dp[k+1][j], arr, i, k, j)  # Adapt based on problem
                
                # Update if better
                dp[i][j] = better_of(dp[i][j], current)  # Adapt based on problem
    
    return dp[0][n-1]  # Result for entire array


# ============================================================================
# 5-B: Problems by Difficulty
# ============================================================================
"""
Easy Problems:
-------------
None

Medium Problems:
--------------
1. LC 1039 - Minimum Score Triangulation of Polygon
   - Find minimum score by multiplying triplets of vertices
   - dp[i][j] = min(dp[i][k] + dp[k][j] + arr[i]*arr[j]*arr[k]) for all k between i and j

Hard Problems:
------------
1. LC 312 - Burst Balloons
   - Maximum coins by bursting balloons
   - dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1]) for all k

2. LC 1000 - Minimum Cost to Merge Stones
   - Minimum cost to merge stone piles
   - Complex interval DP with multiple merges

3. LC 546 - Remove Boxes
   - Maximum points by removing consecutive boxes
   - 3D DP with intervals and additional state
"""

# ============================================================================
# PATTERN 6: DECISION MAKING DP
# ============================================================================
"""
Pattern Characteristics:
-----------------------
- Problems involving sequential decisions with state transitions
- Often tracks multiple states at each position (e.g., buy/sell/cooldown)
- State transitions depend on decisions made
- Typically involves maximizing profit or minimizing cost

When to Use:
-----------
- Problems with distinct states at each step
- When different actions lead to different state transitions
- Problems asking to optimize a sequence of decisions
- When current decisions depend on previous states
"""

# ============================================================================
# 6-A: State Machine DP Template
# ============================================================================

def state_machine_template(arr):
    """
    Template for state machine DP problems
    
    Pattern:
    1. Identify the possible states at each position
    2. Define state transitions based on actions
    3. Fill the DP arrays for each state
    4. Return the optimal final state
    """
    n = len(arr)
    
    # Initialize DP arrays for different states
    state1 = [0] * n  # E.g., holding stock
    state2 = [0] * n  # E.g., not holding stock
    
    # Base cases
    state1[0] = initial_state1  # Adapt based on problem
    state2[0] = initial_state2  # Adapt based on problem
    
    # Fill DP arrays
    for i in range(1, n):
        # State transitions based on decisions
        state1[i] = max(state1_transition1(state1[i-1], arr[i]), 
                         state1_transition2(state2[i-1], arr[i]))
        
        state2[i] = max(state2_transition1(state1[i-1], arr[i]), 
                         state2_transition2(state2[i-1], arr[i]))
    
    # Return optimal final state
    return max(final_state1(state1[n-1]), final_state2(state2[n-1]))


# ============================================================================
# 6-B: Buy/Sell Stock Template
# ============================================================================

def buy_sell_stock_template(prices):
    """
    Template for buy/sell stock problems
    
    Pattern:
    1. Define states: holding and not holding stock
    2. Define transitions: buy, sell, hold, rest
    3. Optimize for maximum profit
    """
    n = len(prices)
    
    # Edge case
    if n <= 1:
        return 0
    
    # Initialize DP arrays
    # hold[i]: maximum profit if holding stock after day i
    # not_hold[i]: maximum profit if not holding stock after day i
    hold = [0] * n
    not_hold = [0] * n
    
    # Base cases
    hold[0] = -prices[0]  # Buy on first day
    not_hold[0] = 0       # Do nothing on first day
    
    # Fill DP arrays
    for i in range(1, n):
        # If holding stock, either kept from previous day or bought today
        hold[i] = max(hold[i-1], not_hold[i-1] - prices[i])
        
        # If not holding stock, either kept from previous day or sold today
        not_hold[i] = max(not_hold[i-1], hold[i-1] + prices[i])
    
    # Final answer must be not holding stock
    return not_hold[n-1]


# ============================================================================
# 6-C: Problems by Difficulty
# ============================================================================
"""
Easy Problems:
-------------
1. LC 121 - Best Time to Buy and Sell Stock
   - Maximum profit by buying once and selling once
   - Track minimum price seen so far

2. LC 122 - Best Time to Buy and Sell Stock II
   - Maximum profit by buying and selling multiple times
   - Add up all price increases

Medium Problems:
--------------
1. LC 309 - Best Time to Buy and Sell Stock with Cooldown
   - Max profit with cooldown constraint
   - Three states: hold, not_hold_ready, not_hold_cooldown

2. LC 714 - Best Time to Buy and Sell Stock with Transaction Fee
   - Max profit with fee for each transaction
   - Two states with transaction fee applied during sell

Hard Problems:
------------
1. LC 123 - Best Time to Buy and Sell Stock III
   - Max profit with at most 2 transactions
   - Four states tracking number of transactions

2. LC 188 - Best Time to Buy and Sell Stock IV
   - Max profit with at most k transactions
   - DP array with states for each transaction
"""

# ============================================================================
# PATTERN 7: COUNTING DP
# ============================================================================
"""
Pattern Characteristics:
-----------------------
- Problems asking to count the number of ways to do something
- Often uses addition in the recurrence relation
- Results can be very large (requiring modulo operations)
- Typically involves combinatorial mathematics

When to Use:
-----------
- When asked to count the number of ways, arrangements, or combinations
- Problems involving permutations or combinations with constraints
- When the order of elements matters (or doesn't matter)
- Problems asking for probability
"""

# ============================================================================
# 7-A: Counting DP Template
# ============================================================================

def counting_dp_template(n, constraints):
    """
    Template for counting DP problems
    
    Pattern:
    1. Define state: dp[i] = number of ways for subproblem of size i
    2. Define base cases (typically dp[0] = 1, one way to do nothing)
    3. Build solutions by adding the number of ways from smaller subproblems
    4. Apply constraints to limit the valid transitions
    """
    MOD = 10**9 + 7  # Common requirement for large results
    
    # Initialize DP array
    dp = [0] * (n + 1)
    
    # Base case
    dp[0] = 1  # One way to do nothing
    
    # Fill DP array
    for i in range(1, n + 1):
        for j in range(constraints.min, constraints.max + 1):
            if i - j >= 0:
                # Add the number of ways from the smaller subproblem
                dp[i] = (dp[i] + dp[i - j]) % MOD
    
    return dp[n]


# ============================================================================
# 7-B: Combinatorial DP Template
# ============================================================================

def combinatorial_dp_template(n, k):
    """
    Template for combinatorial DP problems (e.g., C(n,k))
    
    Pattern:
    1. Define state: dp[i][j] = number of ways to choose j elements from i elements
    2. Use the recurrence relation: C(n,k) = C(n-1,k-1) + C(n-1,k)
    3. Build up the results iteratively
    """
    # Initialize DP array
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base cases
    for i in range(n + 1):
        dp[i][0] = 1  # One way to choose 0 elements
    
    # Fill DP array
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            # Either include the current element or exclude it
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    return dp[n][k]


# ============================================================================
# 7-C: Problems by Difficulty
# ============================================================================
"""
Easy Problems:
-------------
1. LC 70 - Climbing Stairs
   - Count ways to climb n steps taking 1 or 2 steps at a time
   - dp[i] = dp[i-1] + dp[i-2]

Medium Problems:
--------------
1. LC 62 - Unique Paths
   - Number of unique paths from top-left to bottom-right
   - dp[i][j] = dp[i-1][j] + dp[i][j-1]

2. LC 91 - Decode Ways
   - Count ways to decode a string of digits
   - dp[i] = dp[i-1] if valid + dp[i-2] if valid pair

3. LC 377 - Combination Sum IV
   - Number of combinations that sum to target
   - dp[i] += dp[i-num] for each num in nums

4. LC 1155 - Number of Dice Rolls With Target Sum
   - Ways to get sum using dice with f faces
   - dp[i][j] = sum(dp[i-1][j-k]) for k in 1 to f

Hard Problems:
------------
1. LC 1359 - Count All Valid Pickup and Delivery Options
   - Count valid pickup/delivery sequences
   - Mathematical solution: (2n)! / 2^n

2. LC 1220 - Count Vowels Permutation
   - Count strings following rules for vowel transitions
   - Matrix exponentiation for efficient calculation
   
3. LC 940 - Distinct Subsequences II
   - Count distinct subsequences with duplicates
   - Use DP with character last seen positions
"""

# ============================================================================
# PATTERN 8: ADVANCED PATTERNS
# ============================================================================
"""
Pattern Characteristics:
-----------------------
- Problems requiring more complex state representation or optimization techniques
- May combine multiple DP patterns or use additional data structures
- Often involve multiple dimensions or compressed state representations
- Typically found in hard problems

When to Use:
-----------
- When basic DP patterns are insufficient
- Problems with complex state spaces or constraints
- When optimizations are needed for performance
- Problems on trees, graphs, or requiring state compression
"""

# ============================================================================
# 8-A: Tree DP Template
# ============================================================================

def tree_dp_template(root):
    """
    Template for Tree DP problems
    
    Pattern:
    1. Use post-order traversal to solve subproblems bottom-up
    2. Maintain states for each node (often two states: included/excluded)
    3. Combine results from child nodes based on states
    4. Return optimal result from root
    """
    # Define memoization dictionary or function
    memo = {}
    
    def dfs(node, state):
        if not node:
            return 0
        
        # Check if already computed
        if (node, state) in memo:
            return memo[(node, state)]
        
        # Compute result based on state
        if state == 0:  # Node not included
            result = sum(dfs(child, 1) for child in node.children)
        else:  # Node included
            result1 = node.val + sum(dfs(child, 0) for child in node.children)
            result2 = sum(dfs(child, 1) for child in node.children)
            result = max(result1, result2)
        
        # Memoize and return
        memo[(node, state)] = result
        return result
    
    # Start DFS from root
    return max(dfs(root, 0), dfs(root, 1))


# ============================================================================
# 8-B: Bitmask DP Template
# ============================================================================

def bitmask_dp_template(n):
    """
    Template for Bitmask DP problems
    
    Pattern:
    1. Represent a subset of n elements using an integer with n bits
    2. Define state: dp[mask] = result for subset represented by mask
    3. Iterate through all possible masks
    4. Use bit operations to manipulate and check the mask
    5. Return the result for the target mask
    """
    # Number of possible subsets is 2^n
    dp = [0] * (1 << n)
    
    # Base case
    dp[0] = base_case_value  # Adapt based on problem
    
    # Fill DP array
    for mask in range(1, 1 << n):
        # Process based on the current mask
        dp[mask] = initial_value  # Adapt based on problem
        
        # Consider all elements that could be included in this mask
        for i in range(n):
            if mask & (1 << i):  # Check if bit i is set in mask
                # Previous mask without element i
                prev_mask = mask ^ (1 << i)
                
                # Update DP value based on including element i
                dp[mask] = better_of(dp[mask], 
                                     combine(dp[prev_mask], element_value(i)))  # Adapt based on problem
    
    return dp[(1 << n) - 1]  # Result for including all elements


# ============================================================================
# 8-C: DP with Binary Search Template
# ============================================================================

def dp_with_binary_search_template(arr):
    """
    Template for DP problems optimized with binary search
    
    Pattern:
    1. Maintain an auxiliary array to track optimal values
    2. Use binary search to find the insertion position efficiently
    3. Update the auxiliary array and DP values
    """
    n = len(arr)
    
    # Initialize auxiliary array
    aux = [float('inf')] * (n + 1)
    aux[0] = float('-inf')
    
    # Initialize DP array (if needed)
    dp = [0] * n
    
    # Length of the optimal solution
    length = 0
    
    # Process each element
    for i in range(n):
        # Binary search to find the position to insert current element
        left, right = 0, length
        while left < right:
            mid = (left + right + 1) // 2
            if aux[mid] < arr[i]:
                left = mid
            else:
                right = mid - 1
        
        # Insert position is left+1
        pos = left + 1
        
        # Update auxiliary array
        aux[pos] = arr[i]
        
        # Update DP value
        dp[i] = pos
        
        # Update length of the solution
        length = max(length, pos)
    
    # Return result based on problem requirements
    return length  # or reconstruct the solution using dp array


# ============================================================================
# 8-D: Problems by Difficulty
# ============================================================================
"""
Tree DP Problems:
---------------
1. LC 337 - House Robber III (Medium)
   - Maximum money that can be robbed from houses in a tree
   - Two states: rob current node or not

2. LC 1372 - Longest ZigZag Path in a Binary Tree (Medium)
   - Longest path where directions alternate
   - States track both left and right zigzag lengths

3. LC 834 - Sum of Distances in Tree (Hard)
   - Sum of distances from each node to all others
   - Two-pass DP with tree re-rooting technique

Bitmask DP Problems:
------------------
1. LC 1434 - Number of Ways to Wear Different Hats to Each Other (Hard)
   - People wearing hats with constraints
   - dp[mask][hat] for subsets of people and hat choices

2. LC 1125 - Smallest Sufficient Team (Hard)
   - Smallest team with all required skills
   - dp[mask] = minimum people needed for skill mask

3. LC 943 - Find the Shortest Superstring (Hard)
   - Find shortest string containing all strings as substrings
   - dp[mask][last] for visited strings and last added

DP with Binary Search:
--------------------
1. LC 300 - Longest Increasing Subsequence (Medium)
   - Length of longest strictly increasing subsequence
   - Patience sort with binary search: O(n log n)

2. LC 1235 - Maximum Profit in Job Scheduling (Hard)
   - Maximum profit from non-overlapping jobs
   - Sort by end time, binary search for previous non-overlapping job

3. LC 354 - Russian Doll Envelopes (Hard)
   - Max number of envelopes that can be nested
   - Sort by width, LIS on height with binary search
"""

# ============================================================================
# SUMMARY AND LEARNING PATH
# ============================================================================
"""
Recommended Learning Path:

1. Start with Basic Patterns:
   - Linear DP (Sequence)
   - Simple 2D Grid Problems
   - Basic Counting Problems

2. Move to Intermediate Patterns:
   - String DP Problems (Subsequence, Palindromes)
   - Partition DP (Knapsack variants)
   - Decision Making DP (State Machines)

3. Advanced Patterns:
   - Interval DP
   - Tree/Graph DP
   - Bitmask DP
   - DP with Optimization Techniques

General Approach to DP Problems:
-------------------------------
1. Identify the subproblems and define the state
2. Establish the recurrence relation
3. Determine the base cases
4. Decide the traversal order
5. Implement the solution (bottom-up or top-down)
6. Optimize for space if needed
7. Trace through a small example to verify correctness

Remember: Practice is key for mastering DP. Start with easier problems
in each pattern and gradually work your way up to harder ones.
"""
