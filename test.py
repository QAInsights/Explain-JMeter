import json


def main():
    commands = "h g"
    each_arg = commands.split(" ")

    with open("commands/jmeter.json") as f:
        data = json.load(f)
        for i, j in data['commands'].items():
            print(i, j)


    return


if __name__ == '__main__':
    main()
