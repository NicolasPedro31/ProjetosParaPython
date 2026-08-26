Salario = int(input("Coloque seu salario aqui: R$"))
Aumento = int(input("Digite o aumento: %"))
AumentoSalarial = Salario + (Salario * Aumento / 100)
resultado = AumentoSalarial
print(f"Seu salario é R${Salario} + {Aumento}% é R${resultado}: ")