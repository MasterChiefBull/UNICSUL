## PIT - ClipNote_Luís Tiago Medeiros Raunheitte_25853953

import datetime
from datetime import date

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

DIASescrito = [
    ['Segunda feira','Segunda','Seg','seg','segunda','segunda feira'],
    ['Terça feira','terça feira','Terça','Ter', 'ter','terça'],
    ['Quarta feira','Quarta','Qua','qua','quarta','quarta feira'],
    ['Quinta feira','Quinta','Qui','qui','quinta','quinta feira'],
    ['Sexta feira','Sexta','Sex','sex','sexta','sexta feira'],
    ['Sábado','sabado','Sabado','sab','Sab'],
    ['Domingo','dom','domingo','Dom']
]

def dias(d):
	if   (d in DIASescrito[0]):
		return 0
	elif (d in DIASescrito[1]):
		return 1
	elif (d in DIASescrito[2]):
		return 2
	elif (d in DIASescrito[3]):
		return 3
	elif (d in DIASescrito[4]):
		return 4
	elif (d in DIASescrito[5]):
		return 5
	elif (d in DIASescrito[6]):
		return 6
	else:
 		print('Escreva o dia da semana em um formato diferente.')
 		newagenda()

Notes  = {}
Agend = []
op     = 10
ag     = True
t      = True

def menu ():
	print(40*'+')
	print('0 	- Cadastrar nova agenda.')
	print('1 	- Incluir nova anotação.')
	print('2	- Ver todas anotações.')
	print('3 	- Excluir anotação.')
	print('4 	- Sair.')
	print(40*'+')

def Agenda():	
	Nome = str(input(' Informe o nome da sua atividade: '))
	D    = dias(str(input(' Informe o dia da semana da atividade: ')))
	hi   = int(input(' Informe a hora inicial da atividade: '))
	mi   = int(input(' Informe o minuto  inicial da atividade: '))
	hf   = int(input(' Informe o horario final da atividade: '))
	mf   = int(input(' Informe o minuto final da atividade: '))
	Agend.append([Nome,D,hi+mi/60,hf+mf/60])
	Notes[Nome]=[]
	# print(Agenda)
	# sleep(20) 

def newagenda():
	while True:
		a = str(input('Cadastrar nova atividade na agenda (S/N) : '))
		if a == 'S': # or a== 's'):
			Agenda()
			newagenda()
		else: # or a=='n'):
			break
		#else:
			# a=input('Cadastrar nova atividade na agenda (S/N) : ')

menu()

op = int(input("\n Digite a opcao desejada: "))

while t==True:
	if op == 0:
		print('Criando nova Agenda... \n')
		newagenda()
		print(Agend)
		print('\n')
		menu()
		op = int(input("\n Digite a opcao desejada: "))
	
	elif op == 1:
		print('Criando nova Anotacao... \n')
				# op=0
		x 		= datetime.datetime.now()   #traz dia e hora
		xweek	= x.weekday() # dia da semana de 0 a 6 que pode converter usando vetor DIAS
		 									# print(DIAS[x.weekday()])   # Monday is 0 and Sunday is 6
		hdec	= float(str(x)[11:13])+float(str(x)[14:16])/60 # horario em decimal
		#se o evento existe na agenda execute:
		for i in Agend:
			if ((xweek in i) and (i[2]<=hdec<=i[3])):
				ativ=i[0]
				note 	= str(input("\n O que voce deseja anotar: \n\n"))
				if ativ in Notes.keys():
					Notes[ativ].append([str(date.today()),note])
				else:
					Notes[ativ]=[[str(date.today()),note]]
			else:
				print('não existe atividade cadastrada na agenda para este horario, cadastre ela na agenda antes de iniciar a anotação.')
				menu()
				op = int(input("\n Digite a opcao desejada: "))
											# print(Notes)
		print('\n')
		menu()
		op = int(input("\n Digite a opcao desejada: "))
	
	elif op == 2:		###	
		# op=0
		# print("\n Todas suas anotacoes: \n\n")
		# for i in Notes:
		# 	op+=1
		# 	print (str(op)+' - ' + i + '\n')
		# 	print(Notes)
		op=0
		print("\n Todas suas anotacoes: \n\n")
		keys=Notes.keys()
		for i in Agend:
			op+=1
			print (i[0]+'\n')
			# value=Notes[i[0]].values()
			if Notes[i[0]]!= []:
				for n in Notes[i[0]]:
					print(n)
			else:
				print ( str(i[0]) + 'Atividade ainda sem anotações... ')
		print('\n')
		menu()
		op = int(input("\n Digite a opcao desejada: "))

	elif op == 3:			
		op=0		
		for i in Notes:
			op+=1
			print (str(op)+' - ' + i + '\n')
		delete = input('Qual anotacao deseja apagar... \n')
		Notes.pop(delete)
		print('\n a anotacao foi removida com sucesso. \n')
		menu()
		op = int(input("\n Digite a opcao desejada: "))

	elif op == 4:			
		print('Voce escolheu sair do bloco de notas.')
		resp = str(input('Confirma: S/N ... '))
		if resp == ('S' or 's'):
			print('saindo do bloco de notas... \n')
			t=False
		else:
			op=10
			menu()
			op = int(input("\n Digite a opcao desejada: "))

# para melhorar esse programa eu posso oferecer a opcao de criar uma nova lista para cada dia
'''
criar uma agenda de hora e dia da semana com as atividades
criar listas para cada dia da semana 
pedir data e hora antes de guardar nova anotacao
fazer a selecao if else para encontrar em qual lista devo armazenar a nova nota


É importante observar que o método weekday() da classe date retorna o dia da semana como um número inteiro, onde 0 representa a segunda-feira e 6 representa o domingo.
indice_da_semana = data.weekday()
date.today() traz o dia
date.now()   traz dia e hora

x=datetime.datetime.now()   #traz dia e hora
print(DIAS[x.weekday()])   # Monday is 0 and Sunday is 6
print(x) 

 '''
# print('wOw')  #ctrl + cmd + L = editor de varias linhas
							# CTRL + ? comenta a linha atual

#Desenvolvido por Prô Terra - MakerZine
#Para mais detalhes, acesse: https://www.makerzine.com.br

		# x=datetime.datetime.now()   #traz dia e hora
		# xweek=x.weekday() # dia da semana de 0 a 6 que pode converter usando vetor DIAS
		# # print(DIAS[x.weekday()])   # Monday is 0 and Sunday is 6
		# hdec=float(str(x)[11:13])+float(str(x)[14:16])/60 # horario em decimal
		# note=str(input("\n O que voce deseja anotar: \n\n"))
		# Notes.append(note)
		# # print(Notes)