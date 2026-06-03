# Official slim image
FROM python:3.12.3-alpine

# Author information
LABEL maintainer="Bartosz Brudkowski"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8090


# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8090/')" || exit 1

# Run skrypt.py
CMD ["textual", "serve", "-p", "8090", "--host", "0.0.0.0", "--dev", "python3", "my_app.py"]

#docker build -t my-textual-app .
#docker run -p 8090:8090 my-textual-app
