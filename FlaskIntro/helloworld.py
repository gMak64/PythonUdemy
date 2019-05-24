from flask import Flask, jsonify
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


if __name__=="__main__":
    app.run(debug=True)
