import json


def explain_commands(command):
    print(f"inside explain module {command}")
    with open("commands/jmeter.json") as f:
        data = json.load(f)
        print(f"User input is {command}")
        for items in data['commands']:
            # print(items)
            for key, value in items.items():
                # print(key, value)
                if command == key:
                    # print(key, value)
                    return key, value
