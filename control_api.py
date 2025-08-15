from flask import Flask, request, send_file
import subprocess
import os
app = Flask(__name__)
def download(data):
    path = None
    if not data["name"]:
        return {"status": "no name"}, 400
    name = data["name"]
    if not os.path.exists(f"/Users/rorybolan/Desktop/Download_files/{name}"):
        return {"status": "file not found"}, 404
    return send_file(f"/Users/rorybolan/Desktop/Download_files/{name}", as_attachment=True)




@app.route("/command", methods=["POST"])
def run_command():
    data = request.get_json(silent=True) or {}
    path = data.get("path")
    if not path:
        return {"status": "failed"}, 400
    match data["command"]:
        case 10:
            return download(data)
        case _:
            return {"status": "failed"}, 400
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)