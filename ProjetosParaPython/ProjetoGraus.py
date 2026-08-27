import math
from math import trunc
Graus = float(input("Digite quantos fahrenheit você quer para graus: "))
Fahrenheit = (Graus - 32) * 5/9
resultado = Fahrenheit
print(f"O calculo de Graus para Fahrenheit é: °C{resultado:.0f}")

Graus = float(input("Digite quantos fahrenheit você quer para graus: "))
Fahrenheit = (Graus - 32) * 5/9
resultado = Fahrenheit
resultado = math.trunc(Fahrenheit + 0.5)
print(f"O calculo de Graus para Fahrenheit é: °C{resultado}")