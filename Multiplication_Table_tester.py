import random
passed = 0
failed = 0
missed = 0

print("Welcome to the multiplication test !!")
limit = int(input('Enter how many times you wanted to be tested: '))

for i in range(limit):
    num_1 = random.randrange(1, 10)
    num_2 = random.randrange(1, 10)
    print(num_1, 'X', num_2 , '= ', end ='')
    try:
        ans = int(input())
    except ValueError:
        missed += 1
        ans = 0
    if(ans == num_1 * num_2):
        continue
    else:
        failed += 1

print('No of questions attempted:', limit - missed)
print('Your score is :', limit - failed)
print('Missed ones:', missed)
