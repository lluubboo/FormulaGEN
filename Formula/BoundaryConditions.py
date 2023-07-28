from dataclasses import dataclass


@dataclass
class BoundaryConditions:
    """
    Just simple dataclass boundary conditions for formula generator.
    (choosedLeafCount, [userParamList])
    """

    # theoretical formula size, limited by leaf count in tree representation
    __leafCount: int
    # user known parameters
    __userParamList: []

    def getLeafCount(self):
        return self.__leafCount

    def getUserParamList(self):
        return self.__userParamList

    def isValid(self):
        if not self.__userParamList or self.__leafCount == 0:
            print("Not valid boundary conditions")
            print("Leaf count: ", self.__leafCount)
            print("User parameter list: ", self.__userParamList)
            return False
        else:
            return True
