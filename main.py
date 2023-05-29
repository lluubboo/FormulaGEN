from Formula.Formula import Formula

formulaRec = Formula()
formulaRec.getFormulaBoundaryConditions().setBoundaryConditions(5, {1, 2, 3})
formulaRec.generateRandomRecursion()
print("Recursion formula")
formulaRec.getFormula().show()

formulaWow = Formula()
formulaWow.getFormulaBoundaryConditions().setBoundaryConditions(5, {1, 2, 3})
formulaWow.generateRandomCode()
print("Sleep formula")
print(formulaWow.getFormula())