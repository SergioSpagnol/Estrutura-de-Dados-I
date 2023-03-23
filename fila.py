class Fila:
    
    def __init__(self):
        self.minhaFila = []
        self.inicio = str
        self.fim = str

    def enfileirar(self, item):
        self.minhaFila.append(item)

    def desenfileirar(self):
        if len(self.minhaFila) == 0:
            print("Erro")
        else:
            self.minhaFila.pop(0)

    def imprimir_inicio(self):
        if len(self.minhaFila) == 0:
            print("Vazio")
        else:
            self.inicio = self.minhaFila[0]
            print(self.inicio)

    def imprimir_fim(self):
        if len(self.minhaFila) == 0:
            print("Vazio")
        else:
           self.fim = self.minhaFila[-1]
           print(self.fim)

    def imprimir_tudo(self):
        if len(self.minhaFila) == 0:
            print("Vazio")
        else:
            for item in self.minhaFila:
                print(item, end=" ")
            
    def excluir_tudo(self):
        if len(self.minhaFila) == 0:
            print("Vazio")
        else:
            while len(self.minhaFila) != 0:
                self.minhaFila.pop(0)


def main():
    f1 = Fila()
 
    while True:
        print("")
        print("1- Enfileirar")
        print("2- Desenfileirar")
        print("3- Imprimir inicio")
        print("4- Imprimir fim")
        print("5- Imprimir tudo")
        print("6- Excluir tudo")
        print("7- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        if opcao == 1:
            item = input("Digite o item a ser enfileirado: ")
            f1.enfileirar(item)
            pass
        elif opcao == 2:
            f1.desenfileirar()
            pass
        elif opcao == 3:
            f1.imprimir_inicio()
            pass
        elif opcao == 4:
            f1.imprimir_fim()
            pass
        elif opcao == 5:
            f1.imprimir_tudo()
            pass
        elif opcao == 6:
            f1.excluir_tudo()
            pass
        else:
            break

if __name__ == "__main__":
    main()
