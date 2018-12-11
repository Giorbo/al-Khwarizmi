"""
    File name: AvlLinkedList.py
    Author: Francesco Lasco && Giorgio Luciano Liberatore
    Date created: 01/12/2018
    Date last modified: 14/12/2018
    Python Version: 3.7

    Questo modulo contiene la classe AvlLinkedList che rappresenta
    una struttura di dati che organizza dizionari costruiti con
    alberi AVL e liste collegate.
"""


from dictionary.linkedListDictionary import LinkedListDictionary as linkedList
from dictionary.dictTrees.avlTree import AVLTree as avl
from dictionary.Dictionary import Dictionary

class avlLinkedList(Dictionary):
    """
    Questa classe implementa un dizionario composto da un array che punta ad altre strutture dati.
    Le strutture (lista concatenata/albero avl) cambiano in base al numero di elementi presenti.
    """
    def __init__(self, minimo, massimo, b):
        assert (massimo > minimo), "massimo deve essere maggiore di minimo."
        assert (b > 6), "b deve essere maggiore di 6."
        assert ((abs(massimo - minimo)%b) == 0), "|massimo - minimo| deve essere multiplo di b."
        self.minimo = minimo
        self.massimo = massimo
        self.b = b
        self.r = 6
        self.d = int((massimo-minimo)/b)
        self.array = [None] * (self.d+2)
        self.counterList = [0]*(self.d+2)

    def insert(self, key, value):
        #index selection:
        #int i will be the index.
        i = self.__getIndex(key)
        if self.array[i] == None:
        	self.array[i] = linkedList()
        self.array[i].insert(key, value)
        self.counterList[i] += 1
        if self.counterList[i] == self.r:
            self.__linkedListToAvl(i)

    def delete(self, key):
        #index selection:
        #int i will be the index.
        i = self.__getIndex(key)
        assert(self.array[i] != None), "key not in data structure."
        if self.counterList[i] == 1:
            self.array[i] = None
            self.counterList[i] = 0
        else:
            self.array[i].delete(key)
            self.counterList[i] -= 1
            if self.counterList[i] == self.r - 1:
                self.__avlToLinkedList(i)

    def search(self, key):
        i = self.__getIndex(key)
        assert(isinstance(self.array[i], linkedList) or isinstance(self.array[i], avl)),"Error, the selected item can't be found in an existing set"
        return self.array[i].search(key)

    def __getIndex(self, key):
        """
        Questo metodo ausiliario calcola e ritorna l'indice Bi a partire dalla key.
        :param key:
        :return index:
        """
        if (key < self.minimo):
            index = self.d
        elif (key >= self.massimo):
            index = self.d + 1
        else:
            for i in range(self.d):
                if (self.minimo+(i*self.b)) <= key < (self.minimo+(i+1)*self.b):
                    index = i
        return index

    def __linkedListToAvl(self, index):
        """
        Questo metodo ausiliario trasforma il dizionario basato su lista collegata in
        un dizionario basato su albero avl
        :param index:
        :return:
        """
        current = self.array[index].theList.first
        tempAvl = avl()
        while current != None:
            tempAvl.insert(current.elem[0], current.elem[1])
            current = current.next
        self.array[index] = tempAvl

    def __avlToLinkedList(self, index):
        """
        Questo metodo ausiliario trasforma il dizionario basato su albero avl in
        un dizionario basato su lista collegata
        """
        tempLinkedList = linkedList()
        for i in range(self.counterList[index]):
            rootKey = self.array[index].tree.root.info[0]
            rootValue = self.array[index].tree.root.info[1]
            tempLinkedList.insert(rootKey, rootValue)
            self.array[index].delete(rootKey)
        self.array[index] = tempLinkedList
