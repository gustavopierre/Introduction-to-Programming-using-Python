try:
    fh = open("filename")
except IOError as e:
    print(e)
else:
    for i in fh: print()
    