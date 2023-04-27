def greedy(v,w,C,n):
    x=[]
    r=[]
    for i in range(n):
        x.append(0)
        r.append(v[i]/w[i])
    for i in range(n):
        for j in range(n-1):
            if(r[i]>r[j]):
                r[i], r[j] = r[j], r[i]
                w[i], w[j] = w[j], w[i]
                v[i], v[j] = v[j], v[i]
    p = 0.0
    for i in range(n):
        if C >= w[i]:
            x[i] = 1
            C = C - w[i]
            p = p + v[i]
        else:
            x[i] = C / w[i]
            p = p + v[i] * x[i]
            print(x)
            print(p)
            break        


n = int(input("Enter the number of objects: "))
v,w = [],[]
C = int(input("Enter the weight of the bag: "))
print("Enter the values of each object: ")
for i in range(n):
    v.append(int(input()))
print("Enter the weights of each object: ")
for i in range(n):
    w.append(int(input()))
greedy(v,w,C,n)
