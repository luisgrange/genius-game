'''
NOTA: Antes de rodar o código é necessário utilizar:

pip install -r requirements.txt

'''

import random as rd
import time 
import pyfiglet
import os

# Limpa a tela do terminal a cada vez que é chamada
def limpa_tela():
	os.system("cls" if os.name == "nt" else "clear")

# Gera uma lentra com base no índice da lista
def nova_letra():
	letras = "abcdefghijklmnopqrstuvwxyz"
	return letras[rd.randint(0, 25)]

# Verifica se a sequência está correta
def sequencia_correta(sequencia, usr_string):
	string_certa = ''
	for letra in sequencia:			# Para cada letra da variavel que a função recebe
		string_certa += letra  		# ela é concatenada para uma variavel que armazena a sequência certa
									
	if usr_string == string_certa:	# e retorna um valor booleano
		return True
	else:
		return False

def salvar(nome, pontos):
	salvamento = open("EstDadosGame.txt", "a")
	salvamento.write(f"Nome:{nome}\tPontuação:{pontos}\n")
	salvamento.close()

def jogo():
	limpa_tela()
	banner = pyfiglet.figlet_format("Genius Game")	# Biblioteca pyfiglet para criar banners
	print("="*75)
	print(banner)
	print("="*75)

	nome = input("Digite seu nome: ")
	pontuacao = 0
	sequencia_letras = []
	tempo = 3

	limpa_tela()

	while True:										# O loop mantem a "função principal" rodando
		sequencia_letras.append(nova_letra())		# a cada novo loop, uma letra da função é chamada e adicionada na pilha/lista
		print(f"As letras são: {sequencia_letras}")		
		time.sleep(tempo)
		limpa_tela()

		if sequencia_correta(sequencia_letras, input("Digite a sequencia: ")):	# caso a função `sequencia_correta` retorne True
			pontuacao += 10														# o tempo diminui e o jogo continua
			tempo = tempo - 0.1  												# e o erminal é limpo para a próxima sequência
			limpa_tela()

		else:																	# caso a função `sequencia_correta` retorne False
			limpa_tela()
			perdeu = pyfiglet.figlet_format("Voce perdeu !!")					# o pyfiglet gera um banner de fim de jogo bem discreto
			print(perdeu)														# e a pontuação é exibida junto do nome
			print(f"\nNome: {nome}\tPontuação: {pontuacao}")
			print(f"\nA sequência certa era: {sequencia_letras}")
			salvar(nome, pontuacao)
			return nome, pontuacao 												# retornamos o nome e a pontuaçã final para ser usado para
																				# exibir na tela posteriormente


if __name__ == "__main__":
	pontuacao_secao = []

	while True:																	# criamos outro loop infinito para manter o jogo
		nome, pontos = jogo()													# até que o usuário resolva sair
		pontuacao_secao.append({'Nome':nome, 'Pontos':pontos})
		jogar_novamente = input("Deseja jogar novamente S / N? ").upper()

		if jogar_novamente != "S":
			break

