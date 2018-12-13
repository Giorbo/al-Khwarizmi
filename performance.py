from main import *
from random import *
from time import *


avl1 = open("performanceData/performanceAvl1.txt", "w+")
avl2 = open("performanceData/performanceAvl2.txt", "w+")
dic1 = open("performanceData/performanceDic1.txt", "w+")
dic2 = open("performanceData/performanceDic2.txt", "w+")

def randomList(lenght):
    minimo = 88 
    massimo = 12454 
    b = 9
    check = True

    listRandom = []
    for i in range(lenght):

        num = choice([randint(minimo,massimo), choice([randint(minimo-10000, minimo), 
            randint(massimo,massimo+10000)])])

        if num not in listRandom:
            listRandom.append(num)

        else:
            while check:

                num = choice([randint(minimo,massimo), choice([randint(minimo-10000, minimo), 
                    randint(massimo,massimo+10000)])])

                if num not in listRandom:
                    listRandom.append(num)
                    check = False

            check = True
    #print(listRandom)
    #print(len(listRandom))
    return listRandom





def testPerformance(size):
    for n in range(0, size+1, 100):
        avlll = AvlLinkedList(88,12454,9)
        dic = {}
        if n == 0:
            continue
        print(n)

        listRandom = randomList(n)
        #insert    
        for elem in listRandom:
            avlll.insert(elem, str(elem))

        for elem in listRandom:
           dic[elem] = str(elem)
        #/insert

    	#avl-search and avg times
        start = time()
        for elem in listRandom:
           avlll.search(elem)
        tempo = time() - start
    	#end
        avl1.write("{}\t{}\n".format(n, tempo/n))
    	

        #dictionary-search and avg times
        start = time()
        for elem in listRandom:
           dic[elem]
        tempo = time() - start
        dic1.write("{}\t{}\n".format(n, tempo/n))
        #end
    	
        #avl-delete time
        start = time()
        for elem in listRandom:
           avlll.delete(elem)
        tempo = time() - start
    	#end
        avl2.write("{}\t{}\n".format(n, tempo/n))

    	#dictionary-delete time
        start = time()
        for elem in listRandom:
           dic.pop(elem)
        tempo = time() - start
        dic2.write("{}\t{}\n".format(n, tempo/n))
        #end
    
    avl1.close()
    avl2.close()
    dic1.close()
    dic2.close()