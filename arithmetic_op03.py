#Create a variable called 'number' and assign it the two-digit number
number=23
#Find the reverse of the number and assign it to a variable called 'answer'.
x1=number%10
number//=10

x2=number%10
number//=10
answer=(x1*10+x2)
#Print the answer variable
print(answer)