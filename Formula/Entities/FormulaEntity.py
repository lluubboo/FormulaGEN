from abc import ABC


class FormulaEntity(ABC):
    """
    """

    def __init__(self):
        pass

    @classmethod
    def getInstance(cls):
        return cls()
