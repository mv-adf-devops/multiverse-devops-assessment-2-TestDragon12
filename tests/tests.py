from extract import read_csv, read_csv_nb, read_csv_nb_CAP, read_csv_nb_CAP_val,remove_duplicates, validate_ans_3
from input import main
""""
The results.csv data file can be successfully processed into an array
Each line of the file is read into a new array item
The file read method must be in a sub-module
"""
## Ticket 1
def test_file_read_into_list():
     # Arrange
    filename = "results.csv"
    expected_output = list


     # Act
     # we want a sub module
    output = type(read_csv(filename))
    
     # Assert
    assert output == expected_output

def test_list_not_empty():
        # Arrange
    filename = "results.csv"
    


     # Act
     # we want a sub module
    output = read_csv(filename)
    
     # Assert
    assert len(output) > 0

def test_first_row_is_correct():
    # Arrange
    filename = "results.csv"
    expected_output = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    # Act
    output = read_csv(filename)
    # Assert
    assert output[0] == expected_output

## Ticket 3
def test_no_empty_rows():
    #Arrange
    filename = "results.csv"
    # Act
    output = read_csv_nb(filename)
    # Assert
    for x in output:
        if set(x) == {''}:
            assert x == []
        else:
            assert 1 == 1

## Ticket 4
def test_name_capitalized():
    #Arrange
    filename = "results.csv"
    # Act
    output = read_csv_nb_CAP(filename)
    # Assert
    for x in output:
        assert x[1].capitalize() == x[1]
        assert x[2].capitalize() == x[2]

## Ticket 2
def test_no_duplicates():
    #Arrange
    filename = "results.csv"
    output = read_csv_nb_CAP_val(filename)
     

    # Act
    no_dupl = remove_duplicates(output)
    print(type(no_dupl))
    

    # Assert
    assert len(no_dupl) == len(set(no_dupl))
