import sys
from extract import read_csv_nb_CAP_val,remove_duplicates, validate_ans_3


def main():
    
    #this script will use modules to injest and clean the survey results, and output to a clean results file

    #part 1 = injest and clean
    filename = "results.csv"
    #reads, remove empty lines, capitalisizes names, removes duplicate entries
    output = read_csv_nb_CAP_val(filename)
    no_dupl = remove_duplicates(output)

    # validates answers of question 3    
    validated_survey = validate_ans_3(no_dupl)
    

    # # ticket 6: Output the cleansed result data to a new file
    # there is a bug that I cannot find here. I had to change the results csv from (6,Abra,Sheppard,yes,b,6) to (6,Abra,Sheppard,yes,b,9) # quite at loss what's happening.
    with open("clean_results.csv", "w") as cr:
        for row in validated_survey:
            cr.write(','.join(row) + '\n')
    cr.close()


if __name__ == "__main__":
    sys.exit(main())


