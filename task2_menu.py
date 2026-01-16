import csv

records = []
headings = []


def load(file_path):
    print("Loading data...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        global headings
        headings = next(csv_reader)

        global records
        for values in csv_reader:
            records.append(values)

    print("Done!")


def menu():
    print()
    print("Please select one of the following options:")
    print("[1] Display the names of all passengers")
    print("[2] Display the number of passengers that survived")
    print("[3] Display the number of passengers per gender")
    print("[4] Display the number of passengers per age group")
    print()
    return int(input())


def run_task2():
    load("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")

    option = menu()
    print(f"You have selected option: {option}")


if __name__ == "__main__":
    run_task2()
