def main():
    try:
        for line in readline('file1.txt'): print(line.strip())
    except IOError as e:
        print('cannot read file: ', e)


def readline(filename):
    fh = open(filename)
    return fh.readlines()


main()
