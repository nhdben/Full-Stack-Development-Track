# Task 1:
# You are required to complete the function reverse(x). given a string "x" as an input it is expected to return that same string but reversed.
# Example:
# input : "again"
# output: "niaga"
# you can change the string value in the variable text
#but you are not allowed to change the variable names or edit any other code, please only complete the function's definition.

def reverse(x):
    #complete this function so that it takes string x as an input 
    #and returns its reverse
    return  ''.join(reversed(x))

print("reversed string is: "+ reverse("again"))

##########

# Task 2:
# You are required to complete the function average(x). where "x" is a list of numbers.
# the function is expected to return the average from that list.
# Example:
# input : [10,20,30,40]
# output: 25
# you can change the numbers in the list no_list but you are not allowed to change the variable names or edit any other code, please only complete the function's definition.

no_list = [22,68,90,78,90,88]

def average(x):
    #complete the function's body to return the average
    result = sum(x)/ len(x)
    return result

print(average(no_list))

##########

# Task 3:
# You are required to complete the function maximum(x). where "x" is a list of numbers.
# the function is expected to return the highest number in that list.
# Example:
# input : [5,20,12,6]
# output: 20
# you can change the numbers in the list no_list but you are not allowed
# to change the variable names or edit any other code, please only complete the function's definition.

no_list = [1,2,3,4]

def maximum(no_list):
    #complete the function to return the highest number in the list
     return max(no_list)
    
print(maximum(no_list))

##########

# Task 4:
# You are required to complete the function unique_list(l).
# where "l" is a list of numbers. the function is expected to return the unique 
#numbers in that list.
# Example:
# input : [1,1,1,2,2,3,3,3,3,4,5,5,6]
# output: [1,2,3,4,5,6]
# you are not allowed to change the variable names or their 
# values or edit any other code, please only complete the function's definition.

no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]

def unique_list(l):
    #complete the function's body to return the unique list of numbers
    
print(unique_list(no_list))







