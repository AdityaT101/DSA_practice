# fibonacci using recursion.
def fibo_without_memoization(N):
    if N <= 0:
        return 0
    if N == 1:
        return 1
    return fibo_without_memoization(N-1) + fibo_without_memoization(N-2)
# print(fibo_without_memoization(42))


# fibonacci using DP - memoization.
hmap = {    0:0,
            1:1     }
def fibo_with_memoization(N):
    if N <= 0:
        return 0
    if N == 1:
        return 1
    if N in hmap:
        return hmap[N]
    hmap[N] = fibo_with_memoization(N-1) + fibo_with_memoization(N-2)
    return  hmap[N]
# print( fibo_with_memoization(42) )


# fibonacci using DP - tabulation.
def fibo_with_tabulation(N):
    i = 2
    current = 0
    prev_1 = 1
    prev_2 = 0

    while ( i <= N ):
        current = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = current
        i+=1

    return current

# print(fibo_with_tabulation(9))

##=================================================

# problems on subsequence
arr = [3,1,2,4]

i = 0
current = []
result = []
N = len(arr)

def backtrack(i, current):
    if i == N:
        result.append(current[:])
        return

    current.append(arr[i])
    backtrack(i+1, current)

    current.pop()
    backtrack(i+1, current)

    return result

# print( backtrack(i, current) )

##=================================================

# find sub-sequences whose sun == target
arr = [2,2,3,6,7]
target=7
result = []
current = []

def backtrack_sub_sequence_sum(i, sum, current):
    if i==len(arr):
        if sum == target:
            result.append(current[:])
        return

    current.append(arr[i])
    sum=sum+arr[i]
    backtrack_sub_sequence_sum(i+1, sum, current)

    current.pop()
    sum = sum - arr[i]
    backtrack_sub_sequence_sum(i+1,sum, current)

    return result

# print( backtrack_sub_sequence_sum(0, 0, [] ))


##=================================================
arr = [2,3,6]
target = 7
i = 0
sum = 0

def backtracking_whether_sum_exists( i, sum):
    if i == len(arr):
        if(sum == target):
            return True
        return False

    current.append(arr[i])
    sum += arr[i]
    # add the element and traverse the left subtree , thereby picking/choosing/adding the element into current list
    if backtracking_whether_sum_exists( i+1, sum):
        return True

    current.pop()
    sum -= arr[i]
    # now remove th element and  traverse the left subtree , thereby picking/choosing/adding the element into current list
    if backtracking_whether_sum_exists( i+1, sum):
        return True

    return False

# print( backtracking_whether_sum_exists( i, sum) )

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


def climbStairs(N):
    """
    Approach: 1D DP - Fibonacci Pattern

    Key Insight:
    - To reach step n, you can come from step n-1 (1 step) or n-2 (2 steps)
    - f(n) = f(n-1) + f(n-2)

    Time: O(n)
    Space: O(1) with space optimization
    """

    hmap= {0:1,1:1}
    def backtrack_climbing_stairs(N):

        if N <= 0  :
            return 1

        if N - 1 in hmap:
            one_step = hmap[N-1]
        else:
            one_step = backtrack_climbing_stairs(N - 1)
            hmap[N-1] = one_step

        if N - 2 in hmap:
            two_steps = hmap[N-2]
        else:
            two_steps = backtrack_climbing_stairs(N - 2)
            hmap[N - 1] = two_steps

        number_of_ways = one_step + two_steps

        return number_of_ways

    return backtrack_climbing_stairs(N)


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


def frogJump(arr):
    """
    Approach: 1D DP
    dp[i] = min(dp[i-1] + |h[i]-h[i-1]|, dp[i-2] + |h[i]-h[i-2]|)

    Time: O(n), Space: O(1)
    """

    hmap = {0: 0}


    def backtrack_frog_jump(i):

        if i == 0:
            return 0

        if i in hmap:
            return hmap[i]

        small_jump = backtrack_frog_jump(i-1) + abs(arr[i] - arr[i-1])

        long_jump = float('inf')
        if i > 1:
           long_jump = backtrack_frog_jump(i-2) + abs(arr[i] - arr[i-2])


        hmap[i] = min( small_jump , long_jump )
        return hmap[i]

    return backtrack_frog_jump(len(arr)-1)


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
# ============================================================================
# ============================================================================
# 2.
# test_climbing_stairs()

# 3.
test_frog_jump()










