cigarrosdia = int(input('Quantos cigarros fuma por dia? '))
anosfumando = int(input('Por quantos anos já fumou? '))
qtdano = cigarrosdia * 365 * anosfumando
perderumdia = 6 * 24
diasperdidos = int(qtdano / perderumdia)
print ('Você perderá %d dias de vida! :(' % diasperdidos)
