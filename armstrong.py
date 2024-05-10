#There are 14 Armstrong numbers in the range 1-5000, which are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634.

num = int(input('Enter an Armstrong number to check: '))

sum_of_digits = 0
len_of_digits = len(str(num))
temp = num
while temp > 0:
   digit = temp % 10
   sum_of_digits = sum_of_digits + digit ** len_of_digits
   temp = temp // 10
   
if num == sum_of_digits:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")