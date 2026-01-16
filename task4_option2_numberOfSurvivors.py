import csv

records = []
headings = []


def load(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        global headings
        headings = next(csv_reader)

        global records
        for values in csv_reader:
            records.append(values)


def menu():
    print()
    print("Please select one of the following options:")
    print("[1] Display the names of all passengers")
    print("[2] Display the number of passengers that survived")
    print("[3] Display the number of passengers per gender")
    print("[4] Display the number of passengers per age group")
    print()
    return int(input())


def display_survivors_total():
    count = 0
    for values in records:
        if int(values[1]) == 1:
            count += 1
    print(count)


def run_task4():
    load("titanic.csv")

    option = menu()

    if option == 2:
        display_survivors_total()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run_task4()
