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
