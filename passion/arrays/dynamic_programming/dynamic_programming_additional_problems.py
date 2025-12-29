"""
Dynamic Programming Additional Problems
========================================
This file contains additional high-frequency dynamic programming problems
commonly asked in FAANG and top tech company interviews.

Each problem includes:
1. Problem statement and examples
2. Key insights for solving
3. Pattern template/approach
4. Solution with detailed explanations
5. Time and space complexity
6. Test cases with expected outputs

These problems complement the ones in dynamic_programming_solutions.py and
dynamic_programming_medium_hard_solutions.py.
"""

# ============================================================================
# MEDIUM PROBLEMS
# ============================================================================


# ============================================================================
# PROBLEM 1: LeetCode 91 - Decode Ways (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into 
letters using the reverse of the mapping above (there may be multiple ways).
For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' 
since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero.

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zeros.
"""

def numDecodings(s):
    """
    Approach: Dynamic Programming
    
    Key Insight:
    - At each position, we need to decide if we decode the current digit alone
      or combine it with the previous digit
    - For each position i, we can decode in two ways:
      1. Use the current digit alone (if it's not '0')
      2. Use the current digit with the previous digit (if the resulting number is between 10 and 26)
    - We can sum up these ways to get the total number of ways to decode
    - Base case: for empty string, there's 1 way to decode (do nothing)
    
    DP State:
    - dp[i] = number of ways to decode substring s[0...i-1]
    
    DP Recurrence:
    - dp[i] = dp[i-1] if s[i-1] != '0' else 0  # decode current digit alone
    - dp[i] += dp[i-2] if '10' <= s[i-2:i] <= '26' else 0  # decode current + previous digit
    
    Pattern Recognition:
    - Decision-making at each position
    - Handling edge cases (zeros, invalid combinations)
    - Building up solution from smaller subproblems
    
    Time: O(n) where n is the length of s
    Space: O(n) for the DP array (can be optimized to O(1))
    """
    if not s or s[0] == '0':  # Handle edge cases
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string has 1 way to decode
    dp[1] = 1  # First digit can only be decoded in 1 way, unless it's '0'
    
    for i in range(2, n + 1):
        # Check if current digit can be decoded independently
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        
        # Check if current digit can be decoded with previous digit
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]


# Optimized solution with constant space
def numDecodings_optimized(s):
    """
    Space-optimized solution using only two variables.
    
    Time: O(n)
    Space: O(1)
    """
    if not s or s[0] == '0':
        return 0
    
    # Initialize with values for empty string and first character
    prev2 = 1  # dp[i-2]
    prev1 = 1  # dp[i-1]
    
    for i in range(1, len(s)):
        current = 0
        
        # Single digit decode
        if s[i] != '0':
            current += prev1
        
        # Two digit decode
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            current += prev2
        
        # Update for next iteration
        prev2, prev1 = prev1, current
    
    return prev1


# Test cases
print("\n" + "=" * 70)
print("Problem 1: LeetCode 91 - Decode Ways")
print("=" * 70)

test_cases_91 = [
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("10", 1),
    ("2101", 1),
    ("111111", 13)
]

for s, expected in test_cases_91:
    result = numDecodings(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 2: LeetCode 416 - Partition Equal Subset Sum (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given a non-empty array nums containing only positive integers, find if the array 
can be partitioned into two subsets such that the sum of elements in both subsets 
is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100
"""

def canPartition(nums):
    """
    Approach: Dynamic Programming (0/1 Knapsack Variation)
    
    Key Insight:
    - If the array can be divided into two equal sum subsets, then each subset sum is total_sum/2
    - This is equivalent to finding a subset of the array that sums exactly to total_sum/2
    - This is a variation of the 0/1 Knapsack problem where we decide whether to include each number
    - We can use DP to build up possible sum values from smaller subproblems
    - If the total sum is odd, it's impossible to have two equal subsets
    
    DP State:
    - dp[i][j] = whether it's possible to form sum j using elements from nums[0...i-1]
    - Optimized to 1D: dp[j] = whether it's possible to form sum j using any elements processed so far
    
    DP Recurrence:
    - dp[i][j] = dp[i-1][j] (don't take ith element) OR dp[i-1][j-nums[i-1]] (take ith element)
    - 1D optimized: dp[j] = dp[j] OR dp[j-nums[i]] for j from target to nums[i]
    
    Pattern Recognition:
    - Subset sum problem (0/1 Knapsack variation)
    - Binary decision for each element: include or exclude
    - Bottom-up DP with space optimization
    
    Time: O(n * target) where n is array length and target is sum/2
    Space: O(target) for optimized solution
    """
    total_sum = sum(nums)
    
    # Handle edge cases
    if total_sum % 2 != 0:  # If sum is odd, can't partition equally
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # Optimized 1D DP array
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: always possible to make sum 0 by taking no elements
    
    for num in nums:
        # Have to iterate backward to avoid using the same element multiple times
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]


# Test cases
print("\n" + "=" * 70)
print("Problem 2: LeetCode 416 - Partition Equal Subset Sum")
print("=" * 70)

test_cases_416 = [
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
    ([1, 1, 2, 2], True),
    ([1, 2, 5], False)
]

for nums, expected in test_cases_416:
    result = canPartition(nums)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 3: LeetCode 1143 - Longest Common Subsequence (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some 
characters (can be none) deleted without changing the relative order of the remaining 
characters. (e.g., "ace" is a subsequence of "abcde" while "aec" is not).

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
"""

def longestCommonSubsequence(text1, text2):
    """
    Approach: Dynamic Programming (2D Table)
    
    Key Insight:
    - At each pair of characters, we have two choices:
      1. If characters match, extend the LCS from the previous characters
      2. If they don't match, take the maximum LCS from either skipping a character from text1 or text2
    - This builds up the longest subsequence incrementally
    
    DP State:
    - dp[i][j] = length of LCS between text1[0...i-1] and text2[0...j-1]
    
    DP Recurrence:
    - If text1[i-1] == text2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
    - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    Pattern Recognition:
    - Classic string comparison problem
    - Character-by-character matching
    - Table filling from smaller to larger subproblems
    - Maximum length tracking
    
    Time: O(m * n) where m, n are lengths of the strings
    Space: O(m * n) for the DP table (can be optimized to O(min(m, n)))
    """
    m, n = len(text1), len(text2)
    
    # Initialize DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                # If current characters match, extend the LCS
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                # Otherwise, take the maximum from skipping a character in either string
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 3: LeetCode 1143 - Longest Common Subsequence")
print("=" * 70)

test_cases_1143 = [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
    ("bsbininm", "jmjkbkjkv", 1),
    ("oxcpqrsvwf", "shmtulqrypy", 2)
]

for text1, text2, expected in test_cases_1143:
    result = longestCommonSubsequence(text1, text2)
    status = "✅" if result == expected else "❌"
    print(f"text1='{text1}', text2='{text2}' → {result} (expected: {expected}) {status}")


# ============================================================================
# HARD PROBLEMS
# ============================================================================


# ============================================================================
# PROBLEM 4: LeetCode 32 - Longest Valid Parentheses (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given a string containing just the characters '(' and ')', find the length of the 
longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
- 0 <= s.length <= 3 * 10^4
- s[i] is '(', or ')'.
"""

def longestValidParentheses(s):
    """
    Approach: Dynamic Programming
    
    Key Insight:
    - A valid parentheses string must start with '(' and end with ')'
    - Define dp[i] as length of longest valid parentheses ending at position i
    - Two cases to extend valid parentheses:
      1. Current ')' matches with a previous '(' directly: s[i-1] == '('
      2. Current ')' closes a larger valid sequence: s[i-1] == ')' and there's a matching '(' before
    
    DP State:
    - dp[i] = length of longest valid parentheses substring ending at position i
    
    DP Recurrence:
    - If s[i] == ')' and s[i-1] == '(': dp[i] = dp[i-2] + 2
    - If s[i] == ')' and s[i-1] == ')' and s[i-dp[i-1]-1] == '': 
        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
    
    Pattern Recognition:
    - Parentheses matching
    - Looking back at previous valid sequences
    - Building on top of previous results
    
    Time: O(n) where n is the length of s
    Space: O(n) for the DP array
    """
    n = len(s)
    if n == 0:
        return 0
    
    dp = [0] * n
    max_length = 0
    
    for i in range(1, n):
        if s[i] == ')':
            # Case 1: Current ')' matches with the previous '('
            if s[i-1] == '(':
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            
            # Case 2: Current ')' matches with a '(' before the last valid substring
            elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                dp[i] = dp[i-1] + (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0) + 2
            
            max_length = max(max_length, dp[i])
    
    return max_length


# Alternative solution using stack
def longestValidParentheses_stack(s):
    """
    Alternative approach using stack
    
    Time: O(n)
    Space: O(n) for the stack
    """
    n = len(s)
    stack = [-1]  # Initialize with -1 as base
    max_length = 0
    
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:  # s[i] == ')'
            stack.pop()  # Pop the matching '(' or the base
            
            if not stack:
                # No matching '(', push current as new base
                stack.append(i)
            else:
                # Calculate length of valid substring
                max_length = max(max_length, i - stack[-1])
    
    return max_length


# Test cases
print("\n" + "=" * 70)
print("Problem 4: LeetCode 32 - Longest Valid Parentheses")
print("=" * 70)

test_cases_32 = [
    ("(()", 2),
    (")()())", 4),
    ("", 0),
    ("()(()", 2),
    ("(()())", 6),
    (")(((((()())()()))()(()))(", 22)
]

for s, expected in test_cases_32:
    result = longestValidParentheses(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 5: LeetCode 329 - Longest Increasing Path in a Matrix (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 2^31 - 1
"""

def longestIncreasingPath(matrix):
    """
    Approach: DP with Memoization (Top-Down DFS)
    
    Key Insight:
    - This is a path-finding problem where we want the longest path
    - For each cell, we can move in 4 directions if the next cell has a larger value
    - Use memoization to avoid redundant calculations
    - The answer is the maximum path length starting from any cell
    
    DP State:
    - memo[i][j] = length of longest increasing path starting from cell (i,j)
    
    DP Recurrence:
    - memo[i][j] = 1 + max(memo[i+di][j+dj]) for all valid neighbors with larger values
    
    Pattern Recognition:
    - Matrix traversal with DFS
    - Memoization to avoid recalculating paths
    - Finding optimal path lengths
    
    Time: O(m * n) where m, n are dimensions of the matrix
    Space: O(m * n) for the memoization array
    """
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]  # Memoization array
    
    def dfs(i, j):
        # If value is memoized, return it
        if memo[i][j] > 0:
            return memo[i][j]
        
        # Initialize path length as 1 (the cell itself)
        max_path = 1
        
        # Try all four directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            # Check if neighbor is valid and has larger value
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                # Update max path length
                max_path = max(max_path, 1 + dfs(ni, nj))
        
        # Memoize result
        memo[i][j] = max_path
        return max_path
    
    # Try starting from each cell and find the maximum path length
    max_length = 0
    for i in range(m):
        for j in range(n):
            max_length = max(max_length, dfs(i, j))
    
    return max_length


# Test cases
print("\n" + "=" * 70)
print("Problem 5: LeetCode 329 - Longest Increasing Path in a Matrix")
print("=" * 70)

test_cases_329 = [
    ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
    ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
    ([[1]], 1),
    ([[7, 8, 9], [9, 7, 6], [7, 2, 3]], 4)
]

for matrix, expected in test_cases_329:
    result = longestIncreasingPath(matrix)
    status = "✅" if result == expected else "❌"
    print(f"matrix={matrix} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 6: LeetCode 221 - Maximal Square (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an m x n binary matrix filled with 0's and 1's, find the largest square 
containing only 1's and return its area.

Example 1:
Input: matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 4
Explanation: The maximal square has area = 4.

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] is '0' or '1'
"""

def maximalSquare(matrix):
    """
    Approach: Dynamic Programming (2D Table)
    
    Key Insight:
    - Define dp[i][j] = side length of largest square with bottom-right corner at (i,j)
    - If current cell is '1', we can extend the square if the three neighboring cells 
      (up, left, and diagonal up-left) also form squares
    - The extension is limited by the minimum of these three neighbors
    - Keep track of the maximum side length found
    
    DP State:
    - dp[i][j] = side length of largest square with bottom-right corner at position (i,j)
    
    DP Recurrence:
    - If matrix[i][j] == '1': dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    - Else: dp[i][j] = 0
    
    Pattern Recognition:
    - 2D matrix traversal with local property extension
    - Taking minimum of surrounding cells
    - Bottom-up DP building larger structures from smaller ones
    
    Time: O(m * n) where m, n are dimensions of the matrix
    Space: O(m * n) for the DP table (can be optimized to O(min(m, n)))
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i-1][j-1] == '1':
                # If current cell is 1, extend from surrounding squares
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    # Return area of the square (side^2)
    return max_side * max_side


# Test cases
print("\n" + "=" * 70)
print("Problem 6: LeetCode 221 - Maximal Square")
print("=" * 70)

test_cases_221 = [
    ([
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ], 4),
    ([["0","1"],["1","0"]], 1),
    ([["0"]], 0),
    ([
        ["1","1","1","1"],
        ["1","1","1","1"],
        ["1","1","1","1"]
    ], 9)
]

for matrix, expected in test_cases_221:
    result = maximalSquare(matrix)
    status = "✅" if result == expected else "❌"
    print(f"matrix=[...] → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 7: LeetCode 309 - Best Time to Buy and Sell Stock with Cooldown (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
- 1 <= prices.length <= 5000
- 0 <= prices[i] <= 1000
"""

def maxProfit(prices):
    """
    Approach: State Machine DP
    
    Key Insight:
    - We can be in one of three states on any given day:
      1. Holding a stock (bought previously)
      2. Not holding a stock and can buy (not in cooldown)
      3. Not holding a stock and cannot buy (in cooldown)
    - We need to track the maximum profit in each state and determine transitions
    
    DP States:
    - hold[i] = max profit on day i if holding stock
    - not_hold_ready[i] = max profit on day i if not holding stock and ready to buy
    - not_hold_cooldown[i] = max profit on day i if not holding stock and in cooldown
    
    DP Recurrence:
    - hold[i] = max(hold[i-1], not_hold_ready[i-1] - prices[i])
    - not_hold_cooldown[i] = hold[i-1] + prices[i]
    - not_hold_ready[i] = max(not_hold_ready[i-1], not_hold_cooldown[i-1])
    
    Pattern Recognition:
    - State machine DP with transitions
    - Multiple decision points (buy/sell/wait)
    - Tracking different states through the sequence
    
    Time: O(n) where n is the length of prices array
    Space: O(n) for the DP arrays (can be optimized to O(1))
    """
    if not prices or len(prices) <= 1:
        return 0
    
    n = len(prices)
    
    # Initialize DP arrays for each state
    hold = [0] * n  # Maximum profit if holding stock
    not_hold_ready = [0] * n  # Maximum profit if not holding stock and ready to buy
    not_hold_cooldown = [0] * n  # Maximum profit if not holding stock and in cooldown
    
    # Base cases
    hold[0] = -prices[0]  # Buy the stock on day 0
    not_hold_ready[0] = 0  # Start with 0 profit
    not_hold_cooldown[0] = float('-inf')  # Cannot be in cooldown on day 0
    
    for i in range(1, n):
        # If holding stock, either continue holding or buy new stock
        hold[i] = max(hold[i-1], not_hold_ready[i-1] - prices[i])
        
        # If in cooldown (just sold), transition to ready to buy
        not_hold_cooldown[i] = hold[i-1] + prices[i]
        
        # If ready to buy, either continue waiting or come from cooldown
        not_hold_ready[i] = max(not_hold_ready[i-1], not_hold_cooldown[i-1])
    
    # The final answer is the maximum of not holding stock states
    return max(not_hold_ready[n-1], not_hold_cooldown[n-1])


# Space-optimized solution
def maxProfit_optimized(prices):
    """
    Space-optimized solution using only variables
    
    Time: O(n)
    Space: O(1)
    """
    if not prices or len(prices) <= 1:
        return 0
    
    # Initialize state variables
    hold = -prices[0]
    not_hold_ready = 0
    not_hold_cooldown = float('-inf')
    
    for i in range(1, len(prices)):
        prev_hold = hold
        prev_ready = not_hold_ready
        prev_cooldown = not_hold_cooldown
        
        # Update states
        hold = max(prev_hold, prev_ready - prices[i])
        not_hold_cooldown = prev_hold + prices[i]
        not_hold_ready = max(prev_ready, prev_cooldown)
    
    return max(not_hold_ready, not_hold_cooldown)


# Test cases
print("\n" + "=" * 70)
print("Problem 7: LeetCode 309 - Best Time to Buy and Sell Stock with Cooldown")
print("=" * 70)

test_cases_309 = [
    ([1, 2, 3, 0, 2], 3),
    ([1], 0),
    ([1, 2], 1),
    ([2, 1, 4], 3),
    ([3, 3, 5, 0, 0, 3, 1, 4], 8)
]

for prices, expected in test_cases_309:
    result = maxProfit(prices)
    status = "✅" if result == expected else "❌"
    print(f"prices={prices} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 8: LeetCode 516 - Longest Palindromic Subsequence (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some 
or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.
"""

def longestPalindromeSubseq(s):
    """
    Approach: Dynamic Programming (2D Table)
    
    Key Insight:
    - Define dp[i][j] = length of longest palindromic subsequence in s[i...j]
    - For each substring s[i...j]:
      1. If s[i] == s[j], we can extend the palindrome from both ends: 2 + dp[i+1][j-1]
      2. If they don't match, we take the best of excluding either character: max(dp[i+1][j], dp[i][j-1])
    - Fill the table diagonally from smaller subproblems to larger ones
    
    DP State:
    - dp[i][j] = length of longest palindromic subsequence in substring s[i...j]
    
    DP Recurrence:
    - If s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
    - Else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    Pattern Recognition:
    - Substring/subsequence problems with palindrome property
    - Compare characters at both ends
    - Bottom-up DP building from smaller to larger substrings
    - Similar to LCS but with the same string in reverse
    
    Time: O(n²) where n is the length of string s
    Space: O(n²) for the DP table
    """
    n = len(s)
    # Initialize DP table
    dp = [[0] * n for _ in range(n)]
    
    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill table diagonally (bottom-up)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If first and last characters match
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                # Otherwise, take maximum of excluding either character
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]  # Entire string


# Alternative solution using LCS
def longestPalindromeSubseq_lcs(s):
    """
    Alternative approach: Find LCS of s and its reverse
    
    Time: O(n²)
    Space: O(n²)
    """
    # The longest palindromic subsequence is the LCS of s and its reverse
    s_rev = s[::-1]
    return longestCommonSubsequence(s, s_rev)


# Test cases
print("\n" + "=" * 70)
print("Problem 8: LeetCode 516 - Longest Palindromic Subsequence")
print("=" * 70)

test_cases_516 = [
    ("bbbab", 4),
    ("cbbd", 2),
    ("racecar", 7),
    ("abcdef", 1),
    ("aabcdebaz", 5)
]

for s, expected in test_cases_516:
    result = longestPalindromeSubseq(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 9: LeetCode 97 - Interleaving String (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided 
into n and m substrings respectively, such that:
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...

Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters.
"""

def isInterleave(s1, s2, s3):
    """
    Approach: Dynamic Programming (2D Table)
    
    Key Insight:
    - Define dp[i][j] = whether s3[0...i+j-1] is an interleaving of s1[0...i-1] and s2[0...j-1]
    - For each position, we can either:
      1. Take the next character from s1 if it matches
      2. Take the next character from s2 if it matches
    - We need both lengths to match s3's length for a valid interleaving
    
    DP State:
    - dp[i][j] = whether s3[0...i+j-1] is an interleaving of s1[0...i-1] and s2[0...j-1]
    
    DP Recurrence:
    - dp[i][j] = (dp[i-1][j] AND s1[i-1] == s3[i+j-1]) OR (dp[i][j-1] AND s2[j-1] == s3[i+j-1])
    
    Pattern Recognition:
    - String matching with multiple sources
    - Decision tree at each position (take from s1 or s2)
    - 2D DP with boolean values
    
    Time: O(m * n) where m, n are the lengths of s1 and s2
    Space: O(m * n) for the DP table (can be optimized to O(min(m, n)))
    """
    m, n = len(s1), len(s2)
    
    # Quick check for lengths
    if len(s3) != m + n:
        return False
    
    # Initialize DP table with False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty strings
    dp[0][0] = True
    
    # Fill first row: s1 is empty, only use s2
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    
    # Fill first column: s2 is empty, only use s1
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    
    # Fill the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Current position in s3
            k = i + j - 1
            
            # Either take from s1 or s2
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[k]) or \
                        (dp[i][j-1] and s2[j-1] == s3[k])
    
    return dp[m][n]


# Space-optimized solution
def isInterleave_optimized(s1, s2, s3):
    """
    Space-optimized solution using 1D array
    
    Time: O(m * n)
    Space: O(n)
    """
    m, n = len(s1), len(s2)
    
    if len(s3) != m + n:
        return False
    
    # Use only one row of DP table
    dp = [False] * (n + 1)
    dp[0] = True
    
    # Fill first row (s1 is empty)
    for j in range(1, n + 1):
        dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
    
    # Fill rest of the rows
    for i in range(1, m + 1):
        dp[0] = dp[0] and s1[i-1] == s3[i-1]  # Update first column
        
        for j in range(1, n + 1):
            k = i + j - 1
            dp[j] = (dp[j] and s1[i-1] == s3[k]) or \
                    (dp[j-1] and s2[j-1] == s3[k])
    
    return dp[n]


# Test cases
print("\n" + "=" * 70)
print("Problem 9: LeetCode 97 - Interleaving String")
print("=" * 70)

test_cases_97 = [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True),
    ("a", "", "a", True),
    ("aa", "ab", "abaa", True)
]

for s1, s2, s3, expected in test_cases_97:
    result = isInterleave(s1, s2, s3)
    status = "✅" if result == expected else "❌"
    print(f"s1='{s1}', s2='{s2}', s3='{s3}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 10: LeetCode 647 - Palindromic Substrings (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c"

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""

def countSubstrings(s):
    """
    Approach: Dynamic Programming + Expand Around Center
    
    Key Insight:
    - Every single character is a palindrome
    - For longer palindromes, we can expand around each center:
      1. Single character centers (for odd-length palindromes)
      2. Between-character centers (for even-length palindromes)
    - Count each valid palindrome
    
    DP State:
    - dp[i][j] = whether substring s[i...j] is a palindrome
    
    DP Recurrence:
    - dp[i][j] = (s[i] == s[j]) AND (j-i <= 2 OR dp[i+1][j-1])
    
    Pattern Recognition:
    - Palindrome checking
    - Counting vs. finding longest
    - Expanding around centers optimization
    
    Time: O(n²) where n is the length of s
    Space: O(1) for the optimized expand-around-center approach
    """
    if not s:
        return 0
    
    count = 0
    n = len(s)
    
    def expand_around_center(left, right):
        """Helper function to expand around a center and count palindromes"""
        count = 0
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    # Count all palindromes by expanding around each center
    for i in range(n):
        # Odd length palindromes (single character center)
        count += expand_around_center(i, i)
        
        # Even length palindromes (between character center)
        count += expand_around_center(i, i + 1)
    
    return count


# DP solution
def countSubstrings_dp(s):
    """
    Dynamic Programming solution
    
    Time: O(n²)
    Space: O(n²)
    """
    n = len(s)
    count = 0
    
    # Initialize DP table
    dp = [[False] * n for _ in range(n)]
    
    # Fill table diagonally
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if substring s[i...j] is a palindrome
            if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                dp[i][j] = True
                count += 1
    
    return count


# Test cases
print("\n" + "=" * 70)
print("Problem 10: LeetCode 647 - Palindromic Substrings")
print("=" * 70)

test_cases_647 = [
    ("abc", 3),
    ("aaa", 6),
    ("racecar", 10),
    ("", 0),
    ("abccba", 9)
]

for s, expected in test_cases_647:
    result = countSubstrings(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 11: LeetCode 123/188 - Best Time to Buy and Sell Stock III/IV (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation:
Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
- 0 <= k <= 100
- 0 <= prices.length <= 1000
- 0 <= prices[i] <= 1000

Note: LC 123 is the specific case where k = 2
"""

def maxProfitWithKTransactions(k, prices):
    """
    Approach: Dynamic Programming with State Machine
    
    Key Insight:
    - Define dp[i][j][0/1] as the maximum profit on day i with at most j transactions,
      where 0 means not holding stock and 1 means holding stock
    - For each day and transaction count, we have two choices:
      1. If not holding stock: either stay that way, or sell stock
      2. If holding stock: either continue holding, or buy new stock
    - The transitions model buying and selling decisions
    
    DP State:
    - dp[i][j][0] = max profit on day i with at most j transactions, not holding stock
    - dp[i][j][1] = max profit on day i with at most j transactions, holding stock
    
    DP Recurrence:
    - dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
    - dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
    
    Pattern Recognition:
    - Multi-state DP with transaction count constraint
    - Buying/selling decisions at each step
    - State machine transitions
    - Special handling for transaction limits
    
    Time: O(n * k) where n is the length of prices and k is the transaction limit
    Space: O(n * k) for the DP array
    """
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    
    # Optimization: if k is large enough, it's equivalent to unlimited transactions
    if k >= n // 2:
        return maxProfitUnlimited(prices)
    
    # Initialize DP array
    # dp[i][j][0] = max profit on day i with at most j transactions, not holding stock
    # dp[i][j][1] = max profit on day i with at most j transactions, holding stock
    dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
    
    # Base cases
    for j in range(k + 1):
        dp[0][j][0] = 0  # No profit if not holding stock initially
        dp[0][j][1] = -prices[0]  # Buy stock on day 0 if holding
    
    # Special case for transaction 0
    for i in range(1, n):
        dp[i][0][0] = 0  # Can't make profit with 0 transactions
        dp[i][0][1] = max(dp[i-1][0][1], -prices[i])  # Can only buy, not sell
    
    # Fill DP array
    for i in range(1, n):
        for j in range(1, k + 1):
            # If not holding stock: either stay that way, or sell
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
            
            # If holding stock: either continue holding, or buy new stock
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
    
    return dp[n-1][k][0]  # Maximum profit on last day with k transactions, not holding stock


def maxProfitUnlimited(prices):
    """
    Helper function for unlimited transactions (greedy approach)
    
    Time: O(n)
    Space: O(1)
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit


# Space-optimized solution
def maxProfitWithKTransactions_optimized(k, prices):
    """
    Space-optimized solution
    
    Time: O(n * k)
    Space: O(k)
    """
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    if k >= n // 2:
        return maxProfitUnlimited(prices)
    
    # Use 1D arrays instead of 3D
    buy = [-float('inf')] * (k + 1)
    sell = [0] * (k + 1)
    
    for price in prices:
        for j in range(1, k + 1):
            # Update buy and sell arrays
            buy[j] = max(buy[j], sell[j-1] - price)  # Buy: use profit from previous transaction
            sell[j] = max(sell[j], buy[j] + price)   # Sell: use current buy state
    
    return sell[k]  # Maximum profit with k transactions


# Test cases for k=2 (LC 123)
print("\n" + "=" * 70)
print("Problem 11: LeetCode 123/188 - Best Time to Buy and Sell Stock III/IV")
print("=" * 70)

test_cases_188 = [
    (2, [2, 4, 1], 2),
    (2, [3, 2, 6, 5, 0, 3], 7),
    (2, [1, 2, 3, 4, 5], 4),
    (3, [3, 3, 5, 0, 0, 3, 1, 4], 8),
    (1, [7, 1, 5, 3, 6, 4], 5)
]

for k, prices, expected in test_cases_188:
    result = maxProfitWithKTransactions(k, prices)
    status = "✅" if result == expected else "❌"
    print(f"k={k}, prices={prices} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 12: LeetCode 1235 - Maximum Profit in Job Scheduling (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], 
obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take 
such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6], we get profit of 50 + 70 = 120.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 20 + 70 + 60 = 150.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
Explanation: The subset chosen is the second job. Profit obtained 6.

Constraints:
- 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
- 1 <= startTime[i] < endTime[i] <= 10^9
- 1 <= profit[i] <= 10^4
"""

def jobScheduling(startTime, endTime, profit):
    """
    Approach: Dynamic Programming with Binary Search
    
    Key Insight:
    - Sort jobs by end time to process them in chronological order
    - For each job, we have two choices:
      1. Include the job and find the next non-overlapping job
      2. Skip the job
    - Use binary search to efficiently find the next non-overlapping job
    - Build up the solution incrementally
    
    DP State:
    - dp[i] = maximum profit considering jobs from 0 to i
    
    DP Recurrence:
    - dp[i] = max(dp[i-1], profit[i] + dp[j]) where j is the latest non-conflicting job
    
    Pattern Recognition:
    - Interval scheduling problem
    - Job selection with constraints
    - Binary search optimization for finding compatible jobs
    - Sorting by end time for efficient processing
    
    Time: O(n log n) where n is the number of jobs
    Space: O(n) for the DP array and the sorted jobs
    """
    import bisect
    
    n = len(startTime)
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    
    # Extract sorted arrays
    start_times = [job[0] for job in jobs]
    end_times = [job[1] for job in jobs]
    profits = [job[2] for job in jobs]
    
    # Initialize DP array
    dp = [0] * n
    dp[0] = profits[0]  # First job's profit
    
    for i in range(1, n):
        # Find latest job that doesn't conflict with current job
        # Binary search for the largest index j such that end_times[j] <= start_times[i]
        j = bisect.bisect_right(end_times, start_times[i]) - 1
        
        # Include current job: its profit + profit from non-conflicting jobs
        include_profit = profits[i] + (dp[j] if j >= 0 else 0)
        
        # Maximum profit: either include current job or skip it
        dp[i] = max(include_profit, dp[i-1])
    
    return dp[n-1]


# Alternative solution with sorting by start time
def jobScheduling_alternative(startTime, endTime, profit):
    """
    Alternative approach sorting by start time
    
    Time: O(n log n)
    Space: O(n)
    """
    import bisect
    
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
    n = len(jobs)
    
    # Extract sorted arrays
    start_times = [job[0] for job in jobs]
    
    # Initialize memo for DP
    memo = {}
    
    def dp(i):
        """Recursive DP function with memoization"""
        if i == n:
            return 0
        if i in memo:
            return memo[i]
        
        # Skip current job
        skip = dp(i + 1)
        
        # Take current job and find next available job
        start, end, prof = jobs[i]
        next_job = bisect.bisect_left(start_times, end)
        take = prof + dp(next_job)
        
        # Maximum profit is max of taking or skipping
        memo[i] = max(skip, take)
        return memo[i]
    
    return dp(0)


# Test cases
print("\n" + "=" * 70)
print("Problem 12: LeetCode 1235 - Maximum Profit in Job Scheduling")
print("=" * 70)

test_cases_1235 = [
    ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),
    ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
    ([1, 1, 1], [2, 3, 4], [5, 6, 4], 6)
]

for start, end, profit, expected in test_cases_1235:
    result = jobScheduling(start, end, profit)
    status = "✅" if result == expected else "❌"
    print(f"jobs → {result} (expected: {expected}) {status}")


# ============================================================================
# CONCLUSION AND UPDATED SUMMARY
# ============================================================================

"""
Comprehensive Dynamic Programming Pattern Summary:

1. Basic DP Patterns:
   - 1D Array Progression: Decode Ways, Climbing Stairs
   - 2D Table Construction: Longest Common Subsequence, Interleaving String

2. Substring/Subsequence Problems:
   - Palindrome Problems: Longest Palindromic Subsequence, Palindromic Substrings
   - String Matching: Interleaving String, Longest Common Subsequence

3. Matrix Problems:
   - Square/Rectangle Finding: Maximal Square, Maximal Rectangle
   - Path Problems: Longest Increasing Path in Matrix, Unique Paths

4. Optimization Problems:
   - Knapsack Variations: Partition Equal Subset Sum
   - Interval Scheduling: Maximum Profit in Job Scheduling
   - Stock Trading: Buy/Sell Stock with various constraints

5. State Machine DP:
   - Multiple States Tracking: Best Time to Buy and Sell Stock with Cooldown
   - Transaction-Limited Problems: Best Time to Buy and Sell Stock III/IV

6. Special Techniques:
   - DP with Binary Search: LIS, Job Scheduling
   - Space Optimization: Reducing 2D to 1D arrays
   - Memoization vs. Tabulation: When to use each approach

7. Pattern Recognition Tips:
   - Identify subproblems and optimal substructure
   - Define clear state transitions and recurrence relations
   - Handle base cases properly
   - Optimize for space when possible
   - Consider alternative approaches (e.g., greedy, binary search)

This collection covers a wide range of DP patterns frequently appearing in 
technical interviews at top tech companies and FAANG/MANGA interviews.
"""
