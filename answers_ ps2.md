  # CMPS 6610 Problem Set 02
## Answe
**Name:**Wesnahika Charles

Place all written answers from `problemset-02.md` here for easier grading.

1. **Asymptotic notation**
 proven in problem_set2_work pdf
2. **Algorithm Selection**
  1. O(n^log_6 2)
  2. O(n^log_4 6)
  3. O(n log n)
  4. O(n^2)
  5. O(n^4)
  6. O(n^3/2 log n)
  7. O(n)
  8. O(n^c+1)
  9. O(log log n)

3. **More Algorithm Selection** 
First scenario:
A: Work = O(n^2) and Span = O(n^2)
B: Work = O(n log n) and Span = O( log n)
C: Work = O(n^1.1) and Span = O(n^1.1)

The Algorithm that is prefered would be the B because it has the smallest span at O(log n) which works the best when it comes to parallelism. 

Second Scenario: 
A: Work = O(n^log_2 5) and Span = O(n log n)
B: Work = O(n) and Span O(n)
C: Work = O(n^2 log n) and Span = O(n^2)

The Algorithm that would be most prefered here would be Algorithm B considering how it has the lowest span and is most suitable for parallelism.  
*4. **Integer Multiplication Timing Results**

|          n |   quadratic |   subquadratic |
|------------|-------------|----------------|
|         10 |       0.000 |          1.603 |
|        100 |       0.000 |          3.092 |
|       1000 |       0.000 |          8.073 |
|      10000 |       0.000 |          7.402 |
|     100000 |       0.000 |         13.092 |
|    1000000 |       0.000 |         14.722 |
|   10000000 |       0.000 |         14.601 |
|  100000000 |       0.000 |         25.184 |
| 1000000000 |       0.000 |         33.523 |

As we can see as n increases the time gets a longer.

