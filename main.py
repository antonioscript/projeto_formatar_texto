#Conversor de Caracteres

def maiuscula():
	entrada = input("Digite seu texto: ")
	print("="*100)
	print(entrada.upper())
	print("="*100)
	apresentacao()

def minuscula():
	entrada = input("Digite seu texto: ")
	print("="*100)
	print(entrada.lower())
	print("="*100)
	apresentacao()

def titulo():
	entrada = input("Digite seu texto: ")
	print("="*100)
	print(entrada.title())
	print("="*100)
	apresentacao()

def apresentacao():
	print("-------------Formatar Texto---------------")
	print("[1] - Colocar todas as letras em Maiúsculas")
	print("[2] - Colocar todas as letra em Minúsculas")
	print("[3] - Colocar a primeira letra de cada palavra em Maíuscula")
	print("[4] - Sair")
	entrada = int(input("O que você quer fazer? "))
	if entrada == 1:
		maiuscula()
	elif entrada == 2:
		minuscula()
	elif entrada == 3:
		titulo()
	elif entrada == 4:
		exit()
	else:
		print("Comando Inválido!")
		print("Tente Novamente")
		apresentacao()

#Começar o programa
apresentacao()
