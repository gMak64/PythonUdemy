from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/skrt')
def skrtskrt():
    return "SKRTTTTTT"


@app.route('/yuh')
def yuh():
    ret_json = {
        'field1': 'yuh',
        'field2': 'nah'
    }
    return jsonify(ret_json)


@app.route('/example')
def info():
    my_json = {
        'Name': 'Grant Mak',
        'Age': '21',
        'Emails': [
            {
                'type': 'work',
                'address': 'grant.mak@garmin.com',
            },
            {
                'type': 'personal',
                'address': 'gmak6464@gmail.com',
            }
        ]
    }
    return jsonify(my_json)


@app.route('/adder', methods=["POST"])
def add_two_nums():
    data = request.get_json()
    x = data['x']
    y = data['y']
    z = x+y
    my_sum = {
        'z': z
    }
    return jsonify(my_sum), 200


if __name__ == "__main__":
    app.run(debug=True)
