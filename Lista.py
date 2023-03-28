class Lista:

    def __init__(self):
        self.minhaLista = []
        self.inicio = None
        self.fim = None
    def Inserir_Inicio(self, item):
        self.minhaLista.insert(0, item)

    def Remover_Inicio(self):
        del self.minhaLista[0]

    def Inserir_Final(self, item):
        self.minhaLista.append(item)

    def Remover_Final(self):
        del self.minhaLista[-1]

    def Imprimir_Tudo(self):
        print(self.minhaLista)

    def Excluir_Tudo(self):
        self.minhaLista.clear()

    def Inserir_na_Posicao(self, posicao, item):
        self.minhaLista.insert(posicao, item)

    def Remover_na_Posicao(self, posicao):
        del self.minhaLista[posicao]

    def Imprimir_na_Posicao(self, posicao):
        print(self.minhaLista[posicao])

    def Calcular_determinante(self, l1, l2, l3):
        matriz = [l1, l2, l3]
        determinante = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + \
                       (matriz[0][1] * matriz[1][2] * matriz[2][0]) + \
                       (matriz[0][2] * matriz[1][0] * matriz[2][1]) - \
                       (matriz[0][2] * matriz[1][1] * matriz[2][0]) - \
                       (matriz[0][0] * matriz[1][2] * matriz[2][1]) - \
                       (matriz[0][1] * matriz[1][0] * matriz[2][2])
        print(determinante)


def main():
    L1 = Lista()

    while True:
        print("")
        print("1- Inserir Inicio")
        print("2– Remover Inicio")
        print("3- Inserir Final")
        print("4- Remover Final")
        print("5- Imprimir Tudo")
        print("6- Excluir Tudo")
        print("7- Inserir na Posicao")
        print("8- Remover da Posicao")
        print("9- Imprimir da Posicao")
        print("10- Calcular determinante")
        print("11- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        if opcao == 1:
            item = input("Digite um item para adicionar na  lista: ")
            L1.Inserir_Inicio(item)
            pass
        elif opcao == 2:
            L1.Remover_Inicio()
            pass
        elif opcao == 3:
            item = input("Digite um item para adicionar na  lista: ")
            L1.Inserir_Final(item)
            pass
        elif opcao == 4:
            L1.Remover_Final()
            pass
        elif opcao == 5:
            L1.Imprimir_Tudo()
            pass
        elif opcao == 6:
            L1.Excluir_Tudo()
            pass
        elif opcao == 7:
            posicao = int(input("Digite a posicao que deseja inserir: "))
            item = input("Digite um item para adicionar na  lista: ")
            L1.Inserir_na_Posicao(posicao, item)
            pass
        elif opcao == 8:
            posicao = int(input("Digite a posicao que deseja remover: "))
            L1.Remover_na_Posicao(posicao)
            pass
        elif opcao == 9:
            posicao = int(input("Digite a posicao que deseja imprimir: "))
            L1.Imprimir_na_Posicao(posicao)
            pass
        elif opcao == 10:
            l1 = []
            l2 = []
            l3 = []
            for i in range(3):
                numero = int(input("Numero: "))
                l1.append(numero)
            for i in range(3):
                numero = int(input("Numero: "))
                l2.append(numero)
            for i in range(3):
                numero = int(input("Numero: "))
                l3.append(numero)
            L1.Calcular_determinante(l1, l2, l3)
            break
        else:
            break


if __name__ == "__main__":
    main()