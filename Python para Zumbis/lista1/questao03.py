d = int(input('Digite a quantidade de dias: '))
h = int(input('Digite a quantidade de horas: '))
m = int(input('Digite a quantidade de minutos: '))
s = int(input('Digite a quantidade de seguntos: '))
seg = s + m * 60
hr = d * 24 + h
seg = seg + hr * 3600
print (str(seg) +' segundos')
