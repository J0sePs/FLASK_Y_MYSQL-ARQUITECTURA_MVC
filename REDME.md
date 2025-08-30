# Flask MVC CRUD Application

Una aplicación web Flask completa implementando el patrón MVC (Modelo-Vista-Controlador) con operaciones CRUD para gestión de usuarios.

## 📋 Características

- ✅ **Arquitectura MVC** bien estructurada
- ✅ **CRUD completo** para usuarios (Crear, Leer, Actualizar, Eliminar)
- ✅ **Base de datos MySQL** con SQLAlchemy ORM
- ✅ **Variables de entorno** para configuración segura
- ✅ **Templates HTML** con herencia usando Jinja2
- ✅ **Mensajes flash** para feedback al usuario
- ✅ **Archivos estáticos** (CSS y JavaScript)

## 🏗️ Estructura del Proyecto

```
mi_proyecto_mvc/
├── .env                    # Variables de entorno
├── config.py              # Configuración de la aplicación
├── requirements.txt       # Dependencias del proyecto
├── run.py                 # Punto de entrada de la aplicación
├── REDME.md               # Documentación del proyecto
└── app/
    ├── __init__.py        # Inicialización de Flask
    ├── controllers/       # Controladores (lógica de rutas)
    │   ├── __init__.py
    │   └── main_controller.py
    ├── models/            # Modelos de datos
    │   ├── __init__.py
    │   └── user_model.py
    └── views/             # Vistas (templates y archivos estáticos)
        ├── static/
        │   ├── css/
        │   │   └── style.css
        │   └── js/
        │       └── script.js
        └── templates/
            ├── base.html      # Template base
            ├── index.html     # Página principal
            ├── about.html     # Página de información
            ├── list.html      # Lista de usuarios
            ├── create.html    # Formulario de creación
            └── edit.html      # Formulario de edición
```

## 🚀 Instalación y Configuración

### 1. Prerrequisitos

- Python 3.8+
- MySQL Server
- pip (gestor de paquetes de Python)

### 2. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd mi_proyecto_mvc
```

### 3. Crear entorno virtual

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar base de datos

1. Crear una base de datos MySQL llamada `users`
2. Configurar las credenciales en el archivo `.env`

### 6. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu_clave_secreta_super_segura_123
DB_USER=root
DB_PASSWORD=tu_password_mysql
DB_PORT=3306
DB_HOST=localhost
DB_NAME=users
```

### 7. Ejecutar la aplicación

```bash
python run.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 🎯 Funcionalidades

### Rutas disponibles:

- **`/`** - Página principal
- **`/about`** - Página de información
- **`/users`** - Lista de todos los usuarios
- **`/users/new`** - Formulario para crear nuevo usuario
- **`/users/<id>/edit`** - Formulario para editar usuario
- **`/users/<id>/delete`** - Eliminar usuario (POST)

### Operaciones CRUD:

1. **Create (Crear)**: Agregar nuevos usuarios
2. **Read (Leer)**: Visualizar lista de usuarios
3. **Update (Actualizar)**: Modificar datos de usuarios existentes
4. **Delete (Eliminar)**: Remover usuarios del sistema

## 🛠️ Tecnologías Utilizadas

- **Flask 2.3.3** - Framework web de Python
- **Flask-SQLAlchemy 3.0.5** - ORM para base de datos
- **python-dotenv 1.0.0** - Manejo de variables de entorno
- **PyMySQL 1.1.0** - Conector MySQL para Python
- **MySQL** - Sistema de gestión de base de datos
- **HTML5** - Estructura de páginas web
- **CSS3** - Estilos de la aplicación
- **JavaScript** - Funcionalidad del lado del cliente

## 📁 Componentes Principales

### Modelos (`app/models/user_model.py`)
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
```

### Controladores (`app/controllers/main_controller.py`)
- Manejo de rutas HTTP
- Lógica de negocio
- Interacción con modelos
- Renderizado de templates

### Vistas (`app/views/templates/`)
- Templates HTML con Jinja2
- Herencia de templates base
- Formularios para CRUD
- Mensajes de feedback

## 🔧 Configuración (`config.py`)

La aplicación utiliza variables de entorno para:
- Clave secreta de Flask
- Credenciales de base de datos
- Configuración de SQLAlchemy

## 🚦 Estado del Proyecto

✅ **Completado**: Aplicación CRUD básica funcional  
✅ **Completado**: Estructura MVC implementada  
✅ **Completado**: Base de datos configurada  
✅ **Completado**: Templates con estilos básicos  

## 🎓 Propósito Educativo

Este proyecto está diseñado como una aplicación de aprendizaje para:
- Comprender el patrón MVC en Flask
- Practicar operaciones CRUD
- Aprender integración de base de datos
- Manejo de templates y archivos estáticos

## 🔮 Próximas Mejoras

- [ ] Validación de formularios
- [ ] Autenticación de usuarios
- [ ] Paginación en lista de usuarios
- [ ] Mejores estilos CSS
- [ ] Tests unitarios
- [ ] Búsqueda y filtros
- [ ] API REST

## 🤝 Contribuciones

Este es un proyecto educativo. Las mejoras sugeridas incluyen:
- Validación de formularios
- Autenticación de usuarios
- Paginación en lista de usuarios
- Mejores estilos CSS
- Tests unitarios

## 📝 Licencia

Proyecto educativo - Uso libre para aprendizaje

---

**Autor**: Desarrollado como proyecto de aprendizaje de Flask MVC  - PRIMENOTE365
**Fecha**: 2025  
**Versión**: 1.0.0



