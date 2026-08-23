from collections import defaultdict , deque

# gneral practise
# queue = deque()
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
#
# while queue:
#     print( queue.popleft())


# ======================================================================

def BalancedParenthesis( str):
    stack = []
    index = 0
    hmap = defaultdict()
    hmap['}'] = '{'
    hmap[')'] = '('
    hmap[']'] = '['

    while( index < len(str)):
        if str[index] not in hmap:
            stack.append( str[index])
        # the not stock condition is used for test cases like-> ')))' , '()))' , '{}[])'
        elif not stack or stack.pop() != hmap[ str[index]]:
               return False
        index += 1

    # if stack: return False
    # else: return True
    # u can either use above or below
    return not stack

# ======================================================================


def NextGreaterElement( arr):
    # -------------------------------------------------------------------------
    # PROBLEM: LeetCode 496 - Next Greater Element I
    # For each element, find the FIRST GREATER element to its RIGHT.
    # If no greater element exists, return -1.
    #
    # EXAMPLE:
    # arr = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
    #
    # idx:   0   1   2   3   4   5   6   7   8   9  10  11
    # arr:   4  12   5   3   1   2   5   3   1   2   4   6
    # NGE:  12  -1   6   5   2   5   6   4   2   4   6  -1
    #
    # For arr[0]=4:  looking right → 12 is first element > 4  → NGE = 12
    # For arr[1]=12: looking right → nothing > 12             → NGE = -1
    # For arr[2]=5:  looking right → 6 at idx 11 is first > 5 → NGE = 6
    # For arr[3]=3:  looking right → 5 at idx 6 is first > 3  → NGE = 5
    # For arr[4]=1:  looking right → 2 at idx 5 is first > 1  → NGE = 2
    # ... and so on
    #
    # -------------------------------------------------------------------------
    # INTUITION:
    # - Traverse RIGHT to LEFT (so we've already seen elements to the right)
    # - Maintain a MONOTONIC DECREASING stack (bottom=largest, top=smallest)
    # - Stack holds "candidates" that could be NGE for future elements
    # - Pop elements <= current (they can never be NGE for anything to the left)
    # - After popping, stack top (if exists) is the NGE
    #
    # -------------------------------------------------------------------------
    # WHY DECREASING STACK?
    # - We want the FIRST greater element, not the largest
    # - Smaller elements block larger ones from being the answer
    # - So we keep only elements that are strictly greater than what we've seen
    #
    # VISUAL: Processing arr = [4, 5, 2, 25] from right to left
    #
    # Step 1: idx=3, element=25
    #         stack = []  (empty)
    #         No NGE → result[3] = -1
    #         Push 25 → stack = [25]
    #
    # Step 2: idx=2, element=2
    #         stack = [25]
    #         2 < 25, so stack top is NGE → result[2] = 25
    #         Push 2 → stack = [25, 2]
    #
    # Step 3: idx=1, element=5
    #         stack = [25, 2]
    #         5 >= 2, pop 2 → stack = [25]
    #         5 < 25, so stack top is NGE → result[1] = 25
    #         Push 5 → stack = [25, 5]
    #
    # Step 4: idx=0, element=4
    #         stack = [25, 5]
    #         4 < 5, so stack top is NGE → result[0] = 5
    #         Push 4 → stack = [25, 5, 4]
    #
    # Final result: [5, 25, 25, -1]
    #
    # -------------------------------------------------------------------------
    # Time: O(n) - each element pushed and popped AT MOST ONCE
    # Space: O(n) - stack + result array
    # -------------------------------------------------------------------------
    stack = []
    return_array = [-1]*len(arr)

    # Traverse from right to left
    # Why? Because we need to know what's on the RIGHT before processing current
    index = len(arr)-1
    while index >= 0:
        element = arr[index]

        # Pop elements that are <= current element
        # WHY? They can NEVER be NGE for any element to the left of current
        # REASON: Current element is:
        #   1. Closer (to the left of them)
        #   2. Greater or equal (so it's a better candidate)
        # Example: stack=[25,5,2], current=3
        #   Pop 2 (3 >= 2), stack=[25,5]
        #   Now 5 is the NGE for 3 (first greater to right)
        while stack and element >= stack[-1] :
            stack.pop()

        # If stack is not empty, top is the first greater element to the right
        # The stack is decreasing, so top is the SMALLEST element that is > current
        # And since we traverse right-to-left, it's also the CLOSEST such element
        if stack and element < stack[-1]:
            return_array[index] = stack[-1]
        # If stack is empty, no greater element exists (already -1 by default)

        # Push current element - it's a candidate NGE for elements to its left
        # Even if current is small, it might be the NGE for an even smaller element
        stack.append( element)

        index -= 1

    return return_array

# ======================================================================

def PreviousSmallerElement( arr):
    # -------------------------------------------------------------------------
    # PROBLEM: For each element, find the FIRST SMALLER element to its LEFT.
    # If no smaller element exists, return -1.
    #
    # EXAMPLE:
    # arr = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
    #
    # idx:   0   1   2   3   4   5   6   7   8   9  10  11
    # arr:   4  12   5   3   1   2   5   3   1   2   4   6
    # PSE:  -1   4   4  -1  -1   1   2   2  -1   1   2   4
    #
    # For arr[0]=4:  looking left → nothing                  → PSE = -1
    # For arr[1]=12: looking left → 4 is first element < 12  → PSE = 4
    # For arr[2]=5:  looking left → 4 at idx 0 is first < 5  → PSE = 4
    # For arr[3]=3:  looking left → nothing < 3              → PSE = -1
    # For arr[4]=1:  looking left → nothing < 1              → PSE = -1
    # For arr[5]=2:  looking left → 1 at idx 4 is first < 2  → PSE = 1
    # ... and so on
    #
    # -------------------------------------------------------------------------
    # INTUITION:
    # - Traverse LEFT to RIGHT (so we've already seen elements to the left)
    # - Maintain a MONOTONIC INCREASING stack (bottom=smallest, top=largest)
    # - Stack holds "candidates" that could be PSE for future elements
    # - Pop elements >= current (they can never be PSE for anything to the right)
    # - After popping, stack top (if exists) is the PSE
    #
    # -------------------------------------------------------------------------
    # WHY INCREASING STACK?
    # - We want the FIRST smaller element, not the smallest
    # - Larger elements block smaller ones from being the answer
    # - So we keep only elements that are strictly smaller than what we've seen
    #
    # VISUAL: Processing arr = [4, 5, 2, 25] from left to right
    #
    # Step 1: idx=0, element=4
    #         stack = []  (empty)
    #         No PSE → result[0] = -1
    #         Push 4 → stack = [4]
    #
    # Step 2: idx=1, element=5
    #         stack = [4]
    #         5 > 4, so stack top is PSE → result[1] = 4
    #         Push 5 → stack = [4, 5]
    #
    # Step 3: idx=2, element=2
    #         stack = [4, 5]
    #         2 <= 5, pop 5 → stack = [4]
    #         2 <= 4, pop 4 → stack = []
    #         Stack empty, no PSE → result[2] = -1
    #         Push 2 → stack = [2]
    #
    # Step 4: idx=3, element=25
    #         stack = [2]
    #         25 > 2, so stack top is PSE → result[3] = 2
    #         Push 25 → stack = [2, 25]
    #
    # Final result: [-1, 4, -1, 2]
    #
    # -------------------------------------------------------------------------
    # COMPARISON WITH NGE (Mirror Patterns!):
    # ┌─────────────────┬──────────────────┬──────────────────┐
    # │                 │       NGE        │       PSE        │
    # ├─────────────────┼──────────────────┼──────────────────┤
    # │ Direction       │ Right to Left    │ Left to Right    │
    # │ Stack Type      │ Decreasing       │ Increasing       │
    # │ Looking for     │ Greater (right)  │ Smaller (left)   │
    # │ Pop condition   │ element >= top   │ element <= top   │
    # │ Answer          │ Stack top        │ Stack top        │
    # └─────────────────┴──────────────────┴──────────────────┘
    #
    # -------------------------------------------------------------------------
    # Time: O(n) - each element pushed and popped AT MOST ONCE
    # Space: O(n) - stack + result array
    # -------------------------------------------------------------------------
    stack = []
    return_array = [-1] * len(arr)

    # Traverse from left to right
    # Why? Because we need to know what's on the LEFT before processing current
    index = 0
    while index < len(arr) :
        element = arr[index]

        # Pop elements that are >= current element
        # WHY? They can NEVER be PSE for any element to the right of current
        # REASON: Current element is:
        #   1. Closer (to the right of them)
        #   2. Smaller or equal (so it's a better candidate)
        # Example: stack=[2,4,5], current=3
        #   Pop 5 (3 <= 5), pop 4 (3 <= 4), stack=[2]
        #   Now 2 is the PSE for 3 (first smaller to left)
        while stack and element <= stack[-1]:
            stack.pop()

        # If stack is not empty, top is the first smaller element to the left
        # The stack is increasing, so top is the LARGEST element that is < current
        # And since we traverse left-to-right, it's also the CLOSEST such element
        if stack and element > stack[-1]:
            return_array[index] = stack[-1]
        # If stack is empty, no smaller element exists (already -1 by default)

        # Push current element - it's a candidate PSE for elements to its right
        # Even if current is large, it might be the PSE for an even larger element
        stack.append( element)

        index += 1

    return return_array

# ======================================================================

def TrappingRainwater( arr):
    # -------------------------------------------------------------------------
    # INTUITION:
    # Water trapped at any index i depends on:
    #   1. The tallest bar to its LEFT (including itself)
    #   2. The tallest bar to its RIGHT (including itself)
    # Water level at i = min(left_max, right_max)
    # Water trapped at i = water_level - height[i]  (if positive)
    #
    # APPROACH: Precompute prefix_max and suffix_max arrays
    # Time: O(n), Space: O(n)
    # -------------------------------------------------------------------------

    # Edge case: empty array has no water
    if arr == []:
        return 0

    # prefix_max_array[i] = max height from index 0 to i (inclusive)
    # suffix_max_array[i] = max height from index i to end (inclusive)
    prefix_max_array = [-1]*(len(arr))
    suffix_max_array = [-1]*(len(arr))

    # Build prefix_max: scan left to right
    # prefix_max[i] = max(prefix_max[i-1], arr[i])
    # Example: arr = [0,1,0,2] → prefix_max = [0,1,1,2]
    prefix_max_array[0] = arr[0]
    for i in range( 1, len(arr)):
        prefix_max_array[i] = max( prefix_max_array[i-1] , arr[i])

    # Build suffix_max: scan right to left
    # suffix_max[i] = max(suffix_max[i+1], arr[i])
    # Example: arr = [0,1,0,2] → suffix_max = [2,2,2,2]
    suffix_max_array[-1] = arr[-1]
    for i in range(len(arr)-2 ,-1,-1 ):
        suffix_max_array[i] = max(suffix_max_array[i + 1], arr[i])

    # Calculate total trapped water
    # For each index, water trapped = min(left_max, right_max) - current_height
    # Only add if current bar is shorter than both boundaries (forms a valley)
    total = 0
    for i in range(0, len(arr)):
        leftmax = prefix_max_array[i]    # tallest bar from left up to i
        rightmax = suffix_max_array[i]   # tallest bar from i to right

        # Water can only be trapped if current bar is lower than both sides
        if arr[i] < leftmax and arr[i] < rightmax:
            # Water level is limited by the shorter of the two boundaries
            # Subtract current height to get trapped water at this position
            total += min( leftmax, rightmax) - arr[i]

    return total

# ======================================================================

def AsteroidCollissions(arr):
    stack = []

    index = 0
    while( index < len(arr)):

        if ( arr[index] < 0 ) :
            element = arr[index]
            while stack and stack[-1] > 0 and stack[-1] < abs( element):
                stack.pop()
            if stack and stack[-1] < 0 :
                stack.append( element)
            if stack and stack[-1] == abs( element):
                stack.pop()
            if not stack:
                stack.append( element)
        else:
            stack.append( arr[index])

        index +=1

    return stack

# ======================================================================


if __name__ == "__main__":

    # ======================================================================
    print("=" * 70)
    print("Problem: LeetCode 735 - Asteroid Collision")
    print("=" * 70)
    test_cases_asteroid = [
        [5, 10, -5],                      # -5 collides with 10, 10 survives → [5, 10]
        [5, -3],                          # Equal size, both destroyed → []
        [10, 2, -5],                      # -5 destroys 2, collides with 10 → [10]
        [-2, -1, 1, 2],                   # No collision → [-2, -1, 1, 2]
        [-2, -2, 1, -2],                  # 1 destroyed by -2 → [-2, -2, -2]
        [1, -1, -2, -2],                  # 1 and -1 destroy each other → [-2, -2]
        [1, -2, -2, -2],                  # -2 destroys 1 → [-2, -2, -2]
        [ 4, 7, 1, 1, 2, -3, -7, 17, -16],  # Complex case
        [1],                              # Single asteroid → [1]
        [],                               # Empty input → []
        [1, 2, 3, 4],                     # All moving right → [1, 2, 3, 4]
        [-1, -2, -3, -4],                 # All moving left → [-1, -2, -3, -4]
    ]

    for arr in test_cases_asteroid:
        result = AsteroidCollissions(arr)
        print(f"Input: {arr}")
        print(f"Result: {result}\n")
    # ======================================================================

    # ======================================================================
    # print("=" * 70)
    # print("Problem: LeetCode 42 - Trapping Rain Water")
    # print("=" * 70)
    # test_cases_trap = [
    #     ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    #     ([4, 2, 0, 3, 2, 5], 9),
    #     ([1, 0, 2], 1),
    #     ([2, 0, 2], 2),
    #     ([3, 0, 0, 2, 0, 4], 10),
    #     ([0, 0, 0, 0], 0),
    #     ([1, 2, 3, 4], 0),
    #     ([4, 3, 2, 1], 0),
    #     ([5], 0),
    #     ([], 0),
    # ]
    #
    # for height, expected in test_cases_trap:
    #     result = TrappingRainwater(height)
    #     status = "✅" if result == expected else "❌"
    #     print(f"Input: {height}")
    #     print(f"Expected: {expected}, Got: {result} {status}\n")

    # ===================================================================

    # print("=" * 70)
    # print("Problem: Previous Smaller Element")
    # print("=" * 70)
    # test_cases_pse = [
    #     ([ 4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6 ], [ -1, 4, 4, -1, -1, 1, 2, 2, -1, 1, 2, 4 ]),
    #     ([4, 5, 2, 25], [-1, 4, -1, 2]),
    #     ([13, 7, 6, 12], [-1, -1, -1, 6]),
    #     ([1, 2, 3, 4], [-1, 1, 2, 3]),
    #     ([4, 3, 2, 1], [-1, -1, -1, -1]),
    #     ([2, 7, 4, 3, 5], [-1, 2, 2, 2, 3]),
    #     ([1], [-1]),
    #     ([1, 1, 1, 1], [-1, -1, -1, -1]),
    # ]
    #
    # for arr, expected in test_cases_pse:
    #     result = PreviousSmallerElement(arr)
    #     status = "✅" if result == expected else "❌"
    #     print(f"Input: {arr}")
    #     print(f"Expected: {expected}, Got: {result} {status}\n")

    # ===================================================================

    # ===================================================================
    # print("=" * 70)
    # print("Problem: LeetCode 496 - Next Greater Element I")
    # print("=" * 70)
    # test_cases_nge = [
    #     ([ 4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6],  [12, -1, 6, 5, 2, 5, 6, 4, 2, 4, 6, -1] ),
    #     ([4, 5, 2, 25], [5, 25, 25, -1]),
    #     ([13, 7, 6, 12], [-1, 12, 12, -1]),
    #     ([1, 2, 3, 4], [2, 3, 4, -1]),
    #     ([4, 3, 2, 1], [-1, -1, -1, -1]),
    #     ([2, 7, 4, 3, 5], [7, -1, 5, 5, -1]),
    #     ([1], [-1]),
    #     ([1, 1, 1, 1], [-1, -1, -1, -1]),
    # ]
    #
    # for arr, expected in test_cases_nge:
    #     result = NextGreaterElement(arr)
    #     status = "✅" if result == expected else "❌"
    #     print(f"Input: {arr}")
    #     print(f"Expected: {expected}, Got: {result} {status}\n")

    # ===================================================================
    # print("=" * 70)
    # print("Problem: LeetCode 20 - Valid Parentheses")
    # print("=" * 70)
    # test_cases_20 = [
    #     ("()", True),
    #     ("()[]{}", True),
    #     ("(]", False),
    #     ("([{}])", True),
    #     ("([)]", False),
    #     ("(((", False),
    #     ("", True),
    #     ("{[()()]}", True),
    #     ("{[(])}", False),
    #     ("[({(())}[()])]", True),
    #     ("[({(())}[()]))", False),
    #     ("((()))[]{[]}", True),
    #     ("((()))[]{[]", False),
    #     (")(", False),
    #     ("{{{{}}}}", True),
    #     ("{{{{}}}}}", False),
    #     ("[({})](]", False),
    # ]
    #
    # for s, expected in test_cases_20:
    #     result = BalancedParenthesis(s)
    #     status = "✅" if result == expected else "❌"
    #     print(f"Input: '{s}'")
    #     print(f"Expected: {expected}, Got: {result} {status}\n")
    # ===================================================================


