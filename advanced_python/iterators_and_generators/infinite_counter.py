def counter():
    n = 1
    while True:
        yield n
        n += 1
count = counter()
for _ in range(10):
    print(next(count))