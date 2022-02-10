class pySet:
    def __init__(self, Set):
        if type(Set)==set:
            self.Set=Set
        else:
            raise Exception('Input type must be Set')

    def Add(self, item):
        '''Add an element to a set.'''
        try:
            self.Set=self.Set|{item}
        except Exception as e:
            return e

    def Clear(self):
        '''Remove all items from set.'''
        try:
            self.Set=set()
        except Exception as e:
            return e

    def Copy(self):
        '''Return a shallow copy of the set.'''
        return self.Set

    def Difference(self, *args):
        '''Return the difference of two or more sets as a new set.'''
        try:
            diff=self.Set
            for i in args:
                d=diff & set(i)
                diff=diff-d
            return diff
        except Exception as e:
            return e

    def Difference_Update(self, *args):
        '''Remove all elements of another set from this set.'''
        try:
            for i in args:
                diff=self.Set & set(i)
                self.Set=self.Set - diff
        except Exception as e:
            return e

    def Discard(self, item):
        '''Remove an element from a set if it is a member.'''
        try:
            self.Set = self.Set - {item}
        except Exception as e:
            return e

    def Intersection(self, *args):
        '''Return the intersection of two sets as a new set.'''
        try:
            new=self.Set
            for i in args:
                new=new & set(i)
            return new
        except Exception as e:
            return e
    def Intersection_Update(self, *args):
        '''Update a set with the intersection of itself and another.'''
        try:
            for i in args:
                self.Set=self.Set & set(i)
        except Exception as e:
            return e

    def IsDisJoint(self, item):
        '''Return True if two sets have a null intersection.'''
        try:
            if (self.Set & set(item))==set():
                return True
            else:
                return False
        except Exception as e:
            return e

    def IsSubset(self, item):
        '''Report whether another set contains this set.'''
        try:
            if self.Set & set(item) == self.Set:
                return True
            else:
                return False
        except Exception as e:
            return e

    def IsSuperset(self, item):
        '''Report whether this set contains another set.'''
        try:
            if self.Set & set(item) == set(item):
                return True
            else:
                return False
        except Exception as e:
            return e

    def Pop(self):
        '''Remove and return an arbitrary set element.
            Raises KeyError if the set is empty.'''
        try:
            if self.Set == set():
                raise KeyError
            else:
                pop_item = list(self.Set)[0]
                self.Set = self.Set - {pop_item}
                return  pop_item
        except Exception as e:
            return e

    def Remove(self, item):
        '''Remove an element from a set; it must be a member.'''
        try:
            se_list=list(self.Set)
            if item in se_list:
                new_set = [i for i in se_list if i!= item]
                self.Set = set(new_set)
            else:
                raise KeyError(item)
        except Exception as e:
            return e

    def Symmetric_Difference(self, item):
        '''Return the symmetric difference of two sets as a new set.'''
        try:
            intersection = self.Set & set(item)
            union = self.Set | set(item)
            new_set =  union - intersection
            return new_set
        except Exception as e:
            return e

    def Symmetric_Difference_Update(self, item):
        '''Update a set with the symmetric difference of itself and another.'''
        try:
            intersection = self.Set & set(item)
            union = self.Set | set(item)
            self.Set =  union - intersection
        except Exception as e:
            return e

    def Union(self,item):
        '''Return the union of sets as a new set.'''
        try:
            union = self.Set | set(item)
            return union
        except Exception as e:
            return e

    def Update(self, *args):
        '''Update a set with the union of itself and others.'''
        try:
            for i in args:
                self.Set = self.Set | set(i)
        except Exception as e:
            return e
