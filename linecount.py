import os
from sys import stdout

VALID_EXTENSION = [
    '.txt','.py','.rs','.toml','.sh','.bat'
]

COLLAPSE_MSG = '[multiple binaries collapsed]'

collapse_binary = False

def count(f):
    global collapse_binary
    if os.path.isdir(f):
        return sum([count(os.path.join(f,n)) for n in os.listdir(f)])
    elif os.path.isfile(f):
        if any([f.endswith(x) for x in VALID_EXTENSION]):
            data = open(f).readlines()
            line_count = len(data)
            if collapse_binary:
                collapse_binary=False
                print ''
            print f.ljust(70)+': '+str(line_count)
            return line_count
        else:
            if collapse_binary:
                stdout.write('\r'+COLLAPSE_MSG.ljust(70)+': n/a')
            else:
                stdout.write(f.ljust(70)+': n/a')
            collapse_binary=True
            return 0

print '\n\nTotal lines: '+str(count('.'))
