#Problem :to take the magnitude from the user and provide them the kind of magnitude of earthquake

#Inputs : the inputs are the numbers entered by the user the input can be float or integer

#output : output is given in form of string representing the level of earthquake imact


#code :
eartude = float(input("Enter earthquake magnitude: "))
if eartude < 4:
    i = "Minor"
elif 4 <= eartude < 6:
    i = "Moderate"
elif 6 <= eartude < 7:
    i = "Strong"
elif 7 <= eartude < 8:
    i = "Major"
else:
    i = "Great"
print("Earthquake Impact Level:", i)
#validation : the code is tested with diffrent kind of outputs and performed as expected
