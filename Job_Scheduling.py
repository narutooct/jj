def jobsched(n,p,d):
    max = d[0]
    job = [i+1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if p[i]>p[j]:
                p[i], p[j] = p[j], p[i]
                d[i], d[j] = d[j], d[i]
                job[i], job[j] = job[j], job[i]
        if d[i]>max:
            max = d[i]
    jobs = [0 for i in range(max)]
    time = [0 for i in range(max)]
    for i in range(n):
        for j in range(d[i],0,-1):
            if time[j-1] == 0:
                time[j-1] = p[i]
                jobs[j-1] = job[i]
                break
    print(jobs)
    print(time)

n = int(input("Enter the number of jobs: "))
p = list(map(int, input("Enter the profits: ").split()))
d = list(map(int, input("Enter the deadlines: ").split()))
jobsched(n,p,d)