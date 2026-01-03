def swap_numbers(a, b):
    a, b = b, a
    return a, b
if __name__ == "__main__":
    x = 5
    y = 10
    print("Before swapping: x =", x, ", y =", y)
    x, y = swap_numbers(x, y)
    print("After swapping: x =", x, ", y =", y)
