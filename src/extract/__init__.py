def read_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            rows.append(line.strip().split(','))
    return rows
    

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
        rows[i][1] = rows[i][1].upper()
        rows[i][2] = rows[i][2].upper()
        i += 1
    return rows

