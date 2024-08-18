#!/usr/bin/python3
"""
Module for full deployment on web servers.
"""
import os
from datetime import datetime
from fabric.api import *


env.hosts = ['3.86.7.210', '100.25.202.154']


def do_pack():
    """ Fabric script to generate .tgz from web_static contents."""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """ Fabric script to distribute archive to web servers."""
    if not os.path.exists(archive_path):
        return False

    archivename = os.path.basename(archive_path)
    filename = archivename.split('.')[0]
    target = '/data/web_static/releases/{}'.format(filename)

    try:
        put(archive_path, "/tmp")
        run("sudo mkdir -p {}".format(target))
        run("sudo tar -xzf /tmp/{} -C {}".format(archivename, target))
        run("sudo rm /tmp/{}".format(archivename))
        run("sudo mv {}/web_static/* {}".format(target, target))
        run("sudo rm -rf {}/web_static".format(target))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(target))
        return True
    except Exception as e:
        return False


def deploy():
    """ Fabric script to create & distribute archive to web servers."""
    filepath = do_pack()
    if not filepath:
        return None
    return do_deploy(filepath)
