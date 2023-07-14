# list
friends = ["Kevin", "Karen", "Jim"]
print(friends[2])
# square bracket allows us to access elements based on their index
print(friends[-1])
print(friends[-3])
# colon access all elements 1 including eerything after 1 
print(friends[1:])
print(friends[0:3]) # to 3 not 3

friends [1] = "Mike"
print(friends[1])


def cube(num):
    return num*num*num 

result = cube(4)
print(result)
