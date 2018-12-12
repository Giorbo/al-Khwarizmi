from main import *
from random import *
from time import *

avl1 = open("performanceData/performanceAvl1.txt", "w+")
avl2 = open("performanceData/performanceAvl2.txt", "w+")
dic1 = open("performanceData/performanceDic1.txt", "w+")
dic2 = open("performanceData/performanceDic2.txt", "w+")

def performanceTestSeria():
	minimo = 88 #1717
	massimo = 12454 #4377
	b = 9 #7
	offset = 20
	avlll = avlLinkedList(minimo, massimo, b)
	check = True
	#listaInserimenti = [10, 100, 1000, 5000, 10000]
	
	listaInserimenti = []
	n = 50
	for i in range(200):
		listaInserimenti.append(i*n)
	print(listaInserimenti)

	for lenght in listaInserimenti:
		avlll = avlLinkedList(minimo, massimo, b)
		dic = {}
		listaPerFavorio = []
		for i in range(lenght):
			num = choice([randint(minimo,massimo), choice([randint(minimo-10000, minimo), 
				randint(massimo,massimo+10000)])])
			if num not in listaPerFavorio:
				listaPerFavorio.append(num)
			else:
				while check:
					num = choice([randint(minimo,massimo), choice([randint(minimo-10000, minimo), 
						randint(massimo,massimo+10000)])])
					if num not in listaPerFavorio:
						listaPerFavorio.append(num)
						check = False
				check = True
		##print(len(listaPerFavorio))
		print(lenght)

		#avl
		#insert time
		start = time()
		for elem in listaPerFavorio:
			avlll.insert(elem, str(elem))
		temporio = time() - start
		##print("AVLLL-Insert time for {} elements: {}".format(lenght, temporio))
		##print(avlll.counterList)
		#end insert

		#dictionary
		#insert time
		start = time()
		for elem in listaPerFavorio:
			dic[elem] = str(elem)
		temporio = time() - start
		##print("Dictionary-Insert time for {} elements: {}".format(lenght, temporio))
		#end insert


		#avl
		#search and avg times
		start = time()
		for elem in listaPerFavorio:
			avlll.search(elem)
		temporio = time() - start
		##print("AVLLL-Search time for {} elements: {}".format(lenght, temporio))
		##print("AVLLL-Average search time for {} elements: {}".format(lenght, temporio/lenght))
		#end search
		avl1.write("{}\t{}\n".format(lenght, temporio))

		#dictionary
		#search and avg times
		start = time()
		for elem in listaPerFavorio:
			dic[elem]
		temporio = time() - start
		##print("Dictionary-Search time for {} elements: {}".format(lenght, temporio))
		##print("Dictionary-Average search time for {} elements: {}".format(lenght, temporio/lenght))
		#end search
		dic1.write("{}\t{}\n".format(lenght, temporio))

		#avl
		#delete time
		start = time()
		for elem in listaPerFavorio:
			avlll.delete(elem)
		temporio = time() - start
		##print("AVLLL-Delete time for {} elements: {}".format(lenght, temporio))
		#end delete
		avl2.write("{}\t{}\n".format(lenght, temporio))

		#dictionary
		#delete time
		start = time()
		for elem in listaPerFavorio:
			dic.pop(elem)
		temporio = time() - start
		##print("Dictionary-Delete time for {} elements: {}".format(lenght, temporio))
		dic2.write("{}\t{}\n".format(lenght, temporio))


	avl1.close()
	avl2.close()
	dic1.close()
	dic2.close()