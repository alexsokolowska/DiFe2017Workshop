from sys import argv

script, arg1 = argv

def read():
    fh = open(raw_input("Filename to read:"), 'r')
    for line in fh:
        print line
    fh.close()

def write():
    new_name = raw_input("Name of a file to write:")
    fnew = open(new_name, 'w')
    fnew.write(raw_input("Numer to write:"))
    fnew.close()

if arg1=='read':
    read()
elif arg1=='write':
    write()
else:
    print "USAGE: python script.py keyword \n where keyword is read or write."