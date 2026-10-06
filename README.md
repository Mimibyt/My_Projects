Analisador de Logs de Sistema

Projeto em Python que lê um arquivo de log e identifica falhas de conexão e autenticações bem-sucedidas, mostrando em qual linha cada ocorrência aparece.

Criei este projeto para praticar Python e, ao mesmo tempo, treinar uma tarefa comum em Help Desk e Suporte Técnico: ler logs para entender o que aconteceu com um sistema.

O que o programa faz hoje
Lê um arquivo de log linha por linha
Identifica falhas de conexão com o servidor
Identifica autenticações bem-sucedidas
Mostra a quantidade e a linha de cada ocorrência
Avisa quando não encontra nada, em vez de terminar sem mensagem
Formato de log esperado

Cada linha segue o padrão data hora NÍVEL mensagem:

2026-03-01 15:32:01 ERROR Falha ao conectar ao servidor
2026-03-01 15:32:15 INFO Usuário autenticado com sucesso
Como executar

Requisitos: Python 3 instalado.

Baixe ou clone este repositório
Coloque o arquivo sistema.log na mesma pasta do script
Execute:
bash
python leitordeerror.py
Exemplo de saída
Analisando o arquivo de log...
1 falha(s) de conexão encontrada(s):
Linha 1: 2026-03-01 15:32:01 ERROR Falha ao conectar ao servidor
1 Usuário(s) autenticado(s) com sucesso.
Linha 2: 2026-03-01 15:32:15 INFO Usuário autenticado com sucesso

Com um log que não contém nenhuma das duas ocorrências:

Analisando o arquivo de log...
Nenhuma falha de conexão encontrada.
Nenhum usuário autenticado com sucesso encontrado.
Próximos passos
 Identificar o motivo de cada falha (por exemplo: timeout, credenciais incorretas)
 Reconhecer outros tipos de erro além de conexão e autenticação
 Contar as ocorrências por horário do dia
 Gerar um relatório com gráfico
O que aprendi
<!--## O que aprendi

- A importância da atenção aos detalhes, pois tive erros simples que passavam despercebidos.
- Estou começando a aprender como os arquivos interagem com o código. -->
Autor

Micael Alves Barbosa Estudante de Análise e Desenvolvimento de Sistemas, em busca da primeira oportunidade em Help Desk / Suporte Técnico.


/........................................................................................................................................../

# 🛒 Terminal Store: Stock Lookup & Shopping Cart

A simple command-line store written in **Python**. The user searches for products, adds them to a cart, and gets a purchase summary at the end. Stock is only updated when the purchase is finalized.

> Note: the program's messages are displayed in Brazilian Portuguese.

## Features

- Search for a product by name (case-insensitive)
- Shows price and available quantity
- Shopping cart: buy multiple items in a single session
- Input validation:
  - Rejects zero, negative, and non-numeric quantities
  - Rejects quantities above the available stock
  - Accounts for items already in the cart, so stock can't be exceeded across multiple additions
- Final summary with subtotal per item and total
- Stock is deducted only at checkout

## Concepts practiced

- Nested dictionaries
- `while True` loops with `break` and `continue`
- Conditionals and input validation
- Error handling with `try/except`
- f-string formatting

## Requirements

- Python 3.8 or higher
- No external libraries

## How to run

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
python main.py
```

Type the product name to add it to the cart, and `fim` to finish the purchase.

## Example

```
Digite o nome do produto para comprar ou 'fim' para finalizar.

Qual produto você está procurando? cafe
Preço: R$18.50 (100 disponíveis). Quantas unidades? 2
2x cafe adicionado ao carrinho.

Qual produto você está procurando? pao
Preço: R$6.00 (50 disponíveis). Quantas unidades? 5
5x pao adicionado ao carrinho.

Qual produto você está procurando? fim

=== RESUMO DA COMPRA ===
2x cafe       R$ 18.50  =  R$  37.00
5x pao        R$  6.00  =  R$  30.00
------------------------------------
TOTAL: R$67.00
```

## Available products

`cafe`, `pao`, `leite`, `ovos`, `manteiga`, `queijo`, `presunto`

## Possible improvements

- [ ] Split the code into functions (`search_product`, `add_to_cart`, `show_summary`)
- [ ] Add a command to list all available products
- [ ] Remove items from the cart before checkout
- [ ] Persist stock in a JSON file so it survives between runs
- [ ] Add unit tests

## Author

**Micael Alves Barbosa**
Systems Analysis and Development graduate, looking for opportunities in Technical Support / Help Desk.

[LinkedIn](https://www.linkedin.com/in/micael-barbosa-aa50b9332/) · [GitHub](https://github.com/Mimibyt)
LinkedIn
