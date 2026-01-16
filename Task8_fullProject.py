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
    print("[5] Display the number of survivors per age group")
    print()
    return int(input())


def display_names():
    for values in records:
        print(values[3])  # Name


def display_survivors_total():
    count = 0
    for values in records:
        if int(values[1]) == 1:
            count += 1
    print(count)


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


def display_survivors_by_age_group():
    children_total = 0
    adults_total = 0
    elderly_total = 0

    children_survived = 0
    adults_survived = 0
    elderly_survived = 0

    for values in records:
        age_text = values[5].strip()

        age = float(age_text)
        survived = int(values[1])

        if age < 18:
            children_total += 1
            if survived == 1:
                children_survived += 1
        elif age < 65:
            adults_total += 1
            if survived == 1:
                adults_survived += 1
        else:
            elderly_total += 1
            if survived == 1:
                elderly_survived += 1

    print(
        f"children: {children_survived}/{children_total}, "
        f"adults: {adults_survived}/{adults_total}, "
        f"elderly: {elderly_survived}/{elderly_total}"
    )


def run_task8():
    load("titanic.csv")

    option = menu()

    if option == 1:
        display_names()
    elif option == 2:
        display_survivors_total()
    elif option == 3:
        display_gender_counts()
    elif option == 4:
        display_age_groups()
    elif option == 5:
        display_survivors_by_age_group()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run_task8()
