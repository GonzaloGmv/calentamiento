dinero = 2000
edad = 19
nHelados = 1
hambre = edad * nHelados
precioI = 100

if hambre < 85:
    nHelados = int(85 / edad)

precio1 = precioI
precio2 = 1.2 * precio1
precio3 = 1.2 * precio2
precio4 = 1.2 * precio3
precioT = precio1 + precio2 + precio3 + precio4

print("Número de helados: ", nHelados)
print("Precio ", precioT)