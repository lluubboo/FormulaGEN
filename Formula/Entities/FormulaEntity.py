from abc import ABC


class FormulaEntity(ABC):
    """
    """
    tag = None

    @classmethod
    def getInstance(cls):
        return cls()
