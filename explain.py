import json


def explain_commands(commands):
    print(commands)
    each_arg = commands.split(" ")
    for arg in each_arg:
        print(f"User input is {arg}")
        with open("commands/jmeter.json") as f:
            data = json.load(f)
            for k, v in data['commands'].items():
                print(k, v, arg)
                if str(k) is str(arg):
                    print(f"match {k}")

    return
