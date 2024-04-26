#code snippet to show the datatypes in python

a = 10                                                                       # int
b = 23.4566                                                                  # float
c = "Hello Multimise"                                                        # string
d = (10 + 0j)                                                                # complex
e = [1, 2, 3, 4, 5, 6, 7, "Grow", "Learn", "Explore", 1114.67, (19+0j)]      # List
f = (1, 2, 3, 4, 5, 6, 7, "Grow", "Learn", "Explore", 1114.67, (19+0j))      # Tuple
g = {0, 1, 2, 3, 4}                                                          # set
h = calories = {'apple' : 52, 'banana' : 89, 'choco' : 546}                  # Dictionary
k = True                                                                     # Boolean

allInOne = [a, b, c, d, e, f, g, h, k]

for i in allInOne[:]:
    print('Object Name = ', i, ' and it belongs to ',type(i), sep=' ')
    print('-' * 100)
   
    



