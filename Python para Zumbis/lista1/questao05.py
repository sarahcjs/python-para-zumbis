preco = float(input('Informe o preço da mercadoria: '))
percentual = float(input('Informe o percentual de desconto: '))
percentual = percentual / 100
desconto = preco * percentual
novopreco = preco - desconto
print ('O valor do desconto foi R$%.2f e o preço a pagar será R$%.2f.' % (desconto, novopreco))
