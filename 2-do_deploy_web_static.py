#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers, using the
function do_deploy."""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.23.177.244', '34.232.78.203']


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
        run('mv {0}{1}/web_static/* {0}{1}/'.format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except:
        return False
