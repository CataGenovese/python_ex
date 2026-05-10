# ex15
frutas = ["poma", "platan", "maduixa"]

for i, fruta in enumerate(frutas):
    print(f"{i} - {fruta}")

# ex16
notes = [4, 7, 9, 2]

for i, nota in enumerate(notes, start=1):
    print(f"Alumne {i}: {nota}")

# ex17
notes = [4, 7, 9, 2, 6]

for i, nota in enumerate(notes, start=1):
    if nota > 5:
        print(f"Alumne {i}: {nota}")


# ex18
for i, par in enumerate(notes):
    if par % 2 == 0:
        print(par)

