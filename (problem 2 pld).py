def swap_numbers(a, b):
    print("before swapping: a =", a, "b =", b)
    a = a + b
    b = a - b
    a = a - b
    print("after swapping: a =", a, "b =", b)