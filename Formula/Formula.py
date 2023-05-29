from Formula.BoundaryConditions import BoundaryConditions
from Formula.FormulaFactory import FormulaFactory


class Formula:
    """
    Class represents math formula
    """
    __boundaryConditions = BoundaryConditions()
    __formula = None

    def evaluate(self, node):
        # if node.is_leaf():
        #     return node.data.getValue()
        # else:
        #     return evaluate() + evaluate()
        pass

    def generateRandomRecursion(self):
        fGen = FormulaFactory(self.__boundaryConditions)
        self.__formula = fGen.generateRandomFormula()

    def generateRandomCode(self):
        fGen = FormulaFactory(self.__boundaryConditions)
        self.__formula = fGen.generateRandomFormulaCode()

    def getFormula(self):
        return self.__formula

    def getFormulaBoundaryConditions(self):
        return self.__boundaryConditions
