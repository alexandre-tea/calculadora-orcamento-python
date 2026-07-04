# Calculadora de Orçamento em Python

Projeto desenvolvido em Python para calcular o orçamento de um serviço com base nas horas trabalhadas, valor da hora, desconto e imposto.

## Funcionalidades

- Cálculo do subtotal.
- Aplicação automática de desconto para projetos com 20 horas ou mais.
- Cálculo do imposto.
- Cálculo do valor total.
- Validação de entrada com `try/except`.
- Organização do código em funções.

## Tecnologias utilizadas

- Python 3

## Estrutura do projeto

- `ler_int()` → Lê números inteiros.
- `ler_float()` → Lê números decimais.
- `calcular_projeto()` → Realiza todos os cálculos do orçamento.
- `mostrar_orcamento()` → Exibe o orçamento formatado.
- `main()` → Controla o fluxo do programa.

## Exemplo de execução

```
Horas programadas: 120
Taxa por hora: 20
Desconto (0.10 para 10%): 0.10
Imposto (0.20 para 20%): 0.20

=== ORÇAMENTO ===
Horas: 120
Taxa: R$ 20.00/h
Subtotal: R$ 2160.00
Desconto (10%): -R$ 240.00
Imposto (20%): R$ 432.00
Total: R$ 2592.00
```

## Objetivo

Este projeto foi desenvolvido com foco em praticar:

- Funções
- Tratamento de exceções (`try/except`)
- Organização de código
- Reutilização de funções
- Lógica de programação

---
Desenvolvido para fins de estudo em Python.
