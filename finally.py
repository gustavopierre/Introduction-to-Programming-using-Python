def main():
    counter = 0
    try:
        fh = open('file1.txt')
        for line in fh: print(line.strip())
    except:
        counter += 1
        #print('there was an error')
        pass
    finally:
        print()
        print('there were %d errors in the process'%counter)
        print('all work was done')


main()
