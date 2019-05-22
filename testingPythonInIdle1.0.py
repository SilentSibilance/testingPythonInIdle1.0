import sqlite3
from sqlite3 import Error


print("Hello World")
print("Celebrate! You are demonstrating your knowledge! And writing code!")

#GLOBAL VARIABLES
#For safety, let's assign values originally,
#to lock each variable into the type we want.
#Will need to implement error handling later.
drug_name = "empty"
total_pills = 0
pills_per_dose = 0

# OBJECTS
# Initializing with "c_drug_name" etc. instead of "drug_name", while I confirm
# variable scope.
class Prescription:
    def __init__(self, c_drug_name, c_total_pills, c_pills_per_dose):
        self.c_drug_name = c_drug_name
        self.c_total_pills = c_total_pills
        self.c_pills_per_dose = c_pills_per_dose



# DATABASE
def create_connection(db_file):
    # Create a database connection to an SQLite database.
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        print("Connection created.")
        return conn
    except Error as e:
        print(e)
    # Taking out. Must close database at some point. 
    # finally:
        # conn.close()


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_prescription(conn, prescription):
    # Create and insert a new prescription into the prescriptions table in the database. 
    sql = '''INSERT INTO prescriptions(name,total_pills,pills_per_dose)
            VALUES(?,?,?) '''
    c = conn.cursor()
    c.execute(sql, prescription)
    print("Prescription has been added.")
    return c.lastrowid




# FUNCTIONS
def new_entry():
    drug_name = input("Drug name:")
    total_pills = input("Total number of pills:")
    pills_per_dose = input("Number of pills taken per dose:")

    with conn:
        l_prescription = (drug_name, total_pills, pills_per_dose)
        prescription_id = create_prescription(conn, l_prescription)
        print("New prescription has been added to the database by user.")
    main_menu()


def display_prev_entry():
    print(drug_name)
    print(total_pills)
    print(pills_per_dose)
    main_menu()


def test_prescription():
    # get 3 user inputs
    l_drug_name = input("Drug name:")
    l_total_pills = input("Total number of pills:")
    l_pills_per_dose = input("Number of pills taken per dose:")

    my_prescription = Prescription(l_drug_name, l_total_pills, l_pills_per_dose)
    # print values from object
    print("\nThis is what we have on file for you:")
    print("Drug name: " + my_prescription.c_drug_name)
    print("Number of total pills: " + my_prescription.c_total_pills)
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
database = "/Users/taffybear/Coding Folders/testingPythonInIdle1.0/prescript.db"

sql_create_prescriptions_table = """ CREATE TABLE IF NOT EXISTS prescriptions (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        total_pills integer NOT NULL,
                                        pills_per_dose integer NOT NULL
                                        ); """                                        

#  Create a database connection.
conn = create_connection(database)
if conn is not None:
    create_table(conn, sql_create_prescriptions_table)
    print("Created prescription table.")
elif conn is None:
    print("Conn is None.")
else:
    print("Error! Cannot create the database connection.")


# HANDLE USER ACTION
main_menu()

