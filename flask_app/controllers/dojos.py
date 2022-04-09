from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect ('/dojos')
# get dojos from db route
@app.route('/dojos')
def dojos():
    dojos=Dojo.read_all()
    return render_template('index.html', all_dojos = dojos )

#add dojos route

@app.route('/add', methods=["POST"])
def add_dojo():
    data = {
      'name': request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')
