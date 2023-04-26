def speed(v, t):
    y = v * t % 109
    return y
v = int(input("Введіть значення швидкості:"))
t = int(input("Введіть значення часу:"))
s = speed(v, t)
print(s)
