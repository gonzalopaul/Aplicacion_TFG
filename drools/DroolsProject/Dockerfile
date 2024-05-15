# Usar una imagen base oficial de Maven para construir y ejecutar la aplicación
FROM maven:3.8.1-openjdk-11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo pom.xml y descargar las dependencias
COPY pom.xml .
RUN mvn dependency:go-offline

# Copiar el resto del proyecto al contenedor
COPY . .

# Exponer el puerto en el que Spring Boot correrá
EXPOSE 8080

# Comando para correr la aplicación
CMD ["mvn", "spring-boot:run"]

