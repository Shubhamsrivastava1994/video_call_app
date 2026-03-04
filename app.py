import os
from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("join-room")
def join(data):
    room = data["room"]
    join_room(room)
    emit("user-connected", room=room, broadcast=True, include_self=False)

@socketio.on("offer")
def offer(data):
    emit("offer", data, broadcast=True, include_self=False)

@socketio.on("answer")
def answer(data):
    emit("answer", data, broadcast=True, include_self=False)

@socketio.on("ice-candidate")
def candidate(data):
    emit("ice-candidate", data, broadcast=True, include_self=False)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)