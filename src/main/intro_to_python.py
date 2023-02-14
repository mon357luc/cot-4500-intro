"intro to python - COP4600"

for i in range(3):
    for j in range(3):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

print()

for i in range(3):
    for j in range(3):
        if i == j:
            print(1, end=" ")
        else:
            print(3, end=" ")
    print()

print()

for i in range(3):
    for j in range(2):
        if i == j:
            print(1, end=" ")
        else:
            print(3, end=" ")
    print()