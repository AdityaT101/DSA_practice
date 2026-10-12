from math import ceil



# ============================================================================# ============================================================================# ============================================================================
# ============================================================================# ============================================================================# ============================================================================# ============================================================================
# PROBLEM 1: Merge Sort Algorithm
# ============================================================================# ============================================================================# ============================================================================# ============================================================================
# ============================================================================# ============================================================================# ============================================================================

arr = [ 3, 1, 2, 4, 1, 5, 2, 6, 4]

left = 0
right = len(arr)-1

def merge( arr, left , mid, right):
    left_pointer = left
    right_pointer = mid + 1

    ret_arr = []

    while( left_pointer <= mid and right_pointer <= right):
        if arr[left_pointer] <= arr[right_pointer]:
            ret_arr.append(arr[left_pointer])
            left_pointer += 1
        else:
            ret_arr.append(arr[right_pointer])
            right_pointer += 1

    while( left_pointer <= mid):
            ret_arr.append( arr[left_pointer])
            left_pointer += 1
    while( right_pointer <= right):
            ret_arr.append(arr[right_pointer])
            right_pointer += 1

    arr[left:right + 1] = ret_arr


def mergesort(arr, left , right):
    if left < right:
        mid = ( right + left ) // 2
        mergesort( arr, left, mid)
        mergesort( arr, mid+1, right)
        merge( arr, left , mid, right)
    else :
        return

# mergesort( arr , left , right)
# print(arr)

# ============================================================================
# LeetCode 704 - Binary Search
# ============================================================================

def binary_search( arr, target):
    left = 0
    right = len(arr)

    while( left <= right):
        mid = (left + right)//2

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            right = mid

        elif target > arr[mid]:
            left = mid+1

    return -1


# print( binary_search( [ 1, 2, 3, 4, 5, 6], 2) )


# ============================================================================
# LeetCode 35 - Search Insert Position
# ============================================================================

def searchInsert( arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right)//2

        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1

    return left


test_cases_35 = [
    ([1, 3, 5, 5,5,5,5,5,5,5,5,5,5,6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([1], 1, 0),
    ([1], 2, 1),
]

# for nums, target, expected in test_cases_35:
#     result = searchInsert( nums, target)
#     status = "✅" if result == expected else "❌"
#     print(f"Input: nums={nums}, target={target}")
#     print(f"Expected: {expected}, Got: {result} {status}")


# ============================================================================
# Similar to LeetCode 35: Implement Lower Bound in an Array
# ============================================================================

arr = [1, 2, 3, 3, 5, 8, 8, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 22, 23, 24, 25, 26, 30]
arr = [5,7,7,8,8,10]

def ImplementTheLowerBound( arr, target):
    left = 0
    right = len(arr)
    LowerBound = len(arr) # lower bound Index

    while( left < right):
        mid = ( left+right)//2
        if target <= arr[mid]:
            LowerBound = right = mid
        elif target > arr[mid]:
            left = mid+1

    print( LowerBound)

# ImplementTheLowerBound( arr,6)

# ============================================================================
# PROBLEM 15: Implement Upper Bound in an Array
# ============================================================================

arr = [1, 2, 3, 3, 5, 8, 8, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 22, 23, 24, 25, 26, 30]
arr = [ 5,7,7,8,8,10,11,13,19,29]

def ImplementTheUpperBound( arr, target):
    left = 0
    right = len(arr)
    UpperBound = len(arr)

    while( left < right):
        mid = ( left+right)//2
        if target < arr[mid]:
            UpperBound = right = mid
        elif target >= arr[mid]:
            left = mid+1

    print( UpperBound , arr[UpperBound] )

# ImplementTheUpperBound( arr,13)


# ============================================================================
# LeetCode 34 - Find First and Last Position of Element in Sorted Array
# ============================================================================

def ImplementTheLowerBound_new( arr, target):
    left = 0
    right = len(arr)
    LowerBound = -1

    while( left < right):
        mid = ( left+right)//2

        if target < arr[mid]:
            right = mid

        elif target == arr[mid]:
            LowerBound = right = mid

        elif target > arr[mid]:
            left = mid+1

    return LowerBound


def ImplementTheUpperBound_new( arr, target):
    left = 0
    right = len(arr)
    UpperBound = -1

    while( left < right):
        mid = ( left+right)//2

        if target < arr[mid]:
            right = mid

        if target == arr[mid]:
            UpperBound = left = mid+1

        elif target > arr[mid]:
            left = mid+1

    return UpperBound-1 if UpperBound != -1 else -1


def searchRange( arr, target):
    print(  [ ImplementTheLowerBound_new( arr, target) , ImplementTheUpperBound_new( arr, target)] )


arr = [ 5, 7, 7, 8, 8, 10]
target = 7

# searchRange( arr, target)

# ============================================================================
# PROBLEM 4: LeetCode 278 - First Bad Version (EASY) ⭐⭐  [TEMPLATE 2]
# ============================================================================

"""
Problem:
--------
You are a product manager and currently leading a team to develop a new product.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version). Implement a function to find
the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
isBadVersion(3) → false
isBadVersion(5) → true
isBadVersion(4) → true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
- 1 <= bad <= n <= 2^31 - 1
"""

def firstBadVersion(n, isBadVersion):
    """
    Approach: Binary Search on a Boolean Function (Template 2)

    Key Insight:
    - There is NO array here — just a monotonic function:
      G G G G B B B B  (Good... then Bad forever)
    - "First bad" = first True of isBadVersion → Template 2 exactly
    - This is the bridge to "binary search on answer": the search space is a
      range of numbers and the condition is a function call, not an array lookup

    Pattern Recognition:
    - "first X where property flips" → boundary binary search
    - "minimize API calls" → O(log n) → binary search
    - Same shape as: first true, lower bound, min feasible answer

    Time: O(log n)
    Space: O(1)
    """
    left, right = 1, n

    while left < right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid          # mid is bad, might be first
        else:
            left = mid + 1       # mid is good, first bad is after

    return left


# Test cases
print("\n" + "=" * 70)
print("Problem 4: LeetCode 278 - First Bad Version")
print("=" * 70)

test_cases_278 = [
    (5, 4),
    (1, 1),
    (10, 1),
    (10, 10),
    (100, 37),
]

for n, bad in test_cases_278:
    api_calls = [0]

    def isBadVersion(v, _bad=bad, _calls=api_calls):
        _calls[0] += 1
        return v >= _bad

    result = firstBadVersion(n, isBadVersion)
    status = "✅" if result == bad else "❌"
    print(f"Input: n={n}, bad={bad}")
    print(f"Expected: {bad}, Got: {result} {status}  (API calls: {api_calls[0]})")
    print()




# ============================================================================
# LeetCode 33 - Search in Rotated Sorted Array
# ============================================================================

def search_element_in_a_rotated_array( arr, target):
    left = 0
    right = len(arr)-1

    while( left <= right):
        mid = (left+right)//2

        if arr[mid] == target:
            return mid

        elif arr[left] <= arr[mid]:
            if arr[left] <= target <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        elif arr[mid] < arr[right]:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

arr = [ 7, 8, 9, 1, 2, 3, 4, 5, 6]
target = 7
# print( search_element_in_a_rotated_array( arr, target))

# ============================================================================
# LeetCode 153 - Find Minimum in Rotated Sorted Array
# ============================================================================

def minimum_in_a_rotated_sorted_array(arr):
    left = 0
    right = len(arr)-1
    min_element = arr[0]

    while( left <= right):
        mid = (left+right)//2

        if arr[left] <= arr[mid]:
            min_element = min( min_element, arr[left])
            left = mid + 1

        elif arr[mid] <= arr[right]:
            min_element = min( min_element, arr[mid])
            right = mid - 1

    return min_element

# arr = [ 17, 18, 19, 0, 1, 2, 3]
arr = [-1]
# print( minimum_in_a_rotated_sorted_array(arr))


# ============================================================================
# LeetCode 162 - Find Peak Element
# ============================================================================

arr = [ 1, 10, 13, 7, 6, 5, 4, 2, 1, 0]
arr = [ 12, 20, 30, 40, 50, 60, 4, 2, 1, 0]

def find_peak_element(arr):
    if len(arr) == 1: return 0
    if arr[0] > arr[1]: return 0
    if arr[len(arr)-2] < arr[len(arr)-1] : return len(arr)-1

    left = 1
    right = len(arr)-2

    while( left <= right):
        mid = (left+right)//2

        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return mid

        # means that peak on the left, hence mover your window to the left side
        # this is a decreasing curve
        elif arr[mid-1] > arr[mid]:
            right = mid-1

        # means that peak on the right, hence move your window to the right side
        # this is an increasing curve
        elif arr[mid] < arr[mid+1]:
            left = mid + 1


# print( find_peak_element(arr))

# ============================================================================
# LeetCode 56 - Merge Intervals (MEDIUM) [ SORT + SWEEP] [ RIPPLE ASKED]
# ============================================================================

def mergeIntervals(arr):
    if not arr:
        return []

    arr.sort(key=lambda x: x[0])
    return_array = [arr[0]]

    for i in range( 1, len(arr)):
        if return_array[-1][1] >= arr[i][0]:
            return_array[-1][1] = max( arr[i][1] , return_array[-1][1])
        else:
            return_array.append(arr[i])

    return return_array


# Test cases
# print("\n" + "=" * 70)
# print("Problem 11: LeetCode 56 - Merge Intervals  [RIPPLE ASKED]")
# print("=" * 70)

test_cases_56 = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [0, 4]], [[0, 4]]),                  # unsorted input
    ([[1, 4], [2, 3]], [[1, 4]]),                  # fully contained
    ([[1, 10], [2, 3], [4, 5], [11, 12]], [[1, 10], [11, 12]]),
    ([[5, 5]], [[5, 5]]),
]

# for intervals, expected in test_cases_56:
#     original = [iv[:] for iv in intervals]
#     result = mergeIntervals([iv[:] for iv in intervals])
#     status = "✅" if result == expected else "❌"
#     print(f"Input: {original}")
#     print(f"Expected: {expected}, Got: {result} {status}")
#     print()


# ============================================================================
# PROBLEM 3: Second Largest Number in Array
# ============================================================================
import heapq

arr = [ 20, 3, 45, 1, -1, 451, 10, 9, 7, 0]
pq =  []

def second_largest_number( arr):

    # for i in range( 0, len(arr)):
    #     heapq.heappush( pq, arr[i])
    #     if len(pq) > 2:
    #         heapq.heappop(pq)
    #
    # print( heapq.heappop( pq))

    largest = arr[0]
    second_largest = -1

    for i in range( 1, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

    print( second_largest)

# second_largest_number( arr)


# ============================================================================
# LeetCode 215 - Kth Largest Element in an Array (MEDIUM) [HEAP / QUICKSELECT]
# ============================================================================

def findKthLargest_heap( arr, k):
    import heapq
    pq = []
    for i in range(0, len(arr)):
        heapq.heappush(pq, arr[i])
        if len(pq) > k:
            heapq.heappop(pq)
    element = heapq.heappop(pq)
    return element

# findKthLargest_heap(arr, k)

# ============================================================================
# LeetCode 875 - Koko Eating Bananas (MEDIUM) [BINARY SEARCH ON ANSWER]
# ============================================================================


def minEatingSpeed( piles, hours_available):
    """
    Find minimum eating speed (bananas/hour) to finish all piles within hours_available.

    Binary search on ANSWER: search space is [1, max(piles)]
    - Speed too slow → need more hours → increase speed
    - Speed fast enough → try slower speed to find minimum
    """

    def hours_needed_at_speed( piles, speed):
        """Calculate total hours needed to eat all piles at given speed."""
        total_hours = 0
        for pile in piles:
            total_hours += ceil( pile/speed)
        return total_hours


    # Search space: speed can be 1 to max(piles)
    left = 1
    right = max(piles)
    answer = right  # worst case: eat fastest pile in 1 hour

    while left <= right:
        mid = (left + right) // 2
        
        hours_at_current_speed = hours_needed_at_speed( piles, mid)

        if hours_at_current_speed <= hours_available:
            # Can finish in time → this speed works, try slower
            answer = min( mid, answer)
            right = mid - 1
        else:
            # Too slow → need faster speed
            left = mid + 1

    return answer



# print( minEatingSpeed( [3,6,7,11], 8))


# ============================================================================
# LeetCode 146 - LRU Cache
# ============================================================================
from collections import deque, defaultdict, OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        self.hmap.move_to_end(key)
        return self.hmap[key]

    def put(self, key: int, value: int) -> None:
        self.hmap[key] = value
        self.hmap.move_to_end(key)
        if len(self.hmap) > self.capacity:
            self.hmap.popitem(last=False)

    def print_ordered_dict(self):
        print(self.hmap)


# obj = LRUCache(4)
# obj.put(2,6)
# obj.put(4,7)
# obj.put(8,11)
# obj.put(7,10)
# obj.print_ordered_dict()
# print(obj.get(2))
# print(obj.get(8))
# obj.print_ordered_dict()
# obj.put(5,6)
# obj.print_ordered_dict()
# print(obj.get(7))
# obj.print_ordered_dict()
# obj.put(5,7)
# obj.print_ordered_dict()



# ============================================================================
# leetcode 189: Rotate Array by D Places
# ============================================================================

d = 3
arr = [1,2,3,4,5,6,7,8,9,10]

def reverse_in_place( arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def rotate_the_array_by_d_places( arr, d):
    # here, d can be in ranges of > 1, it can be 13, 56 etc ,
    # hence we use modulo operator
    N = len(arr)
    # d = d % N
    # i = 0
    #
    # temp_arr = arr[:d]
    # for j in range( d, N):
    #     arr[i] = arr[j]
    #     i += 1
    #
    # arr[N-d:] = temp_arr
    # print( arr)

    reverse_in_place(arr, 0, d-1)
    reverse_in_place(arr, d, N-1)
    reverse_in_place(arr, 0, N-1)
    print(arr)

# rotate_the_array_by_d_places( arr , d)


# ============================================================================
# Leetcode 88. Merge Sorted Array
# ============================================================================
def merge_sorted_arrays(arr_1, m, arr_2, n):
        """
        Solution 1
        """
        # if arr_1 == []:
        #     return arr_2
        # if arr_2 == []:
        #     return arr_1
        #
        # left = 0
        # right = 0
        #
        # temp_arr = []
        #
        # while( left < m and right < n):
        #     if arr_1[left] < arr_2[right]:
        #         temp_arr.append(arr_1[left])
        #         left += 1
        #     elif arr_1[left] == arr_2[right]:
        #         temp_arr.append(arr_1[left])
        #         temp_arr.append(arr_2[right])
        #         left += 1
        #         right += 1
        #     else:
        #         temp_arr.append(arr_2[right])
        #         right += 1
        #
        # while( left < m):
        #     temp_arr.append(arr_1[left])
        #     left += 1
        #
        # while( right < n):
        #     temp_arr.append(arr_2[right])
        #     right += 1
        #
        # return temp_arr

        if arr_1 == []:
            return arr_2
        if arr_2 == []:
            return arr_1

        left = m - 1
        right = n - 1
        pointer = len(arr_1) - 1

        while( right >= 0):
            if left >= 0 and arr_1[left] > arr_2[right]:
                arr_1[pointer] = arr_1[left]
                left -= 1
            else:
                arr_1[pointer] = arr_2[right]
                right -= 1


            pointer -= 1

        return arr_1

# time complexity is O( M+N)
# print( merge_sorted_arrays([ 1, 2, 3, 0, 0, 0], 3, [ 2, 5, 6], 3))

# ============================================================================
# PROBLEM 5: Union of 2 Sorted Arrays
# ============================================================================

def union_of_2_sorted_arrays( arr_1 , arr_2):
    if arr_1 == []:
        return arr_2
    if arr_2 == []:
        return arr_1

    # i = 0
    # j = 0
    # return_array = []
    #
    # while( i < len(arr_1) and j < len(arr_2)):
    #     if arr_1[i] <= arr_2[j] :
    #         if not return_array or return_array[-1] != arr_1[i]:
    #            return_array.append( arr_1[i])
    #         i += 1
    #
    #     elif arr_2[j] <= arr_1[i]:
    #         if not return_array or return_array[-1] != arr_2[j]:
    #            return_array.append( arr_2[j])
    #         j += 1
    #
    # while( i < len(arr_1)):
    #     if not return_array or  return_array[-1] != arr_1[i]:
    #         return_array.append(arr_1[i])
    #     i += 1
    #
    # while (j < len(arr_2)):
    #     if not return_array or return_array[-1] != arr_2[j]:
    #         return_array.append(arr_2[j])
    #     j += 1
    #
    #
    # print(return_array)

    m = len(arr_1)
    n = len(arr_2)
    interval = ceil((m + n)/2)

    def swap(swap_arr_1, index_1, swap_arr_2, index_2):
        if swap_arr_1[index_1] > swap_arr_2[index_2]:
            swap_arr_1[index_1], swap_arr_2[index_2] = swap_arr_2[index_2], swap_arr_1[index_1]

    while (interval > 0):
        left = 0
        right = left + interval

        while( right < (m+n)):
            # if arr_1 and arr_2
            if left < m and right >= m:
                swap(arr_1, left, arr_2, right - m)
            # if arr_2 and arr_2
            elif left >= m and right >= m:
                swap(arr_2, left - m, arr_2, right - m)
            # if arr_1 and arr_1
            elif left < m and right < m:
                swap(arr_1, left, arr_1, right)

            left += 1
            right += 1

        if interval == 1 : break
        interval = ceil( interval/2)

    print( arr_1, arr_2)


arr_1 = [1,1,2,3,4,5]
arr_2 = [2,3,4,4,5,6]
# union_of_2_sorted_arrays( arr_1 , arr_2)


# ============================================================================
# Leetcode 349: Intersection of 2 Sorted Arrays
# ============================================================================

def intersection_of_2_sorted_arrays( arr_1 , arr_2):
    if arr_1 == []:
        return arr_2
    if arr_2 == []:
        return arr_1

    i = 0
    j = 0
    return_array = []

    while( i < len(arr_1) and j < len(arr_2)):
        if arr_1[i] < arr_2[j] :
            i += 1

        elif arr_2[j] < arr_1[i]:
            j += 1

        elif arr_2[j] == arr_1[i]:
            return_array.append( arr_2[j])
            i += 1
            j += 1

    print(return_array)

arr_1 = [ 0,1,1,2,3,4,5]
arr_2 = [ 2,3,4,4,5,6]
# intersection_of_2_sorted_arrays( arr_1 , arr_2)

# ============================================================================
# PROBLEM 7: LeetCode 1 - Two Sum
# ============================================================================

def twoSum( arr, target: int):
    hmap = defaultdict(list)

    for i in range( 0, len(arr)):
        if target-arr[i] in hmap:
            if i not in list( hmap[ target-arr[i]]):
                return [ i, list( hmap[ target-arr[i]])[0]]

        hmap[ arr[i]].append(i)

# Test cases
test_cases_1 = [
    ([2, 7, 11, 15], 9),           # Basic case: 2 + 7 = 9
    ([3, 2, 4], 6),                # 2 + 4 = 6
    ([3, 3], 6),                   # Duplicate elements: 3 + 3 = 6
    ([-3, 4, 3, 90], 0),           # Negative + positive: -3 + 3 = 0
    ([1, 5, 8, 1, 2], 3),          # 1 + 2 = 3
    ([0, 4, 3, 0], 0),             # Two zeros: 0 + 0 = 0
]

# for nums, target in test_cases_1:
#     result = twoSum(nums, target)
#     print(f"Input: {nums}, Target: {target}")
#     print(f"Result: {result}\n")

# ============================================================================
# LeetCode 15 - Three Sum
# ============================================================================

arr = [ -2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2]
result_set = set()

def three_sum( arr):
    arr.sort()

    for i in range( 0, len(arr)-2 ):
        j = i+1
        k = len(arr)-1

        while( j < k):
            if arr[i] + arr[j] + arr[k] == 0:
                result_set.add( ( arr[i] , arr[j] , arr[k]) )
                j += 1
                k -= 1

            elif arr[i] + arr[j] + arr[k] > 0:
                k -= 1

            else:
                j += 1

    return_list = [ list(a) for a in result_set ]
    print(return_list)

# three_sum(arr)

# ============================================================================# ============================================================================
# ============================================================================# ============================================================================
# LeetCode 53 - Maximum Sum Subarray (Kadane's Algorithm)
# ============================================================================# ============================================================================
# ============================================================================# ============================================================================

def maxSubArray( arr) :
    global_max_sum = float('-inf')
    current_sum = 0

    for i in range(0, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        global_max_sum = max( global_max_sum, current_sum)

    return global_max_sum

# print( maxSubArray( [-2,1,-3,4,-1,2,1,-5,4]))

# ============================================================================
# PROBLEM 10: Maximum Sum Subarray with Indices
# ============================================================================

def maxSubArray_with_indices(arr):
    global_max_sum = float('-inf')
    current_sum = 0

    temp_left = 0  # Track potential left index
    left_index = 0
    right_index = 0

    for i in range(0, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_left = i  # Start new subarray here
        else:
            current_sum = current_sum + arr[i]

        if current_sum > global_max_sum:
            global_max_sum = current_sum
            left_index = temp_left  # Capture left when we find new max
            right_index = i

    return [ global_max_sum, left_index, right_index]

# print( maxSubArray_with_indices( [-2,1,-3,4,-1,2,1,-5,4]))

# ============================================================================
# PROBLEM 11: Minimum Sum Subarray with Indices
# ============================================================================

def minSubArray(arr):
    global_min_sum = float('inf')
    previous_sum = 0

    for i in range( 0, len(arr)):
        current_min_sum = min( arr[i], previous_sum + arr[i])

        global_min_sum = min( global_min_sum, current_min_sum)

        previous_sum = current_min_sum

    return global_min_sum


def minSubArray_with_indices(arr):
    min_sum = float('inf')
    previous_sum = 0

    left_index = 0
    right_index = 0
    temp_left_index = 0

    for i in range( 0, len(arr)):
        if arr[i] <= previous_sum+arr[i]:
            temp_left_index = i
            current_sum = arr[i]
        else:
            current_sum = previous_sum+arr[i]

        if current_sum < min_sum:
            left_index = temp_left_index
            right_index = i
            min_sum = current_sum

        previous_sum = current_sum

    return [ min_sum, left_index, right_index]

# print( minSubArray([ -2, 1, -3, 4, -1, -10, 2, 1, -5, 4]))
# print( minSubArray_with_indices([ -2, 1, -3, 4, -1, -10, 2, 1, -5, 4]))


# ============================================================================
#  LeetCode 152 - Maximum Product Subarray
# ============================================================================

"""
1. PATTERN RECOGNITION:
   - Similar to maximum sum subarray but with multiplication
   - Key difference: negative numbers can flip signs
   - Two negatives make a positive!

2. CRITICAL INSIGHT:
   - Need to track BOTH maximum and minimum
   - Why? A negative number can turn:
     * Small negative (min) → Large positive (new max)
     * Large positive (max) → Small negative (new min)

3. STATE TRANSITIONS:
   At each position, three choices:
   a) Start fresh with current number
   b) Multiply with previous max (if current is positive)
   c) Multiply with previous min (if current is negative)

4. ALGORITHM:
   - Track max_prod and min_prod at each step
   - When we see a negative number:
     * Swap max_prod and min_prod (signs flip)
   - Update: max_prod = max(num, max_prod * num, min_prod * num)
   - Update: min_prod = min(num, max_prod * num, min_prod * num)

5. EDGE CASES:
   - Zero resets both max and min to 0
   - Single negative number
   - Even number of negatives (all multiply to positive)
   - Odd number of negatives (need to exclude one)
"""

def maxProduct( arr):
    """
    Approach 1: Track both max and min products

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    global_max_product = previous_min_product = previous_max_product = arr[0]

    for i in range( 1, len(arr)):
        if arr[i] < 0:
            previous_min_product, previous_max_product = previous_max_product, previous_min_product

        current_min_product = min(arr[i], previous_min_product * arr[i])
        current_max_product = max(arr[i], previous_max_product * arr[i])

        global_max_product = max(current_min_product, current_max_product, global_max_product)

        previous_min_product, previous_max_product = current_min_product, current_max_product

    return global_max_product


# Test cases for Problem 4
def test_max_product():
    print("\nTesting Problem 4: Maximum Product Subarray")
    print("=" * 60)

    test_cases = [
        ([2, 3, -2, 4], 6, "Mixed with negative"),
        ([-2, 0, -1], 0, "Contains zero"),
        ([-2, 3, -4], 24, "All multiply to positive"),
        ([2, -5, -2, -4, 3], 24, "Multiple negatives"),
        ([-2], -2, "Single negative"),
        ([0, 2], 2, "Zero at start"),
        ([2, 3, 4], 24, "All positive"),
        ([-1, -2, -3, -4], 24, "All negative, even count"),
    ]

    for nums, expected, description in test_cases:
        result = maxProduct(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print()

# test_max_product()



