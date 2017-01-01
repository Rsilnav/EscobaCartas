import itertools




mazo = []
def iniciarMazo():
	for i in range(4):
		for j in range(10):
			mazo.append(j+1)
	mazo.sort()

def quitardeMazo(x):
	print "asd"
	for carta in x:
		if carta not in x:
			raise "NOPE"
		else:
			mazo.remove(carta)

# Combinaciones posibles
def posibles(x):
	pos = []
	for L in range(0, len(x)+1):
		for subset in itertools.combinations(x, L):
			if sum(subset) < 15 and sum(subset) >= 5:
				t = 15 - sum(subset)
				if t not in pos:
					pos.append(t)
	return pos



def prob(x):
	return mazo.count(x)*100.0/len(mazo)

def main():
	iniciarMazo()

	

	while (True):

		l = raw_input("Que cartas te han tocado?")
		tus_cartas = map(int, l.strip().split(" "))
		quitardeMazo(tus_cartas)

		cartas_que_no_tiene = []

		# Para cada carta en la mano
		for i in range(3):

			# Lee el estado de la mesa
			l = raw_input("Que cartas hay en mesa?")
			cartas_mesa = map(int, l.strip().split(" "))

			# Turno rival
			su_carta = input("Que carta ha puesto?")
			quitardeMazo([su_carta])

			l = raw_input("Se ha llevado algo?")
			if l == "si":
				l = raw_input("Que cartas hay en mesa?")
				cartas_mesa = map(int, l.strip().split(" "))
			elif l == "no":
				pos = posibles(cartas_mesa)
				cartas_mesa.append(su_carta)
				for carta in pos:
					if carta not in cartas_que_no_tiene:
						cartas_que_no_tiene.append(carta)

			print "Tu contrincante no puede tener en la mano:", cartas_que_no_tiene

			print "Te toca poner!"
			print "Las cartas del mazo son...", mazo

		if len(mazo) <= 0:
			break

	


if __name__ == '__main__':
	main()