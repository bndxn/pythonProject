#Q2. Counting the lines in files

import sys

print ('List of arguments:', sys.argv)
print ('Total number of arguments:', len(sys.argv), 'arguments.')

for i in sys.argv:
    f = open(i,'r')
    print('File :', str(i), ', length :', str(len(f.readlines())))
