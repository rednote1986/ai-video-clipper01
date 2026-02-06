from flask import Flask, request, jsonify
from clipper import process_video
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    if "video" not in request.files:
        return jsonify({"error": "video tidak ditemukan"}), 400

    video = request.files["video"]
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    clips = process_video(video_path)

    return jsonify({
        "status": "berhasil",
        "jumlah_klip": len(clips),
        "klip": clips
    })

if __name__ == "__main__":
    app.run(debug=True)
