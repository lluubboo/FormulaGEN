import tabulate


class TablePrinter:

    @staticmethod
    def printTable(data):
        print("\n" + tabulate.tabulate(data, headers=["Entity ID", "Specific ID", "Value ID", "Entity name"]))
