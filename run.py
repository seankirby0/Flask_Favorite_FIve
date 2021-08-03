from flask import Flask, render_template

app = Flask(__name__)

class Config:
    FLASK_APP = 'run'
    FLASK_ENV = 'development'

app.config.from_object(Config)

@app.route('/')
def home():
    title = "Kirby's Faves"
    return render_template('home.html', title = title)

@app.route('/fab')
def fav_five():
    favorite_teams = ['chicago bulls', 'duke blue devils', 'chicago bears', 'chicago cubs', 'chicago fire']
    return render_template('fav_five.html', favorite_teams = favorite_teams)