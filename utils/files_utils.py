import os


def get_scripts():
    scripts = []

    for file in os.listdir("scripts"):
        name = file.rsplit(".", 1)[0]
        scripts.append(name)

    return scripts