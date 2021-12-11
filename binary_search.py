from random import randint

lista = range(0, 101)

num = randint(0, 101)

chute = 0

while chute != num:

	chute = lista[0] + ((lista[-1] - lista[0]) // 2)
	if chute > num:
		input(f'Numero alto, seu chute foi {chute}')
		lista = range(lista[0], chute + 1)

	if chute < num:
		input(f'Numero baixo, seu chute foi {chute}')
		lista = range(chute, lista[-1] + 1)

print(f'Acertou o nro {num}')
