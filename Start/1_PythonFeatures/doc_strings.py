# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """This doesn't really do anything.
    
        arg1 = whatever you feels like
        arg2 = whatever you feels like too"""
    
    arg1 = "Hi, My name is Tony."
    arg2 = "Hi, My name is Ezikiel."
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
