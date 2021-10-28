import random
dinero = 2000
edad = random.randrange(0,50)
hambre = edad
precio = 100
total = 0

while hambre < 85:
    if hambre > edad:
        precio = precio * 1.2
        total = total + precio
    else:
        total += precio
    hambre = hambre + edad

print(edad)
print(total)