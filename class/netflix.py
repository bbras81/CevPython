class Cliente:
    def __init__(self, nome, email, plano) -> None:
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano invalido")
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print("Plano alterado")
        else:
            print("Plano invalido")
            
            
    def ver_filme(self, filme):
        pass
    
    
    
cliente = Cliente("Bruno", "lira@gmail.com", "basic")

cliente.mudar_plano("premium")

print(cliente.plano)