# Example file for Advanced Python by Joe Marini
# Using special module names

import collections
# __name__ is the name of the module
print("Module Name:", __name__)
print(collections.__name__)

# __file__ contains the path to the file from which the module was loaded
print("File Path:", __file__)

# __package__ indicates the package that the module belongs to.
print("Module Package:", __package__)
print(collections.__package__)

if __name__ == "__main__":
  print("This code is being run directly.")