def ksp():
    val = list(map(int, input("Enter values separated by space: ").split()))
    wt = list(map(int, input("Enter weights separated by space: ").split()))
    W = int(input("Enter the maximum weight capacity: "))
    
    n = len(val) - 1

    def knapsack(W, n):
        if n < 0 or W <= 0:
            return 0
        if wt[n] > W:
            return knapsack(W, n - 1)
        else:
            return max(val[n] + knapsack(W - wt[n], n - 1), knapsack(W, n - 1))

    result = knapsack(W, n)
    print(f"The maximum value that can be obtained is: {result}")

if __name__ == "__main__":
    ksp()