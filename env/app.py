import requests
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

API_BASE_URL = 'http://localhost:3000/users'

@app.route('/')
def index():
    response = requests.get(API_BASE_URL)
    users = response.json()
    return render_template('index.html', users=users)

@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    response = requests.get(f'{API_BASE_URL}/{user_id}')
    user = response.json()
    return render_template('edit.html', user=user)

@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    names = request.form['names']
    surname = request.form['surname']

    payload = {
        'names': names,
        'surname': surname
    }

    response = requests.put(f'{API_BASE_URL}/{user_id}', json=payload)

    return redirect('/')

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    response = requests.delete(f'{API_BASE_URL}/{user_id}')
    return redirect('/')

@app.route('/create', methods=['POST'])
def create_user():
    identification = request.form['identification']
    names = request.form['names']
    surname = request.form['surname']

    payload = {
        'identification': int(identification),
        'names': names,
        'surname': surname
    }

    response = requests.post(API_BASE_URL, json=payload)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
