'''Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5,
 and “equal” if it’s equal to 5'''

def check_each(lst:list):
    for x in lst:
        if x > 5:
            print("bigger")
        elif x < 5:
            print("smaller")
        else:
            print("equal")
check_each([1,2,3,4,5,6,7,8,9])