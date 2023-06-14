class NodeUtils:
    @staticmethod
    def getSuccessorsCount(node, treeId):
        return len(node.successors(treeId))

    @staticmethod
    def getRemainingChildrenCount(node, treeId):
        return 2 - NodeUtils.getSuccessorsCount(node, treeId)
