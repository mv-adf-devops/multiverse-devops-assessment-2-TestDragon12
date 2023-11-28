from extract import read_csv

""""
The results.csv data file can be successfully processed into an array
Each line of the file is read into a new array item
The file read method must be in a sub-module
"""

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

def test_no_duplicates():
    #Arrange
    