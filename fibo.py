import sys


def main(argv):
    print("fibonacci numbers")
    print(argv)
    if len(argv) != 2:
        print("anna yksi luku")
        return
    n=int(argv[1])
    print(n, fibo(n))

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)









if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)

