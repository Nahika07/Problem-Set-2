# CMPS 6610 Problem Set 04
## Answers

**Name:**Wesnahika Charles


Place all written answers from `assignment-05.md` here for easier grading.




- **1d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt      |             1340    |    826            | 0.616
alice29.txt |        1039367      |       676374      |0.615
asyoulik.txt|        876253       |         606448    |0.692
grammar.lsp |     26047           |     17356         |0.666
fields.c    |     78050           |     56206         |0.72

The ratio stays at around 70%, which indicates that the hoffman coding is more efficient 


- **1d.**
The huffman coding would behave similarly to the fixed length coding and the cost would be the same. 




- **2a.**
You could paralellize the heap construction process by dividing the arrays into sub arrays and build mini heaps afterwards you can merge them. The work will still be O(n).



- **2b.**
However the span will be O(log n) because the heapifications can be dont parallel at every level of the tree.



- **3a.**
You would want to start with the largest coin there is, collect all instances of that coin, subtract the total value and repeat the process by using the next largesrt untill N - 0. 


- **3b.**
When looking at the Greedy Choice property,, the algorithm alsways goes for the largest unit that isn't bigger than N. This would be  optimal considering how you would end up using less coins in the lomg run. For Optimal Substructure, the problem stays the same but with a smaller N, the opyimal solution for the next problem, can be combined with the previous choice to create the optimal solution for the original problem  



- **3c.**
The work would be O(log n) since the denominations are powers of two and you are continously reducing the problem. And the SPan would be the same since you are selecting the largest denomination Log N times. 


- **4a.**
A counter example would be if the denominations were 1,5,7. The greedy algorithm chose 7,1,1,1 if you wanted the value of 10 coin when the most optimal option would be 5,5.


- **4b.**
If we need to make change for n dollars uisng d1,d2,d3..dn denominations, the optimal number of coins needed would be c and Di is the value of a given coin. To get the optimal solution, we must use any of the denominatiosn such that n - di, then you must make change for the remander of the value reccursively until the remaining amount is 0. Each time you are reducing the amount by the value of one coin and adding 1 to the total of coins used. 



- **4c.**
The woork would be O(nk), because you iterate overe all of the denominations. And the span would be O(n) since you would need to go through it sequentially for each i. 