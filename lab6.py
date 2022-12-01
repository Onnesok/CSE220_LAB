######################### Question 1 ##############################
#@@@@@@@@@@@@@@@@@@@@@@@@@@  A  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def fact(n):
#   if n == 1:
#     return 1
#   else:
#     return n*fact(n-1)
# print(fact(4))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  B  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def fibonacci(n):
#   if n <= 1:
#     return 1
#   else:
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  C  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def arr(a, i, n):
#   if i == n:
#     return
#   else:
#     print(a[i])
#     return arr(a, i+1, n)
  
# arr([1,2,5,4,10], 0, 5)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  D  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def power(a, n):
#   if n ==0:
#     return 1
#   else:
#     return a * power(a, n-1)

# print(power(3,3))

################################ Task 2  ###############################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   A   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
list to binary 


###############################  Task 4  ###############################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  A  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def num(i, n):
#   if i == n+1:
#     print()
#     return
#   print(i, end=" ")
#   i = i+1
#   return num(i, n)

# def pattern(a, i):
#   if i == a+1:
#     return
#   num(1, i)
#   pattern(a, i+1)
# pattern(5, 1)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  B  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def forward(i, n):
#   if i == n+1:
#     print()
#     return
#   print(i, end=" ")
#   i = i+1
#   return forward(i, n)

# def num(a, i, j):
#   if i == j-1:
#     return
#   print(" ", end=" ")
#   i = i-1
#   return num(a, i, j)

# def pattern(a, i):
#   if i == a:
#     return
#   num(a, a-i, 1)
#   forward(1, i)
#   pattern(a, i+1)
#   if i == a-1:
#       forward(1, i+1)
# pattern(5, 1)