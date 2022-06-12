from logging import logProcesses


#Definite Loop

#Looping through an array
for i in [5,4,3,2,1]:
    print(i)
print("Get out of the house!")
print("") #Create a space before the next function

#Here, i is a moving position indicator that runs through the values from left to right

#Using stored variables
#We are using friend instead of i, but you can use anyword or letter to represent the looping tool
friends = ['John', 'Jerry', 'Jammie']
for friend in friends:
    print('Happy Birthday:', friend)
print('Done!')
print('')

#What's the largest number?
#How do you identify the largest number efficiently?
#Start with a variable with a -1
largestSoFar = -1
print( 'Start', largestSoFar)
for number in [3,41,12,9,74,15] : # loop through each number and keep changing the value of largestSoFar
    if number > largestSoFar :
        largestSoFar = number
    print(largestSoFar, number)
print('End', largestSoFar)
print('')

#Summing in a loop
Rocks =0
print('Before', Rocks)
for i in [3,41,12,9,74,15] :
    Rocks = Rocks + i #Adding the item value to the initial Rocks value
    print(Rocks ,i)
print("After", Rocks) #The running total

#Find the average

print('') #Create a spaced line atop this block
count =0 #item number
sum=0 #Summing the items
print('Before', count)
for value in [3,41,12,9,74,15] :
    count = count + 1
    sum = sum + value #Adding the item value to the initial Rocks value
    print(count, value, sum)
print("After", count, sum, sum/count) #The running total