from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# Liste des utilisateurs 
users = []

# Route GET pour récupérer la liste des utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Route POST pour ajouter un utilisateur
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

# Route pour la page d'accueil avec les options d'ajout et de liste des utilisateurs
@app.route('/')
def index():
    return render_template('main.html')
# Route pour afficher la liste des utilisateurs
#@app.route('/')
#def index():
#    return render_template('index.html', users=users)

# Route pour afficher le formulaire d'ajout
@app.route('/add_user', methods=['GET', 'POST'])
def add_user_page():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        birth_city = request.form['birth_city']
        new_user = {
            'id': len(users) + 1,
            'first_name': first_name,
            'last_name': last_name,
            'birth_date': birth_date,
            'birth_city': birth_city
        }
        users.append(new_user)
        print(users)  # Debugging: print the list of users to the console
        return redirect(url_for('index'))
    return render_template('add_user.html')

# Route pour afficher la liste des utilisateurs
@app.route('/list_users')
def list_users_page():
    return render_template('list_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)