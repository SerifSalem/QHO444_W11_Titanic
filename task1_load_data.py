import csv

# global variables (similar pattern to Week 6 solutions)
records = []
headings = []


def load(file_path):
    print("Loading data...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        # first row is the headings
        global headings
        headings = next(csv_reader)

        # all remaining rows are data records
        global records
        for values in csv_reader:
            records.append(values)

    print("Done!")


def run_task1():
    load("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")


if __name__ == "__main__":
    run_task1()
