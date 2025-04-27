from tkinter import *
from tkinter import ttk
import re

#Cria a janela
root = Tk()
#Cria o frame que ira receber os widgets(Componentes gráficos)
frm = ttk.Frame(root, padding=10)
frm.grid()

#Cria o título da janela
root.title("Calculadora")

#Defino a variável que irá Atualizar minha Entry

operacao = StringVar(frm)

#Defino um valor padrão
operacao.set("0")

#Aqui eu verifico se os operadores podem ser utilizados e colocados na Entry
def verifica(operador):

    atual = operacao.get()

    if operador in "+-*/":
        # Não permitir operadores no começo
        if not atual:
            return
        # Se o último caractere for operador, substitui pelo novo operador
        if atual[-1] in "+-*/":
            operacao.set(atual[:-1] + operador)
        else:
            operacao.set(atual + operador)
        
        #Não permite mais de um operador na operação
        if all(op not in atual for op in ["/", "*", "-", "+"]):
            return

    elif operador == ".":
        #Caso seja o primeiro número e ele não tem vírgula ainda adiciona uma vírgula
        if all(op not in atual for op in ["/", "*", "-", "+"]) and atual != "":
            if operador not in atual:
                operacao.set(atual + operador)
        #Caso seja o segundo número e ele não tem vírgula ainda adiciona uma vírgula
        else:
            partes = re.split(r'(\+|\-|\*|/)', atual)
            print(partes)
            if operador not in partes[2] and partes[2] != "":
                operacao.set(atual+operador)

   #Realiza a operação em sim          
    elif operador == "=":
        #Caso esteja vazio só retorna
        if atual == "":
            return
        #Caso só tenha um número e nenhum operador
        if all(op not in atual for op in ["/", "*", "-", "+"]) and atual != "":
            return
        
        #Caso tenha um operador e só um número
        else:
             if atual[-1] in "+-*/":
                #Vai ser realizada a operação escolhida pelo primeiro número em si
                partes = re.split(r'(\+|\-|\*|/)', atual)

                #Se for tentada uma divisão por zero 
                if partes[0].strip('0') == '' and partes[1] == '/':
                    operacao.set('0')
                else:
                    partes[0] = str(float(partes[0]))
                    operacao.set(eval(partes[0]+partes[1]+partes[0]))
                    return

        #No mais realiza a operação normalmente, menos se for divisão por 0
        partes = re.split(r'(\+|\-|\*|/)', atual)

        if partes[0].strip('0') == '' and partes[1] == '/':
                operacao.set('0')
        else:
            partes[0] = str(float(partes[0]))
            partes[2] =  str(float(partes[2]))
            
            operacao.set(eval(partes[0]+partes[1]+partes[2]))

    else:
        # Adiciona o operador
        operacao.set(atual + operador)





def main():

    #Cria o espaço onde vai aparecer a operação do usuário e o resultado

    ttk.Entry(frm,justify="right", textvariable = operacao).grid(row=0)

    #Cria o botão de apagar o número digitado
    ttk.Button(frm, text="<-",command= lambda: operacao.set(operacao.get()[:-1] )).grid(column=1, row=1)

    #Cria o botão de resetar a operação
    ttk.Button(frm, text="CE",command= lambda: operacao.set("")).grid(column=2, row=1)

    #Cria o botão de limpar a tela
    ttk.Button(frm, text="C",command= lambda: operacao.set("")).grid(column=3, row=1)

    #Cria o botão da operação de divisão
    ttk.Button(frm, text="/",command=lambda: verifica("/")).grid(column=4, row=1)

    #Cria os botões dos números
    numero = 1
    for linha in range(2,5):         # 3 linhas
        for col in range(1,4):       # 3 colunas
            ttk.Button(frm, text=str(numero),command= lambda n = numero: operacao.set(operacao.get() + str(n))).grid(column=col, row=linha)
            numero += 1
        
    #Cria o botão do número 0
    ttk.Button(frm,text="0", command= lambda: operacao.set(operacao.get() + str(0))).grid(column=2,row=5)

    #Cria o botão da operação multiplicação
    ttk.Button(frm,text="*",command=lambda: verifica("*")).grid(column=4,row=2)

    #Cria o botão da operação subtração
    ttk.Button(frm,text="-",command=lambda: verifica("-")).grid(column=4,row=3)

    #Cria o botão da operação soma
    ttk.Button(frm,text="+",command=lambda: verifica("+")).grid(column=4,row=4)

    #Cria o botão da operação resultado
    ttk.Button(frm,text="=",command=lambda: verifica("=")).grid(column=4,row=5)

    #Cria o botão da ponto
    ttk.Button(frm,text=".",command=lambda: verifica(".")).grid(column=3,row=5)


    root.mainloop()
    return



if __name__ == "__main__":
    main()
    
