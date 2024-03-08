#!/usr/bin/env bash

# Bash script that sets up web servers for the deployment of web_static

# Check if the location block already exists in the configuration
if ! grep -q "location /hbnb_static" /etc/nginx/sites-enabled/default; then
    # If not, proceed to add the location block
    sudo apt-get update
    sudo apt-get -y install nginx
    sudo ufw allow 'Nginx HTTP'

    sudo mkdir -p /data/
    sudo mkdir -p /data/web_static/
    sudo mkdir -p /data/web_static/releases/
    sudo mkdir -p /data/web_static/shared/
    sudo mkdir -p /data/web_static/releases/test/
    sudo touch /data/web_static/releases/test/index.html
    sudo echo "<html>
      <head>
      </head>
      <body>
        Holberton School
      </body>
    </html>" | sudo tee /data/web_static/releases/test/index.html

    sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

    sudo chown -R ubuntu:ubuntu /data/

    # Add the location block to the Nginx configuration
    sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

    # Restart Nginx
    sudo service nginx restart
else
    echo "Location block for /hbnb_static already exists. No action taken."
fi

