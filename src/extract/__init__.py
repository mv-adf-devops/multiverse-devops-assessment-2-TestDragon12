#basic function: reads all the content of the results file
def read_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            rows.append(line.strip().split(','))
    return rows
    
#Ticket 3: improved function: ignores empty lines
def read_csv_nb(filename):
    rows = []
    empty_rows= 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.strip() == ',,,,,':
                empty_rows += 1
            else:
                rows.append(line.strip().split(','))
    print('there are ' + str(empty_rows) + ' empty answers in the survey') 
    return rows

#Ticket 4: improved function: capitalise user name fields
def read_csv_nb_CAP(filename):
    rows = []
    empty_rows= 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.strip() == ',,,,,':
                empty_rows += 1
            else:
                rows.append(line.strip().split(','))
    print('there are ' + str(empty_rows) + ' empty answers in the survey') 

    i = 0
    while i < len(rows):
        rows[i][1] = rows[i][1].capitalize()
        rows[i][2] = rows[i][2].capitalize()
        i += 1
    return rows

#Ticket 3 & 4: final function, capitalise names and remove empty lines << ===
def read_csv_nb_CAP_val(filename):
    rows = []
    empty_rows= 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.strip() == ',,,,,':
                empty_rows += 1
            else:
                rows.append(line.strip().split(','))
    print('there are ' + str(empty_rows) + ' empty answers in the survey') 

    i = 0
    while i < len(rows):
        rows[i][1] = rows[i][1].capitalize()
        rows[i][2] = rows[i][2].capitalize()
        i += 1

    return rows

#ticket 2: remove duplicate entries
def remove_duplicates(l_list):
     
    no_dupl = []
    no_dupl_set = set()
    for x in l_list:
        if tuple(x[0]) not in no_dupl_set:
            no_dupl.append(x)
            no_dupl_set.add(tuple(x[0]))
    
    return no_dupl

    #ticket 5: Validate the responses to answer 3 (of the survey)

def validate_ans_3(no_dupl):
    val_sur =[]
    val_index_set = set()
    for x in no_dupl:
            
        if x[5] == 'answer_3' or (int(x[5]) > 0 and int(x[5]) < 11):
            val_sur.append(x)
           
    return val_sur
    