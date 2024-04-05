#Problem : to take  input from thw user and convert it  from  Celsius to Fahrenheitor fahrenite to celsius 

#Inputs : the inputs are the  numbers entered by the user the input can be float or integer

#output : the output is in form of float after the conversion 

#constraints : the inputs shoud be in integer format or float

#code :
a = float(input("Enter temperature in Celsius: "))
b = (a * 9/5) + 32
print("Temperature in Fahrenheit:", b)


c = float(input("Enter temperature in Fahrenheit: "))
d = (c - 32) * 5/9
print("Temperature in Celsius:", d)
# the code is tested with diffrent types of vlues like floats and integeres .
