def main():
    try:
        for line in readline('file1.doc'): print(line.strip())
    except IOError as e:
        print('cannot read file: ', e)
    except ValueError as e:
        print('wrong file extension: ', e)


def readline(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')


main()
