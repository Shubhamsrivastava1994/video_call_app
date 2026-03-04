from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("join-room")
def join(data):
    room = data["room"]
    join_room(room)

    print("User joined room:", room)

    emit("user-connected", room=room, include_self=False)


@socketio.on("offer")
def offer(data):

    room = data["room"]
    offer = data["offer"]

    emit("offer", offer, room=room, include_self=False)


@socketio.on("answer")
def answer(data):

    room = data["room"]
    answer = data["answer"]

    emit("answer", answer, room=room, include_self=False)


@socketio.on("ice-candidate")
def candidate(data):

    room = data["room"]
    candidate = data["candidate"]

    emit("ice-candidate", candidate, room=room, include_self=False)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
