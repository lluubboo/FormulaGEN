import random

from treelib import Tree
from Formula.BoundaryConditions import BoundaryConditions
from Formula.Entities.ValueEntity import ValueEntity
from Formula.Formula import Formula
from Formula.FormulaUtils import NodeUtils
from Formula.NodeFactory import NodeFactory


class FormulaFactory:
    """
    Class is used as formula generator.
    Factory class for formula (Tree).
    """
    __boundaryConditions: BoundaryConditions

    def __init__(self, formulaBoundaryConditions):
        self.__boundaryConditions = formulaBoundaryConditions

    def generateRandomFormula(self):
        """
        Method returns random generated formula.
        Formula is specified by boundary conditions.
        :return: Formula
        """
        tree = self.__binaryToTree(self.__generateRandomFormulaBinaryRepresentation())
        formula = Formula(tree, self.__boundaryConditions)
        return formula

    def __generateRandomFormulaBinaryRepresentation(self):
        """
        Method generates balanced binaries representing binary tree in a uniform random manner.
        Based on Arnold and Sleep - Uniform Random Number Generation of n Balanced Parenthesis Strings (1980)
        This solution leads immediately to an O(n) algorithm for the generator.
        :return:
        """
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

            if choice <= self.__codingFunction(currentWalkValue, nodeCount, index):
                currentWalkValue = currentWalkValue + 1
                codedTree.append(0)
            else:
                currentWalkValue = currentWalkValue - 1
                codedTree.append(1)

        return codedTree

    def __codingFunction(self, x, n, t):
        """
        Function which returns value by Arnold and Sleep - Uniform Random Number Generation of n Balanced Parenthesis
        Strings (1980)
        :param x:
        :param n:
        :param t:
        :return:
        """
        value = ((x + 2) / (x + 1)) * (((2 * n) - t - x) / (2 * ((2 * n) - t)))
        return value

    def __binaryToTree(self, codedTree):
        """
        Method is converting binary list to binary tree (without leaf nodes) in O(n).
        :param codedTree: binary list
        :return: Tree
        """
        tree = Tree()
        nodeStack = []

        # rest of the tree
        for i in range(len(codedTree)):

            char = codedTree[i]

            if char == 0:
                if nodeStack:
                    node = NodeFactory.generateInnerNode()
                    tree.add_node(node, nodeStack[-1])
                else:
                    node = NodeFactory.generateRootNode()
                    tree.add_node(node)
                nodeStack.append(node)
            else:
                nodeStack.pop() if codedTree[i - 1] == 1 else None

        # add leafs
        tree = self.__addLeafsToTree(tree)

        return tree

    def __addLeafsToTree(self, tree: Tree):
        """
        Method adds leaf's to generated leafless binary tree
        :param: Tree
        :return: Tree
        """
        for innerNode in tree.all_nodes():
            freeSlotCount = NodeUtils.getRemainingChildrenCount(innerNode, tree.identifier)
            for freeSlot in range(freeSlotCount):
                leafNode = NodeFactory.generateLeafNode()
                self.setLeafValue(leafNode.data, self.__boundaryConditions)
                tree.add_node(leafNode, innerNode)
        return tree

    def setLeafValue(self, formulaEntity: ValueEntity, boundaryConditions: BoundaryConditions):
        """
        Method fills empty value entities in the formula (UserParam & Constant).
        Constant - random number from given interval
        UserParam - random param from user param list
        :param formulaEntity:
        :param boundaryConditions:
        :return:
        """
        if formulaEntity.isConstant():
            formulaEntity.setValue(random.uniform(-1000000, 1000000))
        else:
            formulaEntity.setValue(random.choice(boundaryConditions.getUserParamList()))
