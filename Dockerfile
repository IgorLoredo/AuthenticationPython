
# Use a base Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install the required dependencies
RUN pip install -r requirements.txt

# Expose the necessary ports
EXPOSE 5000

# Specify the command to run the application
CMD ["python", "login.py"]



# # Construir a imagem Docker
# docker build -t my-python-app .

# # Executar o container Docker
# docker run -p 5000:5000 my-python-app