# 1
def q1():
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    print(x + y)

# 2
def q2():
    metros = float(input('Digite um valor em metros: '))
    mm = metros * 100
    print(str(mm) +' milímetros')

# 3
def q3():
    d = int(input('Digite a quantidade de dias: '))
    h = int(input('Digite a quantidade de horas: '))
    m = int(input('Digite a quantidade de minutos: '))
    s = int(input('Digite a quantidade de seguntos: '))
    seg = s + m * 60
    hr = d * 24 + h
    seg = seg + hr * 3600
    print (str(seg) +' segundos')

# 4
def q4():
    salario = float(input('Informe o salário recebido: '))
    percentual = float(input('Informe a porcentagem de aumento: '))
    aumento = salario * percentual / 100
    novosalario = salario + aumento
    print ('O aumento foi de R$%.2f e o novo salário é R$%.2f' % (aumento, novosalario))

#5
def q5():
    preco = float(input('Informe o preço da mercadoria: '))
    percentual = float(input('Informe o percentual de desconto: '))
    percentual = percentual / 100
    desconto = preco * percentual
    novopreco = preco - desconto
    print ('O valor do desconto foi R$%.2f e o preço a pagar será R$%.2f.' % (desconto, novopreco))

#6
def q6():
    distancia = float(input('Qual a distância a percorrer em km? '))
    velocidade = float(input('E qual a velocidade média em km/h? '))
    horas = distancia / velocidade
    tempo = '%.1f horas.' % horas
    if (horas > 24):
        dias = horas % 24
        horas = horas - (horas / dias)
        tempo = '%d dias e %d horas.' % (dias,horas)
    print ('Tempo estimado de viagem: '+tempo)

#7
def q7():
    celsius = float(input('Digite a temperatura em ºCelsius: '))
    fahr = 9 * celsius / 5 + 32
    print ('%.1f ºC = %.1f ºF.' % (celsius,fahr))

#8
def q8():
    fahr = float(input('Digite a temperatura em ºFahrenheit: '))
    celsius = 5 * (fahr - 32) / 9
    print ('%.1f ºF = %.1f ºC.' % (fahr, celsius))
