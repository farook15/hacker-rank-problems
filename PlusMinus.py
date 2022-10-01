def plusMinus(arr):
    length = len(arr)
    
    positivecount = 0
    negativecount = 0
    zerocount     = 0
    
    for i in range(0,length):
        if(arr[i]>0):
            positivecount += 1
        elif(arr[i]<0):
            negativecount +=1
        elif(arr[i]==0):
            zerocount +=1
    a = (positivecount/length)
    result = round(a,6)
    print(result)
    b = (negativecount/length)
    result1 = round(b,6)
    print(result1)
    c = (zerocount/length)
    result2 = round(c,6)
    print(result2)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
