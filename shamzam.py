import requests
from flask import Flask, request


TRACKS_SERVICE_URL = "http://localhost:3000/tracks"

RECOGNITION_SERVICE_URL = "http://localhost:3001/recognise"

app = Flask(__name__)


@app.route("/shamzam", methods=["POST"])
def identify_song():

    request_json = request.get_json()

    headers = {
        "Content-Type": "application/json"
    }

    recognition_response = requests.post(
        RECOGNITION_SERVICE_URL,
        headers=headers,
        json=request_json
    )

    if recognition_response.status_code != 200:
        return "", 404

    recognition_result = recognition_response.json()

    track_id = recognition_result["id"]

    catalogue_response = requests.get(
        f"{TRACKS_SERVICE_URL}/{track_id}"
    )

    if catalogue_response.status_code != 200:
        return "", 404

    return catalogue_response.json(), 200


if __name__ == "__main__":
    # Shamzam Gateway Service
    app.run(host="localhost", port=3002)
