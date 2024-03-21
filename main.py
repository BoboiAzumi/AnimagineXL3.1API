from flask import Flask, jsonify, request
from flask_cors import CORS
from API.AnimagineClient import animagine
import random

App = Flask(__name__)

CORS(App)

@App.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method != "POST":
            data = {
                "status": "error",
                "msg": "Must include a prompt with the post request"
            }
        else:
            requestdata = request.get_json()

            if requestdata["seeds"] == 0:
                seeds = random.randint(0, 2147483647)
            else:
                seeds = requestdata["seeds"]

            data = animagine(
                    requestdata["prompt"],
                    requestdata["neg_prompt"],
                    seeds,
                    requestdata["width"],
                    requestdata["height"],
                    requestdata["scale"],
                    requestdata["steps"],
                    requestdata["sampler"],
                    requestdata["ratio"],
                    requestdata["style"],
                    requestdata["quality"],
                    requestdata["upscaler"],
                    requestdata["strength"],
                    requestdata["upscale"],
                    requestdata["quality_tags"]
                )

        return jsonify(data)

    except:
        return jsonify({
            "status": "Internal Server Error"
        })

if __name__ == "__main__":
    App.run(debug=False)