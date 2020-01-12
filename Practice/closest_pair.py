'''
[the divide and conquer algorithm design paradigm]
1. DIVIDE your problem into smaller subproblems.
2. CONQUER subproblems recursively.
3. COMBINE solutions of subproblems into one for the original problem.

[Closest Pair]
1.Here in the closest pair problem,
we're going to proceed exactly as we did in the merge sort and counting inversions problems,
where we took the array and broke it into its left and right half.
So here, we're going to take the input point set, and again,
just recurse on the left half of the points, and recurse on the right half of the points.
So here, by left and right, I mean with respect to the points x coordinates.

2.There's pretty much never any ingenuity in the conquer step,
that just means you take the sub-problems you identified in the first step,
and you solve them recursively.
That's what we'll do here,
we'll recursively complete the closest pair in the left half of the points,
and the closest pair in the right half of the points.

3.So where all the creativity in divide and conquer algorithms is in the combined step.
Given the solutions to your sub problems,
how do you somehow recover a solution to the original problem?
The one that you actually care about.
So for closest pair, the questionis going to be,
given that you've computed the closest pair on the left half of the points,
and the closest pair on the right half of the points,
how do you then quickly recover the closest pair for the whole point set?


ClosestPair(Px,Py) (Base case omitted):
1) We sort all points according to x coordinates to get Px and Py sorted by y coordinates.

2) Divide all points according to its x coordinates in two halves.

3) Recursively find the smallest distances in both subarrays.

4) Take the minimum of two smallest distances. Let the minimum be d.

5) Create an array strip[] that stores all points which are at most d distance away from the middle line dividing the two sets.

6) Find the smallest distance in strip[].

7) Return the minimum of d and the smallest distance calculated in above step 6.

The great thing about the above approach is,
because we sorted the array by its y coordinates (and get Py) at the beginning,
so array strip[] can be got by extracting [x-d, x+d] part of the numbers of Py iterating through its x coordinates,
which allows us to spend only O(n) to get the array strip instead of O(nlogn)
then we can find the smallest distance in strip[] in O(n) time, because we only need to look at at most 7 points within strip[],
so we can take it as O(n).


https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2
'''
