#!/usr/bin/python3
"""
Module to delete out of date archives.
"""
from os import listdir
from fabric.api import *

env.hosts = ['3.86.7.210', '100.25.202.154']


def do_clean(number=0):
    """Fabric command to delete old archives."""
    number = 1 if int(number) == 0 else int(number)

    local_versions_dir = "versions"
    local_files = sorted(listdir(local_versions_dir))
    files_to_remove = local_files[:-number]

    for file in files_to_remove:
        local(f"sudo rm ./{local_versions_dir}/{file}")

    with cd("/data/web_static/releases"):
        remote_files = run("ls -tr").split()
        remote_files = [f for f in remote_files if "web_static_" in f]
        files_to_remove = remote_files[:-number]

        for file in files_to_remove:
            run(f"sudo rm -rf ./{file}")
