"""""
inp = input(("Enter a number: "))
contador_deu= 0
contador= 0

while inp.isnumeric():
    contador += 1
    if int(inp) == 10:
        contador_deu += 1

    inp = input(("Enter a number: "))

print(f"TOTAL NOTES: {contador}, NOTES10: {contador_deu}")
"""""

