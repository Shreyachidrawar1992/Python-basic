
try:
    open('sample.txt')
except FileNotFoundError:
    print 'File not present'