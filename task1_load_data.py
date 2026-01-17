import csv

# 'records' will store all passenger data rows - Each item in this list represents one passenger
records = []

# 'headings' will store the column names from the CSV file
headings = []

def load(file_path):
    """ Loads the Titanic CSV file into memory.
        - The first row is stored as headings.
        - All remaining rows are stored as records. """

    # Inform the user that data loading has started
    print("Loading data...", end="")

    # Open the CSV file for reading
    with open(file_path) as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Read the first row of the CSV - This row contains the column headings
        global headings
        headings = next(csv_reader)

        # Read all remaining rows in the CSV - Each row represents one passenger
        global records
        for values in csv_reader:
            records.append(values)

    # Inform the user that data loading has finished
    print("Done!")


def run_task1():
     # Load the CSV file located in the same folder
    load("titanic.csv")

    # Display the number of data records loaded
    print(f"Successfully loaded {len(records)} records.")


# Standard Python entry point check
# Ensures this code runs only when the file is executed directly, not when imported
if __name__ == "__main__":
    run_task1()
