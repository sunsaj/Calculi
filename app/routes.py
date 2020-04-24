from app import app
from flask import render_template, redirect, request, url_for
from app.model import User, db


@app.route('/')
def index():
    all_user = User.query.all()
    return render_template('index.html', title='Home',users=all_user)


@app.route('/insert', methods=['POST','GET'])
def insert():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))
