from extract import read_csv_nb_CAP_val
filename = "results.csv"
output = read_csv_nb_CAP_val(filename)
#print(output)

#ticket 2
no_dupl = []
no_dupl_set = set()
for x in output:
    if tuple(x[0]) not in no_dupl_set:
        no_dupl.append(x)
        no_dupl_set.add(tuple(x[0]))
#print(no_dupl)

#ticket 5

val_sur =[]
val_index_set = set()
for x in no_dupl:
    
    if x[5] == 'answer_3' or (int(x[5]) > 0 and int(x[5]) < 11):
        val_sur.append(x)
        
print(val_sur)
