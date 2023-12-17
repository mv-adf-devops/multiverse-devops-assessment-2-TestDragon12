#ticket 7 part 1

with open(r"clean_results.csv", "r") as cr_r:
    for item in cr_r:
        print(item)

#ticket 7 - stretch (fixed length)
from extract import read_csv

filename_clean = "clean_results.csv"
output_clean = read_csv(filename_clean)

#this works if the clean_results.csv is correct. Unfortunately this contains an extra comma that I need to debug
def space(i, d):
  max_len = len(max(list(zip(*output_clean))[i], key=len))
  return d+' '*(max_len-len(d))

clean_FL = '\n'.join(' '.join(space(*c) for c in enumerate(b)) for b in output_clean)

print(clean_FL)