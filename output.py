import sys

old = sys.stdout

sys.stdout = open("output.txt", "w")
print("this file should be in the output.txt file")
sys.stdout = old
print("this printed on the console")
