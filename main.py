from tkinter import *
from tkinter import ttk

def main():

    #Cria a janela
    root = Tk()
    #Cria o frame que ira receber os widgets(Componentes gráficos)
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    #Cria o título da janela
    root.title("Calculadora")

    #Cria o espaço onde vai aparecer a operação do usuário e o resultado
    ttk.Label(frm, text="O número vai aqui").grid(row=0)

    #Cria o botão de apagar o número digitado
    ttk.Button(frm, text="<-",).grid(column=1, row=1)

    #Cria o botão de resetar a operação
    ttk.Button(frm, text="CE",).grid(column=2, row=1)

    #Cria o botão de limpar a tela
    ttk.Button(frm, text="C",).grid(column=3, row=1)

    #Cria o botão da operação de divisão
    ttk.Button(frm, text="/",).grid(column=4, row=1)

    #Cria os botões dos números
    numero = 1
    for linha in range(2,5):         # 3 linhas
        for col in range(1,4):       # 3 colunas
            ttk.Button(frm, text=str(numero)).grid(column=col, row=linha)
            numero += 1
        
    #Cria o botão do número 0
    ttk.Button(frm,text="0").grid(column=2,row=5)

    #Cria o botão da operação multiplicação
    ttk.Button(frm,text="*").grid(column=4,row=2)

    #Cria o botão da operação subtração
    ttk.Button(frm,text="-").grid(column=4,row=3)

    #Cria o botão da operação soma
    ttk.Button(frm,text="+").grid(column=4,row=4)

    #Cria o botão da operação resultado
    ttk.Button(frm,text="=").grid(column=4,row=5)

    #Cria o botão da vírgula
    ttk.Button(frm,text=",").grid(column=3,row=5)


    root.mainloop()
    return




if __name__ == "__main__":
    main()
    
