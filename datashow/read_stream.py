import time
import os
import sys

filename = 'data/stream.txt'
with open(filename, 'r') as f:
    filesize = os.stat(filename).st_size
    f.seek(filesize)
    while True:
        where = f.tell()
        line = f.readline()
        if not line:
            time.sleep(1)
            f.seek(where)
        else:
            print line