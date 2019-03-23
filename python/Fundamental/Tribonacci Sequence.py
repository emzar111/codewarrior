def tribonacci(signature, n):
    r = signature
    if n > 3:
        for i in range(3, n + 1):
            r.append(r[i - 1] + r[i - 2] + r[i - 3])
    return r[:n]

print(tribonacci([1, 1, 1], 10))
