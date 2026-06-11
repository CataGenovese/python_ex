entrada = int(input())

p= 0
n= 0

while entrada != 0:

    if entrada > 0:
        p += 1
    else:
        n += 1

    entrada = int(input())

if p > n:
    print("POSITIVE")
else:
    print("NEGATIVE")

