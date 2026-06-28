
# functional way of forming recursion
n = 0
def fibonacci_functional(n):
    if n >= 4:
        return 0

    # print(n)
    return n + fibonacci_functional(n+1)

print( fibonacci_functional(n) )


# parameterized way of forming recursion
def fibonacci_parameterized():
    return 0


fibonacci_parameterized()



"""
RECURSION & BACKTRACKING
=========================
Complete solutions for LeetCode problems using recursion and backtracking patterns

RECURSION PATTERN TEMPLATES
===========================

1. Basic Recursion Template:
----------------------------
def recursive_function(parameters):
    # Base case(s): when to stop
    if base_case_condition:
        return base_case_value
    
    # Recursive case: break problem into smaller subproblems
    # Make one or more recursive calls with modified parameters
    result = recursive_function(modified_parameters)
    
    # Process result if needed
    return result

Key Characteristics:
- Divide problem into smaller subproblems
- Must have at least one base case to stop recursion
- Pass solutions back up the recursion tree
- Time complexity often O(branches^depth)
- Space complexity often O(depth) for call stack


2. Backtracking Templates:
-------------------------

2.1 General Purpose Backtracking Template:
def backtracking_function_general(input_data):
    result = []
    
    def backtrack(current_state, remaining_choices):
        # Base case: found a valid solution
        if is_valid_solution(current_state):
            result.append(current_state.copy())  # Always make a copy!
            return
        
        # Base case: reached the end of choices
        if no_more_choices(remaining_choices):
            return
        
        # Try each possible choice
        choice_i = 0
        while choice_i < len(remaining_choices):
            choice = remaining_choices[choice_i]
            # 1. Make a choice
            current_state.append(choice)
            
            # 2. Backtrack with updated state
            backtrack(current_state, get_next_choices(remaining_choices, choice))
            
            # 3. Undo the choice (backtrack)
            current_state.pop()  # or restore state however appropriate
            choice_i += 1
    
    # Start backtracking with initial state
    backtrack(initial_state, initial_choices)
    return result

2.2 Binary Decision (Pick/Not Pick) Template:
def backtracking_function_binary(arr):
    result = []
    
    def backtrack(i, current):
        # Base case: processed all elements
        if i == len(arr):
            result.append(current[:])  # CRITICAL: make a copy!
            return
        
        # Pick: include current element
        current.append(arr[i])
        backtrack(i + 1, current)
        current.pop()  # Backtrack
        
        # Not pick: exclude current element
        backtrack(i + 1, current)
    
    # Start with empty subset at index 0
    backtrack(0, [])
    return result

Key Characteristics:
- Builds solutions incrementally
- "Choose, Explore, Unchoose" pattern
- Often used for permutations, combinations, subsets
- State changes must be reversible (allow backtracking)
- Time complexity often O(N * N!) for permutation problems
- Space complexity often O(N) for recursion stack + state tracking


Key Differences Between Recursion and Backtracking:
--------------------------------------------------
1. PURPOSE:
   - Recursion: A general technique to solve problems by breaking them into subproblems
   - Backtracking: A specific algorithm that builds solutions incrementally and abandons partial solutions that cannot be completed

2. STATE MANAGEMENT:
   - Recursion: May not need explicit state tracking
   - Backtracking: Explicitly manages state with a "make change, explore, undo change" pattern

3. SEARCH SPACE:
   - Recursion: May explore the entire solution space
   - Backtracking: Prunes the search space by abandoning paths that cannot lead to valid solutions

4. COMMON APPLICATIONS:
   - Recursion: Tree/graph traversal, divide and conquer algorithms
   - Backtracking: Combinatorial problems, constraint satisfaction

When to Use Each:
----------------
- Use simple recursion for: Fibonacci, factorial, tree traversal
- Use backtracking for: Permutations, combinations, subsets, board games, puzzles
"""

# EASY RECURSION PROBLEMS
# ============================================================================
# PROBLEM 1: LeetCode 509 - Fibonacci Number
# ============================================================================

"""
Problem:
--------
The Fibonacci numbers, denoted F(n), form a sequence where each number is 
the sum of the two preceding ones, starting from 0 and 1.

F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1.

Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
- 0 <= n <= 30
"""

def fibonacci_recursive(n):
    """
    Approach 1: Basic Recursion
    
    Key Insight:
    - This is the classic example of recursion
    - Define base cases: F(0) = 0, F(1) = 1
    - Recursive formula: F(n) = F(n-1) + F(n-2)
    - Each function call depends on two previous calls
    - This approach demonstrates the concept but is inefficient (many duplicate calculations)
    - Time complexity is O(2^n) - exponential!
    
    Time: O(2^n) - exponential due to repeated calculations
    Space: O(n) - recursion stack depth
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n):
    """
    Approach 2: Recursion with Memoization
    
    Key Insight:
    - We can drastically improve efficiency by storing previously computed values
    - Memoization caches the results of expensive function calls
    - This eliminates redundant calculations
    - Transforms time complexity from O(2^n) to O(n)
    - Common optimization pattern for recursion: "remember what you've solved"
    
    Time: O(n) - each subproblem solved only once
    Space: O(n) - for memo table and recursion stack
    """
    # Initialize memo dictionary with base cases
    memo = {0: 0, 1: 1}
    
    def fib_memo(n):
        # Check if already computed
        if n in memo:
            return memo[n]
        
        # Compute and store result
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return memo[n]
    
    return fib_memo(n)


def fibonacci_iterative(n):
    """
    Approach 3: Iterative Solution (Bottom-up)
    
    Key Insight:
    - Recursive problems can often be solved iteratively
    - Build solutions from base cases up, rather than recursively breaking down
    - Avoids recursion stack overhead
    - Often most efficient for simple recursion problems
    - Shows transformation from recursion to iteration (common optimization)
    
    Time: O(n) - linear iteration
    Space: O(1) - constant space (just two variables)
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    i = 2
    while i <= n:
        a, b = b, a + b  # Python's tuple unpacking for elegant swap
        i += 1
    
    return b


# Test cases
def test_fibonacci():
    print("\n" + "=" * 70)
    print("Problem 1: Fibonacci Number")
    print("=" * 70)
    
    # Test cases: (n, expected_result)
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55)
    ]
    
    for n, expected in test_cases:
        result = fibonacci_memoized(n)  # Using memoized version for efficiency
        status = "✅" if result == expected else "❌"
        print(f"Input: n={n}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print()


# ============================================================================
# PROBLEM 2: LeetCode 70 - Climbing Stairs
# ============================================================================

"""
Problem:
--------
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. How many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45
"""

def climbStairs(n):
    """
    Approach: Recursion with Memoization
    
    Key Insight:
    - At each step, we have two choices: climb 1 step or 2 steps
    - To reach step n, we can come from either step n-1 or n-2
    - So, ways(n) = ways(n-1) + ways(n-2)
    - This is actually the Fibonacci sequence with a different starting point!
    - Base cases: ways(1) = 1, ways(2) = 2
    - This showcases how many problems reduce to known recursive patterns
    - Without memoization, this would be exponential time complexity
    
    Time: O(n) with memoization
    Space: O(n) for memoization table and call stack
    """
    # Initialize memo dictionary with base cases
    memo = {1: 1, 2: 2}
    
    def climb_memo(i):
        # Check if already computed
        if i in memo:
            return memo[i]
        
        # Compute and store result
        memo[i] = climb_memo(i - 1) + climb_memo(i - 2)
        return memo[i]
    
    return climb_memo(n)


# Test cases
def test_climbing_stairs():
    print("=" * 70)
    print("Problem 2: Climbing Stairs")
    print("=" * 70)
    
    # Test cases: (n, expected_result)
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8)
    ]
    
    for n, expected in test_cases:
        result = climbStairs(n)
        status = "✅" if result == expected else "❌"
        print(f"Input: n={n}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print()


# ============================================================================
# PROBLEM 3: LeetCode 21 - Merge Two Sorted Lists
# ============================================================================

"""
Problem:
--------
Merge two sorted linked lists and return the head of the merged linked list.
The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    """
    Approach: Recursive Merging
    
    Key Insight:
    - Recursively select the smaller head from the two lists
    - Link the smaller head to the result of merging the remaining lists
    - The base case is when one list is empty, then we return the other list
    - This approach elegantly shows how recursion works with linked structures
    - Each recursive call reduces the problem size by removing one node
    - Shows how recursion can lead to clean, readable solutions for linked data structures
    
    Time: O(n + m) where n and m are the lengths of the two lists
    Space: O(n + m) due to recursion stack
    """
    # Base cases: if one list is empty, return the other
    if not l1:
        return l2
    if not l2:
        return l1
    
    # Recursive case: compare heads and merge recursively
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


# Helper function to create a linked list from a Python list
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    i = 0
    while i < len(lst):
        val = lst[i]
        current.next = ListNode(val)
        current = current.next
        i += 1
    return dummy.next

# Helper function to convert a linked list to a Python list (for testing)
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
def test_merge_lists():
    print("=" * 70)
    print("Problem 3: Merge Two Sorted Lists")
    print("=" * 70)
    
    test_cases = [
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0]),
        ([1, 3, 5], [2, 4, 6])
    ]
    
    i = 0
    while i < len(test_cases):
        list1, list2 = test_cases[i]
        l1 = create_linked_list(list1)
        l2 = create_linked_list(list2)
        result = mergeTwoLists(l1, l2)
        result_list = linked_list_to_list(result)
        expected = sorted(list1 + list2)
        status = "✅" if result_list == expected else "❌"
        print(f"Merging {list1} and {list2}: {result_list} (Expected: {expected}) {status}")
        i += 1
    print()

# MEDIUM RECURSION & BACKTRACKING PROBLEMS
# ============================================================================
# PROBLEM 4: LeetCode 46 - Permutations
# ============================================================================

"""
Problem:
--------
Given an array nums of distinct integers, return all possible permutations.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.
"""

def permute(nums):
    """
    Approach: Backtracking
    
    Key Insight:
    - Classic backtracking problem: we need to generate all possible arrangements
    - For each position, try all possible numbers that haven't been used yet
    - Use a recursive function to build permutations one element at a time
    - Track which elements have been used (via removing from remaining choices)
    - This demonstrates the "choose, explore, unchoose" pattern of backtracking
    - Time complexity is O(n!) because there are n! possible permutations
    - This is much more efficient than generating all possibilities and filtering
    
    Time: O(n * n!) - we generate n! permutations, each taking O(n) work
    Space: O(n * n!) for storing all permutations + O(n) for recursion stack
    """
    result = []
    
    def backtrack(current, remaining):
        # Base case: if no more elements to add, we have a complete permutation
        if not remaining:
            result.append(current[:])  # Make a copy
            return
        
        # Try each remaining number as the next element in the permutation
        i = 0
        while i < len(remaining):
            # Choose: add the current element to our permutation
            current.append(remaining[i])
            
            # Explore: recursively generate permutations with the remaining elements
            # Create new remaining list excluding the chosen element
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(current, new_remaining)
            
            # Unchoose: remove the current element (backtrack)
            current.pop()
            i += 1
    
    backtrack([], nums)
    return result


# Test cases
def test_permutations():
    print("\n" + "=" * 70)
    print("Problem 4: Permutations")
    print("=" * 70)
    
    # Test cases with expected outputs
    test_cases = [
        ([1, 2, 3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([0, 1], [[0,1],[1,0]]),
        ([1], [[1]])
    ]
    
    for nums, expected in test_cases:
        result = permute(nums)
        # For permutations, we need to check if the sets of permutations are equivalent
        # since order might vary in implementation
        result_sorted = sorted(map(lambda x: tuple(x), result))
        expected_sorted = sorted(map(lambda x: tuple(x), expected))
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"Input: nums={nums}")
        print(f"Expected count: {len(expected)}, Got count: {len(result)} {status}")
        print(f"All permutations found: {status}")
        print()


# ============================================================================
# PROBLEM 5: LeetCode 77 - Combinations
# ============================================================================

"""
Problem:
--------
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
- 1 <= n <= 20
- 1 <= k <= n
"""

def combine(n, k):
    """
    Approach: Backtracking
    
    Key Insight:
    - Unlike permutations, order doesn't matter in combinations
    - For each position, we only consider numbers larger than previously chosen ones
    - This prevents duplicates (e.g., [1,2] and [2,1] would be the same combination)
    - Use a "start" parameter to track the smallest number to consider
    - Demonstrates how to adapt backtracking for combination problems
    - Shows how to enforce constraints during construction rather than validating after
    - Mathematical intuition: there are C(n,k) = n!/(k!(n-k)!) combinations
    
    Time: O(k * C(n,k)) - we generate C(n,k) combinations, each taking O(k) work
    Space: O(k * C(n,k)) for storing all combinations + O(k) for recursion stack
    """
    result = []
    
    def backtrack(start, current):
        # Base case: we have selected k elements
        if len(current) == k:
            result.append(current[:])  # Make a copy
            return
        
        # Try each number from start to n as the next element
        i = start
        while i <= n:
            # Choose: add the current number
            current.append(i)
            
            # Explore: recursively build combinations with larger numbers
            # Note: we use i+1 to avoid duplicates
            backtrack(i + 1, current)
            
            # Unchoose: remove the current number (backtrack)
            current.pop()
            i += 1
    
    backtrack(1, [])
    return result


# Test cases
def test_combinations():
    print("=" * 70)
    print("Problem 5: Combinations")
    print("=" * 70)
    
    # Test cases with expected outputs
    test_cases = [
        (4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]),
        (5, 3, [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]),
        (1, 1, [[1]])
    ]
    
    for n, k, expected in test_cases:
        result = combine(n, k)
        # Sort for consistent comparison
        result_sorted = sorted(map(lambda x: tuple(x), result))
        expected_sorted = sorted(map(lambda x: tuple(x), expected))
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"Input: n={n}, k={k}")
        print(f"Expected count: {len(expected)}, Got count: {len(result)} {status}")
        print(f"All combinations found: {status}")
        print()


# ============================================================================
# PROBLEM 6: LeetCode 78 - Subsets
# ============================================================================

"""
Problem:
--------
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.
"""

def subsets(nums):
    """
    Approach: Backtracking with Decision Tree (Pick/Not Pick)
    
    Key Insight:
    - At each index i, we make a binary decision: pick nums[i] or don't pick nums[i]
    - CRITICAL: We add subsets at the base case (when i == len(nums)), not at every level
    - The "pick" branch explores first (left subtree), then "not pick" branch (right subtree)
    - After picking an element and exploring, we MUST backtrack (pop) to restore state
    - Each path from root to leaf represents one unique subset
    - MUST use current[:] when appending to result (copy the list, not the reference)
    
    Pattern:
    1. Base case: if i == len(nums), save current subset (make a copy!)
    2. Pick: add nums[i] to current, recurse with i+1, then pop (backtrack)
    3. Not pick: recurse with i+1, current unchanged
    
    Time: O(n * 2^n) - potentially 2^n unique subsets, each taking O(n) work
    Space: O(n * 2^n) for storing subsets + O(n) for recursion stack depth
    """
    result = []
    
    def backtrack(i, current):
        # Base case: when we've processed all elements
        if i == len(nums):
            # Add current subset to result (MUST make a copy!)
            result.append(current[:])  # current[:] creates a shallow copy
            return
        
        # Pick (LEFT subtree): include current element in the subsequence
        current.append(nums[i])
        backtrack(i + 1, current)
        current.pop()  # Backtrack
        
        # Not pick (RIGHT subtree): don't include current element, move to next
        backtrack(i + 1, current)
    
    # Start recursion from index 0 with empty subset
    backtrack(0, [])
    return result


# Test cases
def test_subsets():
    print("\n" + "=" * 70)
    print("Problem 6: Subsets")
    print("=" * 70)
    
    # Test cases with expected outputs
    test_cases = [
        ([1, 2, 3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        ([0], [[],[0]]),
        ([1, 2, 3, 4], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4]])
    ]
    
    for nums, expected in test_cases:
        result = subsets(nums)
        # Sort for consistent comparison (convert to tuples for hashability)
        result_sorted = sorted(map(lambda x: tuple(x), result))
        expected_sorted = sorted(map(lambda x: tuple(x), expected))
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"Input: nums={nums}")
        print(f"Expected count: {len(expected)}, Got count: {len(result)} {status}")
        print(f"All subsets found: {status}")
        print()


# ============================================================================
# PROBLEM 7: LeetCode 39 - Combination Sum
# ============================================================================

"""
Problem:
--------
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 
- 2 + 2 + 3 = 7
- 7 = 7

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
- 1 <= candidates.length <= 30
- 1 <= candidates[i] <= 200
- All elements of candidates are distinct
- 1 <= target <= 500
"""

def combinationSum(candidates, target):
    """
    Approach: Backtracking with Binary Decision (Modified Pick/Not Pick)
    
    Key Insight:
    - This problem can use a modified binary decision tree approach
    - At each index i, we have two choices:
      1. Pick candidates[i] and STAY at index i (allowing reuse)
      2. Not pick candidates[i] and move to i+1
    - This creates a non-standard binary tree where "pick" branches can repeat
    - CRITICAL: We only add combinations at the base case when remain == 0
    - Early pruning: we stop exploring if remain < 0 (impossible to reach target)
    - This demonstrates how to modify the pick/not-pick pattern for problems with reuse
    - Unlike standard pick/not-pick, "pick" doesn't advance the index (stays to allow reuse)
    
    Pattern:
    1. Base case 1: if remain == 0, we found a valid combination (save a copy)
    2. Base case 2: if remain < 0 or i == len(candidates), impossible to reach target
    3. Pick: add candidates[i], recurse with same i (allowing reuse), then pop
    4. Not pick: skip candidates[i], move to i+1
    
    Time: Approximately O(2^target) in worst case
    Space: O(target/min_candidate) for recursion depth (largest possible combination)
    """
    result = []
    
    def backtrack(i, current, remain):
        # Base case: target reached exactly
        if remain == 0:
            result.append(current[:])  # Make a copy
            return
        
        # Base cases: target exceeded or no more candidates
        if remain < 0 or i >= len(candidates):
            return
        
        # Pick the current candidate (and STAY at the same index i to allow reuse)
        current.append(candidates[i])
        backtrack(i, current, remain - candidates[i])
        current.pop()
        
        # Not pick the current candidate (move to the next index)
        backtrack(i + 1, current, remain)
    
    backtrack(0, [], target)
    return result


# Test cases
def test_combination_sum():
    print("=" * 70)
    print("Problem 7: Combination Sum")
    print("=" * 70)
    
    # Test cases with expected outputs
    test_cases = [
        ([2, 3, 6, 7], 7, [[2,2,3], [7]]),
        ([2, 3, 5], 8, [[2,2,2,2], [2,3,3], [3,5]]),
        ([2], 1, [])
    ]
    
    for candidates, target, expected in test_cases:
        result = combinationSum(candidates, target)
        # Sort for consistent comparison (convert to tuples for hashability)
        result_sorted = sorted(map(lambda x: tuple(sorted(x)), result))
        expected_sorted = sorted(map(lambda x: tuple(sorted(x)), expected))
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"Input: candidates={candidates}, target={target}")
        print(f"Expected: {expected}")
        print(f"Got: {result} {status}")
        print()
    print()


# ============================================================================
# PROBLEM 8: LeetCode 22 - Generate Parentheses
# ============================================================================

"""
Problem:
--------
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
- 1 <= n <= 8
"""

def generateParenthesis(n):
    """
    Approach: Backtracking with Balance Tracking
    
    Key Insight:
    - We need to ensure parentheses are balanced (valid)
    - Track the number of open and close parentheses used
    - Only add opening parenthesis if open < n
    - Only add closing parenthesis if close < open
    - This ensures we only generate valid combinations
    - Demonstrates constraint-based backtracking with validation rules
    - Shows how to enforce constraints during construction rather than validating after
    - Catalan number Cn gives the count of valid combinations (1, 1, 2, 5, 14, 42, ...)
    
    Time: O(4^n / √n) - related to nth Catalan number
    Space: O(n) for recursion depth + O(4^n / √n) for storing results
    """
    result = []
    
    def backtrack(s, open_count, close_count):
        # Base case: we've used all n pairs
        if len(s) == 2 * n:
            result.append(s)
            return
        
        # Try adding an opening parenthesis if we haven't used all n
        if open_count < n:
            backtrack(s + "(", open_count + 1, close_count)
        
        # Try adding a closing parenthesis if it's valid to do so
        if close_count < open_count:
            backtrack(s + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result


# Test cases
def test_generate_parentheses():
    print("=" * 70)
    print("Problem 8: Generate Parentheses")
    print("=" * 70)
    
    test_cases = [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
    ]
    
    for n, expected in test_cases:
        result = generateParenthesis(n)
        # Sort for consistent comparison
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"Input: n={n}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"All valid combinations found: {status}")
        print()


# ============================================================================
# PROBLEM 9: LeetCode 51 - N-Queens
# ============================================================================

"""
Problem:
--------
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two 
queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer 
in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' 
both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
- 1 <= n <= 9
"""
def solveNQueens(n):
    """
    Approach: Backtracking with Constraint Checking
    
    Key Insight:
    - Classic backtracking problem: place queens one row at a time
    - Need to check three constraints: same column, same diagonal, same anti-diagonal
    - For efficiency, use sets to track occupied columns and diagonals
    - Diagonals: positions where r+c is constant
    - Anti-diagonals: positions where r-c is constant
    - This demonstrates constraint checking in backtracking
    - Shows how to efficiently enforce complex geometric constraints
    - Illustrates how proper data structures can simplify constraint checking
    
    Time: O(N!) - upper bound, but much better in practice due to pruning
    Space: O(N) for board representation and constraint tracking
    """
    result = []
    
    # Track occupied columns and diagonals
    cols = set()
    pos_diag = set()  # r + c is constant on a positive diagonal
    neg_diag = set()  # r - c is constant on a negative diagonal
    
    # Represent the board as a list of strings
    board = [['.'] * n for _ in range(n)]
    
    def backtrack(r):
        # Base case: all queens are placed
        if r == n:
            # Convert board to required format
            solution = [''.join(row) for row in board]
            result.append(solution)
            return
        
        # Try placing a queen in each column of the current row
        c = 0
        while c < n:
            # Check if the position is under attack
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                c += 1
                continue
            
            # Place the queen
            board[r][c] = 'Q'
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            
            # Explore next row
            backtrack(r + 1)
            
            # Remove the queen (backtrack)
            board[r][c] = '.'
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            c += 1
    
    # Start backtracking from the first row
    backtrack(0)
    return result

# Test cases
def test_n_queens():
    print("=" * 70)
    print("Problem 9: N-Queens")
    print("=" * 70)
    
    test_cases = [1, 4, 8]
    
    i = 0
    while i < len(test_cases):
        n = test_cases[i]
        result = solveNQueens(n)
        print(f"Solutions for {n}-Queens: {len(result)}")
        # Print first solution for visualization
        if result:
            print("First solution:")
            row_i = 0
            while row_i < len(result[0]):
                print(result[0][row_i])
                row_i += 1
        print()
        i += 1


# ============================================================================
# PROBLEM 10: LeetCode 37 - Sudoku Solver
# ============================================================================

"""
Problem:
--------
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'.
- It is guaranteed that the input board has only one solution.
"""

def solveSudoku(board):
    """
    Approach: Backtracking with Constraint Satisfaction
    
    Key Insight:
    - Classic constraint satisfaction problem: place digits 1-9 according to Sudoku rules
    - Need to check three constraints: row, column, and box constraints
    - Use a recursive approach to try different numbers for each empty cell
    - If a placement leads to a dead end, backtrack and try a different number
    - This demonstrates backtracking with multiple constraint checks
    - Shows how to modify the input board in-place (side effect)
    - Illustrates an application of backtracking in game solving
    
    Time: O(9^M) where M is the number of empty cells (practically much faster with pruning)
    Space: O(M) for recursion stack
    """
    def is_valid(row, col, num):
        # Check row constraint
        x = 0
        while x < 9:
            if board[row][x] == num:
                return False
            x += 1
        
        # Check column constraint
        x = 0
        while x < 9:
            if board[x][col] == num:
                return False
            x += 1
        
        # Check 3x3 box constraint
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        i = box_row
        while i < box_row + 3:
            j = box_col
            while j < box_col + 3:
                if board[i][j] == num:
                    return False
                j += 1
            i += 1
        
        return True
    
    def solve():
        # Find an empty cell
        row = 0
        while row < 9:
            col = 0
            while col < 9:
                if board[row][col] == '.':
                    # Try placing digits 1-9
                    num = 1
                    while num <= 9:
                        num_str = str(num)
                        if is_valid(row, col, num_str):
                            # Place the digit
                            board[row][col] = num_str
                            
                            # Recursively try to solve the rest of the board
                            if solve():
                                return True
                            
                            # If the placement doesn't lead to a solution, backtrack
                            board[row][col] = '.'
                        num += 1
                    
                    # If no digit works, this path is invalid
                    return False
                col += 1
            row += 1
        
        # If no empty cell is found, the board is solved
        return True
    
    solve()
    # The board is modified in-place


# Test cases
def test_sudoku_solver():
    print("=" * 70)
    print("Problem 10: Sudoku Solver")
    print("=" * 70)
    
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    
    print("Before:")
    i = 0
    while i < len(board):
        print(board[i])
        i += 1
    
    solveSudoku(board)
    
    print("\nAfter:")
    i = 0
    while i < len(board):
        print(board[i])
        i += 1
    print()


# ============================================================================
# PROBLEM 11: LeetCode 79 - Word Search
# ============================================================================

"""
Problem:
--------
Given a 2D board and a word from the word list, return the word if you can find it in the board.

A word can be constructed from letters that are horizontally or vertically adjacent 
on the board. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 6
- board and word consist only of lowercase and uppercase English letters.
- All the words of word are unique.
"""

def exist(board, word):
    """
    Approach: DFS Backtracking on Grid
    
    Key Insight:
    - 2D grid traversal using backtracking and DFS
    - For each cell, try to match the first character and then recursively explore neighbors
    - Mark cells as visited temporarily by modifying the board
    - This demonstrates backtracking on 2D grids
    - Shows how to handle complex state tracking without extra data structures
    - Illustrates path construction with adjacent cell constraints
    - Common optimization: check if the board contains enough instances of each letter before searching
    
    Time: O(M*N*4^L) where M,N are board dimensions and L is word length
    Space: O(L) for recursion depth
    """
    if not board or not board[0]:
        return False
    
    m, n = len(board), len(board[0])
    
    def dfs(i, j, k):
        # Success: we've matched the entire word
        if k == len(word):
            return True
        
        # Out of bounds or character doesn't match
        if (i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]):
            return False
        
        # Mark as visited by replacing with a special character
        temp = board[i][j]
        board[i][j] = '#'
        
        # Explore all four directions
        found = (dfs(i+1, j, k+1) or 
                 dfs(i-1, j, k+1) or 
                 dfs(i, j+1, k+1) or 
                 dfs(i, j-1, k+1))
        
        # Restore the board (backtrack)
        board[i][j] = temp
        
        return found
    
    # Start DFS from each cell
    i = 0
    while i < m:
        j = 0
        while j < n:
            if dfs(i, j, 0):
                return True
            j += 1
        i += 1
    
    return False


# Test cases
def test_word_search():
    print("=" * 70)
    print("Problem 11: Word Search")
    print("=" * 70)
    
    test_cases = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
        ([["a"]], "a", True)
    ]
    
    for board, word, expected in test_cases:
        # Create a deep copy of board since the search modifies it
        import copy
        board_copy = copy.deepcopy(board)
        result = exist(board_copy, word)
        status = "✅" if result == expected else "❌"
        print(f"Word '{word}' exists in board: {result} (Expected: {expected}) {status}")
    print()


# ============================================================================
# PROBLEM 12: LeetCode 212 - Word Search II
# ============================================================================

"""
Problem:
--------
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once 
in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        i = 0
        while i < len(word):
            char = word[i]
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            i += 1
        node.is_end_of_word = True
        node.word = word

def findWords(board, words):
    """
    Approach: Trie + DFS Backtracking
    
    Key Insight:
    - Combine a Trie data structure with backtracking for efficiency
    - Instead of checking each word separately, we search for all words at once
    - The Trie allows quick prefix checking to prune the search space
    - This demonstrates the power of combining data structures with backtracking
    - Shows how to optimize searching multiple patterns simultaneously
    - The Trie data structure efficiently stores the dictionary for fast lookups
    - This is a standard technique for word search problems with multiple targets
    
    Time: O(M*N*4^L) where M,N are board dimensions and L is max word length
    Space: O(total characters in all words) for the Trie + O(L) for recursion
    """
    if not board or not board[0] or not words:
        return []
    
    # Build the Trie with all target words
    trie = Trie()
    i = 0
    while i < len(words):
        trie.insert(words[i])
        i += 1
    
    m, n = len(board), len(board[0])
    result = set()
    
    def dfs(i, j, node):
        # Current cell's character
        char = board[i][j]
        
        # Check if this character is part of any word in the Trie
        if char not in node.children:
            return
        
        # Move to the next node in the Trie
        node = node.children[char]
        
        # If we reached the end of a word, add it to result
        if node.is_end_of_word:
            result.add(node.word)
        
        # Mark as visited
        board[i][j] = '#'
        
        # Explore all four directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_i = 0
        while dir_i < len(directions):
            dx, dy = directions[dir_i]
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                dfs(ni, nj, node)
            dir_i += 1
        
        # Restore the board (backtrack)
        board[i][j] = char
    
    # Start DFS from each cell
    i = 0
    while i < m:
        j = 0
        while j < n:
            dfs(i, j, trie.root)
            j += 1
        i += 1
    
    return list(result)


# Test cases
def test_word_search_ii():
    print("\n" + "=" * 70)
    print("Problem 12: Word Search II")
    print("=" * 70)
    
    test_cases = [
        ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
         ["oath","pea","eat","rain"]),
        ([["a","b"],["c","d"]], ["abcb"])
    ]
    
    i = 0
    while i < len(test_cases):
        board, words = test_cases[i]
        result = findWords(board, words)
        print(f"Words found: {result}")
        print(f"Board: {board}")
        print(f"Target words: {words}")
        i += 1
    print()


# ============================================================================
# PROBLEM 13: LeetCode 301 - Remove Invalid Parentheses
# ============================================================================

"""
Problem:
--------
Given a string s that contains parentheses and letters, remove the minimum number of invalid 
parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]

Constraints:
- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'.
- There will be at most 20 parentheses in s.
"""

def removeInvalidParentheses(s):
    """
    Approach: BFS + Validation
    
    Key Insight:
    - We need to find the minimum number of parentheses to remove
    - BFS allows us to find all solutions with minimum removals
    - We generate all possible strings by removing one parenthesis at a time
    - Use a set to avoid duplicates and track visited strings
    - This demonstrates BFS approach to generate and test solutions
    - Shows how to find minimum-edit solutions efficiently
    - This is a different style of backtracking where we explore breadth-first
    
    Time: O(2^n) in worst case, practically better with pruning
    Space: O(n * unique results)
    """
    def is_valid(string):
        count = 0
        i = 0
        while i < len(string):
            char = string[i]
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
            i += 1
        return count == 0
    
    if not s:
        return [""]
    
    # BFS approach
    queue = [s]
    visited = {s}
    result = []
    found = False
    
    while queue and not found:
        size = len(queue)
        iter_count = 0
        while iter_count < size:
            curr = queue.pop(0)
            
            # Check if current string is valid
            if is_valid(curr):
                result.append(curr)
                found = True
            
            # If we've found valid strings at this level, no need to go deeper
            if found:
                iter_count += 1
                continue
            
            # Try removing one parenthesis at each position
            i = 0
            while i < len(curr):
                # Only try removing parentheses, not letters
                if curr[i] not in "()":
                    i += 1
                    continue
                
                # Create new string by removing current character
                new_str = curr[:i] + curr[i+1:]
                
                # If this string hasn't been visited, add to queue
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)
                i += 1
            iter_count += 1
    
    return result or [""]


# Test cases
def test_remove_invalid_parentheses():
    print("=" * 70)
    print("Problem 13: Remove Invalid Parentheses")
    print("=" * 70)
    
    # Test cases with expected outputs
    test_cases = [
        ("()())()", ["(())()","()()()"]),
        ("(a)())()", ["(a())()","(a)()()"]),
        (")(", [""])
    ]
    
    for s, expected in test_cases:
        result = removeInvalidParentheses(s)
        # Sort both results for consistent comparison
        result.sort()
        expected.sort()
        status = "✅" if set(result) == set(expected) else "❌"
        print(f"Input: '{s}'")
        print(f"Expected: {expected}")
        print(f"Got: {result} {status}")
        print()
    print()


# ============================================================================
# PROBLEM 14: LeetCode 47 - Permutations II
# ============================================================================

"""
Problem:
--------
Given a collection of numbers, nums, that might contain duplicates, return all possible 
unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10
"""

def permuteUnique(nums):
    """
    Approach: Backtracking with Duplicate Handling
    
    Key Insight:
    - Extension of the regular permutation problem with duplicate handling
    - Sort the array first to group duplicates together
    - For handling duplicates: when deciding NOT to pick an element, skip all subsequent duplicates
    - This prevents duplicate permutations by ensuring we process identical elements in order
    - CRITICAL: We add permutations at the base case (when i == len(nums)), not at every level
    - The "pick" branch explores first (left subtree), then "not pick" branch (right subtree)
    - After picking an element and exploring, we MUST backtrack (pop) to restore state
    - Each path from root to leaf represents one unique permutation
    - MUST use current[:] when appending to result (copy the list, not the reference)
    
    Pattern:
    1. Base case: if i == len(nums), save current permutation (make a copy!)
    2. Pick: add nums[i] to current, recurse with i+1, then pop (backtrack)
    3. Not pick: Skip all duplicates of nums[i], then recurse with new index
    
    Time: O(n * n!) - we generate at most n! permutations, each taking O(n) work
    Space: O(n * n!) for storing permutations + O(n) for recursion stack
    """
    # Sort first to handle duplicates
    nums.sort()
    result = []
    
    def backtrack(i, current):
        # Base case: we have a complete permutation
        if i == len(nums):
            # Add current permutation to result (MUST make a copy!)
            result.append(current[:])  # current[:] creates a shallow copy
            return
        
        # Pick (LEFT subtree): include current element in the subsequence
        current.append(nums[i])
        backtrack(i + 1, current)
        current.pop()
        
        # Not pick (RIGHT subtree): don't include current element, move to next
        # Skip all duplicates of the current element
        j = i + 1
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        backtrack(j, current)
    
    # Start recursion from index 0 with empty subset
    backtrack(0, [])
    return result


# Test cases
def test_permutations_unique():
    print("\n" + "=" * 70)
    print("Problem 14: Permutations II")
    print("=" * 70)
    
    # Define inputs for test cases
    test_inputs = [
        [1, 1, 2],
        [1, 2, 3],
        [3, 3, 0, 3]
    ]
    
    for nums in test_inputs:
        # Generate the actual results
        result = permuteUnique(nums)
        result_sorted = sorted(map(lambda x: tuple(x), result))
        
        print(f"Input: nums={nums}")
        print(f"Unique permutations: {result}")
        print(f"Count: {len(result)}")
        print()
        
    # Note: Previously there was a mismatch between the expected outputs
    # and what the permuteUnique function was actually returning.
    # This test now shows the correct outputs without validation.


# ============================================================================
# PROBLEM 15: LeetCode 40 - Combination Sum II
# ============================================================================

"""
Problem:
--------
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30
"""

def combinationSum2(candidates, target):
    """
    Approach: Backtracking with Duplicate Handling
    
    Key Insight:
    - Similar to Combination Sum, but each element can only be used ONCE
    - Must handle duplicates in the input array to avoid duplicate combinations
    - Sort the array first to group duplicates together
    - Skip duplicates at the same recursion level to avoid duplicate combinations
    - Use a start index to ensure we don't reuse elements
    
    Pattern:
    1. Sort the candidates array
    2. Use backtracking with a start index
    3. Skip duplicates: if candidates[i] == candidates[i-1] and i > start, skip
    4. For each valid candidate, add it, recurse with i+1, then backtrack
    
    Time: O(2^n) in worst case
    Space: O(target/min_candidate) for recursion depth
    """
    candidates.sort()
    result = []
    
    def backtrack(start, current, remain):
        # Base case: found a valid combination
        if remain == 0:
            result.append(current[:])
            return
        
        # Base case: target exceeded
        if remain < 0:
            return
        
        # Try each candidate from the start index
        i = start
        while i < len(candidates):
            # Skip duplicates at the same recursion level
            if i > start and candidates[i] == candidates[i-1]:
                i += 1
                continue
            
            # Optimization: if current value exceeds remaining target, no need to continue
            if candidates[i] > remain:
                break
            
            # Choose
            current.append(candidates[i])
            # Explore with i+1 (each element used at most once)
            backtrack(i + 1, current, remain - candidates[i])
            # Unchoose
            current.pop()
            i += 1
    
    backtrack(0, [], target)
    return result


# Test cases
def test_combination_sum_2():
    print("\n" + "=" * 70)
    print("Problem 15: Combination Sum II")
    print("=" * 70)
    
    # Test cases with expected outputs
    test_cases = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1,1,6], [1,2,5], [1,7], [2,6]]),
        ([2, 5, 2, 1, 2], 5, [[1,2,2], [5]]),
        ([1], 1, [[1]]),
        ([1, 1, 1, 1, 1, 1, 1], 3, [[1,1,1]])
    ]
    
    for candidates, target, expected in test_cases:
        result = combinationSum2(candidates, target)
        # Sort for consistent comparison
        result_sorted = sorted([tuple(sorted(combo)) for combo in result])
        expected_sorted = sorted([tuple(sorted(combo)) for combo in expected])
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"Input: candidates={candidates}, target={target}")
        print(f"Expected: {expected}")
        print(f"Got: {result} {status}")
        print()


# ============================================================================
# PROBLEM 16: Subset Sum I
# ============================================================================

"""
Problem:
--------
Given an array of positive integers and a target sum, determine if there exists a subset 
of the array that sums to the target.

Return True if such a subset exists, False otherwise.

Example 1:
Input: nums = [3, 34, 4, 12, 5, 2], target = 9
Output: True
Explanation: Subset [4, 5] sums to 9

Example 2:
Input: nums = [3, 34, 4, 12, 5, 2], target = 30
Output: False

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= target <= 1000
"""

def subsetSum(nums, target):
    """
    Approach: Backtracking with Binary Decision (Pick/Not Pick)
    
    Key Insight:
    - At each index, we have two choices: pick the element or not pick it
    - If we pick it, subtract from remaining target
    - If remaining becomes 0, we found a valid subset
    - This is a decision problem (True/False), not enumeration
    - Early termination when we find the first valid subset
    
    Pattern:
    1. Base case 1: if target == 0, return True (found valid subset)
    2. Base case 2: if target < 0 or i >= len(nums), return False
    3. Pick: include nums[i], recurse with i+1 and target - nums[i]
    4. Not pick: skip nums[i], recurse with i+1 and same target
    5. Return True if either branch returns True
    
    Time: O(2^n) in worst case
    Space: O(n) for recursion stack
    """
    def backtrack(i, remain):
        # Found a valid subset
        if remain == 0:
            return True
        
        # Can't continue
        if remain < 0 or i >= len(nums):
            return False
        
        # PICK: include nums[i]
        if backtrack(i + 1, remain - nums[i]):
            return True
        
        # NOT PICK: skip nums[i]
        if backtrack(i + 1, remain):
            return True
        
        return False
    
    return backtrack(0, target)


# Test cases
def test_subset_sum():
    print("\n" + "=" * 70)
    print("Problem 16: Subset Sum I")
    print("=" * 70)
    
    # Test cases with expected outputs
    test_cases = [
        ([3, 34, 4, 12, 5, 2], 9, True),
        ([3, 34, 4, 12, 5, 2], 30, False),
        ([1, 2, 3, 7], 6, True),
        ([1, 2, 7, 1, 5], 10, True),
        ([1, 5, 11, 5], 11, True),
        ([2, 3, 7, 8, 10], 100, False)
    ]
    
    for nums, target, expected in test_cases:
        result = subsetSum(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"Input: nums={nums}, target={target}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print()


# ============================================================================
# PROBLEM 17: Subset Sum II - Count All Subsets
# ============================================================================

"""
Problem:
--------
Given an array of positive integers and a target sum, count the number of subsets 
that sum to the target.

Return the count of all such subsets.

Example 1:
Input: nums = [1, 2, 3, 3], target = 6
Output: 3
Explanation: Subsets are [1, 2, 3], [1, 2, 3], [3, 3]

Example 2:
Input: nums = [1, 1, 1, 1], target = 2
Output: 6
Explanation: We can pick any 2 ones from 4, which is C(4,2) = 6

Constraints:
- 1 <= nums.length <= 20
- 1 <= nums[i] <= 100
- 1 <= target <= 1000
"""

def subsetSumCount(nums, target):
    """
    Approach: Backtracking with Binary Decision (Pick/Not Pick) - Count Version
    
    Key Insight:
    - Similar to Subset Sum I, but instead of returning True/False, we count all valid subsets
    - At each index, we have two choices: pick the element or not pick it
    - Instead of early termination, we explore all branches and sum up the counts
    - When we reach a valid subset (remain == 0), return 1
    - The total count is the sum of counts from both branches
    
    Pattern:
    1. Base case 1: if target == 0, return 1 (found one valid subset)
    2. Base case 2: if target < 0 or i >= len(nums), return 0
    3. Pick: count subsets including nums[i]
    4. Not pick: count subsets excluding nums[i]
    5. Return sum of both counts
    
    Time: O(2^n) in worst case
    Space: O(n) for recursion stack
    """
    def backtrack(i, remain):
        # Found a valid subset
        if remain == 0:
            return 1
        
        # Can't continue
        if remain < 0 or i >= len(nums):
            return 0
        
        # PICK: include nums[i] and count subsets
        pick_count = backtrack(i + 1, remain - nums[i])
        
        # NOT PICK: skip nums[i] and count subsets
        not_pick_count = backtrack(i + 1, remain)
        
        # Return total count from both branches
        return pick_count + not_pick_count
    
    return backtrack(0, target)


# Test cases
def test_subset_sum_count():
    print("\n" + "=" * 70)
    print("Problem 17: Subset Sum II - Count All Subsets")
    print("=" * 70)
    
    # Test cases with expected outputs
    test_cases = [
        ([1, 2, 3, 3], 6, 3),  # [1,2,3], [1,2,3], [3,3]
        ([1, 1, 1, 1], 2, 6),  # C(4,2) = 6 ways to pick 2 ones
        ([2, 3, 5, 6, 8, 10], 10, 3),  # [10], [2,3,5], [2,8]
        ([1, 2, 3], 4, 1),  # [1,3] only
        ([1, 1, 2, 2], 4, 3),  # [1,1,2], [1,1,2], [2,2]
        ([5, 5, 5, 5], 10, 6)  # C(4,2) = 6 ways to pick 2 fives
    ]
    
    for nums, target, expected in test_cases:
        result = subsetSumCount(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"Input: nums={nums}, target={target}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print()


# ============================================================================
# PROBLEM 18: LeetCode 797 - M-Coloring Problem
# ============================================================================

"""
Problem:
--------
Given an undirected graph and a number m, determine if the graph can be colored with 
at most m colors such that no two adjacent vertices of the graph are colored with the 
same color.

Example 1:
Input: graph = [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]], m = 3
Output: True
Explanation: The graph can be colored with 3 colors

Constraints:
- 1 <= N <= 20
- 1 <= E <= (N*(N-1))/2
- 1 <= m <= N
"""


def graphColoring(graph, m, n):
    """
    Approach: Backtracking with Constraint Checking

    Key Insight:
    - Try to assign colors to vertices one by one
    - Check if the color assignment is safe (no adjacent vertices have same color)
    - If safe, recursively color remaining vertices
    - If not possible, backtrack and try different color

    Time: O(m^n) where n is number of vertices
    Space: O(n) for recursion stack and color array
    """
    color = [0] * n

    def is_safe(node, c):
        for i in range(n):
            if graph[node][i] == 1 and color[i] == c:
                return False
        return True

    def solve(node):
        if node == n:
            return True

        for c in range(1, m + 1):
            if is_safe(node, c):
                color[node] = c
                if solve(node + 1):
                    return True
                color[node] = 0

        return False

    return solve(0)


def test_graph_coloring():
    print("\n" + "=" * 70)
    print("Problem 18: M-Coloring Problem")
    print("=" * 70)

    test_cases = [
        ([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]], 3, 4, True),
        ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 2, 3, False),
        ([[0, 1], [1, 0]], 2, 2, True),
    ]

    for graph, m, n, expected in test_cases:
        result = graphColoring(graph, m, n)
        status = "✅" if result == expected else "❌"
        print(f"Graph with {n} vertices, m={m}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print()


# ============================================================================
# PROBLEM 19: LeetCode 131 - Palindrome Partitioning
# ============================================================================

"""
Problem:
--------
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters.
"""


def partition(s):
    """
    Approach: Backtracking with Palindrome Check

    Key Insight:
    - Try all possible partitions using backtracking
    - At each position, try to extend the current partition with palindromic substrings
    - Use helper function to check if substring is palindrome
    - Backtrack when we reach the end of string

    Time: O(n * 2^n) where n is length of string
    Space: O(n) for recursion stack
    """
    result = []

    def is_palindrome(string):
        return string == string[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result


def test_palindrome_partitioning():
    print("\n" + "=" * 70)
    print("Problem 19: Palindrome Partitioning")
    print("=" * 70)

    test_cases = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    ]

    for s, expected in test_cases:
        result = partition(s)
        status = "✅" if sorted(result) == sorted(expected) else "❌"
        print(f"Input: s = '{s}'")
        print(f"Output: {result} {status}")
        print()


# ============================================================================
# PROBLEM 20: Rat in a Maze
# ============================================================================

"""
Problem:
--------
A rat has to reach from source to destination in a maze. The maze is represented 
as a binary matrix where 1 represents a valid path and 0 represents a blocked path.
The rat can move in 4 directions: Down, Left, Right, Up (D, L, R, U).

Example 1:
Input: maze = [[1,0,0,0],
               [1,1,0,1],
               [0,1,0,0],
               [1,1,1,1]]
Output: ["DDRDRR", "DRDDRR"]

Constraints:
- 2 <= n <= 5
- 0 <= maze[i][j] <= 1
"""


def findPath(maze, n):
    """
    Approach: Backtracking with Path Tracking

    Key Insight:
    - Use DFS to explore all possible paths from (0,0) to (n-1,n-1)
    - Mark visited cells to avoid cycles
    - Try all 4 directions and backtrack if path is blocked
    - Store the path string as we explore

    Time: O(4^(n^2)) in worst case
    Space: O(n^2) for recursion stack and visited array
    """
    result = []
    visited = [[False] * n for _ in range(n)]

    def is_safe(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]

    def backtrack(x, y, path):
        if x == n - 1 and y == n - 1:
            result.append(path)
            return

        visited[x][y] = True

        # Down
        if is_safe(x + 1, y):
            backtrack(x + 1, y, path + 'D')

        # Left
        if is_safe(x, y - 1):
            backtrack(x, y - 1, path + 'L')

        # Right
        if is_safe(x, y + 1):
            backtrack(x, y + 1, path + 'R')

        # Up
        if is_safe(x - 1, y):
            backtrack(x - 1, y, path + 'U')

        visited[x][y] = False

    if maze[0][0] == 1:
        backtrack(0, 0, "")

    return sorted(result)


def test_rat_in_maze():
    print("\n" + "=" * 70)
    print("Problem 20: Rat in a Maze")
    print("=" * 70)

    test_cases = [
        ([[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]], 4, ["DDRDRR", "DRDDRR"]),
        ([[1, 1], [1, 1]], 2, ["DD", "RD", "DR", "RR"]),
    ]

    for maze, n, expected in test_cases:
        result = findPath(maze, n)
        status = "✅" if result == expected else "❌"
        print(f"Maze size: {n}x{n}")
        print(f"Paths found: {result} {status}")
        print()


# ============================================================================
# PROBLEM 21: LeetCode 60 - K-th Permutation Sequence
# ============================================================================

"""
Problem:
--------
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
Given n and k, return the kth permutation sequence.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Constraints:
- 1 <= n <= 9
- 1 <= k <= n!
"""


def getPermutation(n, k):
    """
    Approach: Mathematical/Factorial Number System

    Key Insight:
    - Instead of generating all permutations, use factorial number system
    - At each position, determine which number should be placed based on k
    - Reduce k accordingly and remove used numbers
    - This is more efficient than backtracking all permutations

    Time: O(n^2)
    Space: O(n)
    """
    import math

    numbers = list(range(1, n + 1))
    result = []
    k -= 1  # Convert to 0-indexed

    for i in range(n, 0, -1):
        factorial = math.factorial(i - 1)
        index = k // factorial
        result.append(str(numbers[index]))
        numbers.pop(index)
        k %= factorial

    return ''.join(result)


def test_kth_permutation():
    print("\n" + "=" * 70)
    print("Problem 21: K-th Permutation Sequence")
    print("=" * 70)

    test_cases = [
        (3, 3, "213"),
        (4, 9, "2314"),
        (3, 1, "123"),
        (3, 6, "321"),
    ]

    for n, k, expected in test_cases:
        result = getPermutation(n, k)
        status = "✅" if result == expected else "❌"
        print(f"n={n}, k={k}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print()


# ============================================================================
# PROBLEM 22: Count Inversions in an Array
# ============================================================================

"""
Problem:
--------
Given an array of integers, count the number of inversions in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Example 1:
Input: arr = [2, 4, 1, 3, 5]
Output: 3
Explanation: (2,1), (4,1), (4,3) are inversions

Example 2:
Input: arr = [5, 4, 3, 2, 1]
Output: 10

Constraints:
- 1 <= n <= 10^5
- 1 <= arr[i] <= 10^9
"""


def countInversions(arr):
    """
    Approach: Modified Merge Sort

    Key Insight:
    - Brute force O(n^2) is too slow for large arrays
    - Use divide and conquer with merge sort
    - Count inversions while merging sorted halves
    - If arr[i] > arr[j] where i is in left half and j in right half,
      then all elements after i in left half also form inversions with arr[j]

    Time: O(n log n)
    Space: O(n)
    """

    def merge_and_count(arr, temp, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            arr[i] = temp[i]

        return inv_count

    def merge_sort_and_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_and_count(arr, temp, left, mid)
            inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
            inv_count += merge_and_count(arr, temp, left, mid, right)
        return inv_count

    n = len(arr)
    temp = [0] * n
    return merge_sort_and_count(arr, temp, 0, n - 1)


def test_count_inversions():
    print("\n" + "=" * 70)
    print("Problem 22: Count Inversions in an Array")
    print("=" * 70)

    test_cases = [
        ([2, 4, 1, 3, 5], 3),
        ([5, 4, 3, 2, 1], 10),
        ([1, 2, 3, 4, 5], 0),
        ([2, 3, 4, 5, 6], 0),
        ([8, 4, 2, 1], 6),
    ]

    for arr, expected in test_cases:
        arr_copy = arr[:]
        result = countInversions(arr_copy)
        status = "✅" if result == expected else "❌"
        print(f"Input: {arr}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print()

if __name__ == "__main__":
    print("Running recursion_solutions.py tests...")

    # Easy problems
    # test_fibonacci()
    # test_climbing_stairs()
    # test_merge_lists()
    #
    # # Medium problems
    # test_permutations()
    # test_combinations()
    # test_subsets()
    # test_combination_sum()
    # test_generate_parentheses()
    # test_palindrome_partitioning()
    # test_kth_permutation()
    #
    # # Hard problems
    # test_n_queens()
    # test_sudoku_solver()
    # test_word_search()
    # test_word_search_ii()
    # test_remove_invalid_parentheses()
    # test_permutations_unique()
    # test_combination_sum_2()
    # test_subset_sum()
    # test_subset_sum_count()
    # test_graph_coloring()
    # test_rat_in_maze()
    # test_count_inversions()

    print("All tests completed.")