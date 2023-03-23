
class Pilha:
    minhaPilha = None
    topo = None

    def __init__(self):
        self.minhaPilha = list()
        self.topo = str
    def empilhar(self, dado):
        self.minhaPilha.append(dado)
        self.topo = dado
    def imprimirTudo(self):
        for letra in reversed(self.minhaPilha):
            print(letra)
    def desempilhar(self):
        self.minhaPilha.pop()
        for letra in reversed(self.minhaPilha):
            print(letra)
    def imprimeTopo(self):
        print(self.minhaPilha[-1])
    def apagarTudo(self):
        while self.minhaPilha:
            self.minhaPilha.pop()
        print(self.minhaPilha)
    def infixParaPrefix(self, expressao):
        expressao = expressao.split(" ")
        Pilha_ope = list()
        Pilha_num = list()
        while len(expressao) != 0:
            Pilha_num.append(expressao.pop())
            if len(expressao) == 0:
                break
            Pilha_ope.append(expressao.pop())
        while len(Pilha_num) != 0:
            Pilha_ope.append(Pilha_num.pop())
        for i in Pilha_ope:
            print(i, end=" ")
    def infixParaPosfix(self, expressao):
        expressao = expressao.split(" ")
        Pilha_ope = list()
        Pilha_num = list()
        Resultado = []
        while len(expressao) != 0:
            Pilha_num.append(expressao.pop())
            if len(expressao) == 0:
                break
            Pilha_ope.append(expressao.pop())
        Resultado.append(Pilha_num.pop())
        Resultado.append(Pilha_num.pop())
        Resultado.append(Pilha_ope.pop())
        while len(Pilha_num) != 0:
            Resultado.append(Pilha_num.pop())
            Resultado.append(Pilha_ope.pop())
        for i in Resultado:
            print(i, end=" ")
    def infixa(self, expressao):
        resultado = eval(expressao)
        print(resultado)
    def prefix(self, expressao):
        expressao = expressao.split(" ")
        resultado = 0
        pilhaNum = []
        while expressao[-1].isdigit():
            pilhaNum.append(expressao.pop())
        num1 = int(pilhaNum.pop())
        num2 = int(pilhaNum.pop())
        ope = expressao.pop()
        
        if ope == "+":
            resultado = num1 + num2
        else:
            resultado = num1 - num2
            
        while len(expressao) != 0:
            num1 = int(pilhaNum.pop())
            ope = expressao.pop()
            if ope == "+":
                resultado = resultado + num1
            else:
                resultado = resultado - num1
        print(resultado)
    def posfix(self, expressao):
        expressao = expressao.split(" ")
        resultado = 0
        pilha = []
        while len(expressao) != 0:
            pilha.append(expressao.pop())
        num1 = int(pilha.pop())
        num2 = int(pilha.pop())
        ope = pilha.pop()
        
        if ope == "+":
            resultado = num1 + num2
        else:
            resultado = num1 - num2
            
        while len(pilha) != 0:
            num1 = int(pilha.pop())
            ope = pilha.pop()
            if ope == "+":
                resultado = resultado + num1
            else:
                resultado = resultado - num1
        print(resultado)
        
def main():
    
    p1 = Pilha()
    
    while True:
        #opcao = int(input("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: "))
        #print("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: ")
        print("")
        print("1- Empilhar")
        print("2- Desempilhar")
        print("3- Imprimir topo")
        print("4- Imprimir tudo")
        print("5- Apagar tudo")
        print("6- Converter INFIXO para PREFIXO")
        print("7- Converter INFIXO para POSFIXO")
        print("8- Calcular INFIXO")
        print("9- Calcular PREFIXO")
        print("10- Calcular POSFIXO")
        print("11- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        if opcao == 1:
            dado = str(input("Entre com uma letra: ")).upper()
            p1.empilhar(dado)
            pass
        elif opcao == 2:
            p1.desempilhar()
            pass
        elif opcao == 3:
            p1.imprimeTopo()
            pass
        elif opcao == 4:
            p1.imprimirTudo()
            pass
        elif opcao == 5:
            p1.apagarTudo()
            pass
        elif opcao == 6:
            p1.infixParaPrefix(input("Expressão: "))
            break
        elif opcao == 7:
            p1.infixParaPosfix(input("Expressao: "))
            break
        elif opcao == 8:
            p1.infixa(input('Digite uma expressão matemática: '))
            break
        elif opcao == 9:
            p1.prefix(input("Digite uma expresão prefixa: "))
            break
        elif opcao == 10:
            p1.posfix(input("Digite uma expressão posfixa: "))
            break
        else:
            break
    

if __name__ == "__main__":
    main()
