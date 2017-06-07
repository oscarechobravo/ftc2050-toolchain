import os

def create_dir(dname):
    if not os.path.exists(dname):
        os.makedirs(dname)
