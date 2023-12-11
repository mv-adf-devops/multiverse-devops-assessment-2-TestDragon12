import sys
from extract import read_csv_nb_CAP_val,remove_duplicates, validate_ans_3


def main():
    
    #ticket 1: read CSV file
    filename = "results.csv"
    output = read_csv_nb_CAP_val(filename)
    no_dupl = remove_duplicates(output)

   
    
    val_sur = validate_ans_3(no_dupl)

    #ticket 6: Output the cleansed result data to a new file

    with open(r"clean_results.csv", "w") as cr:
        for item in val_sur:
            cr.write("%s\n" % item)

    cr.close()

    with open(r"clean_results.csv", "r") as cr_r:
        for item in cr_r:
            print(item)


if __name__ == "__main__":
    sys.exit(main())


# add error checking