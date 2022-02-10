class pyList:
    def __init__(self, List):
        if type(List)==list:
            self.List=List
        else:
            raise Exception('Input type must be list')
    def Append(self, item):
        '''Append object to the end of the list.'''

        try:
            self.List = self.List + [item]
        except Exception as e:
            return e

    def Clear(self):
        '''Remove all items from list.'''
        try:
            self.List=[]
        except Exception as e:
            return e

    def Copy(self):
        '''Return a shallow copy of the list.'''
        return self.List

    def Count(self, value):
        '''Return number of occurrences of value.'''
        try:
            j=0
            for i in range(len(self.List)):
                if self.List[i]==value:
                    j=j+1
            return j
        except Exception as e:
            return e

    def Extend(self, iterable):
        '''Extend list by appending elements from the iterable.'''
        try:
            ext=pyList(self.List)
            for i in iterable:
                ext.Append(i)
            self.List = ext.List
        except Exception as e:
            return e

    def Index(self, value):
        '''Return first index of value.'''
        try:
            if value in self.List:
                j=0
                for i in range(len(self.List)):
                    if self.List[i]==value:
                        break
                    j=j+1
                return j
            else:
                raise ValueError(f'{value} is not in list')
        except Exception as e:
            return e

    def Insert(self, index, object):
        '''Insert object before index.'''
        try:
            self.List = self.List[:index] + [object] + self.List[index:]
        except Exception as e:
            return e

    def Pop(self, index=-1):
        '''Remove and return item at index (default last).'''
        try:
            a=self.List[index]
            self.List = [i for i in self.List if i!=a]
            return a
        except Exception as e:
            return e

    def Remove(self, value):
        '''Remove first occurrence of value.'''
        try:
            if value in self.List:
                li_len=len(self.List)
                j=0
                for i in range(li_len):
                    if self.List[i]==value:
                        break
                    j=j+1
                self.List=[self.List[i] for i in range(li_len) if i!=j]
            else:
                raise ValueError(f'{value} not in list')
        except Exception as e:
            return  e

    def Reverse(self):
        '''Reverse *IN PLACE*.'''
        try:
            self.List = self.List[::-1]
        except Exception as e:
            return  e

    def Sort(self, reverse=False):
        '''Sort the list in ascending order and return None.'''
        try:
            li=pyList([])
            pyli=pyList(self.List)
            for j in range(len(pyli.List)):
                minimum = pyli.List[0]
                for i in pyli.List:
                    if i < minimum:
                        minimum = i
                li.Append(minimum)
                pyli.Remove(minimum)
            if reverse:
                self.List = li.List[::-1]
            else:
                self.List = li.List
        except Exception as e:
            return e