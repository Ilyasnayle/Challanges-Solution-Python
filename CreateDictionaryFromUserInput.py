def CreateDictionaryFromUserInput():
    """
    This function creates a dictionary from user input.
    """
    dictionary = {}
    while True:
        key = input("Enter key: ")
        if key == "":
            break
        value = input("Enter value: ")
        dictionary[key] = value
        print("To Exit, Press Enter.")
    return dictionary

def PrintDictionary(dictionary):
    """
    This function prints a dictionary.
    """
    for key, value in dictionary.items():
        print(key, value)

def main():
    """
    This is the main function.
    """
    dictionary = CreateDictionaryFromUserInput()
    PrintDictionary(dictionary)

main()
