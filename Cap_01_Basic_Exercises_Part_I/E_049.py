
    # The program lists all files in a directory

from os import listdir
from os.path import isfile, join

filesList = [ f for f in listdir('/home/') if isfile(join('/home/', f) )]

print(filesList)