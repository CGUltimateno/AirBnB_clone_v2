#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx

service nginx start

root="/data/web_static"
html="<html><head></head><body>Holberton School</body></html>"

# Create the folder /data/ if it doesn’t already exist

mkdir -p "$root/releases/test"
mkdir -p "$root/shared"
echo "$html" | tee "$root/releases/test/index.html" > /dev/null

sudo rm -rf "$root/current"
sudo ln -sf "$root/releases/test" "$root/current"
sudo chown -R "ubuntu:ubuntu" "/data/"

nginx_config="/etc/nginx/sites-available/default"
sed -i "/server_name _;/a\\        location /hbnb_static/ {alias $root/current/;}" "$nginx_config" > /dev/null

sudo service nginx restart