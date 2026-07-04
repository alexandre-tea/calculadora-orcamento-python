def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números inteiros.")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite apenas números.")


def calcular_projeto(horas, taxa, desconto, imposto):

    subtotal_original = horas * taxa

    valor_desconto = 0

    if horas >= 20:
        valor_desconto = subtotal_original * desconto

    subtotal = subtotal_original - valor_desconto

    valor_imposto = subtotal * imposto

    total = subtotal + valor_imposto

    return subtotal, valor_desconto, valor_imposto, total


def mostrar_orcamento(horas, taxa, subtotal, valor_desconto, desconto, imposto, valor_imposto, total):

    print("\n=== ORÇAMENTO ===")
    print(f"Horas: {horas}")
    print(f"Taxa: R$ {taxa:.2f}/h")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Desconto ({desconto * 100:.0f}%): -R$ {valor_desconto:.2f}")
    print(f"Imposto ({imposto * 100:.0f}%): R$ {valor_imposto:.2f}")
    print(f"Total: R$ {total:.2f}")


def main():

    horas = ler_int("Horas programadas: ")
    taxa = ler_float("Taxa por hora: ")
    desconto = ler_float("Desconto (0.10 para 10%): ")
    imposto = ler_float("Imposto (0.20 para 20%): ")

    subtotal, valor_desconto, valor_imposto, total = calcular_projeto(
        horas,
        taxa,
        desconto,
        imposto
    )

    mostrar_orcamento(
        horas=horas,
        taxa=taxa,
        subtotal=subtotal,
        valor_desconto=valor_desconto,
        desconto=desconto,
        imposto=imposto,
        valor_imposto=valor_imposto,
        total=total
    )


main()
