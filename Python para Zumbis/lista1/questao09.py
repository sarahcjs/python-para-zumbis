distancia = float(input('Km percorridos com o carro: '))
dias = int(input('Quantidade de dias alugados: '))
aluguel = dias * 60 + distancia * 0.15
print ('O preço a pagar pelo aluguel será R$%.2f.' % aluguel)
