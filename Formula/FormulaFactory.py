import random

from treelib import Tree
from Formula.BoundaryConditions import BoundaryConditions
from Formula.NodeFactory import NodeFactory


class FormulaFactory:
    """
    Class is formula generator
    """
    __generatedFormula = None
    __boundaryConditions = BoundaryConditions()

    def __init__(self, formulaBoundaryConditions):
        self.__boundaryConditions = formulaBoundaryConditions

    def generateRandomFormula(self):
        formula = Tree()
        # tree root node
        formula.add_node(NodeFactory.generateRootNode())
        # the rest of the tree
        self.generateSuccessors(formula, formula.root)
        return formula

    def generateSuccessors(self, formula, ancestorNode):
        # generate successors
        for i in range(2):

            # get successor node type
            successorNodeType = NodeFactory.getRandomNodeType(
                self.__boundaryConditions.getNodeTypeOptionsWeights())

            if successorNodeType is NodeFactory.NodeTypeOptions.LEAF:
                successorNode = NodeFactory.generateNode(successorNodeType)
                formula.add_node(successorNode, ancestorNode)
            else:
                successorNode = NodeFactory.generateNode(successorNodeType)
                formula.add_node(successorNode, ancestorNode)
                self.generateSuccessors(formula, successorNode)

    # generating balanced parenthesis strings in a uniform random manner
    # Based on Arnold and Sleep - Uniform Random Number Generation of n Balanced Parenthesis Strings (1980)
    # This solution leads immediately to an O(n) algorithm for the generator.
    def generateRandomFormulaCode(self):
        # 0, 1 - left, right parentheses
        coddedTree = []
        # top most entities of tree
        leafCount = self.__boundaryConditions.getLeafCount()
        # described often as nodes or n
        innerNodeCount = leafCount - 1
        # all entities count
        nodeCount = leafCount + innerNodeCount
        # symbols count in the code
        symbolCount = 2 * innerNodeCount

        currentWalkValue = 0

        for index in range(symbolCount):
            choice = random.random()

            if choice <= FormulaFactory.AScodingFunction(currentWalkValue, innerNodeCount, index):
                currentWalkValue = currentWalkValue + 1
                coddedTree.append(0)
            else:
                currentWalkValue = currentWalkValue - 1
                coddedTree.append(1)
        
        return coddedTree

    @staticmethod
    def AScodingFunction(x, n, t):
        value = ((x + 2)/(x + 1)) * (((2*n) - t - x)/(2 * ((2*n)-t)))
        return value
    
