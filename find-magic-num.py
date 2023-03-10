import math

def magic_number(num):
	digitCount = int(math.log10(num))+1
	sumOfDigits = 0

	temp = num

	while (digitCount > 1):
		sumOfDigits = 0
		while (temp > 0):
			sumOfDigits += temp%10
			temp = temp//10

		temp = sumOfDigits

		digitCount = int(math.log10(sumOfDigits))+1

	if (sumOfDigits == 1):
		print(num)

low = int(input("Enter lower interval value \n"))
up = int(input("Enter upper interval value \n"))

print("Magic numbers between {x} and {y} are".format(x=low,y=up))

for num in range(low,up+1):
	magic_number(num)