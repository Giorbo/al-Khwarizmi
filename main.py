

from list.DoubleLinkedList import ListaDoppiamenteCollegata as dLinkedList
from dictionary.dictTrees.avlTree import AVLTree as avl
from dictionary.Dictionary import Dictionary


class avlLinkedList(Dictionary):
    def __init__(self, min, max, b):
        assert (max > min), "max deve essere maggiore di min."
        assert (b > 6), "b deve essere maggiore di 6."
        assert ((abs(max - min)%b) == 0), "|max - min| deve essere multiplo di b."

        self.min = min
        self.max = max
        self.b = b
        self.d = (max-min)/b
        self.array = [None] * (d+2)

    def insert(self, key, value):
        #index selection:
        #int i will be the index.
        if (key < min):
            i = self.d
        elif (key >= max):
            i = self.d + 1
        else:
            for j in range(self.d - 1):
                if (self.min+(j*self.b)) <= inputKey < (self.min+j+1):
                    i = j
