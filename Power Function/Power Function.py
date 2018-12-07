# Write a pow(base,exponent) function without using the system pow function
# Try to find a optimized O(log n) solution

def power2(base, exponent):
    result = 1
    if exponent == 0:
        return 1
    if exponent < 0:
        base = 1 / base
    if exponent%2==0:
        result = power(base * base, abs(exponent)//2)
    else:
        for i in range(abs(exponent)):
            result = result * base
    return result

# Better and shorter implementation from GeeksForGeeks
def power(base,exponent):
    if exponent == 0: return 1
    result = power(base, int(exponent/2))

    if exponent%2==0:
        return result * result
    if exponent > 0:
        return result * result * base
    else:
        return result * result / base

# print(power(2, 0))
# print(power(2, 1))
# print(power(2, -1))
# print(power(2, 2))
# print(power(2, -2))
# print(power(2, -3))
# print(power(2, -4))
print(power(2, 5))
# print(power(2, 3))
# print(power(2, -3))
# print(power(2, 10))
# print(power(2, -4))

# 2 * 2
# 2 * 2 * 2
# 2 * 2 * 2 * 2