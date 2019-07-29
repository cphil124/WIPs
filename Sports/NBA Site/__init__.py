from flask import Flask
from flask import render_template

import nba_py as nba
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    get_games()
    return render_template("index.html",
            title="Daily Scores")

def get_games():
    scoreboard = nba.Scoreboard()
    print(scoreboard.line_score())

if __name__=="__main__": 
    app.run(host="0.0.0.0", port = 8080, threaded = True, debug = True)



