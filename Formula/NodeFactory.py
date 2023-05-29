import random
from enum import Enum
from treelib import Node
from Formula.Entities.EntityFactory import EntityFactory
from Formula.NodeDataWrapper import NodeData


class NodeFactory:
    """
    Factory class for tree nodes
    """

    @staticmethod
    def generateRootNode():
        entity = EntityFactory.generateRandomOperator()
        root = Node(entity.__class__.__name__)
        root.data = NodeData(entity, NodeFactory.NodeTypeOptions.INNER_NODE)
        return root

    @staticmethod
    def generateLeafNode():
        entity = EntityFactory.generateRandomValueEntity()
        node = Node(entity.__class__.__name__)
        node.data = NodeData(entity, NodeFactory.NodeTypeOptions.LEAF)
        return node

    @staticmethod
    def generateInnerNode():
        entity = EntityFactory.generateRandomOperator()
        node = Node(entity.__class__.__name__)
        node.data = NodeData(entity, NodeFactory.NodeTypeOptions.INNER_NODE)
        return node

    @staticmethod
    def generateNode(nodeType):
        if nodeType is NodeFactory.NodeTypeOptions.LEAF:
            return NodeFactory.generateLeafNode()
        else:
            return NodeFactory.generateInnerNode()

    # controls the size of the tree by weighted random choice
    # return format cannot be list
    @staticmethod
    def getRandomNodeType(weights):
        return random.choices(NodeFactory.NodeTypeOptions.getNodeTypeOptions(),
                              weights=(weights[0], weights[1]), k=1).pop()

    class NodeTypeOptions(Enum):
        """
        Node basic type enum: Inner node or Lead
        """

        LEAF = "leaf"
        INNER_NODE = "inner_node"

        @staticmethod
        def getNodeTypeOptions():
            return [NodeFactory.NodeTypeOptions.LEAF, NodeFactory.NodeTypeOptions.INNER_NODE]
