# Use an official Python 2.7.18 base image
FROM python:2.7.18

# Set environment variables to prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set up a working directory for your application
WORKDIR /app

# Copy the setup files and any other necessary files into the container
COPY requirements.txt /app/
COPY ez_setup.py /app/
COPY setup.py /app/
COPY development.ini /app/

# Copy the entire source code of your local project into the container
COPY . /app/

# Install system dependencies for Cairo and PyCairo
RUN apt-get update && apt-get install -y \
    gobject-introspection \
    libgirepository1.0-dev \
    libcairo2-dev \
    python-cairo \
    python-gi-cairo \
    build-essential \
    pkg-config

# Set PKG_CONFIG_PATH if necessary
ENV PKG_CONFIG_PATH=/usr/lib/pkgconfig:$PKG_CONFIG_PATH

# Install setuptools using ez_setup.py
RUN python ez_setup.py

# Install an older, compatible version of pip (20.3.4) for Python 2.7
RUN python -m pip install pip==20.3.4
RUN python -m pip install setuptools==44.1.1

# Manually install pycairo and pygobject
RUN pip install pycairo==1.11.1
RUN pip install pygobject==3.27.0

# Ensure that pip is installed and upgrade if necessary
RUN pip install -r requirements.txt

# Install Eutils from GitHub
RUN pip install git+https://github.com/hpiwowar/eutils.git#egg=Eutils

# Install project dependencies from setup.py
RUN python setup.py develop --verbose

# Create the log directory and log file with the correct permissions
RUN mkdir -p /var/log/abstrackr && touch /var/log/abstrackr/default.log && chmod 777 /var/log/abstrackr/default.log

# Set up external database connection information via environment variables
# You'll pass these when running the container
ENV DB_HOST=<db_host>
ENV DB_PORT=<db_port>
ENV DB_USER=<db_user>
ENV DB_PASSWORD=<db_password>
ENV DB_NAME=<db_name>
ENV SMTP_HOST=<smtp_host>
ENV SMTP_PORT=<smtp_port>
ENV SMTP_USERNAME=<smtp_username>
ENV SMTP_PASSWORD=<smtp_password>
ENV SMTP_SENDER=<smtp_sender>

# Expose any necessary ports (e.g., 8000 if the app runs on this port)
EXPOSE 5000

# Run your Pylons application (adjust this based on how your app is started)
CMD ["paster", "serve", "--reload", "production.ini"]