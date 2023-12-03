from flask import Flask, render_template, g
import sqlite3
import Base

app = Flask(__name__)

app.config['DATABASE'] = "static/db/planets.db"
app.secret_key = "jgfouh876"

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def get_connect():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

navMenu = [
    {"link": "/index", "name": "Главная"},
    {"link": "/planets", "name": "Направления"},
    {"link": "/info", "name": "О компании"}
]

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", menu=navMenu)

@app.route("/planets")
def planets():
    con = get_connect()
    base = Base.PlanetsDB(con)
    return render_template("planets.html", menu=navMenu, cards=base.getAllPlanets())

@app.route("/info")
def info():
    return render_template("info.html", menu=navMenu)

@app.route("/planet/<int:value>")
def plnt(value):
    con = get_connect()
    base = Base.PlanetsDB(con)
    planet = base.getPlanet(value)
    return render_template("planet.html", image=planet["image"], price=planet["price"], name=planet["name"], destination=planet["destination"])
   
@app.teardown_appcontext
def close_connect(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == "__main__":
    app.run()