#Create a varaible 'number' and assign it the value of 43.
number=43

#Create a variable 'answer' and assign it the sum of the number's digits.
x1=number%10
number//=10 # number=number//10

x2=number%10
number//=10
answer=x1+x2
#Print answer.
print(answer)