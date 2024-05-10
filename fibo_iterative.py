#fibo - using iterative method
first_num = 0
sec_num = 1

print(first_num, sec_num, sep = '\n')
for i in range(50):
    res = first_num + sec_num
    first_num = sec_num
    sec_num = res
    print(res)