import base64
import os
import requests
from flask import Flask, request


AUDD_API_KEY = os.environ["AUDD_KEY"]

AUDD_API_URL = "https://api.audd.io/recognize"

app = Flask(__name__)


@app.route("/recognise", methods=["POST"])
def recognise_track():

    request_json = request.get_json()

    audio_base64 = request_json.get("audio")

    if audio_base64 is None:
        return "", 400

    headers = {
        "api_token": AUDD_API_KEY
    }

    audio_file = {
        "file": (
            "decoded.wav",
            base64.b64decode(audio_base64)
        )
    }

    response = requests.post(
        AUDD_API_URL,
        headers=headers,
        files=audio_file
    )

    if response.status_code != 200:
        return "", 500

    audd_response = response.json()

    return extract_track_id(audd_response)


def extract_track_id(audd_json):

    if audd_json.get("status") != "success":
        return "", 400

    result = audd_json.get("result")

    if result is None:
        return "", 404

    return {"id": result["title"]}, 200


if __name__ == "__main__":
    # Recognition Service
    app.run(host="localhost", port=3001)
