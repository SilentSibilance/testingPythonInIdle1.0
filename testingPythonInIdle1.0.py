
print("Hello World")

# FUNCTIONS
def new_entry():
    #For safety, let's assign values originally,
    #to lock each variable into the type we want.
    #Will need to implement error handling later.
    drug_name = "empty"
    num_pills = 0
    pills_per_dose = 0
    
    drug_name = input("Drug name:")
    num_pills = input("Total number of pills:")
    pills_per_dose = input("Number of pills taken per dose:")


def display_prev_entry():
    print(drug_name)



# HANDLE USER ACTION
print("Press 'd' if you would like to display the previous entry.")
go_to = input("Press 'n' if you would like to submit a new entry.")
if go_to == "n":
    print("n pressed")
    new_entry()
elif go_to == "d":
    print("d pressed")
# display_prev_entry()
else:
    print("Invalid entry.")
