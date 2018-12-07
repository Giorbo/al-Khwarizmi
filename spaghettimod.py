from dictionary.linkedListDictionary import LinkedListDictionary as linkedList
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
        self.array = [None] * (self.d+2)
        self.counterList = [0]*(self.d+2)

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
        if isinstance(self.array[i], avl):
            print('spippettone')
            self.array[i].insert(key, value)
            self.counterList[i] += 1
        else:
            if self.array[i] == None:
                print('ye')
                self.array[i] = linkedList()
                self.array[i].insert(key,value)
                self.counterList[i] += 1
            else:
                print('dynamint')
                self.array[i].insert(key,value)
                self.counterList[i] += 1
                #controllo se la lista ha più di r elementi
                if self.counterList[i] >= self.r:
                    self.__linkedListToAvl(i)


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
