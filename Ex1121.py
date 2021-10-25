descPorCompra = 0.1
descPorUnidade = 0.01
preco = float(input())
qtd = int(input())
valorReal = float(preco * qtd)
descontoPorPeca = qtd * descPorUnidade
valorDesc = valorReal - (valorReal * descPorCompra) - (valorReal * descontoPorPeca)

print(f"{valorReal:.2f}")
print(f"{valorDesc:.2f}")
