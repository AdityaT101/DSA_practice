# ============================================================================
# PROBLEM 4: LeetCode 643 - Maximum Average Subarray I (EASY)
# ============================================================================

"""
Problem:
--------
You are given an integer array nums consisting of n elements, and an
integer k.

Find a contiguous subarray whose length is equal to k that has the
maximum average value and return this value.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4
"""


def findMaxAverage(arr, k):
    """
    Approach: Fixed sliding window with sum tracking

    Key Insight:
    - This is the SIMPLEST fixed window problem - perfect for beginners!
    - We need to find the maximum sum of any k consecutive elements
    - Then divide by k to get the average
    - Use a fixed window of size k and slide it across the array
    - Track the current sum by adding right element and removing left element
    - Keep track of the maximum sum seen
    - The key is: maintain FIXED window size = k, track sum efficiently

    Time: O(n)
    Space: O(1)
    """

    if len(arr) < k:
        return None

    # find the inital array sum to add and subtract element from.
    max_sum = sum(arr[:k])
    result = max_sum

    left = 0
    right = k

    while right < len(arr):
        max_sum += arr[right]
        max_sum -= arr[left]
        result = max(result, max_sum)
        left += 1
        right += 1

    return result/k


# Test cases
print("=" * 70)
print("Problem 4: LeetCode 643 - Maximum Average Subarray I (EASY)")
print("=" * 70)
test_cases_643 = [
    ([1, 12, -5, -6, 50, 3], 4),
    ([5], 1),
    ([0, 4, 0, 3, 2], 1),
    ([4, 0, 4, 3, 3], 5)
]

# for nums, k in test_cases_643:
#     result = findMaxAverage(nums, k)
#     print(f"nums: {nums}, k: {k}")
#     print(f"Result: {result:.5f}\n")

# ============================================================================
# PROBLEM 5: LeetCode 1456 - Maximum Number of Vowels in a Substring (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a string s and an integer k, return the maximum number of vowel 
letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters
- 1 <= k <= s.length
"""


def maxVowels(arr, k):
    """
    Approach: Fixed sliding window with vowel counting

    Key Insight:
    - We need to find the maximum count of vowels in any k consecutive characters
    - Use a fixed window of size k and slide it across the string
    - Track the current vowel count by adding/removing characters
    - Keep track of the maximum vowel count seen
    - The key is: maintain FIXED window size = k, count vowels efficiently

    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = k
    max_vowels = 0

    vowels = ['a','e','i','o','u']

    i = 0
    while i < k:
        if arr[i] in vowels:
            max_vowels += 1
        i += 1

    result = max_vowels

    while right < len(arr):
        if arr[left] in vowels:
            max_vowels -= 1
        left += 1

        if arr[right] in vowels:
            max_vowels += 1
        right += 1

        result = max(result, max_vowels)

    return result


# Test cases
print("=" * 70)
print("Problem 5: LeetCode 1456 - Maximum Number of Vowels (MEDIUM)")
print("=" * 70)
test_cases_1456 = [
    ("abciiidef", 3),
    ("aeiou", 2),
    ("leetcode", 3),
    ("rhythms", 4)
]

# for s, k in test_cases_1456:
#     result = maxVowels(s, k)
#     print(f"s: '{s}', k: {k}")
#     print(f"Result: {result}\n")

# ============================================================================
# deque
# ============================================================================

from collections import deque

dq = deque()

dq.append(1)
dq.append(2)
dq.append(3)
print(dq)

# def MonotonicallyDecreasingDeque(dq , element):
#
#     while dq and dq[-1] < element:
#         dq.pop()
#
#     if not dq:
#         dq.append(element)
#     else:
#         while dq
#
#     return dq
#
# arr = [90,2,3,101,4,67,88,43,1001]
#
# for element in arr:
#     print( MonotonicallyDecreasingDeque(dq, element) )



# ============================================================================
# PROBLEM 9A: LeetCode 217 - Contains Duplicate I (EASY)
# ============================================================================

"""
Problem:
--------
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""


def containsDuplicate(arr):
    """
    Approach: Hash Set

    Key Insight:
    - Simply check if we've seen each number before
    - Use a set to track seen numbers
    - If we encounter a number already in set, we found a duplicate
    - This is NOT a sliding window problem - just hash set usage

    Time: O(n)
    Space: O(n)
    """

    left = 0
    right = 0
    hset = set()

    while right < len(arr):

        if arr[right] in hset:
            return True

        hset.add(arr[right])
        right += 1

    return False


# Test cases
print("=" * 70)
print("Problem 9A: LeetCode 217 - Contains Duplicate I (EASY)")
print("=" * 70)
test_cases_217 = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
]

# for nums in test_cases_217:
#     result = containsDuplicate(nums)
#     print(f"nums: {nums}")
#     print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 9B: LeetCode 219 - Contains Duplicate II (EASY)
# ============================================================================

"""
Problem:
--------
Given an integer array nums and an integer k, return true if there are 
two distinct indices i and j in the array such that nums[i] == nums[j] 
and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Explanation: nums[0] = nums[3] = 1, and 0 - 3 = 3 <= k

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Explanation: nums[2] = nums[3] = 1, and 3 - 2 = 1 <= k

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Explanation: No duplicates within distance 2

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5
"""


def containsNearbyDuplicate(arr, k):
    """
    Approach: Fixed sliding window with hash set

    Key Insight:
    - We need to check if duplicate exists within a window of size k
    - Use a fixed window of size k and maintain a set of elements in window
    - For each new element, check if it's already in the window set
    - If yes, we found a duplicate within distance k
    - Slide the window by removing leftmost element and adding new element
    - The key is: maintain FIXED window size = k, check for duplicates in set

    Time: O(n)
    Space: O(min(n, k))
    """
    if k == 0:
        return False

    left = 0
    hset = set()
    i = 0

    while i < k :
        if arr[i] in hset:
            return True
        hset.add(arr[i])
        i += 1

    right = k


    while right < len(arr):
      if arr[right] in hset:
          return True
      hset.remove(arr[left])
      hset.add(arr[right])

      left += 1
      right += 1

    return False


# Test cases
print("=" * 70)
print("Problem 9B: LeetCode 219 - Contains Duplicate II (EASY)")
print("=" * 70)
test_cases_219 = [
    ([1, 2, 3, 1], 3),
    ([1, 0, 1, 1], 1),
    ([1, 2, 3, 1, 2, 3], 2),
    ([99, 99], 2)
]

# for nums, k in test_cases_219:
#     result = containsNearbyDuplicate(nums, k)
#     print(f"nums: {nums}, k: {k}")
#     print(f"Result: {result}\n")

# ============================================================================
# PROBLEM 9C: LeetCode 220 - Contains Duplicate III (HARD)
# ============================================================================

"""
Problem:
--------
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:
- i != j,
- abs(i - j) <= indexDiff  (indices are close)
- abs(nums[i] - nums[j]) <= valueDiff  (values are close)

Return true if such pair exists or false otherwise.

Example 1:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: i = 0 and j = 3, abs(0 - 3) = 3, abs(1 - 1) = 0
             Indices 0 and 3 are within distance 3, and values are identical (diff = 0)

Example 2:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: No two elements within distance 2 have value difference <= 3

Example 3:
Input: nums = [1,3,1], indexDiff = 1, valueDiff = 1
Output: false
Explanation: 
  - indices 0,1: distance = 1 ✅, value diff = |1-3| = 2 ❌ (> 1)
  - indices 1,2: distance = 1 ✅, value diff = |3-1| = 2 ❌ (> 1)
  - indices 0,2: distance = 2 ❌ (> indexDiff=1)

Example 4:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 4
Output: true
Explanation: i = 0 and j = 1, abs(0 - 1) = 1 <= 2, abs(1 - 5) = 4 <= 4

Example 5:
Input: nums = [2,4], indexDiff = 1, valueDiff = 1
Output: false
Explanation: Only pair (0,1): distance = 1 ✅, value diff = |2-4| = 2 ❌ (> 1)

Constraints:
- 2 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 1 <= indexDiff <= nums.length
- 0 <= valueDiff <= 10^9

DETAILED WALKTHROUGH:
---------------------

Example: nums = [1, 5, 9, 1, 5, 9], indexDiff = 2, valueDiff = 3

Step-by-step with window of size indexDiff = 2:

i=0, num=1:
  Window: [1]
  Check: No previous elements
  Result: Continue

i=1, num=5:
  Window: [1, 5]
  Check: Is there any num in window where |5 - num| <= 3?
    - |5 - 1| = 4 > 3 ❌
  Result: Continue

i=2, num=9:
  Window: [1, 5, 9]  (size > indexDiff, so remove oldest)
  Window after removal: [5, 9]
  Check: Is there any num in window where |9 - num| <= 3?
    - |9 - 5| = 4 > 3 ❌
  Result: Continue

i=3, num=1:
  Window: [5, 9, 1]  (size > indexDiff, so remove oldest)
  Window after removal: [9, 1]
  Check: Is there any num in window where |1 - num| <= 3?
    - |1 - 9| = 8 > 3 ❌
  Result: Continue

i=4, num=5:
  Window: [9, 1, 5]  (size > indexDiff, so remove oldest)
  Window after removal: [1, 5]
  Check: Is there any num in window where |5 - num| <= 3?
    - |5 - 1| = 4 > 3 ❌
  Result: Continue

i=5, num=9:
  Window: [1, 5, 9]  (size > indexDiff, so remove oldest)
  Window after removal: [5, 9]
  Check: Is there any num in window where |9 - num| <= 3?
    - |9 - 5| = 4 > 3 ❌
  Result: Continue

Final: No pair found → return False


Example: nums = [1, 2, 3, 1], indexDiff = 3, valueDiff = 0

i=0, num=1:
  Window: [1]
  Check: No previous elements
  Result: Continue

i=1, num=2:
  Window: [1, 2]
  Check: Is there any num in window where |2 - num| <= 0?
    - |2 - 1| = 1 > 0 ❌
  Result: Continue

i=2, num=3:
  Window: [1, 2, 3]
  Check: Is there any num in window where |3 - num| <= 0?
    - |3 - 1| = 2 > 0 ❌
    - |3 - 2| = 1 > 0 ❌
  Result: Continue

i=3, num=1:
  Window: [1, 2, 3, 1]  (size = indexDiff + 1)
  Check: Is there any num in window where |1 - num| <= 0?
    - |1 - 1| = 0 <= 0 ✅ FOUND!
  Result: return True

Final: Pair found at indices (0, 3) → return True
"""


def containsNearbyAlmostDuplicate(arr, indexDiff, valueDiff):
    """
    Approach: Fixed sliding window with bucket/set approach

    Key Insight:
    - We need to check if there exist two numbers within indexDiff distance
      that have at most valueDiff difference in value
    - Use a fixed window of size indexDiff
    - For each position, check if there's a number in the window within valueDiff range
    - Use a set to store numbers in current window
    - For each new number, check if any number in [num - valueDiff, num + valueDiff] exists
    - The key is: maintain FIXED window size = indexDiff, check value range

    Time: O(n * indexDiff) in worst case, O(n) average with optimizations
    Space: O(min(n, indexDiff))
    """

    return False


# Test cases with detailed explanations
print("=" * 70)
print("Problem 9C: LeetCode 220 - Contains Duplicate III (HARD)")
print("=" * 70)
print("\nDetailed Test Cases:\n")

# test_cases_220_detailed = [
#     {
#         'nums': [1, 2, 3, 1],
#         'indexDiff': 3,
#         'valueDiff': 0,
#         'expected': True,
#         'explanation': 'Exact duplicate: indices (0,3) have same value 1, distance=3'
#     },
#     {
#         'nums': [1, 5, 9, 1, 5, 9],
#         'indexDiff': 2,
#         'valueDiff': 3,
#         'expected': False,
#         'explanation': 'All pairs within distance 2 have value diff > 3'
#     },
#     {
#         'nums': [1, 3, 1],
#         'indexDiff': 1,
#         'valueDiff': 1,
#         'expected': False,
#         'explanation': 'Pairs (0,1) and (1,2) both have value diff = 2 > valueDiff=1'
#     },
#     {
#         'nums': [1, 5, 9, 1, 5, 9],
#         'indexDiff': 2,
#         'valueDiff': 4,
#         'expected': True,
#         'explanation': 'Pair (0,1): distance=1, value diff=|1-5|=4 <= valueDiff=4'
#     },
#     {
#         'nums': [2, 4],
#         'indexDiff': 1,
#         'valueDiff': 1,
#         'expected': False,
#         'explanation': 'Only pair (0,1): value diff=|2-4|=2 > valueDiff=1'
#     },
#     {
#         'nums': [1, 2, 1, 1],
#         'indexDiff': 1,
#         'valueDiff': 0,
#         'expected': True,
#         'explanation': 'Exact duplicate: indices (2,3) have same value 1, distance=1'
#     },
#     {
#         'nums': [2, 2],
#         'indexDiff': 3,
#         'valueDiff': 0,
#         'expected': True,
#         'explanation': 'Exact duplicate: indices (0,1) have same value 2, distance=1'
#     },
#     {
#         'nums': [1, 0, 1, 1],
#         'indexDiff': 1,
#         'valueDiff': 2,
#         'expected': True,
#         'explanation': 'Pair (0,1): distance=1, value diff=|1-0|=1 <= valueDiff=2'
#     },
#     {
#         'nums': [7, 1, 3],
#         'indexDiff': 2,
#         'valueDiff': 3,
#         'expected': True,
#         'explanation': 'Pair (1,2): distance=1, value diff=|1-3|=2 <= valueDiff=3'
#     },
#     {
#         'nums': [10, 100, 11, 9],
#         'indexDiff': 1,
#         'valueDiff': 2,
#         'expected': True,
#         'explanation': 'Pair (2,3): distance=1, value diff=|11-9|=2 <= valueDiff=2'
#     }
# ]
#
# for i, test in enumerate(test_cases_220_detailed, 1):
#     nums = test['nums']
#     indexDiff = test['indexDiff']
#     valueDiff = test['valueDiff']
#     expected = test['expected']
#     explanation = test['explanation']
#
#     result = containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)
#     status = "✅ PASS" if result == expected else "❌ FAIL"
#
#     print(f"Test {i}:")
#     print(f"  Input: nums={nums}, indexDiff={indexDiff}, valueDiff={valueDiff}")
#     print(f"  Expected: {expected}")
#     print(f"  Got: {result}")
#     print(f"  Status: {status}")
#     print(f"  Explanation: {explanation}")
#     print()
#
# print("=" * 70)
# print("VISUAL EXAMPLES:")
# print("=" * 70)


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 1: LeetCode 438 - Find All Anagrams in a String
# ============================================================================

"""
Problem:
--------
Given two strings s and p, return an array of all the start indices of 
p's anagrams in s.

An Anagram is a word formed by rearranging the letters of a different word.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation: 
The substring "cba" at index 0 is an anagram of "abc"
The substring "bac" at index 6 is an anagram of "abc"

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters
"""
def findAnagrams(arr, target):
    """
    Approach: Fixed sliding window with frequency map

    Key Insight:
    - An anagram has the SAME character frequencies as the original
    - Use a FIXED window of size len(p) and slide it across s
    - Compare character frequencies in the window with p's frequencies
    - Use two hashmaps: one for p (target), one for current window
    - Use a counter to track how many unique characters are satisfied
    - When all characters are satisfied, we found an anagram!
    - Record the starting index of each valid window
    - The key is: maintain FIXED window size = len(p), check if frequencies match

    Time: O(|s|)
    Space: O(1) - at most 26 letters
    """
    if len(arr) < len(target):
        return []

    left = 0
    target_hmap = {}
    source_hmap = {}
    matching_count = 0
    return_array = []

    # add all the elements in the target hashmap
    i = 0
    while i < len(target):
        target_hmap[ target[i] ] = target_hmap.get(target[i],0)+1
        i += 1

    # add all the elements frmo source into hashmap
    # and while the elelments, check if the frequency matches
    k=0
    while k < len(target):
       source_hmap[arr[k]] = source_hmap.get(arr[k], 0) + 1

       if ( source_hmap[ arr[k] ] == target_hmap[target[k]]):
           matching_count += 1

           if matching_count == len(target_hmap):
               return_array.append(0)
       k += 1

    right = k

    while right < len(arr):
        # iterate through the remaining parts of arr add elements into source_hmap
        source_hmap[arr[right]] = source_hmap.get(arr[right], 0) + 1

        if source_hmap[arr[right]] in target_hmap:
            if (source_hmap[arr[right]] == target_hmap[target[right]]):
                matching_count += 1
            if (source_hmap[arr[right]] == target_hmap[target[right]] + 1):
                matching_count -= 1

        if source_hmap[arr[left]] in target_hmap:
            if (source_hmap[arr[left]] == target_hmap[target[left]]):
                matching_count -= 1
            if (source_hmap[arr[left]] == target_hmap[target[left]] + 1):
                matching_count += 1


        source_hmap[arr[left]] -= 1
        if source_hmap[arr[left]] == 0:
            del source_hmap[arr[left]]

        if matching_count == len(target) :
            return_array.append(left+1)


        left +=1
        right += 1

    return return_array



def findAnagrams_simple_approach(arr, target):
    """
    Approach: Fixed sliding window with frequency map

    Key Insight:
    - An anagram has the SAME character frequencies as the original
    - Use a FIXED window of size len(p) and slide it across s
    - Compare character frequencies in the window with p's frequencies
    - Use two hashmaps: one for p (target), one for current window
    - Use a counter to track how many unique characters are satisfied
    - When all characters are satisfied, we found an anagram!
    - Record the starting index of each valid window
    - The key is: maintain FIXED window size = len(p), check if frequencies match

    Time: O(|s|)
    Space: O(1) - at most 26 letters
    """
    if len(arr) < len(target):
        return []

    left = 0
    target_hmap = {}
    source_hmap = {}
    return_array = []

    # add all the elements in the target hashmap
    i = 0
    while i < len(target):
        target_hmap[target[i]] = target_hmap.get(target[i], 0)+1
        i += 1

    # add all the elements frmo source into hashmap
    # and while the elelments, check if the frequency matches
    k=0
    while k < len(target):
       source_hmap[arr[k]] = source_hmap.get(arr[k], 0) + 1
       k += 1

    # this is an expensive operation.
    if source_hmap == target_hmap:
        print(source_hmap)
        print(target_hmap)
        return_array.append(0)

    right = k

    while right < len(arr):
         source_hmap[arr[right]] = source_hmap.get(arr[right], 0) + 1

         source_hmap[arr[left]] -= 1
         if source_hmap[arr[left]] == 0:
             del source_hmap[arr[left]]

         left += 1
         right += 1


         # this is an expensive operation.
         if source_hmap == target_hmap:
             return_array.append(left)

    return return_array


# Test cases
print("=" * 70)
print("Problem 1: LeetCode 438 - Find All Anagrams in a String")
print("=" * 70)
test_cases_438 = [
    ("cbaebabacd", "abc"),
    ("abab", "ab"),
    ("baa", "aa"),
    ("aaaaaaaaaa", "aaaaaaaaaaaaa")
]

# for s, p in test_cases_438:
#     result = findAnagrams_simple_approach(s, p)
#     print(f"s: '{s}', p: '{p}'")
#     print(f"Result: {result}\n")


# HIGHEST FREQUENCY (Must Know for Interviews) - FAANG HARD PROBLEMS
# ============================================================================
# PROBLEM 3: LeetCode 30 - Substring with Concatenation of All Words
# ============================================================================

"""
Problem:
--------
You are given a string s and an array of strings words. All the strings 
of words are of the same length.

A concatenated substring in s is a substring that contains all the 
strings of any permutation of words concatenated.

Return the starting indices of all the concatenated substrings in s.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: 
Substrings starting at index 0 is "barfoo" (permutation of ["bar","foo"])
Substrings starting at index 9 is "foobar" (permutation of ["foo","bar"])

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:
- 1 <= s.length <= 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- s and words[i] consist of lowercase English letters
"""


def findSubstring(arr, words):
    """
    Approach: Fixed sliding window with word-level frequency matching

    Key Insight:
    - This is like "Find All Anagrams" but with WORDS instead of characters
    - Each word has the same length, so we can treat them as units
    - We need to find all substrings that contain ALL words (in any order)
    - Use a hashmap to track required word frequencies
    - Use another hashmap to track current window word frequencies
    - Window size is FIXED: len(words) * word_length
    - Slide the window word by word (not character by character)
    - For efficiency, we try starting from each position in [0, word_length)
    - The key is: treat words as atomic units, match their frequencies with FIXED window

    Time: O(n * word_length) where n = len(s)
    Space: O(m) where m = number of unique words
    """
    #initialize

    source_hmap = {}
    words_hmap = {}

    result = []

    word_length = len(words[0])
    word_count = len(words)

    if len(s) < word_length * word_count:
        return []

    # fill in the words elements into words_hmap
    i=0
    while i < len(words) :
        words_hmap[ words[i] ] = words_hmap.get( words[i], 0 ) + 1
        i += 1

    start_pos = 0
    while start_pos < word_length:
        # Initialize for this starting position
        left = start_pos
        right = start_pos
        source_hmap = {}
        matching_count = 0

        while( right + word_length < len(arr)):
              current_word_in_source = arr[ right : right + word_length]

              if current_word_in_source in words_hmap:
                  source_hmap[current_word_in_source] = source_hmap.get(current_word_in_source, 0) + 1
                  matching_count += 1

                  while source_hmap[current_word_in_source] > words_hmap[current_word_in_source]:
                      leftmost_word_in_source = arr[left:left + word_length]
                      source_hmap[leftmost_word_in_source] -= 1
                      if source_hmap[leftmost_word_in_source] == 0:
                          del source_hmap[leftmost_word_in_source]
                      matching_count -= 1
                      left += word_length

                  if matching_count == len(words):
                      result.append(left)
                      leftmost_word_in_source = arr[left:left+word_length]
                      source_hmap[leftmost_word_in_source] -= 1
                      if source_hmap[leftmost_word_in_source] == 0:
                        del source_hmap[leftmost_word_in_source]
                      matching_count -= 1
                      left += word_length

              else:
                  source_hmap.clear()
                  matching_count = 0
                  left = right+word_length

              right += word_length

        start_pos += 1
    return result

# Test cases
print("=" * 70)
print("Problem 3: LeetCode 30 - Substring with Concatenation of All Words (HARD)")
print("=" * 70)
test_cases_30 = [
    ("barfoothefoobarman", ["foo", "bar"]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
    ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
    ("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"])
]

# for s, words in test_cases_30:
#     result = findSubstring(s, words)
#     print(f"s: '{s}'")
#     print(f"words: {words}")
#     print(f"Result: {result}\n")
