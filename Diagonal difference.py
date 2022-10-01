def diagonalDifference(arr):
    temp1 = 0
    temp2 = 0
    for i in range(0,len(arr)):
        temp1 = temp1 + arr[i][i]
    for j in range(0,len(arr)):
        temp2 = temp2 + arr[j][len(arr)-1-j]
    return abs(temp1-temp2)
        
        
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
     

    fptr.write(str(result) + '\n')

    fptr.close()
