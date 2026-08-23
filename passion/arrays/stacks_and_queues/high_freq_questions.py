"""
====================================================================
  MOST IMPORTANT STACK & QUEUE QUESTIONS FOR FAANG/MANGO INTERVIEWS
====================================================================
  Source: Real interview frequency data (2023-2026) across
  Meta, Apple, Netflix, Google, Amazon, OpenAI, Stripe, Microsoft
  Focus: Google L6 Staff Engineer Level
  Reference: Striver (Take U Forward) Stack & Queue Playlist
====================================================================


====================================================================
  TIER 1 - MUST KNOW (90%+ Interview Frequency)
====================================================================
  These appear in almost EVERY stack/queue-heavy interview round.
  If you only have time for 7 problems, do these.
--------------------------------------------------------------------

1. LeetCode 20 - Valid Parentheses                        [*****]
   - Asked at: Google, Meta, Amazon, Microsoft, Bloomberg, Apple
   - Why: Tests stack fundamentals - matching brackets
   - Striver: L2 - Check for Balanced Parentheses
   - Location in SNQ_snippet_practise_notes.py: BalancedParenthesis()

2. LeetCode 155 - Min Stack                               [*****]
   - Asked at: Google, Meta, Amazon, Microsoft, Apple
   - Why: Design problem - O(1) getMin operation
   - Striver: L4 - Implement Min Stack

3. LeetCode 496 - Next Greater Element I                  [*****]
   - Asked at: Amazon, Meta, Google, Bloomberg
   - Why: Classic monotonic stack pattern
   - Striver: L5 - Next Greater Element
   - Location in SNQ_snippet_practise_notes.py: NextGreaterElement()

4. LeetCode 84 - Largest Rectangle in Histogram           [*****]
   - Asked at: Google, Meta, Amazon, Microsoft
   - Why: HARD - combines NGE + PSE patterns
   - Striver: L12 - Largest Rectangle in Histogram
   - **TOP GOOGLE L6 QUESTION**

5. LeetCode 42 - Trapping Rain Water                      [*****]
   - Asked at: Google, Meta, Amazon, Apple, Microsoft
   - Why: Multiple approaches - prefix/suffix, two-pointer, stack
   - Striver: L8 - Trapping Rainwater | 2 Approaches
   - Location in SNQ_snippet_practise_notes.py: TrappingRainwater()

6. LeetCode 239 - Sliding Window Maximum                  [*****]
   - Asked at: Google, Amazon, Meta, Microsoft
   - Why: Monotonic deque pattern - O(n) solution
   - Striver: L16 - Sliding Window Maximum
   - **FREQUENTLY ASKED AT GOOGLE**

7. LeetCode 146 - LRU Cache                               [*****]
   - Asked at: Meta, Google, Amazon, Microsoft, Apple
   - Why: Design - HashMap + Doubly Linked List
   - Striver: L18 - Implement LRU Cache
   - **ONE OF THE MOST FREQUENT DESIGN QUESTIONS**


====================================================================
  TIER 2 - VERY IMPORTANT (70-90% Frequency)
====================================================================

8.  LeetCode 503 - Next Greater Element II (Circular)     [****]
    - Asked at: Amazon, Meta, Google
    - Why: NGE variant with circular array (2x traversal trick)
    - Striver: L6 - Next Greater Element II

9.  LeetCode 907 - Sum of Subarray Minimums               [****]
    - Asked at: Google, Amazon, Meta
    - Why: Monotonic stack + contribution technique
    - Striver: L9 - Sum of Subarray Minimum

10. LeetCode 2104 - Sum of Subarray Ranges                [****]
    - Asked at: Google, Amazon
    - Why: Extension of L9 - max and min contribution
    - Striver: L10 - Sum of Subarray Ranges

11. LeetCode 735 - Asteroid Collision                     [****]
    - Asked at: Amazon, Google, Meta
    - Why: Stack simulation problem
    - Striver: L11 - Asteroid Collisions

12. LeetCode 85 - Maximal Rectangle                       [****]
    - Asked at: Google, Meta, Amazon
    - Why: Builds on Largest Rectangle in Histogram
    - Striver: L13 - Maximal Rectangle

13. LeetCode 402 - Remove K Digits                        [****]
    - Asked at: Amazon, Google, Microsoft
    - Why: Monotonic stack for optimization
    - Striver: L14 - Remove K Digits

14. LeetCode 901 - Online Stock Span                      [****]
    - Asked at: Amazon, Google
    - Why: Previous Greater Element variant
    - Striver: L15 - Stock Span Problem


====================================================================
  TIER 3 - GOOD TO KNOW (40-70% Frequency)
====================================================================

15. LeetCode 71 - Simplify Path                           [***]
    - Asked at: Meta, Google
    - Why: Stack for path parsing

16. LeetCode 150 - Evaluate Reverse Polish Notation       [***]
    - Asked at: Amazon, Microsoft
    - Why: Stack for expression evaluation
    - Striver: L3 - Prefix, Infix, and Postfix Conversion

17. LeetCode 739 - Daily Temperatures                     [***]
    - Asked at: Amazon, Meta
    - Why: NGE variant - return indices not values

18. LeetCode 232 - Implement Queue using Stacks           [***]
    - Asked at: Amazon, Microsoft
    - Why: Fundamental stack/queue relationship
    - Striver: L1 - Introduction to Stack and Queue

19. LeetCode 225 - Implement Stack using Queues           [***]
    - Asked at: Amazon, Microsoft
    - Why: Fundamental stack/queue relationship
    - Striver: L1 - Introduction to Stack and Queue

20. LeetCode 277 - Find the Celebrity                     [***]
    - Asked at: Meta, Google
    - Why: Stack-based elimination
    - Striver: L17 - The Celebrity Problem


====================================================================
  TIER 4 - L6/STAFF LEVEL ADVANCED
====================================================================

21. LeetCode 460 - LFU Cache                              [***]
    - Asked at: Google, Meta
    - Why: HARD design - HashMap + Doubly Linked List + Frequency
    - Striver: L19 - Implement LFU Cache in C++/Java
    - **L6/STAFF DIFFERENTIATOR**

22. LeetCode 316 - Remove Duplicate Letters               [***]
    - Asked at: Google, Amazon
    - Why: Monotonic stack + greedy

23. LeetCode 1944 - Number of Visible People in Queue     [**]
    - Asked at: Google
    - Why: Monotonic stack variant

24. LeetCode 862 - Shortest Subarray with Sum >= K        [**]
    - Asked at: Google
    - Why: Monotonic deque with prefix sums

25. LeetCode 1425 - Constrained Subsequence Sum           [**]
    - Asked at: Google
    - Why: DP + Monotonic deque optimization


====================================================================
  STRIVER PLAYLIST <-> LEETCODE MAPPING
====================================================================

L1  - Introduction to Stack and Queue
      --> LC 232 - Implement Queue using Stacks
      --> LC 225 - Implement Stack using Queues

L2  - Check for Balanced Parentheses
      --> LC 20 - Valid Parentheses                       [TIER 1 *****]

L3  - Prefix, Infix, and Postfix Conversion
      --> LC 150 - Evaluate Reverse Polish Notation       [TIER 3 ***]
      --> LC 224 - Basic Calculator

L4  - Implement Min Stack
      --> LC 155 - Min Stack                              [TIER 1 *****]

L5  - Next Greater Element
      --> LC 496 - Next Greater Element I                 [TIER 1 *****]

L6  - Next Greater Element II
      --> LC 503 - Next Greater Element II (Circular)     [TIER 2 ****]

L7  - Previous Smaller Element
      --> Foundation for LC 84, LC 907
      --> Location: PreviousSmallerElement()

L8  - Trapping Rainwater | 2 Approaches
      --> LC 42 - Trapping Rain Water                     [TIER 1 *****]

L9  - Sum of Subarray Minimum
      --> LC 907 - Sum of Subarray Minimums               [TIER 2 ****]

L10 - Sum of Subarray Ranges
      --> LC 2104 - Sum of Subarray Ranges                [TIER 2 ****]

L11 - Asteroid Collisions
      --> LC 735 - Asteroid Collision                     [TIER 2 ****]

L12 - Largest Rectangle in Histogram
      --> LC 84 - Largest Rectangle in Histogram          [TIER 1 *****]
      --> **TOP GOOGLE L6 QUESTION**

L13 - Maximal Rectangle
      --> LC 85 - Maximal Rectangle                       [TIER 2 ****]

L14 - Remove K Digits
      --> LC 402 - Remove K Digits                        [TIER 2 ****]

L15 - Stock Span Problem
      --> LC 901 - Online Stock Span                      [TIER 2 ****]

L16 - Sliding Window Maximum
      --> LC 239 - Sliding Window Maximum                 [TIER 1 *****]
      --> Uses Monotonic DEQUE (not stack)

L17 - The Celebrity Problem
      --> LC 277 - Find the Celebrity                     [TIER 3 ***]

L18 - Implement LRU Cache
      --> LC 146 - LRU Cache                              [TIER 1 *****]
      --> **ONE OF THE MOST FREQUENT DESIGN QUESTIONS**

L19 - Implement LFU Cache
      --> LC 460 - LFU Cache                              [TIER 4 ***]
      --> **L6/STAFF DIFFERENTIATOR**


====================================================================
  FREQUENCY BY COMPANY
====================================================================

GOOGLE - Top 5 Stack/Queue Questions:
  1. Largest Rectangle in Histogram (84)
  2. Sliding Window Maximum (239)
  3. Trapping Rain Water (42)
  4. LRU Cache (146)
  5. Sum of Subarray Minimums (907)

META - Top 5 Stack/Queue Questions:
  1. Valid Parentheses (20)
  2. LRU Cache (146)
  3. Trapping Rain Water (42)
  4. Next Greater Element (496)
  5. Simplify Path (71)

AMAZON - Top 5 Stack/Queue Questions:
  1. Valid Parentheses (20)
  2. Min Stack (155)
  3. Next Greater Element (496)
  4. Asteroid Collision (735)
  5. Daily Temperatures (739)

MICROSOFT - Top 4 Stack/Queue Questions:
  1. Valid Parentheses (20)
  2. Min Stack (155)
  3. Trapping Rain Water (42)
  4. LRU Cache (146)

APPLE - Top 4 Stack/Queue Questions:
  1. Valid Parentheses (20)
  2. Min Stack (155)
  3. Trapping Rain Water (42)
  4. LRU Cache (146)


====================================================================
  PATTERN RECOGNITION - KEYWORD MAPPING
====================================================================

KEYWORD                              --> PATTERN
"Matching brackets/parentheses"      --> Stack (push open, pop close)
"Next greater/smaller"               --> Monotonic Stack
"Previous greater/smaller"           --> Monotonic Stack (reverse)
"Histogram/Rectangle area"           --> NGE + PSE combination
"Sliding window max/min"             --> Monotonic Deque
"Expression evaluation"              --> Stack (operand + operator)
"Path simplification"                --> Stack (push/pop directories)
"Cache design (LRU/LFU)"             --> HashMap + Doubly Linked List
"Stock span/prices"                  --> Previous Greater Element
"Asteroid/collision"                 --> Stack simulation
"Remove digits/characters"           --> Monotonic Stack (greedy)
"Subarray min/max contribution"      --> Monotonic Stack + math


====================================================================
  MONOTONIC STACK PATTERNS (Core Concept)
====================================================================

1. NEXT GREATER ELEMENT (NGE):
   - Traverse RIGHT to LEFT
   - Maintain DECREASING stack
   - Pop elements <= current
   - Answer = stack top (or -1 if empty)

2. PREVIOUS SMALLER ELEMENT (PSE):
   - Traverse LEFT to RIGHT
   - Maintain INCREASING stack
   - Pop elements >= current
   - Answer = stack top (or -1 if empty)

3. NEXT SMALLER ELEMENT (NSE):
   - Traverse RIGHT to LEFT
   - Maintain INCREASING stack

4. PREVIOUS GREATER ELEMENT (PGE):
   - Traverse LEFT to RIGHT
   - Maintain DECREASING stack

COMBINATION PROBLEMS:
- Largest Rectangle in Histogram: PSE + NSE
- Sum of Subarray Minimums: PSE + NSE + contribution
- Trapping Rain Water: Prefix Max + Suffix Max (or stack)


====================================================================
  2-WEEK STUDY PLAN FOR STACK/QUEUE MASTERY
====================================================================

WEEK 1 - FOUNDATIONS:
  Day 1:   Stack/Queue basics
           - Valid Parentheses (20)
           - Implement Queue using Stacks (232)

  Day 2:   Min Stack + Expression Evaluation
           - Min Stack (155)
           - Evaluate RPN (150)

  Day 3-4: Monotonic Stack - NGE/PSE
           - Next Greater Element I (496)
           - Next Greater Element II (503)
           - Previous Smaller Element
           - Daily Temperatures (739)

  Day 5:   Trapping Rain Water
           - LC 42 - All approaches (prefix/suffix, two-pointer, stack)

  Day 6-7: Histogram Problems
           - Largest Rectangle in Histogram (84)
           - Maximal Rectangle (85)

WEEK 2 - ADVANCED:
  Day 8:   Subarray Contribution
           - Sum of Subarray Minimums (907)
           - Sum of Subarray Ranges (2104)

  Day 9:   Monotonic Deque
           - Sliding Window Maximum (239)

  Day 10:  Simulation Problems
           - Asteroid Collision (735)
           - Remove K Digits (402)

  Day 11-12: Cache Design
             - LRU Cache (146)
             - LFU Cache (460)

  Day 13-14: Mock interviews + revisit weak spots
             - Time yourself: 30-45 min per problem
             - Practice explaining out loud


====================================================================
  L6/STAFF DIFFERENTIATORS
====================================================================

For Google L6/Staff, these questions appear MORE frequently:

1. Largest Rectangle in Histogram (LC 84)
   - Must know PSE + NSE combination
   - O(n) time, O(n) space
   - Edge cases: all same height, strictly increasing/decreasing

2. LRU Cache (LC 146)
   - HashMap + Doubly Linked List
   - All operations O(1)
   - Be ready to implement from scratch

3. LFU Cache (LC 460)
   - Extension of LRU with frequency tracking
   - Multiple linked lists by frequency
   - **HARD - L6 differentiator**

4. Sum of Subarray Minimums (LC 907)
   - Contribution technique
   - Handle duplicates carefully (strict vs non-strict)

5. Sliding Window Maximum (LC 239)
   - Monotonic deque
   - Explain why deque not stack


====================================================================
  INTERVIEW TIPS FOR STACK/QUEUE PROBLEMS
====================================================================

1. CLARIFY FIRST:
   - Input constraints (size, values)
   - Empty input handling
   - Duplicates allowed?

2. PATTERN RECOGNITION:
   - "Next/Previous Greater/Smaller" → Monotonic Stack
   - "Sliding window optimization" → Monotonic Deque
   - "Matching pairs" → Stack
   - "Cache with eviction" → HashMap + Linked List

3. COMPLEXITY ANALYSIS:
   - Most monotonic stack solutions: O(n) time, O(n) space
   - Each element pushed/popped at most once
   - Amortized analysis for deque operations

4. EDGE CASES:
   - Empty input
   - Single element
   - All same elements
   - Strictly increasing/decreasing
   - Circular arrays (2x traversal)

5. CODE QUALITY (L6 BAR):
   - Clean helper functions
   - Meaningful variable names
   - Handle edge cases at top
   - Modular, testable code


====================================================================
  END OF STACK & QUEUE INTERVIEW CHEAT SHEET
====================================================================
"""
