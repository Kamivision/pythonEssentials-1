# i = 0
# while i <= 5 :
#     i += 1
#     if i % 2 == 0:
#       break
#     print("*")

# i = 0
# while i <= 3 :
#     i += 2
#     print("*")

# for i in range(1):
#     print("#")
# else:
#     print("#")

# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")

# var = 1
# while var < 10:
#     print("#")
#     var = var << 1

# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)

# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
 
# print(c + d + e)

# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])

# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])

# vals = [0, 1, 2]
# vals[0], vals[2] = vals[2], vals[0]
# print(vals)

# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print(vals)

# nums = [1, 2, 3]
# vals = nums[-1:-2]
# print(nums)
# print(vals)

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)

# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)

# my_list = [i for i in range(-1, 2)]
# print(my_list)

# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])

##### MODULE 4 TEST ######

# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)
 
 
# print(f(3))

# def fun(x):
#     x += 1
#     return x


# x = 2
# x = fun(x + 1)
# print(x)

# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     #print(k)
#     print(k[0])

# def func(a, b):
#     return a ** a


# print(func(2))

# def func_1(a):
#     return a ** a


# def func_2(a):
#     return func_1(a) * func_1(a)


# print(func_2(2))

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return


# print(fun(fun(2)) + 1)

# def fun(x):
#     global y
#     y = x * x
#     return y


# fun(2)
# print(y)

# def any():
#     print(var + 1, end='')


# var = 1
# any()
# print(var)

# my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'


# print(my_list(my_list))

# def fun(x, y, z):
#     return x + 2 * y + 3 * z


# print(fun(0, z=1, y=3))

# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']

# for k in range(len(dictionary)):
#     v = dictionary[v]

# print(v)

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# try:
#     value = input("Enter a value: ")
#     print(value/value)
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")
