vel = int(input('Qual é a velocidade atual do swu carro? '))
velmax = 80
multa = (vel - velmax) * 7
if vel >= 80:
    print('MULTADO! Você exedeu o limite de velocidade que é de {}km/h'.format(velmax))
    print('Você deve pagar uma multa de {}R$\n Tenha um bom dia dirija com segurança'.format(multa))
else:
    print('Tenha um bom dia dirija com segurança!!')
