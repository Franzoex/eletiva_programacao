import tkinter as tk

calculo=str()

def inserir_texto(x):
   
   global calculo
   calculo=calculo+x
   texto.delete(1.0, "end")
   texto.insert(1.0, calculo)

def avaliar():
    
    global calculo
    a=str(eval(texto.get(1.0, "end")))
    calculo=str()
    inserir_texto(a)

def apagar():

    global calculo
    calculo=str()
    texto.delete(1.0, "end")

janela=tk.Tk()

#janela.geometry("400x500")

texto=tk.Text(janela,height=4, width=16,font=("Arial",24))
texto.grid(columnspan=20)

botao_0=tk.Button(janela, text="0", command=lambda:inserir_texto("0"),width=7, height=3,font=("Arial",12))
botao_0.grid(column=2,row=6)
botao_1=tk.Button(janela, text="1", command=lambda:inserir_texto("1"),width=7, height=3,font=("Arial",12))
botao_1.grid(column=1,row=5)
botao_2=tk.Button(janela, text="2", command=lambda:inserir_texto("2"),width=7, height=3,font=("Arial",12))
botao_2.grid(column=2,row=5)
botao_3=tk.Button(janela, text="3", command=lambda:inserir_texto("3"),width=7, height=3,font=("Arial",12))
botao_3.grid(column=3,row=5)
botao_4=tk.Button(janela, text="4", command=lambda:inserir_texto("4"),width=7, height=3,font=("Arial",12))
botao_4.grid(column=1,row=4)
botao_5=tk.Button(janela, text="5", command=lambda:inserir_texto("5"),width=7, height=3,font=("Arial",12))
botao_5.grid(column=2,row=4)
botao_6=tk.Button(janela, text="6", command=lambda:inserir_texto("6"),width=7, height=3,font=("Arial",12))
botao_6.grid(column=3,row=4)
botao_7=tk.Button(janela, text="7", command=lambda:inserir_texto("7"),width=7, height=3,font=("Arial",12))
botao_7.grid(column=1,row=3)
botao_8=tk.Button(janela, text="8", command=lambda:inserir_texto("8"),width=7, height=3,font=("Arial",12))
botao_8.grid(column=2,row=3)
botao_9=tk.Button(janela, text="9", command=lambda:inserir_texto("9"),width=7, height=3,font=("Arial",12))
botao_9.grid(column=3,row=3)
botao_abreaspas=tk.Button(janela, text="(", command=lambda:inserir_texto("("),width=7, height=3,font=("Arial",12))
botao_abreaspas.grid(column=1,row=6)
botao_fechaaspas=tk.Button(janela, text=")", command=lambda:inserir_texto(")"),width=7, height=3,font=("Arial",12))
botao_fechaaspas.grid(column=3,row=6)
botao_menos=tk.Button(janela, text="-", command=lambda:inserir_texto("-"),width=7, height=3,font=("Arial",12))
botao_menos.grid(column=4,row=5)
botao_mais=tk.Button(janela, text="+", command=lambda:inserir_texto("+"),width=7, height=3,font=("Arial",12))
botao_mais.grid(column=4,row=6)
botao_vezes=tk.Button(janela, text="*", command=lambda:inserir_texto("*"),width=7, height=3,font=("Arial",12))
botao_vezes.grid(column=4,row=4)
botao_dividir=tk.Button(janela, text="/", command=lambda:inserir_texto("/"),width=7, height=3,font=("Arial",12))
botao_dividir.grid(column=4,row=3)
botao_igual=tk.Button(janela, text="=", command=lambda:avaliar(),width=15, height=3,font=("Arial",12))
botao_igual.grid(column=1,row=7,columnspan=2)
botao_C=tk.Button(janela, text="C", command=lambda:apagar(),width=15, height=3,font=("Arial",12))
botao_C.grid(column=3,row=7, columnspan=2)

janela.mainloop()