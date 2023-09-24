# When to use static methods and class methods

class Item:
    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship with the class
        but not something that must be unique per instance!
        '''

    @classmethod
    def instantiate_read_something(cls):
        '''
        This should also do something that has a relationship
        with the class, but usually, those are used to manipulate
        different structures of data to istantiate objects, like we
        have done with CSV.
        '''