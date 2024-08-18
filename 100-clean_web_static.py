#!/usr/bin/python3
"""
Module to delete out of date archives.
"""
from os import listdir
from fabric.api import *

env.hosts = ['3.86.7.210', '100.25.202.154']


def do_clean(number=0):
    """Fabric command to delete old archives."""
    number = int(number)
    if number < 1:
        number = 1

    local_versions_dir = "versions"
    local_files = sorted(listdir(local_versions_dir))
    files_to_keep = local_files[-number:]
    files_to_remove = local_files[:-number]

    for f in files_to_remove:
        local("sudo rm ./{}/{}".format(local_versions_dir, f))

    with cd("/data/web_static/releases"):
        remote_files = run("ls -tr").split()
        remote_files = [r for r in remote_files if "web_static_" in r]
        files_to_keep = remote_files[-number:]
        files_to_remove = remote_files[:-number]

        for i in files_to_remove:
            run("sudo rm -rf ./{}".format(i))
