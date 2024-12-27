from abc import abstractmethod

class Item:
    def __init__(self):
        pass
    @abstractmethod
    def __eq__(self, other):
        pass
    @abstractmethod
    def __ne__(self, other):
        pass

    @abstractmethod
    def get_category(self):
        pass

    @abstractmethod
    def use(self, target):
        pass