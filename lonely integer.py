def lonelyinteger(a):
    a= sorted(a)
    if(len(a)<3):
        return a[0]
    elif(a[0]!=a[1]):
        return a[0]
    else:
        return lonelyinteger(a[2:])
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
