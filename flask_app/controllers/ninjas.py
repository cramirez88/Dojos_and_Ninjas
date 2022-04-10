from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import ninja, dojo

#Routes

@app.route('/add/ninja')
def add_ninja():
    return render_template('ninja.html', dojos=dojo.Dojo.read_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')
