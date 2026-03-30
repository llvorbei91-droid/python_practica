memoria = {}

nombre = input("Hola, ¿cómo te llamas? ").strip().title()
memoria["nombre"] = nombre

print(f"Encantado {memoria['nombre']} 😄")

gusto = input("¿Te gusta programar? ").strip().lower()
memoria["gusto_programar"] = gusto

if gusto == "si":
    print("Entonces vamos por buen camino 🚀")
else:
    print("No pasa nada, poco a poco 😎")
huellas = input("Quieres dejar algo este años?")
memoria["huellas"] = huellas
if huellas == "si":
    print("No te rinda aun queda mucho tiempos")
else:
   print("Te lo estas plantiando todavia?")
reflecion = input("Tienes alguna refleccion inportante?")
if reflecion == "si":
   print("Es bueno reflecionar las cosas")
else:
   print("No te coma la cabezas con cosas fuera de tu crontor")
memoria["reflecion"] = reflecion
relacion = input("Que tal tus relaciones con las persona / cosa?")
if relacion == "tengo varia":
   print(" Eres toro")
memoria["relacion"] = relacion
futuro_cerca = input ("Como te ves un dentro de 3 meses?")
memoria["futuro_cerca"] = futuro_cerca
futuro_lejos = input ("a largo plazo?")
memoria["futuro_lejos"] = futuro_lejos
