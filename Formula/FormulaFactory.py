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
        formula.add_node(NodeFactory.generateInnerNode())
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
        codedTree = []
        # top most entities of tree
        leafCount = self.__boundaryConditions.getLeafCount()
        # described often as nodes or n
        nodeCount = leafCount - 1
        # symbols count in the code
        symbolCount = 2 * nodeCount

        currentWalkValue = 0

        for index in range(symbolCount):
            choice = random.random()

            if choice <= FormulaFactory.AScodingFunction(currentWalkValue, nodeCount, index):
                currentWalkValue = currentWalkValue + 1
                codedTree.append(0)
            else:
                currentWalkValue = currentWalkValue - 1
                codedTree.append(1)

        return codedTree

    @staticmethod
    def AScodingFunction(x, n, t):
        value = ((x + 2) / (x + 1)) * (((2 * n) - t - x) / (2 * ((2 * n) - t)))
        return value

    @staticmethod
    def decodeNestedStringTree(codedTree):
        formula = Tree()
        nodeStack = []
        # root
        root = NodeFactory.generateInnerNode()
        formula.add_node(root)
        nodeStack.append(root)
        print(codedTree)
        for i in range(len(codedTree)):
            char = codedTree[i]
            if char == 0:
                node = NodeFactory.generateInnerNode()
                formula.add_node(node, nodeStack[-1])
                nodeStack.append(node)
            else:
                if len(nodeStack[-2].successors(formula.identifier)) is not 2:
                    nodeStack.pop()
        return formula

    @staticmethod
    def doNothing():
        pass 
