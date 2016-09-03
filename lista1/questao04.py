salario = float(input('Informe o salário recebido: '))
percentual = float(input('Informe a porcentagem de aumento: '))
aumento = salario * percentual / 100
novosalario = salario + aumento
print ('O aumento foi de R$%.2f e o novo salário é R$%.2f' % (aumento, novosalario))
