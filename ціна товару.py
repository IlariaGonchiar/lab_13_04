def cost(x, y):
    return x * 100 + y
a = int(input("Введіть значення грівнив для 1 товару:"))
b = int(input("Введіть значення копійок для 1 товару:"))
c = int(input("Введіть значення гривнів для 2 товару:"))
d = int(input("Введіть значення копійок для 2 товару"))
grn1 = cost(a, b)
print(grn1)
grn2 = cost(c, d)
print(grn2)
