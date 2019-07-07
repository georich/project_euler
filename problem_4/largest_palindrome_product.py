result = 0
for x in range(1,1000):
    for y in range(1,1000):
        product = x * y
        if product > result and str(product) == str(product)[::-1]:
            result = product
print(result)
