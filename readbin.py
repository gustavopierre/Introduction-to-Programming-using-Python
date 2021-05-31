def main():
    inputfile = open('spacex.jpg', 'rb')
    outputfile = open('spacex2.jpg', 'wb')

    buffersize = 50000
    buffer = inputfile.read(buffersize)
    while len(buffer):
        outputfile.write(buffer)
        print('.', end=' ')
        buffer = inputfile.read(buffersize)
    print()
    print("Copy Complete!")


main()
