from extract import read_csv_nb_CAP
filename = "results.csv"
output = read_csv_nb_CAP(filename)
#print(output)

#ticket 2
no_dupl = []
no_dupl_set = set()
for x in output:
    if tuple(x[0]) not in no_dupl_set:
        no_dupl.append(x)
        no_dupl_set.add(tuple(x[0]))
print(no_dupl)

