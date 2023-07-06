distancia = float(input('Qual é a distância da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {distancia}km.')


if distancia < 200:
    valorKm = 0.5
else:
    valorKm = 0.45


print(f'E o preço do bilhete e de {distancia * valorKm}€.' )
