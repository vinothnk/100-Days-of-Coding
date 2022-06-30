from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
#add.column(fieldname-> string, column -> has to be a list
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align)
table.align = 'l'

print(table)

# column_names = ["Pikachu", "Squirtle", "Charmander"]
# table2 = PrettyTable()
# table2.add_column("Pokemon Names", column_names)
# print(table2.align)
# table2.align = 'l'
# print(table2)
