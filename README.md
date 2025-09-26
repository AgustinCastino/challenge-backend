# Challenge Backend Leafnoise

## Descripción del Proyecto
Este proyecto es una API RESTful desarrollada con Flask que permite gestionar empleados en una base de datos MongoDB Atlas. La API incluye funcionalidades para crear, leer, actualizar y eliminar empleados, así como generar reportes en formato Excel. Además, cuenta con autenticación mediante JWT.

## Configuración del Proyecto
1. Clonar este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Navegar al directorio del proyecto:
   ```bash
   cd challenge-backend
   ```
3. Crear un entorno virtual:
   ```bash
   python3 -m venv env
   ```
4. Activar el entorno virtual:
   - En macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - En Windows:
     ```bash
     .\env\Scripts\activate
     ```
5. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
6. Configurar las variables de entorno en un archivo. Se utilizó Mongo Atlas por lo que recomiendo crear un cluster y hacer la conexión con el driver de Python `.env`:
   ```env
   MONGO_URI=mongodb+srv://<usuario>:<contraseña>@<cluster>.mongodb.net/<base_de_datos>
   SECRET_KEY=
   ```
7. Iniciar la aplicación:
   ```bash
   python src/main.py
   ```

## Endpoints

### **Autenticación**
#### `POST /login`
- **Descripción**: Simula la autenticación de un usuario con JWT. Está hardcodeado para `{user: admin, password: 123}`.
- **Cuerpo de la solicitud**:
  ```json
  {
      "username": "admin",
      "password": "123"
  }
  ```

### **Usuarios**
#### `POST /users`
- **Descripción**: Crea un nuevo empleado. Es el único endpoint que requiere autenticación.
- **Cuerpo de la solicitud**:
  ```json
  {
      "nombre": "Lionel",
      "apellido": "Messi",
      "email": "leo@example.com",
      "puesto": "developer",
      "salario": 10000,
      "fecha_ingreso": "2025-01-01"
  }
  ```
- **Autenticación**: Requiere un token JWT en el encabezado `Authorization`.

#### `GET /users`
- **Descripción**: Obtiene una lista de empleados.

#### `GET /users?puesto=<puesto>`
- **Descripción**: Filtra empleados por puesto.

#### `GET /users?page=<número>&limit=<número>`
- **Descripción**: Obtiene empleados con paginación.

#### `GET /users?puesto=<puesto>&page=<número>&limit=<número>`
- **Descripción**: Filtra empleados por puesto con paginación.

#### `GET /users/<userId>`
- **Descripción**: Obtiene un empleado por su ID.

#### `PUT /users/<userId>`
- **Descripción**: Actualiza un empleado por su ID.
- **Cuerpo de la solicitud**:
  ```json
  {
      "nombre": "Nombre Actualizado",
      "apellido": "Apellido actualizado",
      "email": "nombre1@example.com",
      "puesto": "developer",
      "salario": 50000,
      "fecha_ingreso": "2023-01-01"
  }
  ```

#### `DELETE /users/<userId>`
- **Descripción**: Elimina un empleado por su ID.

### **Reportes**
#### `GET /report`
- **Descripción**: Genera un reporte en formato Excel con estadísticas de los empleados.
- **Respuesta**:
  - Archivo Excel descargable.

## Probar los Endpoints
Se pueden probar los endpoints utilizando el archivo `req.http` incluido en el proyecto. Se debe instalar la extensión **REST Client** en Visual Studio Code.

## Estructura del Proyecto
```
challenge-backend/
├── env/                  # Entorno virtual
├── src/
│   ├── main.py           # Punto de entrada de la aplicación
│   ├── config/           # Configuración de la base de datos
│   ├── routes/           # Definición de rutas
│   ├── controller/       # Controladores
│   ├── service/          # Lógica de negocio
│   ├── model/            # Interacción con la base de datos
│   ├── utils/            # Utilidades (manejo de errores)
│   └── exceptions/       # Definición de excepciones personalizadas
└── requirements.txt      # Dependencias del proyecto
```
