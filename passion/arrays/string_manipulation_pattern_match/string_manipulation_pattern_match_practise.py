# ============================================================================
# PROBLEM 1: LeetCode 242 - Valid Anagram (EASY)
# ============================================================================

"""
Problem:
--------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters

Follow up: What if the inputs contain Unicode characters?
"""


def isAnagram(arr, target):
    """
    Approach: Character Frequency Hash Map

    Key Insight:
    - Two strings are anagrams if they have EXACTLY the same character frequencies
    - We can use a hash map to count character occurrences
    - Compare the two frequency maps for equality
    - Alternative: Sort both strings and compare (O(n log n))
    - Hash map approach is O(n) which is optimal

    Why This Works:
    - Anagrams have same letters, just rearranged
    - If frequencies match, strings are anagrams
    - Dictionary equality in Python compares both keys and values

    Edge Cases:
    - Different lengths → immediately return False
    - Empty strings → both empty means True
    - Single character → check if same

    Algorithm:
    1. Quick check: if lengths differ, return False
    2. Build frequency map for string s
    3. Build frequency map for string t
    4. Compare the two maps

    Optimization:
    - Can use single map: increment for s, decrement for t
    - If all values are 0 at end, it's an anagram
    - Or use Counter from collections module

    Pattern Recognition:
    - "rearrange letters" → frequency counting
    - "same letters" → hash map comparison
    - "anagram" keyword → character frequency

    Time: O(n) where n = len(s) + len(t)
    Space: O(1) - at most 26 lowercase letters
    """
    if len(arr) != len(target):
        return False

    i=0
    source_hmap = {}
    target_hmap = {}

    while( i<len(arr) ):
        source_hmap[ arr[i] ] = source_hmap.get( arr[i], 0) + 1
        target_hmap[target[i]] = target_hmap.get(target[i], 0) + 1
        i+=1

    return True if source_hmap == target_hmap else False


# Test cases
print("\n" + "=" * 70)
print("Problem 1: LeetCode 242 - Valid Anagram")
print("=" * 70)

test_cases_242 = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "a", True),
    ("ab", "ba", True),
    ("abc", "def", False)
]

# for s, t, expected in test_cases_242:
#     result = isAnagram(s, t)
#     status = "✅" if result == expected else "❌"
#     print(f"s='{s}', t='{t}' → {result} (expected: {expected}) {status}")

# ============================================================================
# PROBLEM 2: LeetCode 387 - First Unique Character in a String (EASY)
# ============================================================================

"""
Problem:
--------
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.
 
Example 1:
Input: s = "leetcode"
Output: 0
Explanation: 'l' is the first character that appears only once

Example 2:
Input: s = "loveleetcode"
Output: 2
Explanation: 'v' is the first non-repeating character

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters
"""


def firstUniqChar(arr):
    """
    Approach: Two-Pass with Frequency Map

    Key Insight:
    - Need to find FIRST character that appears only once
    - Two-pass approach: count frequencies, then find first with count=1
    - Can't do in single pass because we need to know total counts
    - Hash map stores character frequencies
    - Second pass finds first character with frequency 1

    Why Two Passes?
    - First pass: Build complete frequency map
    - Second pass: Find first char with freq=1 in original order
    - Order matters! We need the FIRST unique character

    Algorithm:
    1. First pass: Count frequency of each character
    2. Second pass: Iterate through string, return index of first char with freq=1
    3. If no unique character found, return -1

    Alternative Approaches:
    - Use array of size 26 for lowercase letters (slightly faster)
    - Use OrderedDict to maintain insertion order
    - Use two sets: seen_once and seen_multiple

    Pattern Recognition:
    - "first non-repeating" → frequency map + order preservation
    - "unique character" → count occurrences
    - Need to maintain original order → iterate string, not map

    Time: O(n) - two passes through string
    Space: O(1) - at most 26 lowercase letters
    """
    i = 0
    source_hmap = {}

    while( i < len(arr) ):
        source_hmap[arr[i]] = source_hmap.get(arr[i], 0) + 1
        i+=1

    i=0
    while( i < len(arr) ):
        if source_hmap[arr[i]] == 1:
            return i
        i += 1

    return -1

# Test cases
print("\n" + "=" * 70)
print("Problem 2: LeetCode 387 - First Unique Character in a String")
print("=" * 70)

test_cases_387 = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
    ("z", 0),
    ("aabbcc", -1)
]

# for s, expected in test_cases_387:
#     result = firstUniqChar(s)
#     status = "✅" if result == expected else "❌"
#     print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 3: LeetCode 125 - Valid Palindrome (EASY)
# ============================================================================

"""
Problem:
--------
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome

Example 3:
Input: s = " "
Output: true
Explanation: Empty string is palindrome

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters
"""


def isPalindrome(arr):
    """
    Approach: Two Pointers with Character Filtering

    Key Insight:
    - Use two pointers from opposite ends
    - Skip non-alphanumeric characters
    - Compare characters case-insensitively
    - No need to create new string (space efficient)
    - Move pointers inward, skipping invalid chars

    Why Two Pointers?
    - O(n) time with O(1) space
    - Don't need to create filtered string
    - Can check on-the-fly while moving pointers
    - More efficient than reversing and comparing

    Algorithm:
    1. Initialize left=0, right=len(s)-1
    2. While left < right:
       a. Skip non-alphanumeric from left
       b. Skip non-alphanumeric from right
       c. Compare characters (case-insensitive)
       d. If mismatch, return False
       e. Move both pointers inward
    3. Return True if all characters matched

    Edge Cases:
    - Empty string → True
    - Single character → True
    - All spaces/punctuation → True
    - Mixed case → convert to same case

    Pattern Recognition:
    - "reads same forward and backward" → palindrome → two pointers
    - "ignore non-alphanumeric" → filtering while iterating
    - "case-insensitive" → convert to lowercase

    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not arr[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not arr[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if arr[left].lower() != arr[right].lower():
            return False

        left += 1
        right -= 1

    return True



# Test cases
print("\n" + "=" * 70)
print("Problem 3: LeetCode 125 - Valid Palindrome")
print("=" * 70)

test_cases_125 = [
    # ("A man, a plan, a canal: Panama", True),
    # ("race a car", False),
    # (" ", True),
    # ("a", True),
    # ("ab", False),
    (".,", True)
]

# for s, expected in test_cases_125:
#     result = isPalindrome(s)
#     status = "✅" if result == expected else "❌"
#     print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 4: LeetCode 28 - Find the Index of the First Occurrence (EASY)
# ============================================================================

"""
Problem:
--------
Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. First occurrence is at index 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode"

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters
"""


def strStr(arr, target):
    """
    Approach: Sliding Window / Brute Force

    Key Insight:
    - Check every possible starting position in haystack
    - For each position, check if needle matches
    - Can use Python's built-in 'in' operator, but let's implement manually
    - Sliding window of size len(needle) through haystack
    - KMP algorithm is O(n+m) but overkill for this problem

    Why This Approach?
    - Simple and intuitive
    - Works well for small strings
    - Python string slicing is optimized
    - For interviews, brute force is acceptable unless asked to optimize

    Algorithm:
    1. Edge case: if needle is empty, return 0
    2. Iterate through haystack up to (len(haystack) - len(needle) + 1)
    3. At each position, check if substring matches needle
    4. Return index if match found
    5. Return -1 if no match

    Optimization:
    - Can use KMP (Knuth-Morris-Pratt) for O(n+m) worst case
    - Can use Rabin-Karp with rolling hash
    - For most cases, brute force is sufficient

    Pattern Recognition:
    - "find first occurrence" → sliding window or pattern matching
    - "substring search" → iterate and compare
    - Can optimize with KMP if needed

    Time: O(n*m) worst case, where n=len(haystack), m=len(needle)
    Space: O(1)
    """
    if len(arr) < len(target):
        return -1

    left = 0
    right = len(target)
    hmap = {}

    while ( right <= len(arr) ):
        hmap[ arr[left:right] ] = hmap.get( arr[left:right], 0 ) + 1

        if target in hmap:
            return left

        left+=1
        right+=1

    return -1


# Test cases
print("\n" + "=" * 70)
print("Problem 4: LeetCode 28 - Find the Index of the First Occurrence")
print("=" * 70)

test_cases_28 = [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ("hello", "ll", 2),
    ("aaaaa", "bba", -1),
    ("", "", 0),
    ("a", "a", 0)
]

# for haystack, needle, expected in test_cases_28:
#     result = strStr(haystack, needle)
#     status = "✅" if result == expected else "❌"
#     print(f"haystack='{haystack}', needle='{needle}' → {result} (expected: {expected}) {status}")

# ============================================================================
# PROBLEM 5: LeetCode 392 - Is Subsequence (EASY)
# ============================================================================

"""
Problem:
--------
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative 
positions of the remaining characters.

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters

Follow up: If there are lots of incoming s, how would you optimize?
"""


def isSubsequence(s, t):
    """
    Approach: Two Pointers

    Key Insight:
    - Subsequence means characters appear in same order, but not necessarily consecutive
    - Use two pointers: one for s, one for t
    - Move pointer in t always, move pointer in s only when characters match
    - If we reach end of s, all characters were found in order
    - This is greedy: match as soon as we find the character

    Why Two Pointers?
    - O(n) time where n = len(t)
    - O(1) space
    - Simple and efficient
    - Greedy approach works because we just need any valid subsequence

    Algorithm:
    1. Initialize i=0 (pointer for s), j=0 (pointer for t)
    2. While both pointers are in bounds:
       a. If s[i] == t[j], move i forward (found match)
       b. Always move j forward
    3. Return True if i == len(s) (all characters of s found)

    Follow-up Optimization:
    - If many queries with different s but same t:
      - Preprocess t: build index map {char: [list of indices]}
      - For each s, use binary search on index lists
      - Time: O(m log n) per query where m=len(s), n=len(t)

    Pattern Recognition:
    - "subsequence" → two pointers
    - "same order" → greedy matching
    - "not consecutive" → skip characters in t

    Time: O(n) where n = len(t)
    Space: O(1)
    """



# Test cases
print("\n" + "=" * 70)
print("Problem 5: LeetCode 392 - Is Subsequence")
print("=" * 70)

test_cases_392 = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "ahbgdc", True),
    ("abc", "", False),
    ("ace", "abcde", True)
]

# for s, t, expected in test_cases_392:
#     result = isSubsequence(s, t)
#     status = "✅" if result == expected else "❌"
#     print(f"s='{s}', t='{t}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 6: LeetCode 383 - Ransom Note (EASY)
# ============================================================================

"""
Problem:
--------
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters
"""


def canConstruct(ransomNote, magazine):
    """
    Approach: Character Frequency Hash Map

    Key Insight:
    - Check if magazine has enough of each character for ransomNote
    - Build frequency map for magazine
    - For each character in ransomNote, check if available
    - Decrement count as we use characters
    - If any character not available, return False

    Why This Works:
    - Each letter can only be used once
    - Frequency map tracks available letters
    - Simple counting problem

    Algorithm:
    1. Build frequency map for magazine
    2. For each character in ransomNote:
       a. Check if character exists in map with count > 0
       b. If yes, decrement count
       c. If no, return False
    3. Return True if all characters found

    Alternative:
    - Use Counter from collections
    - Sort and compare (slower)

    Pattern Recognition:
    - "can construct" → frequency checking
    - "each letter used once" → count availability

    Time: O(m + n) where m=len(ransomNote), n=len(magazine)
    Space: O(1) - at most 26 lowercase letters
    """
    # Build frequency map for magazine

    hmap = {}

    for element in magazine:
        hmap[element] = hmap.get(element,0) +1

    for element in ransomNote:
        if element in hmap:
            hmap[element] -= 1
            if hmap[element] == 0:
                del hmap[element]
        else:
            return False

    return True

# Test cases
print("\n" + "=" * 70)
print("Problem 6: LeetCode 383 - Ransom Note")
print("=" * 70)

test_cases_383 = [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("abc", "aabbcc", True),
    ("", "abc", True)
]

# ============================================================================
# PROBLEM 8: LeetCode 680 - Valid Palindrome II (EASY) ⭐⭐
# ============================================================================

"""
Problem:
--------
Given a string s, return true if the s can be palindrome after deleting at most 
one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'

Example 3:
Input: s = "abc"
Output: false

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters
"""


def validPalindrome(s):
    """
    Approach: Two Pointers with One Skip

    Key Insight:
    - Use two pointers from both ends
    - When mismatch found, try skipping either left or right character
    - Check if remaining substring is palindrome
    - Only one skip allowed
    - Helper function checks if substring is palindrome

    Why This Works:
    - If string is already palindrome, no skip needed
    - If one mismatch, try both options: skip left or skip right
    - If either option gives palindrome, return True
    - If more than one mismatch needed, return False

    Algorithm:
    1. Use two pointers: left=0, right=len(s)-1
    2. While left < right:
       a. If s[left] == s[right], move both inward
       b. If mismatch, check two options:
          - Is s[left+1...right] a palindrome? (skip left)
          - Is s[left...right-1] a palindrome? (skip right)
       c. Return True if either option works
    3. Return True if no mismatch found

    Helper Function:
    - isPalindrome(left, right): checks if substring is palindrome

    Pattern Recognition:
    - "delete at most one" → try both skip options
    - "palindrome" → two pointers
    - "after deleting" → check remaining substring

    Time: O(n)
    Space: O(1)
    """

    def isPalindrome(left, right):
        """Check if substring s[left...right] is palindrome"""
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping either left or right character
            return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
        left += 1
        right -= 1

    return True


# Test cases
print("\n" + "=" * 70)
print("Problem 8: LeetCode 680 - Valid Palindrome II (EASY)")
print("=" * 70)

test_cases_680 = [
    ("aba", True),
    ("abca", True),
    ("abc", False),
    ("racecar", True),
    ("deeee", True),
    ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True)
]

# for s, expected in test_cases_680:
#     result = validPalindrome(s)
#     status = "✅" if result == expected else "❌"
#     print(f"s='{s[:20]}...' → {result} (expected: {expected}) {status}")

# ============================================================================
# PROBLEM 8: LeetCode 680 - Valid Palindrome II (EASY) ⭐⭐
# ============================================================================

"""
Problem:
--------
Given a string s, return true if the s can be palindrome after deleting at most 
one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'

Example 3:
Input: s = "abc"
Output: false

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters
"""


def validPalindrome(arr):
    """
    Approach: Two Pointers with One Skip

    Key Insight:
    - Use two pointers from both ends
    - When mismatch found, try skipping either left or right character
    - Check if remaining substring is palindrome
    - Only one skip allowed
    - Helper function checks if substring is palindrome

    Why This Works:
    - If string is already palindrome, no skip needed
    - If one mismatch, try both options: skip left or skip right
    - If either option gives palindrome, return True
    - If more than one mismatch needed, return False

    Algorithm:
    1. Use two pointers: left=0, right=len(s)-1
    2. While left < right:
       a. If s[left] == s[right], move both inward
       b. If mismatch, check two options:
          - Is s[left+1...right] a palindrome? (skip left)
          - Is s[left...right-1] a palindrome? (skip right)
       c. Return True if either option works
    3. Return True if no mismatch found

    Helper Function:
    - isPalindrome(left, right): checks if substring is palindrome

    Pattern Recognition:
    - "delete at most one" → try both skip options
    - "palindrome" → two pointers
    - "after deleting" → check remaining substring

    Time: O(n)
    Space: O(1)
    """

    left = 0
    right = len(arr) - 1
    count = 0

    def is_valid_palindrome(arr,left,right):
        while left < right:
            if arr[left] == arr[right]  :
                left += 1
                right -= 1
            else:
                return False

        return True


    while left < right:
        if arr[left] == arr[right]  :
            left += 1
            right -= 1
        else:
            if   is_valid_palindrome(arr,left+1,right) :
                return True
            elif  is_valid_palindrome(arr,left,right-1) :
                return True
            else:
                return False

    return True



# Test cases
print("\n" + "=" * 70)
print("Problem 8: LeetCode 680 - Valid Palindrome II (EASY)")
print("=" * 70)

test_cases_680 = [
    ("aba", True),
    ("abca", True),
    ("abc", False),
    ("racecar", True),
    ("deeee", True),
    ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True)
]
#
# for s, expected in test_cases_680:
#     result = validPalindrome(s)
#     status = "✅" if result == expected else "❌"
#     print(f"s='{s[:20]}...' → {result} (expected: {expected}) {status}")

# ============================================================================
# MEDIUM PROBLEMS - CORE INTERVIEW QUESTIONS
# ============================================================================

print("\n\n" + "=" * 70)
print("MEDIUM PROBLEMS - FAANG FAVORITES")
print("=" * 70)

# ============================================================================
# PROBLEM 9: LeetCode 49 - Group Anagrams (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters
"""


def groupAnagrams(arr):
    """
    Approach: Hash Map with Sorted String as Key

    Key Insight:
    - Anagrams have same characters, just rearranged
    - If we sort the characters, anagrams become identical
    - Use sorted string as key in hash map
    - All anagrams will map to same key
    - Group strings by their sorted representation

    Why Sorted String as Key?
    - Anagrams produce same sorted string
    - Example: "eat", "tea", "ate" all become "aet"
    - Hash map groups all strings with same sorted form
    - Alternative: Use character frequency tuple as key

    Algorithm:
    1. Create hash map: {sorted_string: [list of original strings]}
    2. For each string:
       a. Sort the string to get key
       b. Add original string to list for that key
    3. Return all values (lists of anagrams)

    Alternative Approach:
    - Use character count tuple as key
    - Count = tuple of 26 integers for a-z
    - Slightly faster than sorting for long strings

    Pattern Recognition:
    - "group anagrams" → hash map with canonical form
    - "same letters" → sorting or frequency counting
    - "group together" → hash map values are lists

    Time: O(n * k log k) where n = number of strings, k = max length
    Space: O(n * k) for storing all strings
    """
    hmap = {}

    for index, element in enumerate(arr):
        sorted_element = ''.join( sorted(element) )

        if sorted_element not in hmap:
           hmap[sorted_element] = []
        hmap[sorted_element].append(element)

    return [ hmap[element] for element in hmap]


# Test cases
print("\n" + "=" * 70)
print("Problem 6: LeetCode 49 - Group Anagrams (MEDIUM)")
print("=" * 70)

test_cases_49 = [
    (["eat", "tea", "tan", "ate", "nat", "bat"],
     [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    ([""], [[""]]),
    (["a"], [["a"]])
]

# for strs, expected in test_cases_49:
#     result = groupAnagrams(strs)
#     # Sort for comparison (order doesn't matter)
#     result_sorted = [sorted(group) for group in result]
#     expected_sorted = [sorted(group) for group in expected]
#     result_sorted.sort()
#     expected_sorted.sort()
#     status = "✅" if result_sorted == expected_sorted else "❌"
#     print(f"Input: {strs}")
#     print(f"Output: {result} {status}")
#     print()

# ============================================================================
# PROBLEM 10: LeetCode 451 - Sort Characters By Frequency (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.

Constraints:
- 1 <= s.length <= 5 * 10^5
- s consists of uppercase and lowercase English letters and digits
"""


def frequencySort(arr):
    """
    Approach: Frequency Map + Bucket Sort

    Key Insight:
    - Count character frequencies using hash map
    - Sort characters by frequency (descending)
    - Build result string with characters repeated by frequency
    - Can use bucket sort for O(n) time instead of O(n log n) sorting

    Why Bucket Sort?
    - Frequency range is [1, n] where n = len(s)
    - Create buckets for each frequency
    - Bucket[i] contains all characters with frequency i
    - Iterate buckets from high to low frequency

    Algorithm:
    1. Build frequency map: {char: count}
    2. Create buckets: bucket[freq] = [list of chars with this freq]
    3. Iterate buckets from len(s) down to 1
    4. For each bucket, append chars * frequency to result

    Alternative:
    - Sort by frequency using sorted() - O(n log n)
    - Use heap - O(n log k) where k = unique chars

    Pattern Recognition:
    - "sort by frequency" → frequency map + sorting
    - "decreasing order" → reverse sort
    - Can optimize with bucket sort

    Time: O(n) with bucket sort, O(n log n) with regular sort
    Space: O(n)
    """
    # Count frequencies

    hmap = {}
    for element in arr:
        hmap[element] = hmap.get(element, 0) + 1

    bucket_hmap = {}
    i=0
    while( i<= len(arr)):
        bucket_hmap[i] = []
        i+=1

    for key ,value in hmap.items():
        bucket_hmap[value].append(key)

    return_str = ""
    i = len(bucket_hmap)-1
    while(i >= 0):
        for element in bucket_hmap[i]:
            return_str +=  element*i
        i-=1

    return return_str


# Test cases
print("\n" + "=" * 70)
print("Problem 9: LeetCode 451 - Sort Characters By Frequency")
print("=" * 70)

test_cases_451 = [
    ("tree", ["eert", "eetr"]),
    ("cccaaa", ["aaaccc", "cccaaa"]),
    ("Aabb", ["bbAa", "bbaA"]),
    ("a", ["a"])
]

# for s, expected_options in test_cases_451:
#     result = frequencySort(s)
#     status = "✅" if result in expected_options else "❌"
#     print(f"s='{s}' → '{result}' (expected one of: {expected_options}) {status}")

# ============================================================================
# PROBLEM 11: LeetCode 1347 - Minimum Steps to Make Two Strings Anagram (MEDIUM)
# ============================================================================

"""
Problem:
--------
You are given two strings of the same length s and t. In one step you can choose 
any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a 
different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with 'b', t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0

Constraints:
- 1 <= s.length <= 5 * 10^4
- s.length == t.length
- s and t consist of lowercase English letters only
"""


def minSteps(s, t):
    """
    Approach: Character Frequency Difference

    Key Insight:
    - Count frequency difference between s and t
    - For each character in s that appears more than in t, we need to add it to t
    - Only count positive differences (chars needed in t)
    - Sum of positive differences = minimum steps

    Why This Works:
    - Anagram means same character frequencies
    - If s has 3 'a's and t has 1 'a', we need 2 more 'a's in t
    - Each replacement is one step
    - Only count what's missing (positive diff)

    Algorithm:
    1. Build frequency map for s
    2. Build frequency map for t
    3. For each character in s:
       - If freq[s] > freq[t], add difference to steps
    4. Return total steps

    Optimization:
    - Can use single pass with one frequency map
    - Increment for s, decrement for t

    Pattern Recognition:
    - "make anagram" → frequency comparison
    - "minimum steps" → count differences
    - "replace characters" → frequency adjustment

    Time: O(n)
    Space: O(1) - at most 26 lowercase letters
    """
    # Count frequencies
    return 0


# Test cases
print("\n" + "=" * 70)
print("Problem 10: LeetCode 1347 - Minimum Steps to Make Anagram")
print("=" * 70)

test_cases_1347 = [
    ("bab", "aba", 1),
    ("leetcode", "practice", 5),
    ("anagram", "mangaar", 0),
    ("abc", "def", 3)
]

# for s, t, expected in test_cases_1347:
#     result = minSteps(s, t)
#     status = "✅" if result == expected else "❌"
#     print(f"s='{s}', t='{t}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 12: LeetCode 395 - Longest Substring with At Least K Repeating (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a string s and an integer k, return the length of the longest substring 
of s such that the frequency of each character in this substring is greater 
than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:
- 1 <= s.length <= 10^4
- s consists of only lowercase English letters
- 1 <= k <= 10^5
"""


def longestSubstring(arr, k):
    """
    Approach: Divide and Conquer

    Key Insight:
    - If a character appears less than k times in entire string, it can't be in valid substring
    - Use such characters as split points
    - Recursively check each split segment
    - Base case: if all characters appear >= k times, return length

    Why Divide and Conquer?
    - Sliding window doesn't work well here (hard to maintain constraint)
    - Characters with freq < k act as "invalid" separators
    - Split string by invalid characters
    - Recursively find longest in each segment

    Algorithm:
    1. Count frequency of all characters
    2. If all chars have freq >= k, return len(s)
    3. Find first character with freq < k
    4. Split string by this character
    5. Recursively check each segment
    6. Return maximum length found

    Alternative:
    - Sliding window with 26 iterations (one for each unique char count)
    - For each target unique count, find longest substring

    Pattern Recognition:
    - "at least k repeating" → frequency checking
    - "longest substring" → divide and conquer or sliding window
    - Characters with low freq split the string

    Time: O(n) average, O(n²) worst case
    Space: O(n) for recursion stack
    """
    if len(arr) < k:
        return 0

    hmap = {}
    i=0
    left = 0
    right = 0
    max_length = 0

    while(i < len(arr)):
        hmap[arr[i]] = hmap.get(arr[i],0) + 1
        i+=1

    while( right < len(arr)):
        if hmap[arr[right]] >= k:
            max_length = max(max_length , right+1 -left)
        elif hmap[arr[right]] < k:
            left = right+1

        right+=1

    return max_length


# Test cases
print("\n" + "=" * 70)
print("Problem 12: LeetCode 395 - Longest Substring At Least K Repeating")
print("=" * 70)

test_cases_395 = [
    # ("aaabb", 3, 3),
    # ("ababbc", 2, 5),
    ("aabcdeffghi", 2, 2),
    # ("aaabbb", 3, 6)
]

for s, k, expected in test_cases_395:
    result = longestSubstring(s, k)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', k={k} → {result} (expected: {expected}) {status}")
