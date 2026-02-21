import database
from flask import Flask, request


app = Flask(__name__)


@app.route("/tracks/<string:track_id>", methods=["PUT"])
def add_or_update_track(track_id):

    request_json = request.get_json()

    json_id = request_json.get("id")
    audio_base64 = request_json.get("audio")

    if json_id is None or audio_base64 is None or track_id != json_id:
        return "", 400

    repository = database.track_repository

    if repository.get_track(track_id):

        if repository.update_track(request_json):
            return "", 204

        return "", 500

    else:

        if repository.insert_track(request_json):
            return "", 201

        return "", 500


@app.route("/tracks/<string:track_id>", methods=["GET"])
def get_track(track_id):

    track = database.track_repository.get_track(track_id)

    if track:
        return track, 200

    return "", 404


@app.route("/tracks/<string:track_id>", methods=["DELETE"])
def delete_track(track_id):

    repository = database.track_repository

    if repository.get_track(track_id) is None:
        return "", 404

    if repository.delete_track(track_id):
        return "", 204

    return "", 500


@app.route("/tracks", methods=["GET"])
def list_tracks():

    tracks = database.track_repository.list_tracks()

    return tracks, 200


if __name__ == "__main__":
    # Catalogue Service
    app.run(host="localhost", port=3000)
