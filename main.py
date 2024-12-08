import random
import time
import tabulate


def ssort(L):
    for i in range(len(L)):
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L


def partition(L, pivot_index):
    """
    Partition the list around the pivot.
    """
    pivot = L[pivot_index]
    L[pivot_index], L[-1] = L[-1], L[pivot_index]
    i = 0
    for j in range(len(L) - 1):
        if L[j] < pivot:
            L[i], L[j] = L[j], L[i]
            i += 1
    L[i], L[-1] = L[-1], L[i]
    return i


def qsort(L, pivot_fn):
    """
    QuickSort implementation.
    L........The list to sort.
    pivot_fn...Function to determine the pivot index.
    """
    if len(L) <= 1:
        return L
    pivot_index = pivot_fn(L)
    pivot_new_index = partition(L, pivot_index)
    left = qsort(L[:pivot_new_index], pivot_fn)
    right = qsort(L[pivot_new_index + 1 :], pivot_fn)
    return left + [L[pivot_new_index]] + right


# Fixed pivot function: always select the first element
def fixed_pivot_fn(L):
    return 0


# Random pivot function: select a random index
def random_pivot_fn(L):
    return random.randint(0, len(L) - 1)


def time_search(sort_fn, mylist):
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000


def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    def qsort_fixed_pivot(L):
        return qsort(L, fixed_pivot_fn)

    def qsort_random_pivot(L):
        return qsort(L, random_pivot_fn)

    # Use Python's built-in Timsort as the baseline comparison
    def tim_sort(L):
        return sorted(L)

    result = []
    for size in sizes:
        mylist = list(range(size))
        random.shuffle(mylist)  # Random permutation comparison
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, list(mylist)),
            time_search(qsort_random_pivot, list(mylist)),
            time_search(tim_sort, list(mylist)),
        ])
    return result


def print_results(results):
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim-sort'],
            floatfmt=".3f",
            tablefmt="github",
        )
    )


# Test and output results
random.seed()
print_results(compare_sort())
