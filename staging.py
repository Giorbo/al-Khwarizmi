#####################
##### METHODS #######
#####################

'''il metodo non è ancora finito, bisogna capire come gestire
    elementi con key uguali e sara' un bel dito in culo.'''
    def delete(self, key):
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
        if isinstance(self.array[i], avl):
            self.array[i].delete(key)

        [...]


#####################
##### FUNCTIONS #####
#####################

'''questa funzione ritorna l'indice e sembrerebbe
    il modo migliore per implementare la scelta senza
    appesantire il codice, non essendo un metodo va definita
    fuori dalla classe, mi sono informato e non sembrerebbe
    bad practice, per me e' da mettere. La time complexity e'
    bassa quindi non vedo il motivo di caricare la nostra classe
    di attributi per ogni Bi.'''

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
