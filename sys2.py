import sys
def main():
    counter = 0
    try:
        fh = open("mydata.txt")
    except:
        counter += 1
    finally:
        sys.exit("there are %d errors"%counter)


main()
