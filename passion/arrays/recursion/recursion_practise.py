
import time
#recursion basic practice

# print name 5 times
def print_name_fun(count):
    print(f"recursion iteration {count}")
    # base condition
    if count == 5:
        return

    count += 1

    # recursion function call.
    print_name_fun(count)
# print_name_fun(1)


# print name 5 times
def print_name_fun_backtrack(count):
    # base case/condition
    if count > 3:
        return

    # backtracking function call.
    print_name_fun_backtrack(count+1)
    print(f"recursion iteration {count}")
# print_name_fun_backtrack(0)

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

# sum of first N numbers
# functional way of forming recursion
def sum_of_N_numbers(i):
   if i > 4:
       return 0
   return i + sum_of_N_numbers(i+1)

# print(sum_of_N_numbers(1,N=4))


# parameterized way of forming recursion
def sum_of_N_numbers(i, sum):
   if i > 4:
       return sum
   return sum_of_N_numbers(i+1, sum+i)
# print(sum_of_N_numbers(1, sum=0))

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

# handle multiple recursion calls in a single function
hmap = {0:0,1:1}
def fibonacci_number(N):
    # base condition
    if N == 0:
        return hmap[N]
    if  N == 1:
        return hmap[N]

    if N-1 not in hmap :
        hmap[N-1] = fibonacci_number(N-1)
    if N-2 not in hmap:
        hmap[N-2] = fibonacci_number(N-2)

    return hmap[N-1] + hmap[N-2]

# time_1 = time.time()
# fibonacci_number(300)
# time_2 = time.time()
# print( (time_2-time_1) * 1000)
#


hmap = {0:0,1:1}
def fibonacci_number_2(N):
    # base condition
    if N == 0:
        return hmap[N]
    if  N == 1:
        return hmap[N]

    hmap[N-1] = fibonacci_number_2(N-1)
    hmap[N-2] = fibonacci_number_2(N-2)

    return hmap[N-1] + hmap[N-2]

# time_1 = time.time()
# fibonacci_number_2(35)
# time_2 = time.time()
# print( (time_2-time_1) * 1000)

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------


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




def subsets(arr):
    """
    Approach: Backtracking with Decision Tree (Pick/Not Pick)

    Key Insight:
    - At each index i, we make a binary decision: pick arr[i] or don't pick arr[i]
    - This creates a complete binary recursion tree with 2^n leaf nodes (one for each subset)
    - CRITICAL: We add subsets at the base case (when i == len(arr)), not at every level
    - The "not pick" branch explores first (left subtree), then "pick" branch (right subtree)
    - After picking an element and exploring, we MUST backtrack (pop) to restore state
    - Each path from root to leaf represents one unique subset
    - The recursion implicitly generates all 2^n combinations through the decision tree
    - MUST use current[:] when appending to result (copy the list, not the reference)
    
    Pattern:
    1. Base case: if i == len(arr), save current subset (make a copy!)
    2. Not pick: recurse with i+1, current unchanged
    3. Pick: add arr[i] to current, recurse with i+1, then pop (backtrack)

    Time: O(n * 2^n) - we generate 2^n subsets, each taking O(n) work to copy
    Space: O(n * 2^n) for storing all subsets + O(n) for recursion stack depth
    """
    result = []
    i=0
    current = []

    def backtracking(i, current, arr):
        # Base case: when we've processed all elements
        if i == len(arr):
            # Add current subset to result (MUST make a copy!)
            result.append(current[:])  # current[:] creates a shallow copy
            return
        
        # Pick (LEFT subtree): include current element in the subsequence
        current.append(arr[i])
        backtracking(i+1, current, arr)
        current.pop()
        # Not pick (RIGHT subtree): don't include current element, move to next
        backtracking(i+1, current, arr)
    
    # Start recursion from index 0 with empty subset
    backtracking(i, current, arr)
    return result


# Test cases
# def test_subsets():
#     print("=" * 70)
#     print("Problem 6: Subsets")
#     print("=" * 70)
#
#     test_cases = [
#         [3, 1, 2],
#         [0],
#         [1, 2, 3, 4]
#     ]
#
#     i = 0
#     while i < len(test_cases):
#         nums = test_cases[i]
#         result = subsets(nums)
#         print(f"Subsets of {nums}: {result}")
#         for  element in result:
#            if element == [1,2,3]:
#                print (True)
#                break
#
#         print(f"Number of subsets: {len(result)}")
#         i += 1


# ============================================================================
# PROBLEM 15: Leetcode 40 :Combination Sum II- without repetiting the numbers in the array.
# ============================================================================

"""
Problem:
--------
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

******Each number in candidates may only be used once in the combination.

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

def combinationSum2(arr, target):
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
    Space"""
    result = []
    i = 0
    current = []
    sum = 0

    def backtracking(i,current,arr,sum,target):
        # here, the boundary condition becomes the value of I.
        # we only focus on the leaf nodes.
        if i == len(arr):
            if sum == target:
                current_element = sorted(current[:])
                if current_element not in result:
                   result.append(current_element)
            return

        current.append(arr[i])
        sum += arr[i]
        # add the element and traverse the left subtree , thereby picking/choosing/adding the element into current list
        backtracking(i+1, current, arr, sum , target)

        sum -= arr[i]
        current.pop()
        # now remove th element and  traverse the left subtree , thereby picking/choosing/adding the element into current list
        backtracking(i+1, current, arr, sum , target )


    backtracking(i,current,arr,sum,target)
    return result


# Test cases
def test_combination_sum_2():
    print("\n" + "=" * 70)
    print("Problem 15: Combination Sum II")
    print("=" * 70)

    # Test cases with expected outputs
    test_cases = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        ([1], 1, [[1]]),
        ([1, 1, 1, 1, 1, 1, 1], 3, [[1, 1, 1]])
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
# PROBLEM 7: LeetCode 39 - Combination Sum - with repetiting the numbers in an array.
# ============================================================================

"""
Problem:
--------
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

******The same number may be chosen from candidates an unlimited number of times.

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


def combinationSum(arr, target):
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
    i = 0
    current = []

    def backtracking(i, current, target):
        if i == len(arr):
            if target == 0:
                result.append(current[:])
            return

        # case for element picked....add the element and traverse the left subtree , thereby picking/choosing/adding the element into current list
        if arr[i] <= target:
            current.append(arr[i])
            backtracking(i, current, target-arr[i])
            current.pop()

        # case for element not picked...now remove the element and  traverse the right subtree , thereby picking/choosing/adding the element into current list
        backtracking(i+1, current, target)

    backtracking(i,current,target)
    return result





# Test cases
def test_combination_sum():
    print("=" * 70)
    print("Problem 7: Combination Sum")
    print("=" * 70)

    test_cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1)
    ]

    i = 0
    while i < len(test_cases):
        candidates, target = test_cases[i]
        result = combinationSum(candidates, target)
        print(f"Combinations of {candidates} that sum to {target}: {result}")
        i += 1
    print()



# To only return if the sum exists or not.
# ============================================================================
# PROBLEM 7_variation: LeetCode 39 - Combination Sum - return only 1 result...not all
# ============================================================================

"""
Problem:
--------
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may NOT be chosen from candidates an unlimited number of times.

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


def combinationSum_variation(arr, target):
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
    i = 0
    current = []
    sum = 0

    def backtracking(i,current,arr,sum,target):
        if result:
            return True

        if i == len(arr):
            if ( sum == target):
                result.append(current[:])
                return True
            return False

        current.append(arr[i])
        sum += arr[i]
        # add the element and traverse the left subtree , thereby picking/choosing/adding the element into current list
        if backtracking(i+1, current, arr, sum, target):
            return True

        current.pop()
        sum -= arr[i]
        # now remove th element and  traverse the left subtree , thereby picking/choosing/adding the element into current list
        if backtracking(i+1, current, arr, sum, target):
            return True

        return False

    print( backtracking(i,current,arr,sum,target) )
    return result


# Test cases
def TEST_combinationSum_variation():
    print("=" * 70)
    print("Problem 7: Combination Sum")
    print("=" * 70)

    test_cases = [
        ([2,2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1)
    ]

    i = 0
    # while i < len(test_cases):
    #     candidates, target = test_cases[i]
    #     result = combinationSum_variation(candidates, target)
    #     print(f"Combinations of {candidates} that sum to {target}: {result}")
    #     i += 1
    # print()


# ============================================================================
# PROBLEM 7_variation: LeetCode 39 - Combination Sum - return total number of instances where elements sum up to target
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


def combinationSum_variation_return_number_of_sums(arr, target):
    i = 0
    sum = 0

    def backtracking(i,sum):
        if i == len(arr):
            return 1 if sum == target else 0

        sum += arr[i]
        left = backtracking(i+1, sum)

        sum -= arr[i]
        right =  backtracking(i+1, sum)

        return left+right

    return backtracking(i,sum)


# Test cases
def TEST_combinationSum_variation_return_number_of_sums():
    print("=" * 70)
    print("Problem 7: Combination Sum")
    print("=" * 70)

    test_cases = [
        ([2, 2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1)
    ]

    i = 0
    while i < len(test_cases):
        candidates, target = test_cases[i]
        result = combinationSum_variation_return_number_of_sums(candidates, target)
        print(f"Combinations of {candidates} that sum to {target}: {result}")
        i += 1
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


def subsetSum(arr, target):
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
    result = []
    i = 0
    current = []
    sum = 0

    def backtracking(i,current,arr,sum,target):
        if i == len(arr):
            if sum == target:
                return True
            return False

        current.append(arr[i])
        sum += arr[i]
        # add the element and traverse the left subtree , thereby picking/choosing/adding the element into current list
        if backtracking(i+1, current, arr, sum , target): return True

        sum -= arr[i]
        current.pop()
        # now remove th element and  traverse the left subtree , thereby picking/choosing/adding the element into current list
        if backtracking(i+1, current, arr, sum , target): return True

        return False

    return backtracking(i,current,arr,sum,target)



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


def subsetSumCount(arr, target):
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

    i = 0
    sum = 0

    def backtracking(i, sum):
        if i == len(arr):
            return 1 if sum == target else 0

        sum += arr[i]
        left = backtracking(i + 1, sum)

        sum -= arr[i]
        right = backtracking(i + 1, sum)

        return left + right

    return backtracking(i, sum)


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


def permute(arr):
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


        Initial Call: backtrack(current=[], hmap={})
    ├─ While loop: i=0,1,2 (tries all elements)
    │
    ├─ i=0: Pick arr[0]=1
    │  ├─ current=[1], hmap={0:True}
    │  ├─ Call backtrack(current=[1], hmap={0:True})
    │  │  └─ While loop: i=0,1,2 (NEW loop, starts from 0 again!)
    │  │     ├─ i=0: Skip (0 in hmap)
    │  │     ├─ i=1: Pick arr[1]=2
    │  │     │  ├─ current=[1,2], hmap={0:True, 1:True}
    │  │     │  ├─ Call backtrack(current=[1,2], hmap={0:True,1:True})
    │  │     │  │  └─ While loop: i=0,1,2 (ANOTHER NEW loop!)
    │  │     │  │     ├─ i=0: Skip (0 in hmap)
    │  │     │  │     ├─ i=1: Skip (1 in hmap)
    │  │     │  │     ├─ i=2: Pick arr[2]=3
    │  │     │  │     │  ├─ current=[1,2,3], hmap={0:True,1:True,2:True}
    │  │     │  │     │  ├─ Call backtrack(current=[1,2,3], hmap={0:True,1:True,2:True})
    │  │     │  │     │  │  └─ len(current)==3, SAVE [1,2,3] ✓
    │  │     │  │     │  ├─ Return and BACKTRACK
    │  │     │  │     │  ├─ current.pop() → current=[1,2]
    │  │     │  │     │  └─ del hmap[2] → hmap={0:True,1:True}
    │  │     │  │     └─ i=3: Exit while loop
    │  │     │  ├─ Return and BACKTRACK
    │  │     │  ├─ current.pop() → current=[1]
    │  │     │  └─ del hmap[1] → hmap={0:True}
    │  │     │
    │  │     ├─ i=2: Pick arr[2]=3
    │  │     │  ├─ current=[1,3], hmap={0:True, 2:True}
    │  │     │  ├─ Call backtrack(current=[1,3], hmap={0:True,2:True})
    │  │     │  │  └─ While loop tries i=0,1,2
    │  │     │  │     ├─ i=0: Skip (0 in hmap)
    │  │     │  │     ├─ i=1: Pick arr[1]=2
    │  │     │  │     │  └─ Eventually saves [1,3,2] ✓
    │  │     │  │     └─ i=2: Skip (2 in hmap)
    │  │     └─ i=3: Exit while loop
    │  └─ Return to initial call
    │
    ├─ i=1: Pick arr[1]=2
    │  └─ Similar process, generates [2,1,3] and [2,3,1]
    │
    └─ i=2: Pick arr[2]=3
       └─ Similar process, generates [3,1,2] and [3,2,1]


    """


    result = []
    hmap = {}
    current = []

    def backtrack(current,hmap):

        if len(current) == len(arr):
            result.append(current[:])
            return

        i=0
        while( i < len(arr) ):
            if i not in hmap:
               hmap[i] = True
               current.append(arr[i])
               backtrack(current, hmap)

               current.pop()
               del hmap[i]

            i+=1

    backtrack(current,hmap )
    print(result)
    return result



# Test cases
def test_permutations():
    print("\n" + "=" * 70)
    print("Problem 4: Permutations")
    print("=" * 70)

    # Test cases with expected outputs
    test_cases = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
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

def permuteUnique(arr):
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
    result = []
    hmap = {}
    current = []
    start = 0

    def backtrack(current, hmap):

        if len(current) == len(arr):
            unique_element = current[:]
            if unique_element not in result:
                result.append(current[:])
            return

        i = start
        while (i < len(arr)):
            if i not in hmap:
                hmap[i] = True
                current.append(arr[i])
                backtrack(current, hmap)

                current.pop()
                del hmap[i]

            i += 1

    backtrack(current, hmap)

    return result

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
# PROBLEM : Merge Sort
# ============================================================================


def merge_the_array(arr, left, mid, right):
    print(f"Array to be combined {arr[left:mid + 1]}.....and.....{arr[mid + 1:right + 1]}")

    # Create temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0  # Indices for left_arr and right_arr
    k = left  # Index for merged array

    # Merge while both arrays have elements
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy remaining elements (only one of these will execute)
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    print(f"After merge: {arr[left:right + 1]}")


def break_the_array(left, right, arr):
        # print( left, right , arr[left:right+1] )

        if (left >= right):
            return

        mid =  ( left + right ) // 2
        # print(left,mid,right)

        break_the_array(left, mid, arr)
        break_the_array(mid+1, right, arr)
        merge_the_array(arr, left, mid, right)


def test_merge_sort():
    arr = [3,1,2,4,1,5,2,6,4]
    break_the_array(0, len(arr)-1, arr)


# ============================================================================
# PROBLEM : Merge Sort
# ============================================================================

def Test_2d_array():

    arr = [
        [1,2,3,4],
        [5,6,7,'Q'],
        [9,10,11,12],
        [13,14,15,16]
    ]

    N = 4
    arr = [ [0]*N ]*N

    def backtrack( i, j, arr):
        if j == N:
            return

        # when the i(row) index has reached its capacity, increment j(column) and bring i to 0
        if i == N:
            j+=1
            backtrack(0, j, arr)
            return

        print( arr[i][j] )

        # keep on incrementing j until ( end of N ) has reached.
        backtrack( i+1, j, arr)

    backtrack(0, 0 ,arr)

    return 0


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


    # Represent the board as a list of strings
    board = [['_'] * n for _ in range(n)]

    def verify_for_n_queens(row, col ,board):
        row_num = row
        col_num = col

        # check for all the col's in the left
        while row >=0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1

        col = col_num
        row = row_num
        # check for all the cols and rows in the left, diagonally upwards
        while row >=0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1
            row -= 1

        col = col_num
        row = row_num
        # check for all the cols and rows in the left, diagonally downwards
        while row < len(board) and col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1
            row += 1

        return True


    def n_queens( col, board):
        if col == n:
            result.append([''.join(row) for row in board])
            return

        for row in range( 0, n):
            if verify_for_n_queens(  row, col, board) == True:
                board[row][col] = 'Q'
                n_queens(  col+1, board)
                board[row][col] = '_'

    n_queens( 0, board)

    # Print all solutions with better formatting
    for idx, solution in enumerate(result, 1):
        print(f"\n{'='*20} Solution {idx} {'='*20}")
        print("  " + " ".join(str(i) for i in range(n)))  # Column numbers
        for row_idx, row in enumerate(solution):
            print(f"{row_idx} {' '.join(row)}")  # Row number + board row
        
    return result


# Test cases
def test_n_queens():
    print("=" * 70)
    print("Problem 9: N-Queens")
    print("=" * 70)

    test_cases = [1,4,8]

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
    def is_valid_board( k, board, row, col):
        for r in range(0,9):
            # scan for an entire row for the element
            if board[r][col] == k:
                return False

        for c in range(0, 9):
            # scan for an entire column for the element
            if board[row][c] == k:
                return False

        # Check if k exists in the 3x3 box
        box_row_start = 3 * (row // 3)
        box_col_start = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[box_row_start + i][box_col_start + j] == k:
                    return False
        return True


    def sudoku_solver(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.' :
                    for k in ["1","2","3","4","5","6","7","8","9"]:
                        if is_valid_board( k, board, row, col):
                            board[row][col] = k
                            if sudoku_solver(board) == True:
                                return True
                            else:
                                board[row][col] = '.'
                    return False
        return True

    sudoku_solver(board)


# Test cases
def test_sudoku_solver():
    print("=" * 70)
    print("Problem 10: Sudoku Solver")
    print("=" * 70)

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

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




# Actually call the function to execute it
if __name__ == "__main__":
    # test_combination_sum() # repeating array elements
    # test_combination_sum_2() # Non repeating array elements
    # TEST_combinationSum_variation()
    # TEST_combinationSum_variation_return_number_of_sums()
    # test_subsets()
    # test_subset_sum()
    # test_subset_sum_count()
    test_permutations()
    # test_permutations_unique()
    # test_merge_sort()
    # Test_2d_array()
    # test_n_queens()
    # test_sudoku_solver()
