"""
DYNAMIC PROGRAMMING - STRIVER'S DP SERIES
==========================================
Complete solutions for all DP problems from Striver's DP playlist

DP Patterns Covered:
--------------------
1. 1D DP (Climbing Stairs, Frog Jump, House Robber)
2. 2D/Grid DP (Unique Paths, Minimum Path Sum, Triangle)
3. DP on Subsequences (Subset Sum, Knapsack, Coin Change)
4. DP on Strings (LCS, Edit Distance)

General Approach:
-----------------
1. Try to represent the problem in terms of index
2. Do all possible stuffs on that index according to the problem statement
3. Sum/Min/Max of all stuffs -> return
4. Base case: smallest valid input

Optimization:
-------------
- Recursion -> Memoization -> Tabulation -> Space Optimization
"""


# ============================================================================
# PROBLEM 2: LeetCode 70 - Climbing Stairs
# ============================================================================

"""
Problem:
--------
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways 
can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: (1+1), (2)

Example 2:
Input: n = 3
Output: 3
Explanation: (1+1+1), (1+2), (2+1)

Constraints:
- 1 <= n <= 45
"""

def climbStairs(n):
    """
    Approach: 1D DP - Fibonacci Pattern
    
    Key Insight:
    - To reach step n, you can come from step n-1 (1 step) or n-2 (2 steps)
    - f(n) = f(n-1) + f(n-2)
    
    Time: O(n)
    Space: O(1) with space optimization
    """
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2
    
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    
    return prev1


def test_climbing_stairs():
    print("=" * 70)
    print("Problem 2: Climbing Stairs")
    print("=" * 70)
    
    test_cases = [(2, 2), (3, 3), (4, 5), (5, 8)]
    for n, expected in test_cases:
        result = climbStairs(n)
        status = "✅" if result == expected else "❌"
        print(f"n={n}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 3: Frog Jump (Striver)
# ============================================================================

"""
Problem:
--------
A frog wants to climb from the 0th stair to the (N-1)th stair. At each stair i,
the frog can jump to (i+1)th or (i+2)th stair. The cost to jump from stair i 
to stair j is |height[i] - height[j]|. Find the minimum cost to reach the last stair.

Example 1:
Input: heights = [10, 20, 30, 10]
Output: 20

Constraints:
- 1 <= N <= 10^5
- 1 <= heights[i] <= 10^4
"""

def frogJump(heights):
    """
    Approach: 1D DP
    dp[i] = min(dp[i-1] + |h[i]-h[i-1]|, dp[i-2] + |h[i]-h[i-2]|)
    
    Time: O(n), Space: O(1)
    """
    n = len(heights)
    if n == 1:
        return 0
    
    prev2 = 0
    prev1 = abs(heights[1] - heights[0])
    
    for i in range(2, n):
        jump1 = prev1 + abs(heights[i] - heights[i-1])
        jump2 = prev2 + abs(heights[i] - heights[i-2])
        curr = min(jump1, jump2)
        prev2 = prev1
        prev1 = curr
    
    return prev1


def test_frog_jump():
    print("=" * 70)
    print("Problem 3: Frog Jump")
    print("=" * 70)
    
    test_cases = [([10, 20, 30, 10], 20), ([10, 50, 10], 0)]
    for heights, expected in test_cases:
        result = frogJump(heights)
        status = "✅" if result == expected else "❌"
        print(f"Heights: {heights}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 4: Frog Jump with K Distance
# ============================================================================

"""
Problem: Same as Frog Jump, but frog can jump from i to any stair from i+1 to i+k.

Time: O(n*k), Space: O(n)
"""

def frogJumpK(heights, k):
    n = len(heights)
    if n == 1:
        return 0
    
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                cost = dp[i - j] + abs(heights[i] - heights[i - j])
                dp[i] = min(dp[i], cost)
    
    return dp[n - 1]


def test_frog_jump_k():
    print("=" * 70)
    print("Problem 4: Frog Jump with K Distance")
    print("=" * 70)
    
    test_cases = [([10, 30, 40, 50, 20], 3, 30), ([10, 20, 10], 1, 20)]
    for heights, k, expected in test_cases:
        result = frogJumpK(heights, k)
        status = "✅" if result == expected else "❌"
        print(f"Heights: {heights}, k={k}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 5: LeetCode 198 - House Robber
# ============================================================================

"""
Problem: Max sum of non-adjacent elements.
dp[i] = max(dp[i-2] + nums[i], dp[i-1])

Time: O(n), Space: O(1)
"""

def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, n):
        curr = max(prev2 + nums[i], prev1)
        prev2 = prev1
        prev1 = curr
    
    return prev1


def test_house_robber():
    print("=" * 70)
    print("Problem 5: House Robber")
    print("=" * 70)
    
    test_cases = [([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12)]
    for nums, expected in test_cases:
        result = rob(nums)
        status = "✅" if result == expected else "❌"
        print(f"Nums: {nums}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 6: LeetCode 213 - House Robber 2 (Circular)
# ============================================================================

"""
Problem: Houses in circle - can't rob both first and last.
Solution: max(rob[0:n-1], rob[1:n])
"""

def rob2(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    def rob_linear(arr):
        prev2 = arr[0]
        prev1 = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            curr = max(prev2 + arr[i], prev1)
            prev2 = prev1
            prev1 = curr
        return prev1
    
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


def test_house_robber_2():
    print("=" * 70)
    print("Problem 6: House Robber 2 (Circular)")
    print("=" * 70)
    
    test_cases = [([2, 3, 2], 3), ([1, 2, 3, 1], 4)]
    for nums, expected in test_cases:
        result = rob2(nums)
        status = "✅" if result == expected else "❌"
        print(f"Nums: {nums}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 7: Ninja's Training (2D DP)
# ============================================================================

"""
Problem: Ninja has N days of training with 3 activities each day. Can't do same 
activity on consecutive days. Find max merit points.

Time: O(n*3*3) = O(n), Space: O(1)
"""

def ninjaTraining(points):
    n = len(points)
    prev = points[0][:]
    
    for day in range(1, n):
        curr = [0, 0, 0]
        for activity in range(3):
            max_prev = 0
            for prev_activity in range(3):
                if prev_activity != activity:
                    max_prev = max(max_prev, prev[prev_activity])
            curr[activity] = points[day][activity] + max_prev
        prev = curr
    
    return max(prev)


def test_ninja_training():
    print("=" * 70)
    print("Problem 7: Ninja's Training (2D DP)")
    print("=" * 70)
    
    test_cases = [([[10, 40, 70], [20, 50, 80], [30, 60, 90]], 210)]
    for points, expected in test_cases:
        result = ninjaTraining(points)
        status = "✅" if result == expected else "❌"
        print(f"Points: {points}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 8: LeetCode 62 - Unique Paths
# ============================================================================

"""
Problem: Count paths from top-left to bottom-right (only right/down moves).
dp[i][j] = dp[i-1][j] + dp[i][j-1]

Time: O(m*n), Space: O(n)
"""

def uniquePaths(m, n):
    prev = [1] * n
    
    for i in range(1, m):
        curr = [1] * n
        for j in range(1, n):
            curr[j] = prev[j] + curr[j - 1]
        prev = curr
    
    return prev[n - 1]


def test_unique_paths():
    print("=" * 70)
    print("Problem 8: Unique Paths")
    print("=" * 70)
    
    test_cases = [(3, 7, 28), (3, 2, 3), (1, 1, 1)]
    for m, n, expected in test_cases:
        result = uniquePaths(m, n)
        status = "✅" if result == expected else "❌"
        print(f"m={m}, n={n}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 9: LeetCode 63 - Unique Paths 2 (With Obstacles)
# ============================================================================

"""
Problem: Same as Unique Paths but with obstacles (1 = blocked).
"""

def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0
    
    prev = [0] * n
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            break
        prev[j] = 1
    
    for i in range(1, m):
        curr = [0] * n
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                curr[j] = 0
            elif j == 0:
                curr[j] = prev[j]
            else:
                curr[j] = prev[j] + curr[j - 1]
        prev = curr
    
    return prev[n - 1]


def test_unique_paths_2():
    print("=" * 70)
    print("Problem 9: Unique Paths 2 (With Obstacles)")
    print("=" * 70)
    
    test_cases = [([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2), ([[0, 1], [0, 0]], 1)]
    for grid, expected in test_cases:
        result = uniquePathsWithObstacles(grid)
        status = "✅" if result == expected else "❌"
        print(f"Grid: {grid}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 10: LeetCode 64 - Minimum Path Sum
# ============================================================================

"""
Problem: Find path with minimum sum from top-left to bottom-right.
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

Time: O(m*n), Space: O(n)
"""

def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    
    prev = [0] * n
    prev[0] = grid[0][0]
    for j in range(1, n):
        prev[j] = prev[j - 1] + grid[0][j]
    
    for i in range(1, m):
        curr = [0] * n
        curr[0] = prev[0] + grid[i][0]
        for j in range(1, n):
            curr[j] = grid[i][j] + min(prev[j], curr[j - 1])
        prev = curr
    
    return prev[n - 1]


def test_min_path_sum():
    print("=" * 70)
    print("Problem 10: Minimum Path Sum")
    print("=" * 70)
    
    test_cases = [([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7), ([[1, 2, 3], [4, 5, 6]], 12)]
    for grid, expected in test_cases:
        result = minPathSum(grid)
        status = "✅" if result == expected else "❌"
        print(f"Grid: {grid}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 11: LeetCode 120 - Triangle
# ============================================================================

"""
Problem: Find minimum path sum from top to bottom of triangle.
Bottom-up approach: dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

Time: O(n^2), Space: O(n)
"""

def minimumTotal(triangle):
    n = len(triangle)
    prev = triangle[n - 1][:]
    
    for i in range(n - 2, -1, -1):
        curr = [0] * (i + 1)
        for j in range(i + 1):
            curr[j] = triangle[i][j] + min(prev[j], prev[j + 1])
        prev = curr
    
    return prev[0]


def test_triangle():
    print("=" * 70)
    print("Problem 11: Triangle")
    print("=" * 70)
    
    test_cases = [([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11), ([[-10]], -10)]
    for triangle, expected in test_cases:
        result = minimumTotal(triangle)
        status = "✅" if result == expected else "❌"
        print(f"Triangle: {triangle}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 12: LeetCode 931 - Minimum Falling Path Sum
# ============================================================================

"""
Problem: Min falling path sum - can move to (i+1,j-1), (i+1,j), or (i+1,j+1).
Can start from any cell in first row.

Time: O(n^2), Space: O(n)
"""

def minFallingPathSum(matrix):
    n = len(matrix)
    prev = matrix[0][:]
    
    for i in range(1, n):
        curr = [0] * n
        for j in range(n):
            up = prev[j]
            up_left = prev[j - 1] if j > 0 else float('inf')
            up_right = prev[j + 1] if j < n - 1 else float('inf')
            curr[j] = matrix[i][j] + min(up, up_left, up_right)
        prev = curr
    
    return min(prev)


def test_min_falling_path_sum():
    print("=" * 70)
    print("Problem 12: Minimum Falling Path Sum")
    print("=" * 70)
    
    test_cases = [([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13), ([[-19, 57], [-40, -5]], -59)]
    for matrix, expected in test_cases:
        result = minFallingPathSum(matrix)
        status = "✅" if result == expected else "❌"
        print(f"Matrix: {matrix}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 13: LeetCode 741 - Cherry Pickup (3D DP)
# ============================================================================

"""
Problem: Two people collect cherries going from (0,0) to (n-1,n-1) simultaneously.
If both at same cell, count cherry once. -1 = blocked.

Time: O(n^3), Space: O(n^3)
"""

def cherryPickup(grid):
    n = len(grid)
    dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
    
    def solve(r1, c1, r2):
        c2 = r1 + c1 - r2
        
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
            return float('-inf')
        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float('-inf')
        if r1 == n - 1 and c1 == n - 1:
            return grid[r1][c1]
        if dp[r1][c1][r2] != -1:
            return dp[r1][c1][r2]
        
        cherries = grid[r1][c1]
        if r1 != r2 or c1 != c2:
            cherries += grid[r2][c2]
        
        result = max(solve(r1+1, c1, r2+1), solve(r1+1, c1, r2),
                     solve(r1, c1+1, r2+1), solve(r1, c1+1, r2))
        
        dp[r1][c1][r2] = cherries + result
        return dp[r1][c1][r2]
    
    return max(0, solve(0, 0, 0))


def test_cherry_pickup():
    print("=" * 70)
    print("Problem 13: Cherry Pickup (3D DP)")
    print("=" * 70)
    
    test_cases = [([[0, 1, -1], [1, 0, -1], [1, 1, 1]], 5)]
    for grid, expected in test_cases:
        result = cherryPickup(grid)
        status = "✅" if result == expected else "❌"
        print(f"Grid: {grid}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 14: Subset Sum Equals Target
# ============================================================================

"""
Problem: Check if subset with given sum exists.
dp[j] = True if sum j is achievable

Time: O(n * target), Space: O(target)
"""

def subsetSumTarget(nums, target):
    n = len(nums)
    prev = [False] * (target + 1)
    prev[0] = True
    
    if nums[0] <= target:
        prev[nums[0]] = True
    
    for i in range(1, n):
        curr = [False] * (target + 1)
        curr[0] = True
        for j in range(1, target + 1):
            not_pick = prev[j]
            pick = prev[j - nums[i]] if j >= nums[i] else False
            curr[j] = pick or not_pick
        prev = curr
    
    return prev[target]


def test_subset_sum_target():
    print("=" * 70)
    print("Problem 14: Subset Sum Equals Target")
    print("=" * 70)
    
    test_cases = [([3, 34, 4, 12, 5, 2], 9, True), ([3, 34, 4, 12, 5, 2], 30, False)]
    for nums, target, expected in test_cases:
        result = subsetSumTarget(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"Nums: {nums}, Target: {target}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 15: LeetCode 416 - Partition Equal Subset Sum
# ============================================================================

"""
Problem: Can array be partitioned into two equal sum subsets?
Reduce to: Find subset with sum = total/2
"""

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    return subsetSumTarget(nums, total // 2)


def test_partition_equal_subset():
    print("=" * 70)
    print("Problem 15: Partition Equal Subset Sum")
    print("=" * 70)
    
    test_cases = [([1, 5, 11, 5], True), ([1, 2, 3, 5], False)]
    for nums, expected in test_cases:
        result = canPartition(nums)
        status = "✅" if result == expected else "❌"
        print(f"Nums: {nums}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 16: Partition with Minimum Absolute Difference
# ============================================================================

"""
Problem: Partition into two subsets with minimum |S1 - S2|.
Find all achievable sums, minimize |2*S1 - total|
"""

def minSubsetSumDifference(nums):
    total = sum(nums)
    n = len(nums)
    
    prev = [False] * (total + 1)
    prev[0] = True
    if nums[0] <= total:
        prev[nums[0]] = True
    
    for i in range(1, n):
        curr = [False] * (total + 1)
        for j in range(total + 1):
            curr[j] = prev[j] or (prev[j - nums[i]] if j >= nums[i] else False)
        prev = curr
    
    min_diff = float('inf')
    for s1 in range(total // 2 + 1):
        if prev[s1]:
            min_diff = min(min_diff, abs(total - 2 * s1))
    
    return min_diff


def test_min_subset_diff():
    print("=" * 70)
    print("Problem 16: Partition with Minimum Difference")
    print("=" * 70)
    
    test_cases = [([1, 6, 11, 5], 1), ([1, 2, 3, 4], 0)]
    for nums, expected in test_cases:
        result = minSubsetSumDifference(nums)
        status = "✅" if result == expected else "❌"
        print(f"Nums: {nums}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 17: Count Subsets with Sum K
# ============================================================================

"""
Problem: Count subsets with given sum.
dp[j] = number of ways to form sum j
"""

def countSubsetsWithSum(nums, target):
    n = len(nums)
    prev = [0] * (target + 1)
    prev[0] = 1
    
    if nums[0] <= target:
        prev[nums[0]] += 1
    
    for i in range(1, n):
        curr = [0] * (target + 1)
        for j in range(target + 1):
            not_pick = prev[j]
            pick = prev[j - nums[i]] if j >= nums[i] else 0
            curr[j] = pick + not_pick
        prev = curr
    
    return prev[target]


def test_count_subsets_sum():
    print("=" * 70)
    print("Problem 17: Count Subsets with Sum K")
    print("=" * 70)
    
    test_cases = [([1, 2, 2, 3], 3, 3), ([1, 1, 1, 1], 2, 6)]
    for nums, target, expected in test_cases:
        result = countSubsetsWithSum(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"Nums: {nums}, Target: {target}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 18: Count Partitions with Given Difference
# ============================================================================

"""
Problem: Count partitions where S1 - S2 = diff.
S1 = (total + diff) / 2, count subsets with sum S1
"""

def countPartitionsWithDiff(nums, diff):
    total = sum(nums)
    if (total + diff) % 2 != 0 or total + diff < 0:
        return 0
    return countSubsetsWithSum(nums, (total + diff) // 2)


def test_count_partitions_diff():
    print("=" * 70)
    print("Problem 18: Count Partitions with Given Difference")
    print("=" * 70)
    
    test_cases = [([1, 1, 2, 3], 1, 3)]
    for nums, diff, expected in test_cases:
        result = countPartitionsWithDiff(nums, diff)
        status = "✅" if result == expected else "❌"
        print(f"Nums: {nums}, Diff: {diff}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 19: 0/1 Knapsack
# ============================================================================

"""
Problem: Max value with weight capacity W. Each item used at most once.
dp[w] = max(dp[w], dp[w-wt[i]] + val[i])

Time: O(n*W), Space: O(W)
"""

def knapsack01(weights, values, W):
    n = len(weights)
    prev = [0] * (W + 1)
    
    for w in range(weights[0], W + 1):
        prev[w] = values[0]
    
    for i in range(1, n):
        curr = [0] * (W + 1)
        for w in range(W + 1):
            not_pick = prev[w]
            pick = prev[w - weights[i]] + values[i] if w >= weights[i] else 0
            curr[w] = max(pick, not_pick)
        prev = curr
    
    return prev[W]


def test_knapsack_01():
    print("=" * 70)
    print("Problem 19: 0/1 Knapsack")
    print("=" * 70)
    
    test_cases = [([1, 2, 3], [10, 15, 40], 6, 65), ([3, 4, 5], [30, 50, 60], 8, 90)]
    for weights, values, W, expected in test_cases:
        result = knapsack01(weights, values, W)
        status = "✅" if result == expected else "❌"
        print(f"W={W}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 20: LeetCode 322 - Coin Change (Minimum Coins)
# ============================================================================

"""
Problem: Minimum coins to make amount (unlimited coins).
dp[amt] = min(dp[amt], dp[amt-coin] + 1)

Time: O(n*amount), Space: O(amount)
"""

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for amt in range(coin, amount + 1):
            dp[amt] = min(dp[amt], dp[amt - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def test_coin_change():
    print("=" * 70)
    print("Problem 20: Coin Change (Minimum Coins)")
    print("=" * 70)
    
    test_cases = [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0)]
    for coins, amount, expected in test_cases:
        result = coinChange(coins, amount)
        status = "✅" if result == expected else "❌"
        print(f"Coins: {coins}, Amount: {amount}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 21: LeetCode 494 - Target Sum
# ============================================================================

"""
Problem: Assign + or - to each element to get target sum.
Reduce to: Count subsets with sum = (total + target) / 2
"""

def findTargetSumWays(nums, target):
    total = sum(nums)
    if abs(target) > total or (total + target) % 2 != 0:
        return 0
    
    s1 = (total + target) // 2
    n = len(nums)
    
    prev = [0] * (s1 + 1)
    prev[0] = 1 if nums[0] != 0 else 2
    if nums[0] != 0 and nums[0] <= s1:
        prev[nums[0]] = 1
    
    for i in range(1, n):
        curr = [0] * (s1 + 1)
        for j in range(s1 + 1):
            not_pick = prev[j]
            pick = prev[j - nums[i]] if j >= nums[i] else 0
            curr[j] = pick + not_pick
        prev = curr
    
    return prev[s1]


def test_target_sum():
    print("=" * 70)
    print("Problem 21: Target Sum")
    print("=" * 70)
    
    test_cases = [([1, 1, 1, 1, 1], 3, 5), ([1], 1, 1)]
    for nums, target, expected in test_cases:
        result = findTargetSumWays(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"Nums: {nums}, Target: {target}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 22: LeetCode 518 - Coin Change 2 (Count Ways)
# ============================================================================

"""
Problem: Count ways to make amount (unlimited coins).
dp[amt] += dp[amt - coin]

Time: O(n*amount), Space: O(amount)
"""

def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for amt in range(coin, amount + 1):
            dp[amt] += dp[amt - coin]
    
    return dp[amount]


def test_coin_change_2():
    print("=" * 70)
    print("Problem 22: Coin Change 2 (Count Ways)")
    print("=" * 70)
    
    test_cases = [(5, [1, 2, 5], 4), (3, [2], 0), (10, [10], 1)]
    for amount, coins, expected in test_cases:
        result = change(amount, coins)
        status = "✅" if result == expected else "❌"
        print(f"Amount: {amount}, Coins: {coins}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 23: Unbounded Knapsack
# ============================================================================

"""
Problem: Max value with capacity W. Each item can be used unlimited times.
dp[w] = max(dp[w], dp[w-wt[i]] + val[i]) - use current row for pick
"""

def unboundedKnapsack(weights, values, W):
    dp = [0] * (W + 1)
    
    for i in range(len(weights)):
        for w in range(weights[i], W + 1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[W]


def test_unbounded_knapsack():
    print("=" * 70)
    print("Problem 23: Unbounded Knapsack")
    print("=" * 70)
    
    test_cases = [([2, 4, 6], [5, 11, 13], 10, 27)]
    for weights, values, W, expected in test_cases:
        result = unboundedKnapsack(weights, values, W)
        status = "✅" if result == expected else "❌"
        print(f"W={W}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 24: Rod Cutting Problem
# ============================================================================

"""
Problem: Cut rod of length N to maximize profit. price[i] = price of rod of length i+1.
Same as unbounded knapsack with weights = [1,2,3,...,N]

Time: O(N^2), Space: O(N)
"""

def rodCutting(price, N):
    dp = [0] * (N + 1)
    
    for length in range(1, N + 1):
        for cut in range(1, length + 1):
            dp[length] = max(dp[length], price[cut - 1] + dp[length - cut])
    
    return dp[N]


def test_rod_cutting():
    print("=" * 70)
    print("Problem 24: Rod Cutting Problem")
    print("=" * 70)
    
    test_cases = [([1, 5, 8, 9, 10, 17, 17, 20], 8, 22), ([3, 5, 8, 9, 10, 17, 17, 20], 8, 24)]
    for price, N, expected in test_cases:
        result = rodCutting(price, N)
        status = "✅" if result == expected else "❌"
        print(f"N={N}, Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 25: LeetCode 1143 - Longest Common Subsequence
# ============================================================================

"""
Problem: Find length of LCS of two strings.
dp[i][j] = LCS of s1[0:i] and s2[0:j]
If match: dp[i][j] = 1 + dp[i-1][j-1]
Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

Time: O(m*n), Space: O(n)
"""

def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    
    return prev[n]


def test_lcs():
    print("=" * 70)
    print("Problem 25: Longest Common Subsequence")
    print("=" * 70)
    
    test_cases = [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0)]
    for text1, text2, expected in test_cases:
        result = longestCommonSubsequence(text1, text2)
        status = "✅" if result == expected else "❌"
        print(f"text1='{text1}', text2='{text2}', Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# PROBLEM 26: Print Longest Common Subsequence
# ============================================================================

"""
Problem: Print the actual LCS string.
Build dp table, then backtrack from dp[m][n] to construct the string.

Time: O(m*n), Space: O(m*n)
"""

def printLCS(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack to find the LCS string
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))


def test_print_lcs():
    print("=" * 70)
    print("Problem 26: Print Longest Common Subsequence")
    print("=" * 70)
    
    test_cases = [("abcde", "ace", "ace"), ("abc", "abc", "abc"), ("abcd", "aced", "acd")]
    for text1, text2, expected in test_cases:
        result = printLCS(text1, text2)
        status = "✅" if result == expected else "❌"
        print(f"text1='{text1}', text2='{text2}', Expected: '{expected}', Got: '{result}' {status}")
    print()


# ============================================================================
# MAIN TEST RUNNER
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("DYNAMIC PROGRAMMING - STRIVER'S DP SERIES")
    print("=" * 70 + "\n")
    
    # 1D DP Problems
    test_climbing_stairs()
    test_frog_jump()
    test_frog_jump_k()
    test_house_robber()
    test_house_robber_2()
    
    # 2D DP Problems
    test_ninja_training()
    test_unique_paths()
    test_unique_paths_2()
    test_min_path_sum()
    test_triangle()
    test_min_falling_path_sum()
    test_cherry_pickup()
    
    # DP on Subsequences
    test_subset_sum_target()
    test_partition_equal_subset()
    test_min_subset_diff()
    test_count_subsets_sum()
    test_count_partitions_diff()
    test_knapsack_01()
    test_coin_change()
    test_target_sum()
    test_coin_change_2()
    test_unbounded_knapsack()
    test_rod_cutting()
    
    # DP on Strings
    test_lcs()
    test_print_lcs()
    
    print("=" * 70)
    print("All DP tests completed!")
    print("=" * 70)
