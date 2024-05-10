def fibo(n):
    
    if n in {0, 1}:
        return n
    return ( fibo(n - 1) + fibo(n - 2) )
   
a = [fibo(i) for i in range(int(input('Enter the number of terms in fibo series (within 50): ')))]
print(a)
