from prettytable import PrettyTable

# Creating an object named table from the class PrettyTable()
table = PrettyTable()

# modifying the objects attributes
table.field_names = ["Cycle", "     ", "x29", "x30", "x28", "x27", "x10"]
table.add_row(["1", "       ", "00", "00", "x", "x", "x"])
table.add_row(["2", "       ", "00", "00", "x", "x", "x"])
table.add_row(["3", "       ", "00", "00", "x", "x", "x"])
table.add_row(["4", "       ", "00", "00", "x", "x","x"])
table.add_row(["5", "       ", "00", "1", "x", "x", "x"])
table.add_row(["6", "       ", "00", "1", "45", "x", "x"])
table.add_row(["7", "       ", "00", "1", "45", "-20", "x"])
table.add_row(["8", "       ", "00", "1", "45", "-20", "x"])
table.add_row(["9", "       ", "00", "1", "45", "-20", "45"])
table.add_row(["10", "       ", "00", "1", "45", "-20", "45"])

# table.align = 'l'
print(table)
