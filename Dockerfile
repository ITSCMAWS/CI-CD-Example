# Set the working directory
WORKDIR /app

# Copy all your project files into the directory
COPY . .

# Now, when gunicorn runs, it will execute from /app where your code lives
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "main:app"]
