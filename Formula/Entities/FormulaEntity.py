
class FormulaEntity:
    """
    Class is superclass of all formula entities
    """
    tag = None

    @classmethod
    def getInstance(cls):
        return cls()
