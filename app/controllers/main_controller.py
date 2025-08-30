from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models.user_model import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# CRUD - Read (Listar todos los usuarios)
@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('list.html', users=users)

# CRUD - Create (Mostrar formulario y crear usuario)
@app.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        
        flash('Usuario creado exitosamente!', 'success')
        return redirect(url_for('list_users'))
    
    return render_template('create.html')

# CRUD - Update (Mostrar formulario y actualizar usuario)
@app.route('/users/<int:id>/edit', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        
        flash('Usuario actualizado exitosamente!', 'success')
        return redirect(url_for('list_users'))
    
    return render_template('edit.html', user=user)

# CRUD - Delete (Eliminar usuario)
@app.route('/users/<int:id>/delete', methods=['POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    
    flash('Usuario eliminado exitosamente!', 'warning')
    return redirect(url_for('list_users'))