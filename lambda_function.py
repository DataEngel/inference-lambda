import os

from os import listdir
from os.path import isfile, join


def lambda_handler(event, context):

    cwd = os.getcwd()

    print("Event 1", event)
    
    print("Acual path: ", cwd)

    mypath = cwd

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print("Event 2", event)

    print("List of path ", onlyfiles)


lambda_handler(event = {}, context = None)