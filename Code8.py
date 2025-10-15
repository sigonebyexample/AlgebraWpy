digits= input("Enter a decimal number to convert: ")
exponent= int(len(digits))-1
n= float(digits)
numerator= int(n * 10**exponent)
denominator= 10**exponent
percent= n * 100
print("The decimal is ", n)
print("The fraction is ", numerator, "/", denominator)
print("The percent is ", percent, " %")
