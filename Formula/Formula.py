from Formula.BoundaryConditions import BoundaryConditions


class Formula:
    """
    Class represents math formula.
    Formula is represented by binary tree data structure type.
    """
    __boundaryConditions = BoundaryConditions()
    __formula = None

    def __init__(self, tree, boundaryConditions):
        self.__formula = tree
        self.__boundaryConditions = boundaryConditions

    def evaluate(self, node):
        # if node.is_leaf():
        #     return node.data.getValue()
        # else:
        #     return evaluate() + evaluate()
        pass

    def getFormula(self):
        return self.__formula

    def getFormulaBoundaryConditions(self):
        return self.__boundaryConditions
