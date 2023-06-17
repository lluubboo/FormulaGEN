from Formula.BoundaryConditions import BoundaryConditions
from Formula.FormulaFactory import FormulaFactory

# boundary conditions must be created
boundaryConditions = BoundaryConditions()
boundaryConditions.setBoundaryConditions(4, {1, 2, 3})

# formula factory with boundary conditions
fGen = FormulaFactory(boundaryConditions)

# formula
formula = fGen.generateRandomFormula()
formula.getFormula().show()
