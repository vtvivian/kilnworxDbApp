import datetime
import pandas as pd
import toga

today = datetime.datetime.now()
print("Today's date: " + today.strftime("%Y-%m-%d"))

# Read spreadsheet as database
xlFileName = "/media/Files/RockShare/Climbing/KilnworxDBApp2026/db1.xlsx"
db1 = pd.read_excel(xlFileName, index_col=0, header=0)

# Tidy up data:
#  - use lowercase for all strings
# TODO: do this automatically for all string fields
db1["Name"] = db1["Name"].str.lower()
db1["Member type"] = db1["Member type"].str.lower()

#  - restrict categories for member types
memberTypes = pd.Categorical(["member","visitor","volunteer"])
db1["Member type"] = db1["Member type"].astype("category")
# TODO: check for bad entries

# Identify database entry from name
myName = input("Enter your name: ") #TODO: replace later with app input
myName = myName.lower()
print("Hello, " + myName + "!")
myDb = db1[db1["Name"] == myName]

if myDb.shape[0]>1:
    raise ValueError("Error! More than one person with this name.")
elif myDb.shape[0]<1:
    raise ValueError("Error! No person with this name.")


print(myDb.T)
print("\n")
# TODO: check unique entry in myDb

# Update database with current visit
myDb["Date last visit"] = today.date()
myDb["Total visits"] += 1

# Check membership type
if pd.notna(myDb["Pass expiry"].values):
    if myDb["Pass expiry"].values < today:
        print("Pass expired!")
        # TODO: function renew pass
    else:
        print("Pass active")
        print("Pass expiry date: " + pd.to_datetime(myDb["Pass expiry"].values[0]).strftime("%Y-%m-%d"))
else:
    print("Membership type: " + myDb["Member type"].iloc[0])

# Update main database
db1.loc[myDb.index] = myDb

# Export to spreadsheet
db1.to_excel(xlFileName,date_format='dd/mm/yyyy')
print("Sign-in successful!")