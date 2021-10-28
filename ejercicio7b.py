import random
dinero = 2000
edad = random.randrange(0,50)
hambre = edad
precio = 100

while hambre < 85:
    if hambre > edad:
        precio = precio * 1.2
    hambre = hambre + edad

print(edad)
print(precio)