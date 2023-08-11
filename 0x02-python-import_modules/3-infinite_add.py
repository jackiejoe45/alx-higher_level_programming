#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    for i in range(1, count):
        sum += int(sys.argv[i])
    print("{}".format(sum))
