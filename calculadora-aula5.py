import tkinter as tk

calculo=str(0)

def inserir_texto(x):
   
   global calculo
   calculo=calculo+x
   texto.delete(1.0, "end")
   texto.insert(1.0, calculo)

janela=tk.Tk()

#janela.geometry("400x500")

texto=tk.Text(janela,height=4, width=16,font=("Arial",24))
texto.grid(columnspan=20)


botao_1=tk.Button(janela, text="c", command=lambda:inserir_texto("c"),width=15, height=3,font=("Arial",12))
botao_1.grid(column=3,row=7, columnspan=2)

botao1=tk.Button(janela, text="=", command=lambda:inserir_texto("="),width=15, height=3,font=("Arial",12))
botao1.grid(column=1,row=7,columnspan=2)

botao1=tk.Button(janela, text="7", command=lambda:inserir_texto("7"),width=7, height=3,font=("Arial",12))
botao1.grid(column=1,row=3)

botao2=tk.Button(janela, text="8", command=lambda:inserir_texto("8"),width=7, height=3,font=("Arial",12))
botao2.grid(column=2,row=3)

botao3=tk.Button(janela, text="9", command=lambda:inserir_texto("9"),width=7, height=3,font=("Arial",12))
botao3.grid(column=3,row=3)

botao4=tk.Button(janela, text="4", command=lambda:inserir_texto("4"),width=7, height=3,font=("Arial",12))
botao4.grid(column=1,row=4)

botao1=tk.Button(janela, text="5", command=lambda:inserir_texto("5"),width=7, height=3,font=("Arial",12))
botao1.grid(column=2,row=4)

botao2=tk.Button(janela, text="6", command=lambda:inserir_texto("6"),width=7, height=3,font=("Arial",12))
botao2.grid(column=3,row=4)

botao3=tk.Button(janela, text="1", command=lambda:inserir_texto("1"),width=7, height=3,font=("Arial",12))
botao3.grid(column=1,row=5)

botao4=tk.Button(janela, text="2", command=lambda:inserir_texto("2"),width=7, height=3,font=("Arial",12))
botao4.grid(column=2,row=5)

botao1=tk.Button(janela, text="3", command=lambda:inserir_texto("3"),width=7, height=3,font=("Arial",12))
botao1.grid(column=3,row=5)

botao1=tk.Button(janela, text="0", command=lambda:inserir_texto("0"),width=7, height=3,font=("Arial",12))
botao1.grid(column=2,row=6)

botao1=tk.Button(janela, text="(", command=lambda:inserir_texto("("),width=7, height=3,font=("Arial",12))
botao1.grid(column=1,row=6)

botao1=tk.Button(janela, text=")", command=lambda:inserir_texto(")"),width=7, height=3,font=("Arial",12))
botao1.grid(column=3,row=6)

botao1=tk.Button(janela, text="-", command=lambda:inserir_texto("-"),width=7, height=3,font=("Arial",12))
botao1.grid(column=4,row=5)

botao1=tk.Button(janela, text="+", command=lambda:inserir_texto("+"),width=7, height=3,font=("Arial",12))
botao1.grid(column=4,row=6)

botao1=tk.Button(janela, text="*", command=lambda:inserir_texto("*"),width=7, height=3,font=("Arial",12))
botao1.grid(column=4,row=4)

botao1=tk.Button(janela, text="/", command=lambda:inserir_texto("/"),width=7, height=3,font=("Arial",12))
botao1.grid(column=4,row=3)


janela.mainloop()
