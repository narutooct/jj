def flyod(d):
    for i in range(len(d)):
        for j in range(len(d)):
            for k in range(len(d)):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    for i in range(len(d)):
        print(d[i])

inf=99
("d=[[0, 5, inf, 10],[inf, 0, 3, inf],[inf, inf, 0, 1],[inf, inf, inf, 0]]")
n = int(input("Enter the no of nodes: "))        
d=[]
for i in range(n):
    d.append(list(map(int, input().split())))

flyod(d)