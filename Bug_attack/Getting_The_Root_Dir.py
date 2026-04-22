def path_root_dir(path):
    splitted = path.split("/")
    return splitted[1]

path = "/usr/bin/data"
print(path_root_dir(path))