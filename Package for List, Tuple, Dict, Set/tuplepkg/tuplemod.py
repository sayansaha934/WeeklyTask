class pyTuple:
    def __init__(self, Tuple):
        if type(Tuple)==tuple:
            self.Tuple=Tuple
        else:
            raise Exception('Input type must be tuple')

    def Count(self, value):
        '''Return number of occurrences of value.'''
        try:
            j=0
            for i in range(len(self.Tuple)):
                if self.Tuple[i]==value:
                    j=j+1
            return j
        except Exception as e:
            return e

    def Index(self, value):
        '''Return first index of value.'''
        try:
            j=0
            for i in range(len(self.Tuple)):
                if self.Tuple[i]==value:
                    break
                j=j+1
            return j
        except Exception as e:
            return e