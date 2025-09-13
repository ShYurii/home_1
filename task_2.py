n = int(input("enter number n: "))

multi_factorial = 1
for x in range(1, n + 1):
    multi_factorial *= x
print(f"result: {multi_factorial}")
