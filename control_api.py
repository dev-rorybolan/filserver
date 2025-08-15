from flask import Flask, request, send_file
import subprocess
import os
from moviepy.editor import VideoFileClip
app = Flask(__name__)
def download(data):
    path = None
    if not data.get("name"):
        return {"status": "no name"}, 400
    name = data["name"]
    if not os.path.exists(f"/Users/rorybolan/Desktop/Download_files/{name}"):
        return {"status": "file not found"}, 404
    return send_file(f"/Users/rorybolan/Desktop/Download_files/{name}", as_attachment=True)


def return_files() -> dict:
    
    folder_path = "/Users/rorybolan/Desktop/Download_files"

    names = []
    lengths = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            file_path = os.path.join(folder_path, filename)
            names.append(filename)
            
            clip = VideoFileClip(file_path)
            lengths.append(clip.duration)  
            clip.close() 
    return {
    "names": names,
    "lengths": lengths
    }
@app.route("/command", methods=["POST"])
def run_command():
    data = request.get_json(silent=True) or {}
    path = data.get("path")
    if not path:
        return {"status": "failed"}, 400
    match data["command"]:
        case 10:
            return download(data)
        case 20:
            return return_files()
        case _:
            return {"status": "failed"}, 400
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
