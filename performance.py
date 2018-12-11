from main import *
from random import *
from time import *


def performanceavlll():
	minimo = 1717
	massimo = 4377
	b = 7


	listavlll = []

	listaCifre = [10, 100]
	listaSegno = [-1, 1]

	for i in range(10000):
		listavlll.append(int(random()*choice(listaCifre)*choice(listaSegno)))
	

	for elem in listavlll:
		avlll.insert(elem, str(elem))

	listavlll.reverse()

	for elem in listavlll:
		avlll.delete(elem)

def performanceTestSeria():
	minimo = 4
	massimo = 25
	b = 7
	offset = 20
	avlll = avlLinkedList(minimo, massimo, b)

	listaInserimenti = [10, 100, 1000, 5000, 10000, 1000000]
	for lenght in listaInserimenti:
		avlll = avlLinkedList(minimo, massimo, b)
		dic = {}
		listaPerFavorio = []
		check = True
		for i in range(lenght):
			num = randint(minimo-offset, massimo+offset)
			if num not in listaPerFavorio:
				listaPerFavorio.append(num)
			else:
				while check:
					num = randint(minimo-offset, massimo+offset)
					if num not in listaPerFavorio:
						listaPerFavorio.append(num)
						check = False
		print(len(listaPerFavorio))


		#avl
		#insert time
		start = time()
		for elem in listaPerFavorio:
			avlll.insert(elem, str(elem))
		temporio = time() - start
		print("AVLLL-Insert time for {} elements: ".format(lenght)+str(temporio))
		#end insert

		#dictionary
		#insert time
		start = time()
		for elem in listaPerFavorio:
			dic[elem] = str(elem)
		temporio = time() - start
		print("Dictionary-Insert time for {} elements: ".format(lenght)+str(temporio))
		#end insert


		#avl
		#search and avg times
		start = time()
		for elem in listaPerFavorio:
			avlll.search(elem)
		temporio = time() - start
		print("AVLLL-Search time for {} elements: ".format(lenght)+str(temporio))
		print("AVLLL-Average search time for {} elements: ".format(lenght)+str(temporio/lenght))
		#end search

		#dictionary
		#search and avg times
		start = time()
		for elem in listaPerFavorio:
			dic[elem]
		temporio = time() - start
		print("Dictionary-Search time for {} elements: ".format(lenght)+str(temporio))
		print("Dictionary-Average search time for {} elements: ".format(lenght)+str(temporio/lenght))
		#end search

		#avl
		#delete time
		start = time()
		#listaPerFavorio.reverse()
		for elem in listaPerFavorio:
			avlll.delete(elem)
		temporio = time() - start
		print("AVLLL-Delete time for {} elements: ".format(lenght)+str(temporio))
		#end delete

		#dictionary
		#delete time
		start = time()
		#listaPerFavorio.reverse()
		for elem in listaPerFavorio:
			dic.pop(elem)
		temporio = time() - start
		print("Dictionary-Delete time for {} elements: ".format(lenght)+str(temporio))
