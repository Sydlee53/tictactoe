from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

class Anything:
  def __eq__(self, other):
    return True


@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"

    gameover = session["board"] in [
    [[ "X",  "X",  "X"], [Anything(), Anything(), Anything()], [Anything(), Anything(), Anything()]],
    [[Anything(), Anything(), Anything()], [ "X",  "X",  "X"], [Anything(), Anything(), Anything()]],
    [[Anything(), Anything(), Anything()], [Anything(), Anything(), Anything()], [ "X",  "X",  "X"]],
    [[ "X", Anything(), Anything()], [ "X", Anything(), Anything()], [ "X", Anything(), Anything()]],
    [[Anything(),  "X", Anything()], [Anything(),  "X", Anything()], [Anything(),  "X", Anything()]],
    [[Anything(), Anything(),  "X"], [Anything(), Anything(),  "X"], [Anything(), Anything(),  "X"]],
    [[ "X", Anything(), Anything()], [Anything(),  "X", Anything()], [Anything(), Anything(),  "X"]],
    [[Anything(), Anything(),  "X"], [Anything(),  "X", Anything()], [ "X", Anything(), Anything()]],
    [[ "O",  "O",  "O"], [Anything(), Anything(), Anything()], [Anything(), Anything(), Anything()]],
    [[Anything(), Anything(), Anything()], [ "O",  "O",  "O"], [Anything(), Anything(), Anything()]],
    [[Anything(), Anything(), Anything()], [Anything(), Anything(), Anything()], [ "O",  "O",  "O"]],
    [[ "O", Anything(), Anything()], [ "O", Anything(), Anything()], [ "O", Anything(), Anything()]],
    [[Anything(),  "O", Anything()], [Anything(),  "O", Anything()], [Anything(),  "O", Anything()]],
    [[Anything(), Anything(),  "O"], [Anything(), Anything(),  "O"], [Anything(), Anything(),  "O"]],
    [[ "O", Anything(), Anything()], [Anything(),  "O", Anything()], [Anything(), Anything(),  "O"]],
    [[Anything(), Anything(),  "O"], [Anything(),  "O", Anything()], [ "O", Anything(), Anything()]]
    ]

    return render_template("game.html", game=session["board"], turn=session["turn"], gameover=gameover)

@app.route("/play/<int:row>/<int:col>")
def play(row, col):

    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "O"
    else:
        session["turn"] = "X"

    return redirect(url_for("index"))



@app.route("/reset")
def reset():
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["turn"] = "X"

    return redirect("/")
