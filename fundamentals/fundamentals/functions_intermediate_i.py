# # 1
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# #1-1
# x[1][0] = 15
# print(x)
# #1-2
# students[0]["last_name"] = "bryant"
# print(students)
# #1-3
# sports_directory['soccer'][0] = "Andres"
# print(sports_directory)
# #1-4
# z[0]["y"] = 30
# print(z)

# 2
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(list):
#     newString = ""
#     for x in list:
#         newString += (f"First Name - {x['first_name']}, Last Name - {x['last_name']}\n")
#     return newString

# # iterateDictionary(students)
# value5 = iterateDictionary(students)
# print(value5)

#3 Get Values from a list of Dictionaries
# def iterateDictionary2(keyName, list):
#     for x in list:
#         print(x[f"{keyName}"])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

#4 Iterate Through a Dictionary with list Values

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(list):
#     for x in list:
#         print(f"{len(list[x])} {x}")
#         for y in list[x]:
#             print(y)
#         print()

# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon