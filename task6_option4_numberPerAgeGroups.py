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


def display_age_groups():
    children = 0
    adults = 0
    elderly = 0

    for values in records:
        age_text = values[5].strip()

        age = float(age_text)

        if age < 18:
            children += 1
        elif age < 65:
            adults += 1
        else:
            elderly += 1

    print(f"children: {children}, adults: {adults}, elderly: {elderly}")


def run_task6():
    load("titanic.csv")

    option = menu()

    if option == 4:
        display_age_groups()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run_task6()
