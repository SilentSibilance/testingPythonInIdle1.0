import sqlite3
from sqlite3 import Error


print("Hello World")
print("Celebrate! You are demonstrating your knowledge! And writing code!")

#GLOBAL VARIABLES
#For safety, let's assign values originally,
#to lock each variable into the type we want.
#Will need to implement error handling later.
drug_name = "empty"
num_pills = 0
pills_per_dose = 0

# OBJECTS
# Initializing with "c_drug_name" etc. instead of "drug_name", while I confirm
# variable scope.
class Prescription:
    def __init__(self, c_drug_name, c_num_pills, c_pills_per_dose):
        self.c_drug_name = c_drug_name
        self.c_num_pills = c_num_pills
        self.c_pills_per_dose = c_pills_per_dose

# DATABASE
def create_connection(db_file):
    # Create a database connection to an SQLite database.
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        print("Connection created.")
    except Error as e:
        print(e)
    finally:
        conn.close()


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


def test_prescription():
    # get 3 user inputs
    l_drug_name = input("Drug name:")
    l_num_pills = input("Total number of pills:")
    l_pills_per_dose = input("Number of pills taken per dose:")

    my_prescription = Prescription(l_drug_name, l_num_pills, l_pills_per_dose)
    # print values from object
    print("\nThis is what we have on file for you:")
    print("Drug name: " + my_prescription.c_drug_name)
    print("Number of total pills: " + my_prescription.c_num_pills)
    print("Number of pills per dose: " + my_prescription.c_pills_per_dose)
    main_menu()


def main_menu():
    print("\nPress 'd' if you would like to display the previous entry.")
    print("Press 'c' if you would like to run a test function of Prescription object.")
    go_to = input("Press 'n' if you would like to submit a new entry.")
    if go_to == "n":
        print("n pressed")
        new_entry()
    elif go_to == "d":
        print("d pressed")
        display_prev_entry()
    elif go_to == "c":
        print("c pressed")
        test_prescription()
    else:
        print("Invalid entry.")
        main_menu()


# SETUP DATABASE CONNECTION
create_connection("/Users/taffybear/Coding Folders/testingPythonInIdle1.0/prescript.db")

# HANDLE USER ACTION
main_menu()

