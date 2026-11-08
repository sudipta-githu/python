def generator(n):
    for i in range(1, n + 1):
        yield i

total = sum(generator(100))
print(total)