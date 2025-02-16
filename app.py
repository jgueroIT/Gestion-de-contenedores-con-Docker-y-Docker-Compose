from flask import Flask
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'rootpassword',
    'database': 'testdb'
}

@app.route('/')
def hello_world():
    # Conectar a la base de datos
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    # Obtener el mensaje de la base de datos
    cursor.execute("SELECT message FROM greetings WHERE id = 1")
    message = cursor.fetchone()[0]
    
    cursor.close()
    connection.close()
    
    return message

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
