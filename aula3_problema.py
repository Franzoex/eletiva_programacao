print('''Digite um número: ''')
a=float(input())      
print("Qual operação você quer saber?\n soma\n subtração\n multiplicação\n divisão\n exponenciação\n raiz quadrada\n porcentagem")
c=input()


c=c.lower()

if c=="ao quadrado":
    print(a**2)
    quit() 

b=float(input())

if c=="multiplicação":
    print(a*b)

elif c=="divisão":
    print(a/b)

elif c=="soma":
    print(a+b)

elif c=="subtração":
    print(a-b)

elif c=="porcentagem":
    print(a%b)

elif c=="elevado":
    print(a**b)

