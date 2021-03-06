class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs one or more times in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals:
            return self.vals[e]
        else:
            return 0

    def __add__(self,other):
        """ returns the sum of dict values for same keys across instances"""
        combo = {}
        for val in self.vals:
            if val in combo:
                combo[val] += self.vals[val]
            else:
                combo[val] = self.vals[val]
        for val in other.vals:
            if val in combo:
                combo[val] += other.vals[val]
            else:
                combo[val] = other.vals[val]
        self.vals = combo
        return Container.__str__(self)

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals:
            self.vals.pop(e)

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        return True if e in self.vals else False
