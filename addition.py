# Store input numbers
def inputnumber():
  num1 = input("Enter first number: ")
  num2 = input("Enter second number: ")

# Add two numbers
def total():
  sum = float(num1) + float(num2)

# Display the sum
inputnumber()
total();
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
