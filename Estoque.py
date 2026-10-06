dic_produtos = {
    "cafe": {"preco": 18.50, "quantidade": 100},
    "pao": {"preco": 6.00, "quantidade": 50},
    "leite": {"preco": 5.50, "quantidade": 30},
    "ovos": {"preco": 12.00, "quantidade": 20},
    "manteiga": {"preco": 9.90, "quantidade": 15},
    "queijo": {"preco": 32.00, "quantidade": 10},
    "presunto": {"preco": 24.00, "quantidade": 25},
}

carrinho = {}  

print("Digite o nome do produto para comprar ou 'fim' para finalizar.")

while True:
    produto_buscado = input("\nQual produto você está procurando? ").strip().lower()

    if produto_buscado == "fim":
        break

    produto = dic_produtos.get(produto_buscado)

    if produto is None:
        print(f"Desculpe, o produto {produto_buscado} não está disponível.")
        continue

    
    ja_no_carrinho = carrinho.get(produto_buscado, 0)
    disponivel = produto["quantidade"] - ja_no_carrinho

    if disponivel == 0:
        print("Você já colocou todo o estoque deste produto no carrinho.")
        continue

    try:
        quantidade = int(input(
            f"Preço: R${produto['preco']:.2f} ({disponivel} disponíveis). "
            "Quantas unidades? "
        ))
    except ValueError:
        print("Quantidade inválida. Insira um número inteiro.")
        continue

    if quantidade <= 0:
        print("Informe uma quantidade maior que zero.")
    elif quantidade > disponivel:
        print(f"Desculpe, temos apenas {disponivel} unidades disponíveis.")
    else:
        carrinho[produto_buscado] = ja_no_carrinho + quantidade
        print(f"{quantidade}x {produto_buscado} adicionado ao carrinho.")


if not carrinho:
    print("\nNenhum item no carrinho. Até a próxima!")
else:
    print("\n=== RESUMO DA COMPRA ===")
    total_geral = 0

    for nome, qtd in carrinho.items():
        preco = dic_produtos[nome]["preco"]
        subtotal = preco * qtd
        total_geral += subtotal
        dic_produtos[nome]["quantidade"] -= qtd
        print(f"{qtd}x {nome:<10} R${preco:>6.2f}  =  R${subtotal:>7.2f}")

    print("-" * 36)
    print(f"TOTAL: R${total_geral:.2f}")