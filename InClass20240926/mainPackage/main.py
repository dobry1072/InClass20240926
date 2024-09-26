#main.py
from nicholdwPackage.nicholdw import *
from team07Package.team07 import team07 
# Do not edit this module at all.
# Create some new artifacts in the project...
# Name your package {team}Package
# Name your module {team}.py
# Name your function {team}
# The {} are for clarity and are not part of any name
# Your function should return a list of dictionaries, just a few rows.


if __name__ == "__main__":
    print("testing your code...")
    print("nicholdw")
    data = nicholdw()
    for item in data:
        print(item)
    print("*****************")
    
    print("team07")
    data = team07()
    for item in data:
        print(item)
    print("*****************")
    

    