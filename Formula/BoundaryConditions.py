class BoundaryConditions:
    """
    Formula boundary conditions
    """

    # theoretical formula size, limited by leaf count in tree representation
    __leafCount = None
    # node type option values for random node generation [inner node, leaf node]
    __nodeTypeOptionsWeights = []
    # user known parameters
    __userParamList = []

    def __init__(self):
        pass

    def setCountEntityLimit(self, entityLimit):
        self.__leafCount = entityLimit

    def setUserParamsList(self, paramsList):
        self.__userParamList = paramsList

    def setNodeTypeOptionsValues(self):
        # 50% of the generated equations will have leafNodeCount leafs
        resulProbability = 1 / 2

        leafNodeCount = self.__leafCount
        innerNodeCount = leafNodeCount if (leafNodeCount % 2 == 0) else (leafNodeCount - 1)

        innerNodeOptionValue = pow(resulProbability, 1 / innerNodeCount)
        leafNodeOptionValue = 1 - innerNodeOptionValue

        return [12, 10]

    def setBoundaryConditions(self, leafCount, paramsList):
        self.__userParamList = paramsList
        self.__leafCount = leafCount
        self.__nodeTypeOptionsWeights = self.setNodeTypeOptionsValues()

    def getNodeTypeOptionsWeights(self):
        return self.__nodeTypeOptionsWeights

    def getLeafCount(self):
        return self.__leafCount

    def getUserParamList(self):
        return self.__userParamList
