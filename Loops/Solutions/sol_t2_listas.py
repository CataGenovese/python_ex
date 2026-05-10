# ex10
frutas = ["manzana", "pera", "uva", "plátano"]
num = 0

for i in range(len(frutas)):
    print(num, frutas[i])
    num += 1

#ex11
colores = ["rojo", "azul", "verde", "negro"]
len_colores = len(colores)

for i in range(len_colores):
    print(colores[i])

# ex12
nums = [3, 5, 2, 8, 10]

len_list = len(nums)
max = 0

for i in range(len_list):
    if nums[i] > max:
        max = nums[i]
print(max)

