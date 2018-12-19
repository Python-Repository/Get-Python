from flask import Flask, request, make_response
from random import randint
import random
import json

app = Flask(__name__)


@app.route("/getdata", methods=["GET"])
def produto():
    final_json = {}
    final_json["nome"] = ["armenio", "foo"]
    final_json["idUser"] = randomNumber()
    final_json["situacao"] = "iniciada"
    final_json["vigencia"] = "{}/{}/{} ate {}/{}/{}".format(randint(0, 26), randint(
        1, 12), randint(1980, 2018), randint(0, 26), randint(1, 12), randint(2019, 2030))
    final_json["keyInteger"] = randomNumberInteger()
    response = make_response(json.dumps(final_json))
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


def randomNumber():
    return random.random()*random.randint(0, 99)


def randomNumberInteger():
    return random.randint(100000000000, 999999999999)


def main():
    app.run()


if __name__ == "__main__":
    main()
