medida = float(input('Digite um distancia em metros: '))
km = float(medida / 1000)
hm = float(medida /100)
dam = float(medida / 10)
dm = float(medida * 10)
cm = float(medida * 100)
mm = float(medida * 1000)
print('A medida de {}m corresponde a:'.format(dm))
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(km, hm, dam, dm, cm, mm))