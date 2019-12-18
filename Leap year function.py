import sys


def isLeapYear(year):
    try:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    except TypeError:
        return "{Invalid numerical}"


if __name__ == "__main__":
    print (isLeapYear(int(sys.argv[1])))
