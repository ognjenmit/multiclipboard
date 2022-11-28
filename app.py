import sys
import clipboard
import json

# The application can be accessed from the terminal.

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    # Save currently copied data to clipboard.json file.
    # Command - python app.py save
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")

    # Load previously copied and saved data to the /paste/ command.
    # Command - python app.py load
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    # List all the saved clipboard data.
    # Command - python app.py list
    elif command == "list":
        print(data)
    else:
        print("Unknown command.")