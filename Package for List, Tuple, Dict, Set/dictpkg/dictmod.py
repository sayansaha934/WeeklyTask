class pyDict:
    def __init__(self, Dict):
        if type(Dict)==dict:
            self.Dict=Dict
        else:
            raise Exception('Input type must be dictionary')


    def Clear(self):
        '''Remove all items from D.'''
        try:
            self.Dict={}
        except Exception as e:
            return e

    def Copy(self):
        '''Return a shallow copy of the D.'''
        return self.Dict

    def FromKeys(self, iterable, value=None):
        '''Create a new dictionary with keys from iterable and values set to value.'''
        try:
            d={}
            for key in iterable:
                d[key]=value
            return d
        except Exception as e:
            return e

    def Get(self, key, default=None):
        ''' Return the value for key if key is in the dictionary, else default.'''
        try:
            if key in self.Dict:
                return self.Dict[key]
            else:
                return default
        except Exception as e:
            return e

    def Items(self):
        '''D.items() -> a set-like object providing a view on D's items'''
        try:
            item=[]
            for key in self.Dict:
                value = self.Dict[key]
                item=item+[(key, value)]
            return item
        except Exception as e:
            return e


    def Keys(self):
        '''Provides D's key'''
        try:
            keys=[]
            for key in self.Dict:
                keys=keys+[key]
            return keys
        except Exception as e:
            return e

    def Pop(self, key):
        '''remove specified key and return the corresponding value.'''
        try:
            a=self.Dict[key]
            d = {}
            if key in self.Dict:
                for i in self.Dict:
                    if i!=key:
                        d[i]=self.Dict[i]
            else:
                raise KeyError(key)
            self.Dict=d
            return a
        except Exception as e:
            return e

    def PopItem(self):

        try:
            d = {}
            pydict=pyDict(self.Dict)
            last_key=list(pydict.Keys())[-1]
            last_val= pydict.Dict[last_key]
            for i in self.Dict:
                if i!=last_key:
                    d[i]=self.Dict[i]
            self.Dict=d
            return (last_key, last_val)
        except Exception as e:
            return e

    def SetDefault(self, key, default=None):
        try:
            if key in self.Dict:
                return self.Dict[key]
            else:
                self.Dict[key]=default
                return default
        except Exception as e:
            return e

    def Update(self, dict, **kwargs):
        '''Updates the dictionary'''
        try:
            iterdict=pyDict(dict)
            kwdict=pyDict(kwargs)
            for key, value in iterdict.Items():
                self.Dict[key]=value
            for key,value in kwdict.Items():
                self.Dict[key]=value
        except Exception as e:
            return e


    def Values(self):
        '''Returns the value of the D.'''
        try:
            d=[]
            for key in self.Dict:
                val=self.Dict[key]
                d=d+[val]
            return d
        except Exception as e:
            return e