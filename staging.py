#####################
##### METHODS #######
#####################
    def insert(self, key, value):
        #index selection:
        #int i will be the index.
        i = getIndex(self.massimo, self.minimo, self.b, self.d, key)

        if self.array[i]==None:
        	self.array[i]=linkedList()
        self.array[i].insert(key, value)
        self.counterList[i]+=1
        if self.counterList[i]==6:
        	self.__linkedListToAvl(i)

    def delete(self, key):
        #index selection:
        #int i will be the index.
        i = getIndex(self.massimo, self.minimo, self.b, self.d, key)

        self.array[i].delete(key)
        self.counterList[i]-=1

        if self.counterList[i]==5:
        	self.__avlToLinkedList(i)

#####################
##### FUNCTIONS #####
#####################

