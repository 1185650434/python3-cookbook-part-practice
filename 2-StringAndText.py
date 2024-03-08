

from urllib.request import urlopen

def read_data(name:str):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

def func_2_start_end():
    pass