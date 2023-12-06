#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx

service nginx start

root="/data/web_static"
html="<html><head></head><body>Holberton School</body></html>"
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "$html" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "38i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

sudo service nginx restart