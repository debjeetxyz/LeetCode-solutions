# Climbing Stairs

**LeetCode Link:** https://leetcode.com/problems/climbing-stairs/  
**Difficulty:** Easy  
**Approach:** Dynamic Programming (Space Optimized)

## Problem Statement
You are climbing a staircase. It takes `n` steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?

## Intuition
The number of ways to reach step `n` is the sum of the ways to reach
`n-1` and `n-2`, since those are the only two steps you can jump from.
This gives the recurrence: climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)

This is essentially the Fibonacci sequence. Instead of storing an
entire DP array, only the last two computed values are needed at any
point, so the space can be optimized down to two variables.
