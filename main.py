
def calcular_projeto(horas, taxa, desconto, imposto):
    subtotal = horas * taxa
    if horas >= 20:
        subtotal -= subtotal * desconto 
    valor_imposto = subtotal * imposto
    total = subtotal + imposto
    return subtotal, valor_imposto, total

try: 
    horas = int(input("Horas programada: "))
except ValueError:
    print("Digite apenas números")
    horas = 0
try:
    taxa = int(input("Taxas por horas: "))
except ValueError:
    print("Digite apenas números")
    taxa = 0
try:
    desconto = float(input("Desconto: "))
except ValueError:
    print("Digite apenas números")
    desconto = 0.0
try:
    imposto = float(input("Imposto: "))
except ValueError:
    print("Digite apenas números")
    imposto = 0.0
                
subtotal = horas * taxa
                
subtotal, valor_imposto, total = calcular_projeto(horas, taxa, desconto, imposto )

print("=== ORÇAMENTO ===")
print(f"Horas: {horas}")
print(f"Taxa: R$ {taxa:.2f}/h")
print(f"Subtotal R$ {subtotal:.2f}")
print(f"Desconto (10%):-R$ {horas * taxa * desconto:.2f}")
print(f"Imposto (20%): R$ {valor_imposto:.2f}")
print(f"Total: R$ {total:.2f}")
