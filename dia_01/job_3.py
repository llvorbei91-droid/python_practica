"""
input()
.strip().title()
try/except
if / elif
diccionario
"""

#datos = [nombre, luis, edad, 34, trabajo, ats, familia, si,
#hijos, 3, parejas, 2, coche, si, marca, citröen, modelo, c4 piscaso,
#]
print("*" *50)
print("Nivel Basico ver en Diccionario")
print("*"*50)
print()
persona = {
    "Nombre": 'Luis',
    "Edad" : 34,
    "Ciudad" : "Madrid"
}
for k, v in persona.items():
    print(f"{k}: {v}")
print("Nivel --> 2")
#print("↓"*50)
print(f"{persona['Nombre']} tiene {persona['Edad']} años y vives {persona['Ciudad']}")

