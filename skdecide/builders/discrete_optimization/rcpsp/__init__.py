import fnmatch
import os
import sys

pl = []

for p in sys.path:
    for dirpath, dirs, files in os.walk(p):
        for filename in fnmatch.filter(files, "minizinc*"):
            pl.append(dirpath)

print(pl)
os.environ["PATH"] += os.pathsep + os.pathsep.join(pl)
