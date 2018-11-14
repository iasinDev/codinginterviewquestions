def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    if num <= 0: return 1
    gcd = arr[0]
    for i in range(1, len(arr)):
        if arr[i] % gcd != 0:
            gcd = euklidAlgo(arr[i], gcd)
    return gcd


def euklidAlgo(a, b):
    while b > 0:
        if a > b:
            a = a - b
        elif b >= a:
            b = b - a
    return a


print(generalizedGCD(5, [2, 4, 6, 8, 10]))
print(generalizedGCD(5, [2, 3, 4, 5, 6]))
