#!/usr/bin/python3
"""
Module to generate archive from web_static contents
"""
from datetime import datetime
from fabric.api import *


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
