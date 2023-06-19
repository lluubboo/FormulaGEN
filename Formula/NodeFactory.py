from treelib import Node
from Formula.Entities.EntityFactory import EntityFactory


class NodeFactory:
    """
    Factory class for tree nodes
    """

    @staticmethod
    def generateLeafNode():
        entity = EntityFactory.generateRandomValueEntity()
        node = Node(entity.__class__.__name__)
        node.data = entity
        return node

    @staticmethod
    def generateInnerNode():
        entity = EntityFactory.generateRandomOperator()
        node = Node(entity.__class__.__name__)
        node.data = entity
        return node

    @staticmethod
    def generateRootNode():
        entity = EntityFactory.generateRandomOperator()
        node = Node(entity.__class__.__name__)
        node.identifier = "root"
        node.data = entity
        return node
