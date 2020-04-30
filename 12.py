#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um
#e permita que o usuário possa mostrar as notas de cada aluno individualmente.

cadastro = []

while True:
    aluno = []
    cadastro_nome = input('Informe o nome do aluno(a):')
    aluno.append(cadastro_nome)
    cadastro_nota1 = input(f'Informe a primeira nota do aluno(a) {cadastro_nome}: ')
    aluno.append(float(cadastro_nota1))
    cadastro_nota2 = input('Informe a segunda nota do aluno(a): ')
    aluno.append(float(cadastro_nota2))
    cadastro.append(aluno[:])
    decisao = input('Deseja continuar cadrastando alunos(as)?(S/N):')
    if decisao in 'Nn':
        break
print('''
--------------------------------------------
|                BOLETIM                   |
--------------------------------------------
''')
print('---------------------------------------------------------------')
for aluno in cadastro:
    print(f'{aluno[0]}: | Nota 1: {aluno[1]} | Nota 2: {aluno[2]} | Media: {(aluno[1] + aluno[2])/2}')
    print('---------------------------------------------------------------')
while True:
    opção = input('Deseja visualizar a nota de algum aluno individalemnte?(S/N): ')
    if opção in 'Ss':
        informe = int(input('Informe a posição do aluno que deseja consultar as notas: '))
        print('{}'.format(cadastro[informe - 1]))
    else:
        break
        