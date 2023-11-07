def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def non_recur(n):
    first = 0
    second = 1
    print(first)
    print(second)
    while n - 2 >= 0:
        third = first + second
        first = second
        second = third
        print(third)
        n = n - 1

if __name__ == "_main_":
    n = 10
    first_value = 0
    second_value = 1
    for i in range(n):
        print(recursive_fibonacci(i))
        non_recur(i)