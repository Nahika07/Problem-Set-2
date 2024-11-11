# CMPS 6610  Answers for Lab 04

In this lab, we'll work a bit more with sequences and look at the
divide-and-conquer paradigm.

The sorting algorithms we've discussed so far all work by *comparing* numbers (e.g., `merge_sort`, `insertion_sort`, `selection_sort`). Today, we'll look at an algorithm that sorts without making any pairwise comparisons.

The algorithm is particularly suited for sorting lists with the
following properties:

- elements are non-negative integers

- the maximum element is not too big

- many elements are repeated

For example:

$[2,2,1,0,1,0,1,3] \rightarrow [0,0,1,1,1,2,2,3]$

In addition to the input list of length $n$, the algorithm also takes as input the maximum value in the list ($k$). E.g., $k=3$ in the above example.

The algorithm proceeds by first counting how often each value appears. Based on these counts, the algorithm figures out the range of output locations to place each value. For example, because there are two 0s and three 1s, we know that the first 1 goes in the 3rd position, and the final 1 goes in the 5th position. We'll complete the algorithm `supersort` by implementing three functions, `count_values`, `get_positions`, and `construct_output`.



1. Implement a simple, sequential version of `count_values` (linear span and work) and test it with `test_count_values`.

.  
.  
.  

2. Continuing our example, `counts` should now be `[2, 3, 2, 1]`. We next need to convert this into a list indicating the location of the first appearance of each value in the output.

E.g., `positions=[0, 2, 5, 7]` means that, in the final output, the first 0 appears at index 0, the first 1 appears at index 2, etc.

We can use `scan` to create the needed list. You may need to adjust slightly the output of scan to get the needed list. Complete `get_positions` and test with `test_get_positions`.

.  
.  
. 


3. What is the work and span of `get_positions`? (assume our more efficient version of `scan` from class)

> **put in answers.md**
The work is O(n) because n is the length of the input array for counts. And the span is O(log n) because it operates in parallelism to create the prefix sums. 
.  
.  
. 


4. Finally, we'll use this positions array to construct the final output. First, we'll create the output list ($n$ elements). Then, we will loop through the original input array once again. For each value, we'll look up in the `positions` array where the value should go. E.g., for the first value 2, we look up `positions[2]`, which tells us the 2 should go in index 5 in the output. To update `counts` for future iterations, we will then increment `counts` by one for the value we just read. E.g., `positions[2]` will increment from 5 to 6; the next 2 we read will be placed in index 6.

Implement `construct_output` with a simple for loop and test with `test_construct_output`.

.  
.  
. 


5. What is the work and span of `construct_output`?

> **put in answers.md**
Th work would be O(n) because there is a single loop that reiterates over list a which may have a size of n. The span would also be O(n) since it is sequential and has a propotion to the amount of iterations (which happens for every element in list a). 

.  
.  
. 


6. What is the work and span of `supersort`?

> The work of supersort would be O(n) becase count_values iterates through the list n times, same with get positions and contruct input. The span would be O(log n) because while the span of construct input would be O(1), the span is still dominated by get poistions(O(log n)). 

.  
.  
. 


7. Our implementation of `count_values` has poor span. Let's instead implement it using map-reduce. Complete `count_map`, `count_reduce`, which are used by `count_values_mr` to construct the `counts` variable using map-reduce. Test with `test_count_values_mr`.

.  
.  
. 


8. What is work and span of `count_values_mr`?

> **put in answers.md**
.  The work would be O(n) because if the input has a length of n, then the work of the map phase, the grouping the key pairs and the count_reduce phase is all O(n). For the span, the count map could be done using parallelism so it would be O(1), the time to group those values together would be O(log n) since there are condensing, and the reduce section would also be O(1), so therefore the span is O(log n)
.  
. 

9. We'll turn our focus now to the divide-and-conquer paradigm that we
   are formalizing in Module 4. Recurrences naturally model the
   performance of a divide-and-conquer algorithm, and we have had
   plenty of practice with these. Let's focus on proving correctness.
   
   
a) Before we look at proving the correctness of an algorithm, let's
   get some practice using mathematical induction. Recall that the
   formula for a geometric series was, for $\alpha \neq 0$:
   $$ \sum_{i=0}^n \alpha^i = \frac{\alpha^{n+1} - 1}{\alpha - 1} $$
   
   Prove that this formula is correct by induction.

> **put in answers.md**

When looking at the base case which would be n=0, the formula ends up being a-1/a-1 which equals to 1 so that is true.  When doing the inductive step, we must make sure that n = k. a^k+1 - 1 / a-1. Then k + 1, a^i + a^k+1, then (a^k+1 -1/a-1) + a^k+1, then (a^k+1)-1 +a^k+1 (a-1)/a-1, then after simplifying you get (a^k+2)-1/a-1. 
.  
. 

b) Prove the correctness of `reduce` using induction.
	   

> **put in answers.md**
For the first base case n = 0, in the empty list, it just returns the id element which is true. For the second n = 1, if the list has one element i (reduce f, id, [i]) = i, this is right when you put f with id which will give you the element i. When looking at a list of k + 1, reduce(f, id, x...x k+1), each call to reduce gives the correct result for those peices so when you incorporate f, they will give the proper results. 
.  
. 

c) Prove the correctness of the divide and conquer version of `span` using induction. 


> **put in answers.md**
For an empty list (n = 0) can will result in a list that is empty. In a base case where n = 1, as in a list with one element (scan(f, id, x)) this will output the prefix sum. When looking at a list of length k + 1, when scan is called the list is split and it is called on both parts, then they are both combined with the correct balance for the prefix sums, so when factoring induction, scan is correct. 
.  
. 

d) Prove the correctness of the contraction-based version of `span`
from Module 3. Compare this proof to the divide-and-conquer
version. Are they significantly different? Was one easier than the
other?

> **put in answers.md**
.  The two base cases are the same as above, and when factoring induction, we are till assuming that the function correctly calculates the prefix sums and when each contraction shrinks the problem size, the results are placed together in a correct way. They are similar when it comes to the base cases, however, the divide and conquer verision splits the lists directly while the contraction verison had an alternate way to combine the halves. 
.  
. 

