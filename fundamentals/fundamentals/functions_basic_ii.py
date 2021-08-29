# 1 Countdown
# def countdown(num):
#     for x in range(num, -1, -1):
#         print(x)
# countdown(5)

# 2 Print and Return
# def printReturn(num1, num2):
#     print(num1)
#     return num2
# print2 = printReturn(1, 2)
# print(print2)

#3 First Plus Length
# def onePlusLength(arr):
#     return arr[0] + len(arr)
# answer = onePlusLength([1,2,3,4,5])
# print(answer)

#4 Values Greater than Second
# def values_greater_than_second(arr):
#     if(len(arr) < 2):
#         return False
#     newArray = []
#     NUM = arr[1]
#     for x in range(len(arr)):
#         if(arr[x] > NUM):
#             # print(arr[x])
#             newArray.append(arr[x])
#     if(len(newArray) < 2):
#         return False
#     else:
#         print(len(newArray))
#         return newArray
# value1 = values_greater_than_second([5,2,3,2,1,4])
# value2 = values_greater_than_second([3])
# print(value1)
# print(value2)

#5 This Length, That Value
# def lengthAndValue(repeat, value):
#     newArray = []
#     for x in range(repeat):
#         newArray.append(value)
#     return newArray
# value3 = lengthAndValue(4,7)
# value4 = lengthAndValue(6,2)
# print(value4)