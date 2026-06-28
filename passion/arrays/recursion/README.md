# Recursion & Backtracking Problems

A comprehensive collection of recursion and backtracking problems with detailed solutions, key insights, and test cases.

## 📚 Table of Contents
- [Pattern Templates](#pattern-templates)
- [Easy Problems](#easy-problems)
- [Medium Problems](#medium-problems)
- [Hard Problems](#hard-problems)
- [Problem Statistics](#problem-statistics)

---

## Pattern Templates

### 1. Basic Recursion Template
- Divide problem into smaller subproblems
- Base case to stop recursion
- Recursive case with modified parameters

### 2. Backtracking Template
- "Choose, Explore, Unchoose" pattern
- Build solutions incrementally
- Prune invalid paths early

---

## Easy Problems

### Problem 1: Fibonacci Number (LC 509)
- **Difficulty**: Easy
- **Approaches**: Recursive, Memoized, Iterative
- **Key Concept**: Classic recursion example, memoization optimization
- **Time Complexity**: O(2^n) naive, O(n) with memoization
- **Space Complexity**: O(n) for memoization

### Problem 2: Climbing Stairs (LC 70)
- **Difficulty**: Easy
- **Pattern**: Fibonacci variant
- **Key Concept**: Each step has 2 choices (1 or 2 steps)
- **Time Complexity**: O(n) with memoization
- **Space Complexity**: O(n)

### Problem 3: Merge Two Sorted Lists (LC 21)
- **Difficulty**: Easy
- **Pattern**: Recursive linked list manipulation
- **Key Concept**: Compare heads and merge recursively
- **Time Complexity**: O(n + m)
- **Space Complexity**: O(n + m) for recursion stack

---

## Medium Problems

### Problem 4: Permutations (LC 46)
- **Difficulty**: Medium
- **Pattern**: Backtracking - Generate all arrangements
- **Key Concept**: Choose, explore, unchoose pattern
- **Time Complexity**: O(n * n!)
- **Space Complexity**: O(n * n!)
- **FAANG Frequency**: High

### Problem 5: Combinations (LC 77)
- **Difficulty**: Medium
- **Pattern**: Backtracking - Choose k from n
- **Key Concept**: Use start index to avoid duplicates
- **Time Complexity**: O(k * C(n,k))
- **Space Complexity**: O(k * C(n,k))
- **FAANG Frequency**: High

### Problem 6: Subsets (LC 78)
- **Difficulty**: Medium
- **Pattern**: Backtracking - Power set generation
- **Key Concept**: Binary decision tree (include/exclude)
- **Time Complexity**: O(n * 2^n)
- **Space Complexity**: O(n * 2^n)
- **FAANG Frequency**: Very High (Amazon, Google, Facebook)

### Problem 7: Combination Sum (LC 39)
- **Difficulty**: Medium
- **Pattern**: Backtracking with sum constraint
- **Key Concept**: Elements can be reused unlimited times
- **Time Complexity**: O(N^(T/M)) where T=target, M=min value
- **Space Complexity**: O(T/M)
- **FAANG Frequency**: High (Amazon, Microsoft)

### Problem 8: Generate Parentheses (LC 22)
- **Difficulty**: Medium
- **Pattern**: Backtracking with balance tracking
- **Key Concept**: Track open/close counts, add only when valid
- **Time Complexity**: O(4^n / √n) - Catalan number
- **Space Complexity**: O(n)
- **FAANG Frequency**: Very High (Google, Facebook)

### Problem 14: Permutations II (LC 47)
- **Difficulty**: Medium
- **Pattern**: Backtracking with duplicate handling
- **Key Concept**: Sort first, skip duplicates in same position
- **Time Complexity**: O(n * n!)
- **Space Complexity**: O(n * n!)
- **FAANG Frequency**: Medium

### Problem 15: Subsets II (LC 90)
- **Difficulty**: Medium
- **Pattern**: Backtracking with duplicate handling
- **Key Concept**: Sort first, skip duplicate elements
- **Time Complexity**: O(n * 2^n)
- **Space Complexity**: O(n * 2^n)
- **FAANG Frequency**: Medium

### Problem 16: Combination Sum II (LC 40)
- **Difficulty**: Medium
- **Pattern**: Backtracking - each element used once
- **Key Concept**: Sort and skip duplicates, no reuse
- **Time Complexity**: O(2^n)
- **Space Complexity**: O(target)
- **FAANG Frequency**: High (Amazon)

### Problem 17: Combination Sum III (LC 216)
- **Difficulty**: Medium
- **Pattern**: Backtracking with size and sum constraints
- **Key Concept**: Exactly k numbers from 1-9 that sum to n
- **Time Complexity**: O(C(9,k))
- **Space Complexity**: O(k)
- **FAANG Frequency**: Medium

### Problem 18: Palindrome Partitioning (LC 131)
- **Difficulty**: Medium
- **Pattern**: Backtracking with string partitioning
- **Key Concept**: Check palindrome for each substring
- **Time Complexity**: O(n * 2^n)
- **Space Complexity**: O(n)
- **FAANG Frequency**: High (Amazon, Google)

### Problem 19: Letter Combinations of Phone Number (LC 17)
- **Difficulty**: Medium
- **Pattern**: Backtracking with mapping
- **Key Concept**: Each digit maps to 3-4 letters
- **Time Complexity**: O(4^n)
- **Space Complexity**: O(n)
- **FAANG Frequency**: Very High (Amazon, Google, Facebook)

### Problem 20: Restore IP Addresses (LC 93)
- **Difficulty**: Medium
- **Pattern**: Backtracking with segment validation
- **Key Concept**: 4 segments, each 0-255, no leading zeros
- **Time Complexity**: O(1) - constant (3^4 = 81 max)
- **Space Complexity**: O(1)
- **FAANG Frequency**: Medium (Amazon)

### Problem 21: Beautiful Arrangement (LC 526)
- **Difficulty**: Medium
- **Pattern**: Backtracking with mathematical constraints
- **Key Concept**: Divisibility constraint at each position
- **Time Complexity**: O(k) where k = valid permutations
- **Space Complexity**: O(n)
- **FAANG Frequency**: Low

---

## Hard Problems

### Problem 9: N-Queens (LC 51)
- **Difficulty**: Hard
- **Pattern**: Constraint satisfaction with backtracking
- **Key Concept**: Track columns and diagonals with sets
- **Time Complexity**: O(N!) with pruning
- **Space Complexity**: O(N)
- **FAANG Frequency**: Very High (Google, Amazon, Facebook)
- **Classic Problem**: Yes

### Problem 10: Sudoku Solver (LC 37)
- **Difficulty**: Hard
- **Pattern**: Constraint satisfaction - grid backtracking
- **Key Concept**: Check row, column, and 3x3 box constraints
- **Time Complexity**: O(9^M) where M = empty cells
- **Space Complexity**: O(M)
- **FAANG Frequency**: High (Amazon, Google)
- **Classic Problem**: Yes

### Problem 11: Word Search (LC 79)
- **Difficulty**: Medium/Hard
- **Pattern**: DFS backtracking on 2D grid
- **Key Concept**: Mark visited, explore 4 directions, restore
- **Time Complexity**: O(M*N*4^L) where L = word length
- **Space Complexity**: O(L)
- **FAANG Frequency**: Very High (Amazon, Microsoft, Facebook)

### Problem 12: Word Search II (LC 212)
- **Difficulty**: Hard
- **Pattern**: Trie + DFS backtracking
- **Key Concept**: Build Trie for all words, search once
- **Time Complexity**: O(M*N*4^L)
- **Space Complexity**: O(total characters in words)
- **FAANG Frequency**: Very High (Amazon, Google)
- **Advanced Technique**: Trie data structure

### Problem 13: Remove Invalid Parentheses (LC 301)
- **Difficulty**: Hard
- **Pattern**: BFS + validation
- **Key Concept**: Find minimum removals using BFS
- **Time Complexity**: O(2^n) worst case
- **Space Complexity**: O(n * unique results)
- **FAANG Frequency**: High (Facebook, Google)

### Problem 22: Word Break II (LC 140)
- **Difficulty**: Hard
- **Pattern**: Backtracking with memoization
- **Key Concept**: Segment string into dictionary words
- **Time Complexity**: O(n * 2^n) with memoization
- **Space Complexity**: O(n * k) where k = valid segmentations
- **FAANG Frequency**: High (Amazon, Google)

### Problem 23: Expression Add Operators (LC 282)
- **Difficulty**: Hard
- **Pattern**: Backtracking with expression evaluation
- **Key Concept**: Handle operator precedence (especially *)
- **Time Complexity**: O(4^n)
- **Space Complexity**: O(n)
- **FAANG Frequency**: Medium (Google, Facebook)

### Problem 24: Palindrome Partitioning II (LC 132)
- **Difficulty**: Hard
- **Pattern**: Dynamic Programming + Palindrome checking
- **Key Concept**: Precompute palindromes, DP for min cuts
- **Time Complexity**: O(n^2)
- **Space Complexity**: O(n^2)
- **FAANG Frequency**: Medium

### Problem 25: Concatenated Words (LC 472)
- **Difficulty**: Hard
- **Pattern**: Recursion with set lookup and memoization
- **Key Concept**: Check if word can be formed by other words
- **Time Complexity**: O(n * L^2) where L = avg word length
- **Space Complexity**: O(n)
- **FAANG Frequency**: Medium (Amazon)

---

## Problem Statistics

### By Difficulty
- **Easy**: 3 problems
- **Medium**: 13 problems
- **Hard**: 9 problems
- **Total**: 25 problems

### By Pattern
- **Basic Recursion**: 3 problems
- **Permutations/Combinations**: 7 problems
- **Subsets**: 2 problems
- **Grid-based Backtracking**: 3 problems
- **String Segmentation**: 3 problems
- **Constraint Satisfaction**: 3 problems
- **Expression Building**: 1 problem
- **Advanced (Trie/DP hybrid)**: 3 problems

### FAANG Frequency
- **Very High**: 8 problems (Subsets, Generate Parentheses, Letter Combinations, N-Queens, Word Search, Word Search II, etc.)
- **High**: 10 problems
- **Medium**: 6 problems
- **Low**: 1 problem

### Classic Interview Problems
- N-Queens
- Sudoku Solver
- Subsets
- Permutations
- Generate Parentheses
- Word Search
- Combination Sum

---

## Key Concepts Covered

### Recursion Fundamentals
- Base cases and recursive cases
- Memoization for optimization
- Recursion to iteration transformation

### Backtracking Patterns
- Choose, Explore, Unchoose
- State management and restoration
- Pruning invalid paths
- Duplicate handling (sorting + skipping)

### Advanced Techniques
- Trie data structure integration
- Dynamic Programming with recursion
- Constraint satisfaction
- BFS for minimum solutions
- Mathematical constraints (divisibility)

### Optimization Strategies
- Memoization to avoid recomputation
- Early pruning with constraints
- Set-based lookups for O(1) checks
- Precomputation (palindromes, etc.)

---

## Usage

All problems include:
- ✅ Detailed problem statement
- ✅ Multiple approaches where applicable
- ✅ Comprehensive "Key Insight" explanations
- ✅ Time and space complexity analysis
- ✅ Test cases with edge cases
- ✅ While loop implementations (no for loops)

## Files
- `recursion_solutions.py` - Complete solutions with explanations
- `recursion_practise.py` - Practice file for implementing solutions

---

## Study Recommendations

### Week 1-2: Fundamentals
1. Fibonacci Number (LC 509)
2. Climbing Stairs (LC 70)
3. Merge Two Sorted Lists (LC 21)

### Week 3-4: Core Backtracking
4. Permutations (LC 46)
5. Combinations (LC 77)
6. Subsets (LC 78)
7. Combination Sum (LC 39)

### Week 5-6: Advanced Backtracking
8. Generate Parentheses (LC 22)
9. Permutations II (LC 47)
10. Subsets II (LC 90)
11. Palindrome Partitioning (LC 131)
12. Letter Combinations (LC 17)

### Week 7-8: Hard Problems
13. N-Queens (LC 51)
14. Sudoku Solver (LC 37)
15. Word Search (LC 79)
16. Word Search II (LC 212)

### Week 9+: Expert Level
17. Remove Invalid Parentheses (LC 301)
18. Word Break II (LC 140)
19. Expression Add Operators (LC 282)

---

## Tips for Success

1. **Master the Template**: Understand the "choose, explore, unchoose" pattern
2. **Draw the Tree**: Visualize the recursion tree for each problem
3. **Start Simple**: Begin with base cases and build up
4. **Practice Variations**: Solve problems with/without duplicates
5. **Optimize Later**: Get the brute force working first, then optimize
6. **Test Edge Cases**: Empty input, single element, all same, etc.

---

*Last Updated: January 2026*
