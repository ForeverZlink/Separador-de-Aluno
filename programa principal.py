from modulos import leiaint,tabela,separador_de_salas

cont=0
infomações={}
tudo=[]
while True:
    cont+=1
    infomações['aluno']=str(input('Nome do aluno:')).strip()
    infomações['matricula']=leiaint('Número da matricula:')
    infomações['data_de_nascimento']=leiaint('Data de nascimento:')
    infomações['mes_de_nascimento']=leiaint('Mês de nascimento:')
    infomações['ano_de_nascimento']=leiaint('Ano de nascimento:')
    infomações['turno']=leiaint('Manha ou tarde(0 para manhã e 1 para de tarde):')
    escolha2=leiaint('1 para sair do programa 0 para continuar:')
    tudo.append(infomações.copy())
    
    if escolha2 == 1:
        break

alunosseparado=separador_de_salas(tudo)
tabela(alunosseparado)