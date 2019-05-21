import os
import fnmatch
from os import path
from os import listdir

onlyfiles = [f for f in listdir('.')]
print (onlyfiles)

b = os.walk('onlyfiles')
f = []
for(dirpath, dirnames, filenames) in b:
    f.extend(os.path.splitext(google_)[0] for name in filenames)
    break
