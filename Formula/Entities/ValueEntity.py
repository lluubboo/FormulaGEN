from Formula.Entities.FormulaEntity import FormulaEntity


class ValueEntity(FormulaEntity):
    """
    Value entity is superclass of all formula entities with value [Constant, UserParameter].
    """
    value = None

    def __init__(self):
        super().__init__()

    def isConstant(self):
        return isinstance(self, Constant)

    def isVariable(self):
        return isinstance(self, UserParameter)

    def setValue(self, value):
        """
        Sets value of the entity. Tag of the entity is same as value.
        :param value:
        :return: void
        """
        self.value = self.tag = value


class Constant(ValueEntity):
    """
     Clas represents constants in standard understanding of the concept of a mathematical equation.
    """

    def __init__(self):
        super().__init__()


class UserParameter(ValueEntity):
    """
    Clas represents variables in standard understanding of the concept of a mathematical equation.
    """

    def __init__(self):
        super().__init__()
