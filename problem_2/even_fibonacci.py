initial = 1
second = 2
result = 0

while (initial < 4000000 and second < 4000000):
    new = initial + second
    initial = second
    second = new

    if initial % 2 == 0:
        result += initial

print(result)
