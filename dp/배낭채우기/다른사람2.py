def knapsack2(i, W, w, p):
    if (i <= 0 or W <= 0):
        return 0
    if (w[i] > W):
        value = knapsack2(i - 1, W, w, p)
        print(i - 1, W, value)
        return value
    else:  # w[i] <= W
        left = knapsack2(i - 1, W, w, p)
        print(i - 1, W, left)
        right = knapsack2(i - 1, W - w[i], w, p)
        print(i - 1, W - w[i], right)
        return max(left, p[i] + right)

print(knapsack2(2, 30, [5, 10, 20], [5, 6, 14]), 30)
print(knapsack2(0, 4, [2], [2]), 4)
