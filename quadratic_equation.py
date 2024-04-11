
import sys
import math

def laske(a, b, c):

    try:
        ratkaisu1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
        ratkaisu2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
        return (ratkaisu1, ratkaisu2)
    except ValueError:
        return "Ei arvoa"

def main(argv):

    #print(argv)

    if len(argv) < 4:
        print("anna kolme lukua")
    else:
        print("ratkaisu on:", laske(int(argv[1]), int(argv[2]), int(argv[3])))

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)
