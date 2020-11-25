com=0
def tabela(valor):
    global com
    com+=1
    print(f'           200{com}')
    for c in valor.values():
        for t in c:
            for k,z in t.items():
                print(f'{k:<25}{z}')
            print('='*56)



def leiaint(texto):
    while True:
        numero=str(input(texto))
        if numero.isnumeric():
            return int(numero)
        else:
            print('NÃO É NUMERICO! DIGITE NOVAMENTE')
 

def validaçao(valores):
    manha={'2001':[],'2002':[],'2003':[],'2004':[]}
    print(valores)

