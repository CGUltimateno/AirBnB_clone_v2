#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers,
using the function deploy."""

from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['52.23.177.244	', '34.232.78.203']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder of
    your AirBnB Clone repo."""
    try:
        if not exists("versions"):
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except:
        return False


def deploy():
    """Creates and distributes an archive to your web servers."""
    try:
        path = do_pack()
        return do_deploy(path)
    except:
        return False
