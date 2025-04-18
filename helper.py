# When to use class methods and when to sue static methods?

class Item:
    @staticmethod
    def is_integer():
        # This hsould do something that has a relationship with the class, but not something that must be unique per instance!
        pass

    @classmethod
    def instantiate_from_something(cls):
        # This should also do something that has a relationship with the class, but usually, those are used to manipulate different structures of data to instantiate object, like we have done with CSV.
        pass




    # eugene
    # Barcelona2024!SSS