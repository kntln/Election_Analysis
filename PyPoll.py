# Open the election reusults and read the file
import csv

with open("election_results.csv") as election_data:

# To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    header = next(election_data)
    print(header)




