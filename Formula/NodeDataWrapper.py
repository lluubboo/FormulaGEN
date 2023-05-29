
class NodeData:
    """
    wrapper class for the data inserted into the node
    """

    __data = None
    __nodeType = None

    def __init__(self, data, nodeType):
        self.__data = data
        self.__nodeType = nodeType

    def getNodeType(self):
        return self.__nodeType

