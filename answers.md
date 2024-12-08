# CMPS 6610 Problem Set 6
## Answers

**Name:**Wesnahika Charles


Place all written answers from this assignment here for easier grading.




- **1a.**
P[X >= c * n] <= c1 * n log n/c * n^2 = c1 log n / cn
Therefore as n goes to infinity, the probability goes to 0. It is small for a large n. 



- **1b.**
P[X >= 10c * n ln n] <= c1 * n ln n/ 10c * n ln n = c/10n



- **2a.**
To boost the success probability to at least d, where epsilon is less than d and d is less than one, we run A independently k times and use a deterministic checker C to validate each result. The algorithm returns the first correct result. The number of runs k is determined by the formula k equals the ceiling of the natural logarithm of one minus d divided by the natural logarithm of one minus epsilon. Each run of A takes W of n work, so the total work is proportional to k times W of n, which simplifies to the natural logarithm of one minus d divided by the natural logarithm of one minus epsilon times W of n.



- **2b.**
To ensure the algorithm always produces the correct result, we repeatedly run A and validate each output with C until a correct result is found. Since the probability of success for each run is epsilon, the expected number of runs follows a geometric distribution with an expected value of one divided by epsilon. The expected total work is therefore proportional to W of n divided by epsilon.



- **3b.**
|      n |   qsort-fixed-pivot |   qsort-random-pivot |
|--------|---------------------|----------------------|
|    100 |               0.000 |                0.000 |
|    200 |               0.000 |                1.005 |
|    500 |               0.000 |                1.000 |
|   1000 |               1.000 |                1.000 |
|   2000 |               2.090 |                2.252 |
|   5000 |               6.291 |                6.107 |
|  10000 |              13.507 |               14.512 |
|  20000 |              27.919 |               33.597 |
|  50000 |             116.930 |              110.780 |
| 100000 |             222.821 |              200.964 |

They both are nearly identical and as input sizes increase the execution time begins to exponentially increase as well.  

- **3c.**
|      n |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|--------|---------------------|----------------------|------------|
|    100 |               0.000 |                0.000 |      0.000 |
|    200 |               0.000 |                1.005 |      0.000 |
|    500 |               0.000 |                1.000 |      0.000 |
|   1000 |               1.000 |                1.000 |      0.000 |
|   2000 |               2.090 |                2.252 |      0.000 |
|   5000 |               6.291 |                6.107 |      1.398 |
|  10000 |              13.507 |               14.512 |      0.999 |
|  20000 |              27.919 |               33.597 |      2.000 |
|  50000 |             116.930 |              110.780 |      7.452 |
| 100000 |             222.821 |              200.964 |     13.866 |

Regardless of the size of the list, timesort still greatly out performs. This is simply because of timesorts hybrid nature which causes it to acheive O(n log n) performance every time. 