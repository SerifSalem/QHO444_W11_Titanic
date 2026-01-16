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


def display_gender_counts():
    males = 0
    females = 0

    for values in records:
        sex = values[4].strip().lower()
        if sex == "male":
            males += 1
        elif sex == "female":
            females += 1

    print(f"females: {females}, males: {males}")


def run_task5():
    load("titanic.csv")

    option = menu()

    if option == 3:
        display_gender_counts()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run_task5()
