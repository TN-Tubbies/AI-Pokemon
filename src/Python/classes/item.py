from abc import abstractmethod

class Item:
    def __init__(self):
        pass

    @abstractmethod
    def get_category(self):
        pass