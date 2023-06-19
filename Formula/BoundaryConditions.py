class BoundaryConditions:
    """
    Formula boundary conditions
    """

    # theoretical formula size, limited by leaf count in tree representation
    __leafCount = None
    # user known parameters
    __userParamList = []

    def setCountEntityLimit(self, entityLimit):
        self.__leafCount = entityLimit

    def setUserParamsList(self, paramsList):
        self.__userParamList = paramsList

    def setBoundaryConditions(self, leafCount, paramsList):
        self.__userParamList = paramsList
        self.__leafCount = leafCount

    def getLeafCount(self):
        return self.__leafCount

    def getUserParamList(self):
        return self.__userParamList
