from flask import Flask
from flask import render_template
import os
import nba_py as nba
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # games = get_games()

    return render_template("index.html",
            title="Daily Scores")

def get_games():
    scoreboard = nba.Scoreboard()
    return scoreboard.line_score()

if __name__=="__main__": 
    print(get_games())
    app.run(host="0.0.0.0", port = 8080, threaded = True, debug = True)



