# CMPS 6610 Lab 06
## Answers

**Name:** Wesnahika Charles
**Name:**_________________________


Place all written answers from `lab-06.md` here for easier grading.



- **1)** The work O(1) for insert simply because since the list doesn't have an order, you could easily just append right to the end of the list, and the span is also the same. For deleteMin, you would need to search the entire list for the minimum so it would be O(n) with n being the length of the list and since it is also sequential, the span will be the same. 

- **2a)** The depth would be log_2(n) despite it not being perfectly balanced. This is because the levels grow as the elements does in a logarithmic fashion.

- **2b)** The minimum element will always be at the root and the maximum element will always be a leaf node.

- **4)** For reheapUp, the work would be O(log n) simply because the element would need to go to the root node and the hight is log n. Same case for reheapDown. The span for both would be O(log n) also because the swap must depend on the previous one. 

- **6)** Ther work of heapsort, since it employes the use of O(log n) and there are n elemnets it would be O(n * log n). And the span would be O(log n) since all of the insertions plus deletions are logarithmically dominated
