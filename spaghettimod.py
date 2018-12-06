from list.LinkedList import ListaCollegata as linkedList
from dictionary.dictTrees.avlTree import AVLTree as avl
from dictionary.Dictionary import Dictionary


class avlLinkedList(Dictionary):
    def __init__(self, minimo, massimo, b):
        assert (massimo > minimo), "massimo deve essere maggiore di minimo."
        assert (b > 6), "b deve essere maggiore di 6."
        assert ((abs(massimo - minimo)%b) == 0), "|massimo - minimo| deve essere multiplo di b."

        self.minimo = minimo
        self.massimo = massimo
        self.b = b
        self.r = 6
        self.d = int((massimo-minimo)/b)
        self.array = [None] * int((self.d+2))
        #Modified
        self.counterList = [0]*(d+2)
        #endMod

    def insert(self, key, value):
        #index selection:
        #int i will be the index.
        if (key < self.minimo):
            i = self.d
        elif (key >= self.massimo):
            i = self.d + 1
        else:
            for j in range(self.d - 1):
                if (self.minimo+(j*self.b)) <= key < (self.minimo+(j+1)*self.b):
                    i = j
		#check if array[i] is avlTree or linkedList
        if type(self.array[i])=='dictionary.dictTrees.avlTree':
            self.array[i].insert(key, value)
            #mod
            self.counterList[i] += 1
            #mod
        else:
            if self.array[i] == None:
                self.array[i] = linkedList()
                self.array[i].addAsFirst((key,value))
                #mod
                self.counterList[i] += 1
                #mod
            else:
                self.array[i].addAsLast((key,value))
                #mod
                self.counterList[i] += 1
                #mod
                    
    def linkedListToAvl(self, index):
