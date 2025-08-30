from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea todas las tablas
    app.run(debug=True)
