# Estudiante: Eduardo Luis Noriega Penafiel
# UEA - Movilidad en Linea - Paralelo C

def calcular_promedio(nota1, nota2, nota3):
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return promedio

print("UEA - Eduardo Luis Noriega Penafiel - Paralelo C")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

resultado = calcular_promedio(n1, n2, n3)

print(f"Promedio final de {resultado:.2f}")
print(f"Estudiante: Eduardo Luis Noriega Penafiel")

if resultado >= 7:
    print("Estado: APROBADO")
else:
    print("Estado: REPROBADO")
    
