entrada = int(input())

for i in range(entrada):
    num = int(input())

    p=0
    s=0

    for j in range(num, 0, -1):
        if j % 2 == 0:
            p += j
        else:
            s += j

    print(f"PARELLS {p}, SENARS {s}")
