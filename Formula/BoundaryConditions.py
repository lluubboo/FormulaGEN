from dataclasses import dataclass


@dataclass
class BoundaryConditions:
    """
    Boundary conditions for formula generator
    """

    # theoretical formula size, limited by leaf count in tree representation
    __leafCount: int
    # user known parameters
    __userParamList: []

    def getLeafCount(self):
        return self.__leafCount

    def getUserParamList(self):
        return self.__userParamList

