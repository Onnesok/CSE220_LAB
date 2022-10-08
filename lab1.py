############################  Task 1  ############################
# def shiftLeft(source, k):
#     j = 0
#     while j < k:
#         for i in range(len(source)-1):
#             source[i] = source[i+1]
#         source[-1] = 0
#         j+=1
#     print(source)

# source=[10,20,30,40,50,60]
# shiftLeft(source,3)

##############################  Task 2  ############################
# def rotateLeft(source, k):
#     temp = []
#     for i in range(k):
#         temp.append(source[i])
#     for j in range(k):
#         source[j] = source[k]
#         source[k] = temp[j]
#         k += 1
#     print(source) 

# source=[10,20,30,40,50,60]
# rotateLeft(source,3)

#######################  Task 3  ##################################
# def shiftRight(source, k):
#     for i in range(k):
#         source[-k+i] = source[i]
#         source[i] = 0
#     print(source)

# source=[10,20,30,40,50,60]
# shiftRight(source,3)

########################### Task 4  ##############################
# #  Consider an array named source. Write a method/function named rotateRight( source, k) that rotates all the elements of the source array to the right by 'k' positions. You must execute the method by passing an array and number of cells to be shifted. After calling the method, print the array to show whether the elements have been shifted properly.
# # Example:
# # source=[10,20,30,40,50,60]
# # rotateRight(source,3)
# # After calling rotateRight(source,3), printing the array should give the output as: 
# #  [ 40, 50, 60, 10, 20, 30]
# def rotateRight(source, k):
#     temp = []
#     for i in range(k):
#         temp.append(source[i])
#     for j in range(k):
#         source[j] = source[k]                                 #######################################
#         source[k] = temp[j]                                  ############### confused ##################
#         k += 1                                                ##########################################
#     print(source) 

# source=[10,20,30,40,50,60]
# rotateRight(source,3)

#################################  Task 5  ##################################
# def remove( source, size, idx):
#     i = idx
#     while i <= size:
#         source[i] = source[i+1]
#         i+=1
#     print(source)

# source=[10,20,30,40,50,0,0]
# remove(source,5,2)

#################################  Task 6  #################################
# def  removeAll( source, size, element):
#     for i in range(size):
#         if source[i] == element:
#             j = i
#             while j <= size:
#                 source[j] = source[j+1]
#                 j+=1
#     temp = 0
#     for check in range(size):
#         if source[check] == element:
#             temp += 1 
#     if temp > 0:
#         removeAll(source, size, element)
#     else:
#         print(source)

# source=[10,2,30,2,50,2,2,0,0]
# removeAll(source,7,2)


#################################  Task 7  ####################################
# def split(source):
#     length = int(len(source)/2)
#     left = 0
#     right = 0
#     #for int number
#     if len(source)/2 == type(int):
#         for i in range(length):
#             left = left + source[i]
#             right = right + source[-i-1]
#         if right == left:
#             return True
#         else:
#             return False
#     # for odd numbers
#     else:
#         for i in range(length):
#             left = left + source[i]
#             right = right + source[-i-1]
#         left = left + source[i+1]
#         if right == left:
#             return True
#         else:
#             for i in range(length):
#                 left = left + source[i]
#                 right = right + source[-i-1]
#             right = right + source[-i-2]
#             if left == right:
#                 return True
#             else:
#                 return False

# source = [1, 1, 1, 2, 1]
# print(split(source))

#############################  Task 8  ###################################
# class list:
#     def __init__(self):
#         pass
#     def method(n):                   
#         stacks = n*n                   
#         arr = ([0]*stacks)
#         c = 1
#         for i in range(n-1, stacks, n):
#             for j in range(c):
#                 arr[i-j] = j+1
#             c+=1
                
#         return arr

# print(list.method(int(input("please enter a number: "))))
################################# Task 9  ##################################
# class cls:
#     def __init__(self):
#         pass
#     def bunch(n):
#         main_cnt = 0
#         tempu = 0
#         cnt = 0
#         length = len(n)
#         for i in range(length):
#             if n[i] == tempu:
#                 cnt += 1
#             else:
#                 tempu = n[i]
#                 cnt = 1
#             if main_cnt <= cnt:
#                 main_cnt = cnt
#         print(main_cnt)

# ls = [int(user) for user in input("please enter list items: ").split(",")]
# cls.bunch(ls)


##################################  Task 10  ##############################
# class cls:
#     def __init__(self):
#         pass
#     def repetation(arr):
#         temp = []
#         cache = 0
#         rept = []
#         for i in range(len(arr)):
#             if arr[i] not in temp:
#                 count = 0
#                 for j in range(i+1, len(arr)):
#                     if arr[i] == arr[j]:
#                         count+= 1
#                 rept.append(count+1)
#                 temp.append(arr[i])
#         for i in range(len(rept)):
#             for j in range(i+1, len(rept)):
#                 if rept[i] == rept[j] and (rept[j] != 0 or rept[j] != 1):
#                     cache += 1
#                     break
#         if cache >= 2:
#             return True
#         else:
#             return False

# arr = [3,4,6,3,4,7,4,6,8,6,6]
# print(cls.repetation(arr))

