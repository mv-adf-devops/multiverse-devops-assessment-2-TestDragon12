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
    with open(r"clean_results.csv", "w") as cr:
        for item in validated_survey:
            for i in item:
                if item.index(i) < (len(item) - 1):
                    cr.write("%s," % i)
                else:
                    cr.write("%s" % i)  
            if validated_survey.index(item) < (len(validated_survey)-1):
                cr.write("\n")
    cr.close()


if __name__ == "__main__":
    sys.exit(main())


