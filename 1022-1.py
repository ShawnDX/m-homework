def fibo(n):
    fi = [1, 1]
    for i in range(2, n):
        fi.append(fi[i-2] + fi[i -1 ])
    return fi

def even_sum(m):
    A = fibo(m)
    sum = 0
    for i in range(m + 1):
        if A[i] > m :
            break 
        elif A[i] % 2 ==0 :
            sum += A[i]
    return sum

print(even_sum(8))