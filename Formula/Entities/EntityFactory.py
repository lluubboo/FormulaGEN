import random
from Formula.Entities.Operator import Subtraction, Addition, Multiplication, Division
from Formula.Entities.ValueEntity import UserParameter, Constant


class EntityFactory:
    """
    Entity factory class
    """

    @staticmethod
    def generateRandomOperator():
        entityClass = random.choice(EntityFactory.getOperatorsList())
        return entityClass()

    @staticmethod
    def generateRandomValueEntity():
        entityClass = random.choice(EntityFactory.getValueEntitiesList())
        return entityClass()

    @staticmethod
    def getOperatorsList():
        operatorList = [Subtraction, Addition, Multiplication, Division]
        return operatorList

    @staticmethod
    def getValueEntitiesList():
        entityList = [UserParameter, Constant]
        return entityList
