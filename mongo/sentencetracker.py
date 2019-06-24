from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort
from pymongo import MongoClient
import bcrypt
import re

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://localhost:27017")
db = client["SentencesDatabase"]
users = db["Users"]

parser = reqparse.RequestParser()
parser.add_argument("Username")
parser.add_argument("Password")
parser.add_argument("Sentence")

password_conditions = re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[-+_!@#$%^&*.,?])(?=.{7,15})')
invalid_password = '''Password must: 
Contain at least one uppercase letter
Contain at least one lowercase letter
Contain at least one number
Contain one of: -+_!@#$%^&*.,?
Be between 7 and 15 characters'''


def username_check(username):
    try:
        users.find({"Username": username})[0]
        abort(400, message="This username is already taken")
    except IndexError:
        pass


def password_check(password):
    if not (password_conditions.match(password)):
        abort(400, message=invalid_password)


def verify_password(username, password):
    hashed_password = users.find({
        "Username": username
    })[0]["Password"]
    if bcrypt.hashpw(password.encode('utf8'), hashed_password) == hashed_password:
        return True
    else:
        return False


def count_tokens(username):
    tokens = users.find({
        "Username": username
    })[0]["Tokens"]
    return tokens


class Register(Resource):
    def post(self):
        args = parser.parse_args()
        username = args["Username"]
        password = args["Password"]
        username_check(username)
        password_check(password)

        hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert_one({
             "Username": username,
             "Password": hashed_password,
             "Sentence": "",
             "Tokens": 10
         })

        ret_json = {
            "Status": 200,
            "Message": "You have successfully signed up!"
        }
        return jsonify(ret_json)


class Store(Resource):
    def post(self):
        args = parser.parse_args()
        username = args["Username"]
        password = args["Password"]
        sentence = args["Sentence"]

        correct_info = verify_password(username, password)
        if not correct_info:
            abort(400, message="Username or password incorrect")

        num_tokens = count_tokens(username)
        if num_tokens <= 0:
            abort(403, message="Not enough tokens")

        users.update({
            "Username": username
        }, {
            "$set": {"Sentence": sentence,
            "Tokens": num_tokens-1
            }
        })

        ret_json = {
            "Status": 200,
            "Message": f"'{sentence}' has been stored"
        }
        return jsonify(ret_json)


class Get(Resource):
    def get(self):
        args = parser.parse_args()
        username = args["Username"]
        password = args["Password"]

        correct_info = verify_password(username, password)
        if not correct_info:
            abort(400, message="Username or password incorrect")

        sentence = users.find({"Username": username})[0]["Sentence"]

        ret_json = {
            "Status": 200,
            "Message": sentence
        }
        return jsonify(ret_json)


api.add_resource(Get, '/get')
api.add_resource(Register, '/register')
api.add_resource(Store, '/store')

if __name__ == "__main__":
    app.run(debug=True)
