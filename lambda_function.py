import os

from os import listdir
from os.path import isfile, join


def lambda_handler(event, context):

    cwd = os.getcwd()
    
    print("Acual path: ", cwd)

    mypath = cwd

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print("List of path ", onlyfiles)
    