
print("Hello World")
print("Celebrate! You are demonstrating your knowledge! And writing code!")

#GLOBAL VARIABLES
#For safety, let's assign values originally,
#to lock each variable into the type we want.
#Will need to implement error handling later.
drug_name = "empty"
num_pills = 0
pills_per_dose = 0

# FUNCTIONS
def new_entry():
    drug_name = input("Drug name:")
    num_pills = input("Total number of pills:")
    pills_per_dose = input("Number of pills taken per dose:")
    main_menu()


def display_prev_entry():
    print(drug_name)
    print(num_pills)
    print(pills_per_dose)
    main_menu()


def main_menu():
    print("\nPress 'd' if you would like to display the previous entry.")
    go_to = input("Press 'n' if you would like to submit a new entry.")
    if go_to == "n":
        print("n pressed")
        new_entry()
    elif go_to == "d":
        print("d pressed")
        display_prev_entry()
    else:
        print("Invalid entry.")
        main_menu()


# HANDLE USER ACTION
main_menu()
