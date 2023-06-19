from Formula.BoundaryConditions import BoundaryConditions
from Formula.FormulaFactory import FormulaFactory

# boundary conditions must be created
boundaryConditions = BoundaryConditions()
boundaryConditions.setBoundaryConditions(5, [1, 2, 3])

# formula factory with boundary conditions
fGen = FormulaFactory(boundaryConditions)

# formula
formula = fGen.generateRandomFormula()
formula.getFormula().show(data_property="tag")
print("Result is: " + str(formula.evaluateFormula()))
