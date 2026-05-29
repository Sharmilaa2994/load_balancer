from flask import Flask, render_template, jsonify
import threading, time
from server import Server
from swarm import ai_select, normal_select

app = Flask(__name__)

servers = [Server(i) for i in range(3)]
mode = "AI"
running = False
req_rate = 1

def simulate():
    global running
    while running:
        for _ in range(req_rate):
            if mode == "AI":
                s = ai_select(servers)
            else:
                s = normal_select(servers)
            s.handle_request()

        for s in servers:
            s.decay()

        time.sleep(1)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start():
    global running
    running = True
    threading.Thread(target=simulate).start()
    return "started"

@app.route("/increase")
def inc():
    global req_rate
    req_rate += 2
    return "increased"

@app.route("/mode/<m>")
def set_mode(m):
    global mode
    mode = m
    return "mode set"

@app.route("/data")
def data():
    return jsonify({
        "loads":[s.get_load() for s in servers],
        "history":[s.get_history() for s in servers],
        "mode":mode
    })

if __name__ == "__main__":
    app.run(debug=True)
