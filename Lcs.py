def lcs(a,b):
    l = [[0 for i in range(len(b)+1)]for i in range(len(a)+1)]
    route = [[[0,0] for i in range(len(b)+1)]for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1]==b[j-1]:
                l[i][j] = l[i-1][j-1]+1
                route[i][j] = [i-1,j-1]
            else:
                l[i][j] = max(l[i-1][j],l[i][j-1])
                route[i][j] = [i-1,j] if l[i-1][j] > l[i][j-1] else [i,j-1]
    #chars
    result =""
    i = len(a)
    j = len(b)
    while i != 0 and j != 0:
        if route[i][j] == [i-1,j-1]:
            result += a[i-1]
            i -= 1
            j -= 1
        elif route[i][j] == [i-1,j]:
            i -= 1
        else:
            j -= 1
    print(result[::-1])

a = input("Enter the first string: ")
b = input("Enter the second string: ")
lcs(a,b)