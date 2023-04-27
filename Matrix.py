def matrix_chain_multiplication(p):
    n = len(p) - 1
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n - 1)] for x in range(n - 1)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j - 1] = k
    return m, s

def print_table(m):
    for row in m:
        print(row)

def print_order(i, j, s, name):
    if i == j:
        print("A", i+1, end=" ")
    else:
        print("(", end="")
        k = s[i][j - 1]
        print_order(i, k, s, name)
        print_order(k + 1, j, s, name)
        print(")", end="")


p = [30, 35, 15, 5, 10, 20]
m, s = matrix_chain_multiplication(p)
print_table(m)
print(" ")
print("The Order is ")
print_order(0, len(p) - 2, s, "A")