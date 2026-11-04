print("For loop with break/continue example:")

for i in range(1, 11):
    if i == 5:
        print("Skipping number 5")
        continue
    if i == 8:
        print("Breaking the loop at number 8")
        break
    print(i)


print("\nWhile loop with break/continue example:")
i = 1
while i <= 10:
    if i == 3:
        print("Skipping number 3")
        i += 1
        continue
    if i == 7:
        print("Breaking the loop at number 7")
        break
    print(i)
    i += 1