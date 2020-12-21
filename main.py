# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from explain import explain_commands

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', isHome=True)


@app.route('/explain', methods=['GET'])
def explain():
    commands = request.args['usercommand'].strip()
    commands = commands.split(' ')
    print(f"User input is {commands}")
    result = {}
    try:
        for command in commands:
            print(f"from the form {command}")
            k, v = explain_commands(command)
            print(f"In main {k} {v}")
            result[k] = v
        print(result)
    except TypeError:
        pass
    return render_template('explain.html', string=result)


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    app.run(port=7000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
