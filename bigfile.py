f = open("bigfile.txt", "w")

for i in range(100000):
    msg = "This is line number %d in file "%i
    print(msg, file=f, end="\n")
    