from flask import Flask, request
import requests

app = Flask(__name__)


def poke_controller(headers):

    try:
        endpoint_poke_api = headers['endpoint_poke_api']
        my_ability_name = headers['my_ability_name']
        ability_number = int(headers['ability_number'])

        response = requests.get(endpoint_poke_api)
        response = response.json()

        abilities = response['abilities'][ability_number]
        ability_name = abilities['ability']['name']

    except Exception as e:
        return {'error': e.args[0]}, 400

    else:
        if my_ability_name in ability_name:
            return {"ability exist": True}, 200
        return {"ability exist": False}, 200


@app.route('/poke')
def poke():
    response = poke_controller(request.headers)
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)
