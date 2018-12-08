from dictionary.linkedListDictionary import LinkedListDictionary as linkedList
from dictionary.dictTrees.avlTree import AVLTree as avl
from dictionary.Dictionary import Dictionary

# Functions:

def getIndex(massimo, minimo, b, d, key):
    if (key < minimo):
        i = d
    elif (key >= massimo):
        i = d + 1
    else:
        for j in range(d - 1):
            if (minimo+(j*b)) <= key < (minimo+(j+1)*b):
                i = j
    return i


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
        self.array = [None] * (self.d+2)
        self.counterList = [0]*(self.d+2)

    def insert(self, key, value):
        #index selection:
        #int i will be the index.
        i = getIndex(self.massimo, self.minimo, self.b, self.d, key)

		#check if array[i] is avlTree or linkedList
        if isinstance(self.array[i], avl):
            self.array[i].insert(key, value)
            self.counterList[i] += 1
        else:
            if self.array[i] == None:
                self.array[i] = linkedList()
                self.array[i].insert(key,value)
                self.counterList[i] += 1
            else:
                self.array[i].insert(key,value)
                self.counterList[i] += 1
                #check if counterList has more than r elements
                if self.counterList[i] >= self.r:
                    self.__linkedListToAvl(i)

    def delete(self, key):
        #index selection:
        #int i will be the index.
        i = getIndex(self.massimo, self.minimo, self.b, self.d, key)

        if isinstance(self.array[i], avl):
            self.array[i].delete(key)
            self.counterList[i] -= 1
            #check if counterList has more than r elements
            if self.counterList[i] < self.r:
                self.__avlToLinkedList(i)
        else:
            assert (self.array[i].theList.first != None), "la LinkedList al posto i e' gia' vuota."
            self.array[i].delete(key)
            self.counterList[i] -= 1


    def __linkedListToAvl(self, index):
        current = self.array[index].theList.first
        tempAvl = avl()
        while current != None:
            tempAvl.insert(current.elem[0], current.elem[1])
            current = current.next
        self.array[index] = tempAvl

    def __avlToLinkedList(self, index):
        tempLinkedList = linkedList()
        for i in range(self.counterList[index]):
            rootKey = self.array[index].tree.root.info[0]
            rootValue = self.array[index].tree.root.info[1]
            tempLinkedList.insert(rootKey, rootValue)
            self.array[index].delete(rootKey)
        self.array[index] = tempLinkedList
