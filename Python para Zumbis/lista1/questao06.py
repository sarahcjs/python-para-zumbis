distancia = float(input('Qual a distância a percorrer em km? '))
velocidade = float(input('E qual a velocidade média em km/h? '))
horas = distancia / velocidade
tempo = '%.1f horas.' % horas
if (horas > 24):
    dias = horas % 24
    horas = horas - (horas / dias)
    tempo = '%d dias e %d horas.' % (dias,horas)
print ('Tempo estimado de viagem: '+tempo)
