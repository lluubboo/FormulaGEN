from Formula.Entities.FormulaEntity import FormulaEntity


class Operator(FormulaEntity):

    def __init__(self):
        super().__init__()
        self.tag = self.__class__.__name__

    def isAdition(self):
        return isinstance(self, Addition)

    def isDivision(self):
        return isinstance(self, Division)

    def isSubtraction(self):
        return isinstance(self, Subtraction)

    def isMultiplication(self):
        return isinstance(self, Multiplication)


class Subtraction(Operator):
    """
    """

    def __init__(self):
        super().__init__()


class Addition(Operator):
    """
    """

    def __init__(self):
        super().__init__()


class Multiplication(Operator):
    """
    """

    def __init__(self):
        super().__init__()


class Division(Operator):
    """
    """

    def __init__(self):
        super().__init__()

