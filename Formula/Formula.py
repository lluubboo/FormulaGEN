from treelib import Tree, Node

from Formula.BoundaryConditions import BoundaryConditions
from Formula.Entities.Operator import Operator


class Formula:
    """
    Class represents math formula.
    Formula is represented by binary tree data structure type.
    """
    __boundaryConditions: BoundaryConditions
    __formula: Tree

    def __init__(self, tree: Tree, boundaryConditions: BoundaryConditions):
        self.__formula = tree
        self.__boundaryConditions = boundaryConditions

    def evaluateFormula(self):
        result = "NaN"
        if self.__formula:
            nodes = self.__formula.nodes
            result = self.__evaluate(nodes.get('root'))
        else:
            print("Formula does not exist")
        return result

    def __evaluate(self, node: Node):
        if node.is_leaf():
            return node.data.value
        else:
            successors = self.__formula.children(node.identifier)
            return self.__evaluateOperation(node.data, self.__evaluate(successors[0]),
                                            self.__evaluate(successors[1]))

    def __evaluateOperation(self, operator: Operator, varA, varB):
        if operator.isAddition():
            return varA + varB
        elif operator.isDivision():
            return varA / varB
        elif operator.isSubtraction():
            return varA - varB
        elif operator.isMultiplication():
            return varA * varB

    def getFormula(self):
        return self.__formula

    def getFormulaBoundaryConditions(self):
        return self.__boundaryConditions
