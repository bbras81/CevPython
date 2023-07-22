class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura) -> None:
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        
    def mudar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        elif botao == "-":
            print("Diminuir Volume")
            
            
controle_remoto = ControleRemoto("Preto", "10cm", "2cm", "4cm")

print(controle_remoto.altura)

controle_remoto.mudar_canal("+")