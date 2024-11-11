"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import tabulate

class BinaryNumber:
    def __init__(self, n):
        if isinstance(n, int):  # Ensure n is an integer
            self.decimal_val = n
            self.binary_vec = list('{0:b}'.format(n))
        elif isinstance(n, str):  # For cases where n might be a binary string
            self.decimal_val = int(n, 2)
            self.binary_vec = list(n)
        else:
            raise ValueError("BinaryNumber must be initialized with an integer or binary string.")

    def __repr__(self):
        return f'decimal={self.decimal_val} binary={"".join(self.binary_vec)}'

def binary2int(binary_number):
    binary_vec = binary_number.binary_vec
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(binary_number):
    mid = len(binary_number.binary_vec) // 2
    high = BinaryNumber(int(''.join(binary_number.binary_vec[:mid]), 2))
    low = BinaryNumber(int(''.join(binary_number.binary_vec[mid:]), 2))
    return high, low

def bit_shift(binary_number, n):
    return BinaryNumber(int(''.join(binary_number.binary_vec) + '0' * n, 2))

def pad(x, y):
    max_len = max(len(x.binary_vec), len(y.binary_vec))
    if max_len % 2 != 0:
        max_len += 1
    x_padded = ['0'] * (max_len - len(x.binary_vec)) + x.binary_vec
    y_padded = ['0'] * (max_len - len(y.binary_vec)) + y.binary_vec
    return BinaryNumber(int(''.join(x_padded), 2)), BinaryNumber(int(''.join(y_padded), 2))

def quadratic_multiply(x, y):
    x_int = int(''.join(x.binary_vec), 2)
    y_int = int(''.join(y.binary_vec), 2)
    result_int = x_int * y_int
    return BinaryNumber(result_int)

def subquadratic_multiply(x, y):
    x_vec = x.binary_vec
    y_vec = y.binary_vec

    if len(x_vec) == 1 or len(y_vec) == 1:
        return BinaryNumber(int(''.join(x_vec), 2) * int(''.join(y_vec), 2))

    x, y = pad(x, y)
    x1, x0 = split_number(x)
    y1, y0 = split_number(y)

    print(f"x1: {x1}, x0: {x0}, y1: {y1}, y0: {y0}")

    z2 = subquadratic_multiply(x1, y1)
    z0 = subquadratic_multiply(x0, y0)
    z1 = subquadratic_multiply(BinaryNumber(x1.decimal_val + x0.decimal_val), 
                               BinaryNumber(y1.decimal_val + y0.decimal_val))

    print(f"z2: {z2}, z0: {z0}, z1: {z1}")

    result_int = z2.decimal_val * (2 ** (2 * len(x1.binary_vec))) + \
                 ((z1.decimal_val - z2.decimal_val - z0.decimal_val) * (2 ** len(x1.binary_vec))) + \
                 z0.decimal_val

    print(f"Result: {result_int}")

    return BinaryNumber(result_int)


def test_binary_number():
    bn1 = BinaryNumber(10)
    assert bn1.decimal_val == 10
    assert ''.join(bn1.binary_vec) == '1010'

    bn2 = BinaryNumber('1010')
    assert bn2.decimal_val == 10
    assert ''.join(bn2.binary_vec) == '1010'

    try:
        BinaryNumber([1, 0, 1, 0])
    except ValueError as e:
        assert str(e) == "BinaryNumber must be initialized with an integer or binary string."

test_binary_number()

def test_multiply():
    assert binary2int(quadratic_multiply(BinaryNumber(2), BinaryNumber(2))).decimal_val == 2 * 2
    assert binary2int(subquadratic_multiply(BinaryNumber(2), BinaryNumber(2))).decimal_val == 2 * 2

def time_multiply(x, y, f):
    start = time.time()
    f(x, y)
    return (time.time() - start) * 1000

def compare_multiply():
    res = []
    for n in [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)
        res.append((n, qtime, subqtime))
    print_results(res)

def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))

test_multiply()

compare_multiply()
