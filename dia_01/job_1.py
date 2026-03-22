numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#nume = [f"{p} impar" if p %2 == 0
# else f"{p} par" for p in numeros] no funciona. tengo que busca que funcione

for p in numeros:
   if p %2 == 0:
       print(f'{p} es par')
   else:
        print(f'{p} es impar')
