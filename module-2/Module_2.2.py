#Garrett Woods - 3/9/2024 - Modula 11
#This code will count from 1 to whatever number the user inputs. I will throw an error when 0 or a negative number is entered.
#I included a recusive and nonrecursive function

#Gets the number to count to
rounds = int(input('How many times?: '))

#Handels the rule for non negative number
if rounds < 1: 
    raise ValueError('Please ensure to use a positive number') 

#recursive function to count from 1 to number
def recursion(current, n): 
    if current > n:
        return
    print(current)
    recursion(current + 1, n)

#displays the numbers
print("Recursive Function") 
recursion(1, rounds)
print("Recursive Function") 

#seperator for the different functions
print('~~~~~~~~~~~~~~~~~~~~~')

#non recursvie function to count from 1 to number
def non_recursion(n):
    print('Nonrecusrive Function')
    results = 0
    for i in range(rounds):
        results += 1
        print(results)
    print('Nonrecusrive Function')
non_recursion(rounds)