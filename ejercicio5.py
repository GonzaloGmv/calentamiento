dinero = 2000
edad = 19
hambre = edad
precio = 100
total = 0

while hambre < 85:
    if hambre > edad:
        precio = precio * 1.2
        total += precio
    else:
        total = precio
    hambre = hambre + edad

print("Edad: ", edad)
print("Precio final: ", total)