list = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# squaredList = []
# for i in (list):
#     squaredList.append(i**2)
    
# print(squaredList)

squaredList = [i**2 for i in list]
print(type(squaredList))