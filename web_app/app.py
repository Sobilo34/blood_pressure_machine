#!/usr/bin/python3
"""
This is the app module for Blood pressure machine
"""
from flask import Flask, render_template, request, redirect, url_for
from models import storage
from models.user import User
from models.bp import Bp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = User(name=request.form['name'])
        storage.new(user)
        storage.save()
        return redirect(url_for('index'))
    users = storage.all(User)
    return render_template('index.html', users=users)

@app.route('/bp/<int:user_id>', methods=['GET', 'POST'])
def bp(user_id):
    if request.method == 'POST':
        user = storage.all(User)[user_id]
        bp = Bp(systolic=request.form['systolic'], diastolic=request.form['diastolic'], user_id=user_id)
        storage.new(bp)
        storage.save()
        return redirect(url_for('bp', user_id=user_id))
    user = storage.all(User)[user_id]
    bps = storage.all(Bp)
    return render_template('bp.html', user=user, bps=bps)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
