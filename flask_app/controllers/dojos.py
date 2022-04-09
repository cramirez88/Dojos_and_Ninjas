from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect ('/dojos')

@app.route('/dojos')
def dojos():
    dojos=Dojo.read_all()
    return render_template('index.html', all_dojos = dojos )