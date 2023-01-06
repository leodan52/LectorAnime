
import datetime as dt
from tabulate import tabulate as tabla

def main():

	ruta = "/home/leodan52/Escritorio/"

	file_entrada = "anime_invierno_2023.txt"
	file_salida = "salida.txt"

	agnio = year_(file_entrada)

	entrada = open( ruta + file_entrada, "r")

	animes = []

	for i in entrada:
		anime = process(i)

		aux = anime_emision(anime[0])

		for j in anime:
			if j.find("shortname:") == 0:
				aux2 = j.replace("shortname:","").strip()
				aux.nombre_corto(aux2)
				anime.remove(j)

		try:
			aux.fecha_estreno(anime[1] + " " + agnio)
		except IndexError:
			pass

		try:
			aux.Plataforma(anime[2])
		except IndexError:
			pass

		animes.append(aux)

	salida = open(file_salida, "w")

	pBloque1(salida,animes)
	pBloque2(salida,animes)
	pBloque3(salida,animes)
	pBloque4(salida,animes)

def pBloque1(File,lista):
	lista = ordenar(lista,0)
	print("\nLos animes que se estrenan en la siguiente temporada son:\n", file=File)

	for i in lista:
		imprimirAnime(i, File)

def pBloque2(File,lista):

	plataf = []

	for i in lista:
		if i.plataforma not in plataf:
			plataf.append(i.plataforma)

	plataf = ordenar_alpha(plataf)

	if "Por definir" in plataf:
		plataf.remove("Por definir")
		plataf.append("Por definir")
	else:
		plataf.append("")

	for i in plataf:
		if plataf.index(i) == 0:
			print("\nDe los cuales, en", i, "se veran:\n",file=File)
		elif plataf[-2] == i and plataf[0] != i :
			print("\nY en", i, ":\n",file=File)
		elif i == "Por definir":
			print("\nFaltan por definir:\n",file=File)
		elif i != "":
			print("\nEn", i, ":\n" ,file=File)

		for j in lista:
			if j.plataforma == i:
				imprimirAnime(j, File)

def pBloque3(File,lista):

	lista = ordenar_fecha(lista)
	aux = ""

	print("\nEl calendario de estrenos es el siguiente: ", file=File)

	for i in lista:
		if i.f_estreno != aux:
			print("\n" + i.f_estreno + "\n",file=File)
			aux = i.f_estreno
		imprimirAnime(i, File, mostrar_plataforma=True)

def pBloque4(File,lista):

	lista = ordenar(lista,0)

	weekdays = ("Domingo" , "Lunes", "Martes", "Miércoles", "Jueves", "Viernes" , "Sábado")

	Horario = {day : [] for day in weekdays}

	for i in lista:
		if i.shortname == "None":
			nombre = i.nombre
		else:
			nombre = i.shortname

		Horario[i.dia].append(nombre)

	print("\nEl horario semanal queda de la siguiente forma:\n", file=File)

	print(tabla(Horario, headers="keys") + "\n", file=File)


def ordenar_fecha(lista):
	n = len(lista)

	for i in range(n):
		for j in range(n):
			if lista[i].estreno < lista[j].estreno:
				lista[i],lista[j] = lista[j],lista[i]

	return ordenar(lista)

def ordenar(lista,p = 1):
	n = len(lista)

	for i in range(n):
		for j in range(n):
			if p == 1:
				if lista[i].nombre.lower() < lista[j].nombre.lower() and lista[i].f_estreno == lista[j].f_estreno:
					lista[i],lista[j] = lista[j],lista[i]
			elif p == 0:
				if lista[i].nombre.lower() < lista[j].nombre.lower():
					lista[i],lista[j] = lista[j],lista[i]
	return lista

def ordenar_alpha(lista):
	n = len(lista)

	for i in range(n):
		for j in range(n):
			if lista[i].lower() < lista[j].lower():
				lista[i],lista[j] = lista[j],lista[i]

	return lista


def process(entrada):
	especiales = [[".","*punto*"]]

	i = entrada.strip()

	for j in especiales:
		i = i.replace("\\" + j[0],j[1])

	aux = []

	for j in i.split("."):
		j = j.strip()

		if j == "":
			continue

		for k in especiales:
			j = j.replace(k[1],k[0])

		aux.append(j)

	return aux

def year_(cadena):
	aux = cadena.replace(".txt","").split("_")

	return aux[2]


def imprimirAnime(anime, File, mostrar_plataforma=False):
	if anime.shortname == "None":
		print("\t" + f'{anime.nombre}', file=File, end=" ")
	else:
		print("\t" + f'{anime.nombre} \t ({anime.shortname})', file=File, end=" ")


	if mostrar_plataforma and anime.plataforma != "Por definir":
		print(f' (En {anime.plataforma})', file=File)
	else:
		print(file=File)


class anime_emision:


	def __init__(self,nom):
		self.nombre = nom
		self.estreno = "Sin fecha de estreno"
		self.shortname = "None"
		self.plataforma = "Por definir"

	def fecha_estreno(self,fecha):

		meses = ("","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
		weekdays = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes" , "Sábado", "Domingo")

		if fecha.strip().lower() == "none":
			return

		aux = fecha.split(" ")

		dia = int(aux[0])
		mes = meses.index(aux[1].capitalize().strip())
		anio = int(aux[2])

		self.estreno = dt.date(anio,mes,dia)
		self.dia = weekdays[self.estreno.weekday()]
		self.f_estreno = str(self.estreno.day) + " " + meses[self.estreno.month]

	def nombre_corto(self,sname):
		self.shortname = sname

	def Plataforma(self,nombre):
		if nombre.strip().lower() == "none":
			return
		self.plataforma = nombre


main()
