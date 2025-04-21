from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    root.title("Calculadora")
    ttk.Label(frm, text="O número vai aqui").grid(row=0)
    ttk.Button(frm, text="<-",).grid(column=1, row=1)
    ttk.Button(frm, text="CE",).grid(column=2, row=1)
    ttk.Button(frm, text="C",).grid(column=3, row=1)
    ttk.Button(frm, text="/",).grid(column=4, row=1)

    numero = 1
    for linha in range(2,5):         # 3 linhas
        for col in range(1,4):       # 3 colunas
            ttk.Button(frm, text=str(numero)).grid(column=col, row=linha)
            numero += 1
        
    root.mainloop()
    return




if __name__ == "__main__":
    main()
    
