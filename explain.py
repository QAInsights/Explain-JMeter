import json


def explain_commands(command):
    """
    :param command: each command from the input text box
    :return: valid explanation for each command
    """
    print(f"inside explain module user command is {command}")
    with open("commands/jmeter.json") as f:
        data = json.load(f)
        print(f"User input is {command}")
        for items in data['commands']:
            print(f"JSON data is {items}")
            for key, value in items.items():
                print(key, value)
                try:
                    if command == str(key):
                        print(f"User command is {command}; JSON data is {key}")
                        return key, value
                except TypeError:
                    pass
