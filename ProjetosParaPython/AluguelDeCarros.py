dias = float(input("Quantos dias alugado: "))
km = float(input("Quantos KM rodados: "))
pago = dias * 60 + (km * 0.15)
print(f"O total a pagar é de {pago:.2f}")