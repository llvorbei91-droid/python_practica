nombre = input("Nombre: ").strip().title()
while True:
    try:
       edad = int(input("Edad que tienes?: "))
       break
    except ValueError:
           print("introduce una edad validad")
ciudad = input("Ciudad: ").strip().title()
persona = {
    "Nombre": nombre,
    "Edad": edad,
    "Ciudad": ciudad
}
for k, v, in persona.items():
    print(f'{k}: {v}')
print(f"{persona['Nombre']} tiene {persona['Edad']} años y vive en {persona['Ciudad']}")
#if persona["Edad"] < 25:
   #print("eres menor de edad")
#else:
 # print("Eres mayor")
