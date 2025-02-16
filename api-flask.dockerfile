# Usa una imagen base de Python oficial
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios para la aplicación
COPY requirements.txt /app/

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación a la imagen
COPY . /app/

# Expone el puerto donde la aplicación Flask correrá
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
